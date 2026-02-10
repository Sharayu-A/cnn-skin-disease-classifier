import tensorflow as tf
import numpy as np
from PIL import Image
from io import BytesIO
import os


# =====================================
# PATH SETUP
# =====================================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "ml_models", "disease_classifier_v1 (1).keras")


# =====================================
# LOAD MODEL ONCE (important for Django)
# =====================================
_model = None

def load_model_once():
    global _model

    if _model is None:
        print("Loading model...")
        _model = tf.keras.models.load_model(MODEL_PATH, compile=False)

    return _model


# =====================================
# CLASS MAP
# =====================================
CLASS_MAP = {
    0: 'actinic keratosis',
    1: 'basal cell carcinoma',
    2: 'dermatofibroma',
    3: 'melanoma',
    4: 'nevus',
    5: 'pigmented benign keratosis',
    6: 'seborrheic keratosis',
    7: 'squamous cell carcinoma',
    8: 'vascular lesion'
}


# =====================================
# IMAGE PREPROCESS (BYTES VERSION)
# =====================================
def preprocess(image_bytes):
    img = Image.open(BytesIO(image_bytes)).convert("RGB")
    img = img.resize((256, 256))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)
    return img


# =====================================
# PREDICT FUNCTION (BYTES VERSION)
# =====================================
def predict(image_bytes):
    model = load_model_once()

    preds = model.predict(preprocess(image_bytes))[0]

    idx = int(np.argmax(preds))
    confidence = float(preds[idx]) * 100

    return CLASS_MAP[idx], round(confidence, 2)

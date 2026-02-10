from django import forms
from .models import SkinImage


# ===============================
# SINGLE IMAGE
# ===============================
class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = SkinImage
        fields = ["image"]


# ===============================
# BATCH IMAGE (DJANGO 5 SAFE)
# ===============================
class BatchUploadForm(forms.Form):
    images = forms.FileField(
        required=True
    )

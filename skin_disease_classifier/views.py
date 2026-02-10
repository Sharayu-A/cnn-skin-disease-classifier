import os
import csv
import uuid

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

from .models import Prediction
from .forms import ImageUploadForm
from .services.predictor import predict


# ======================================
# HOME
# ======================================
def home(request):
    return render(request, "home.html")


# ======================================
# SINGLE IMAGE
# ======================================
def single_upload(request):

    form = ImageUploadForm()
    context = {"form": form}

    if request.method == "POST":

        form = ImageUploadForm(request.POST, request.FILES)

        if form.is_valid():

            img_obj = form.save()

            img_obj.image.open()
            label, confidence = predict(img_obj.image.read())

            Prediction.objects.create(
                image=img_obj,
                disease_name=label,
                confidence=confidence
            )

            context["result"] = (label, confidence)

    return render(request, "single.html", context)

# ======================================
# BATCH IMAGE
# ======================================
from django.core.files.storage import default_storage

def batch_upload(request):

    if request.method == "POST":

        images = request.FILES.getlist("images")
        results = []

        for img in images:

            file_path = default_storage.save(img.name, img)

            img.seek(0)
            img_bytes = img.read()

            label, confidence = predict(img_bytes)

            results.append([img.name, label, confidence])

        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="batch_predictions.csv"'

        writer = csv.writer(response)
        writer.writerow(["filename", "prediction", "confidence"])

        for row in results:
            writer.writerow(row)

        return response

    return render(request, "batch.html")

import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import base64
import os
import logging
import traceback
from PIL import Image
import numpy as np

def normalize_image(image_path, target_size=(224, 224)):
    """
    Normalize the image:
    - Resize to target dimensions.
    - Scale pixel values to [0, 1].
    """
    try:
        # Open image
        image = Image.open(image_path).convert('RGB')

        # Resize image
        image = image.resize(target_size)

        # Convert to numpy array and scale pixel values
        image_array = np.array(image) / 255.0  # Normalize to [0, 1]

        return image_array

    except Exception as e:
        print(f"Error during image normalization: {e}")
        return None

logger = logging.getLogger(__name__)

# IBM Watson API details
API_KEY = "ilM7g7UijoIAXfxBoqSL97I2FHFC_zWYcDwP-ORCz1-u"
MODEL_ENDPOINT = "https://us-south.ml.cloud.ibm.com/ml/v4/deployments/954e6391-a0ca-4c87-98d1-98e7c0a860be/predictions?version=2021-05-01"


# Function to get IBM token
def get_ibm_token():
    try:
        response = requests.post(
            'https://iam.cloud.ibm.com/identity/token',
            data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'}
        )
        print(f"Token Request Status: {response.status_code}")
        print(f"Token Request Response: {response.text}")
        response.raise_for_status()
        return response.json()["access_token"]
    except Exception as e:
        print(f"Detailed Token Error: {e}")
        return None

def get_predictions(image_path):
    try:
        mltoken = get_ibm_token()
        if not mltoken:
            return {"error": "Unable to get IBM token"}

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + mltoken
        }

        # Normalize the image
        normalized_image = normalize_image(image_path)
        if normalized_image is None:
            return {"error": "Image normalization failed"}

        # Encode normalized image to Base64
        img_base64 = base64.b64encode(normalized_image.tobytes()).decode('utf-8')

        payload_scoring = {
            "input_data": [{
                "fields": ["image"],
                "values": [[img_base64]]
            }]
        }

        # Send the request
        response_scoring = requests.post(
            MODEL_ENDPOINT,
            json=payload_scoring,
            headers=headers,
            timeout=30  # Add timeout
        )

        print(f"Status Code: {response_scoring.status_code}")
        print(f"Response Headers: {response_scoring.headers}")
        print(f"Response Text: {response_scoring.text}")

        response_scoring.raise_for_status()
        return response_scoring.json()

    except requests.exceptions.RequestException as req_error:
        print(f"Request Error: {req_error}")
        return {"error": f"Request failed: {str(req_error)}"}

    except Exception as e:
        print(f"Prediction Error: {e}")
        return {"error": "Prediction processing failed"}
    
def nails_page(request):
    result = None

    if request.method == 'POST' and request.FILES.get('image'):
        # Get the uploaded file
        image = request.FILES['image']

        # Store the file
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        file_path = os.path.join(settings.MEDIA_ROOT, filename)

        # Perform prediction with normalization
        result = get_predictions(file_path)

    return render(request, 'nail.html', {'result': result})




def home_page(request):
    return render(request, 'home.html')

def eyes_page(request):
    return render(request, 'eyes.html')

def teeth_page(request):
    return render(request, 'teeth.html')
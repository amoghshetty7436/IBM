import os
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import tensorflow as tf
import numpy as np 
import requests
import base64
import getpass

from PIL import Image
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference
# TensorFlow for model loading and predictions

# Load your model when the server starts (SavedModel format)
MODEL_PATH = os.path.join('models', 'nail_disease_saved_model')  # Update with the directory containing the SavedModel
model = tf.keras.layers.TFSMLayer(MODEL_PATH, call_endpoint='serving_default')

WATSONX_EU_APIKEY = ("Du47kj7eiMCDj9RAZ8JjQ6lXCn1tB8SBa5sjymxgzGIL")

WATSONX_EU_PROJECT_ID = ("2d4d6c3e-5f0d-4f6c-8eee-f17a5fbc790a")

URL = "https://s3.au-syd.cloud-object-storage.appdomain.cloud"

credentials = Credentials(
    url=URL,
    api_key=WATSONX_EU_APIKEY,
    instance_id= "openshift"
)

def augment_api_request_body(user_query):
    messages = [
        {
            "role": "user",
            "content": user_query
        }
    ]
    return messages



def nails_analysis(request):
    if request.method == 'POST' and request.FILES.get('image'):
        # Save the uploaded file
        uploaded_file = request.FILES['image']
        fs = FileSystemStorage()
        file_path = fs.save(uploaded_file.name, uploaded_file)

        # Process the image
        image_path = fs.path(file_path)
        image = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224))  # Adjust target size as needed
        image_array = tf.keras.preprocessing.image.img_to_array(image)
        image_array = image_array / 255.0  # Normalize image data if required by your model
        image_array = image_array.reshape((1, *image_array.shape))  # Add batch dimension

        # Predict using the local model
        prediction = model(image_array)
        class_names =  ['Darier_s disease', 'Muehrck-e_s lines', 'aloperia areata', 'beau_s lines', 'bluish nail', 'clubbing', 'eczema', 
                        'half and half nailes (Lindsay_s nails)', 'koilonychia', 'leukonychia', 
                        'onycholycis', 'pale nail', 'red lunula', 'splinter hemmorrage', 'terry_s nail', 'white nail', 'yellow nails']
        disease = class_names[np.argmax(prediction)]
        
        # Initialize the model
        model = ModelInference(
            model_id="meta-llama/llama-3-2-11b-vision-instruct",
            credentials=credentials,
            project_id=WATSONX_EU_PROJECT_ID,
            params={
                "max_tokens": 200
            }
)
        user_query = f"What causes this disease? How can we prevent it? What is the diagnosis for it? {disease} is what I have."

# Construct the request body
        messages = augment_api_request_body(user_query)

# Make the API call
        response = model.chat(messages=messages)
        # Return the result to the template
        return render(request, 'nail.html', {'result': response})

    return render(request, 'nail.html')


def home_page(request):
    return render(request, 'home.html')

def eyes_page(request):
    return render(request, 'eyes.html')

def teeth_page(request):
    return render(request, 'teeth.html')
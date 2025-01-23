import os
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import tensorflow as tf
import numpy as np  # TensorFlow for model loading and predictions

# Load your model when the server starts (SavedModel format)
MODEL_PATH = os.path.join('models', 'nail_disease_saved_model')  # Update with the directory containing the SavedModel
model = tf.keras.layers.TFSMLayer(MODEL_PATH, call_endpoint='serving_default')

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
        
        # Return the result to the template
        return render(request, 'nail.html', {'result': disease})

    return render(request, 'nail.html')


def home_page(request):
    return render(request, 'home.html')

def eyes_page(request):
    return render(request, 'eyes.html')

def teeth_page(request):
    return render(request, 'teeth.html')
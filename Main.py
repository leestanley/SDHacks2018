"""
Filename: Main.py
Date: 10/13/18
Users: Sravya, Titan, Jill, Stanley
"""

"""
MVP
--------
WebApp that displays Clarifai's normal results in classifying images of vacations

"""

# Import Clarifai
from clarifai.rest import ClarifaiApp

# PREDICT API
# Returns a list of concepts in an image based on model
# Used for access in localHost to imageLink

def picPredict(imageLink, myApi):  # URL should be a string for process
    # Creates an "app" that runs Clarifai
    app = ClarifaiApp(api_key=myApi)

    # Training model for images, can be specified
    model = app.public_models.general_model

    # All data given by model
    response = model.predict_by_url(url=imageLink)
    # Accessing the concepts from all the data returned by predict_by_url
    concepts = response['outputs'][0]['data']['concepts']
    results = []

    for concept in concepts:
        results.append((concept['name'], str(concept['value'])))

    return results


# importing webapp libraries
import os
from flask import Flask, url_for, render_template, request, jsonify
from flask import *

# importing clarifai api + app setup
from clarifai.rest import ClarifaiApp
#change myApi with new api key
myApi = '32256d518ae94e9597fe852eb356250a' 

#myApi = '47b3bc03e8b5465aa428115b98030bcb' backup key - 2k left

app = ClarifaiApp(api_key=myApi)
model = app.public_models.general_model

#importing functions
from Main import picPredict
from Test_Upload import run
from Test_Search import output

# local host app set up
app = Flask(__name__)
#http://127.0.0.1:5000/ <-- put this in url bar

# https://www.telegraph.co.uk/content/dam/Travel/Destinations/Asia/Japan/cherry-blossom-hirosaki-park-japan.jpg?imwidth=450 <-- imageLink sample

@app.route('/')  # home page
def home():
    run(myApi)
    return render_template('index.html')

@app.route('/results')
def results():
    imageLink = request.args['inputname']

    #runs concept confidence
    results = picPredict(imageLink, myApi)
    #top 5 concepts and their confidence levels

    eyes = [0,1,2,3,4]
    concepts = []
    percentages = []

    for i in eyes:
        aTuple = results[i]
        concepts.append(aTuple[0])
        concepts[i] = concepts[i].capitalize()
        percentages.append(float(aTuple[1]) * 100)
        percentages[i] = round(percentages[i], 3)

    #runs search by image
    placeList = output(imageLink, myApi)#returns list with 3 tuples (location name, place)
    place1 = placeList[0]
    place2 = placeList[1]
    place3 = placeList[2]
    print(place1)
    print(place2)
    print(place3)

    return render_template('test.html', concept1=concepts[0], concept2=concepts[1], concept3=concepts[2], concept4=concepts[3], concept5=concepts[4], percentage1=percentages[0], percentage2=percentages[1], percentage3=percentages[2], percentage4=percentages[3], percentage5=percentages[4], name1=place1[0], name2=place2[0], name3=place3[0], image1=place1[1], image2=place2[1], image3=place3[1])

# run local host
if __name__ == "__main__":
    app.run()


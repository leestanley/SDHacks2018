from clarifai.rest import ClarifaiApp
app = ClarifaiApp(api_key='9f4c8fdd79b24c4aa14ed9f3fec060e2')

search = app.inputs.search_by_image(url='https://s3.amazonaws.com/cdn-origin-etr.akc.org/wp-content/uploads/2017/11/12224412/Shiba-Inu-On-White-01.jpg')

for search_result in search:
    print("Score:", search_result.score, "| URL:", search_result.url)

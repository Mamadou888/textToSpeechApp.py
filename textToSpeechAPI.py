import requests
import webbrowser

"""Detailed Intrustion on API:
	Do you want to convert the text "hello world" to an MP3? Simply fetch:

http://tts-api.com/tts.mp3?q=hello+world.
Adding the parameter &return_url=1 to the URL will give you the URL to the generated MP3 instead of MP3 content."""
#This parameter must be there
theParam = {'param': "&return_url=1"}
#sending a request with the parameter
theTextToSpeech = requests.get("http://tts-api.com/tts.mp3?q=hello+world.", params=theParam)
#This produces the '<Response [200]>' response thing on the terminal
print theTextToSpeech

#code below acutally combines this new site
origWebsite = "http://tts-api.com/tts.mp3?q="
#later make it take up a file!
with open ("physicsEssay.txt", "r") as myfile:
    data=myfile.read().replace('\n', '')
    sData = data.replace(" ", "+")
#When I want it to say one word
sayThis="Anglican Church"
website = origWebsite + sayThis
finalwebsite = website
# print text
# print finalwebsite
webbrowser.open(finalwebsite)
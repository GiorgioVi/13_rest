from flask import Flask, render_template
import urllib2, json

my_app = Flask(__name__)

dictionary_string = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=SwvVGWrlWhzNXuLCsZXMoKS1xIZO4a7Uo1HEsNRV").read()
dictionary = json.loads(dictionary_string)

@my_app.route('/')
def root():
    return render_template("base.html", image_url = dictionary["hdurl"])

if __name__ == "__main__":
    my_app.debug = True
    my_app.run()

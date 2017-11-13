from flask import Flask, render_template
import urllib2, json

my_app = Flask(__name__)

dictionary_string = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=SwvVGWrlWhzNXuLCsZXMoKS1xIZO4a7Uo1HEsNRV").read()
dictionary = json.loads(dictionary_string)

string = urllib2.urlopen("https://forex.1forge.com/1.0.2/convert?from=USD&to=EUR&quantity=100&api_key=gwfSIsXHlrX5FDYREYwP1eExX1YJKxQv").read();
dict = json.loads(string);

@my_app.route('/')
def root():
    return render_template("base.html")

@my_app.route('/nasa', methods=["POST"])
def nasa():
    return render_template("nasa.html", image_url = dictionary["hdurl"])

@my_app.route('/currencies', methods=["POST"])
def currency():
    return render_template("currency.html", exchange_rate = dict["text"])

if __name__ == "__main__":
    my_app.debug = True
    my_app.run()

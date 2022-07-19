import requests
from subprocess import Popen
from urllib.parse import urlparse
from flask import Flask, request, url_for, render_template, redirect

app = Flask(__name__, template_folder='pages')
app.config['DEBUG'] = True

@app.route("/")
def start():
    return render_template("index.html")

@app.route("/ssrf_check", methods = ['POST'])
def ssrf():
    url = request.form['url']

    if "http" not in str(urlparse(url).scheme):
        return render_template("index.html", result_error = "The URL schema is not valid.")
    try:
        if "2852039166" in url:
            req = requests.get(url, timeout=5.000)
            return render_template("index.html", result = "Valid Website Found!", html_content = req.text)
        else:
            return render_template("index.html", result_error = "Wow! that's a invalid web.")
    except Exception as e:
        if "NewConnectionError" in str(e):
            return render_template("index.html", result_error = e)
        else:
            return render_template("index.html", result = e)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
  app.run(host = '0.0.0.0')


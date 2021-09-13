from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

genderize_url = 'https://api.genderize.io'
agify_url = 'https://api.agify.io'


@app.route('/')
def home():
    year = datetime.datetime.now().year
    print(year)

    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, year=year)


@app.route('/guess/<name>')
def guess(name):
    params = {
        'name': name
    }
    gender_response = requests.get(url=genderize_url, params=params)
    gender = gender_response.json()['gender']
    age_response = requests.get(url=agify_url, params=params)
    age = age_response.json()['age']
    return render_template("guess.html", name=name.title(), gender=gender, age=age)


@app.route('/blog')
if __name__ == "__main__":
    app.run(debug=True)

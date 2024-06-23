import requests
import string
import geoip2.database

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////python-docker/weather.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SECRET_KEY'] = 'thisisasecret'
db = SQLAlchemy(app)


class City(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable=False)

def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=4e0149545aed90761a349cde25e32e1a"
    r = requests.get(url).json()
    return r

@app.route('/')
def index_get():
    cities = City.query.all()
    print(cities)
    print(dir(cities))

    weather_data = []

    for city in cities:
        r = get_weather_data(city.name)
        weather = {
            'city' : city.name,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }
        weather_data.append(weather)

    return render_template('weather.html', weather_data=weather_data)

@app.route('/', methods=['POST'])
def index_post():
    err_msg = ''
    new_city = request.form.get('city')
    new_city = new_city.lower()
    new_city = string.capwords(new_city)
    if new_city:
        existing_city = City.query.filter_by(name=new_city).first()
        
        if not existing_city:
            new_city_data = get_weather_data(new_city)
            if new_city_data['cod'] == 200:
                new_city_obj = City(name=new_city)

                db.session.add(new_city_obj)
                db.session.commit()
            else:
                err_msg = 'That is not a valid city!'
        else:
            err_msg = 'City already exists in the database!'

    if err_msg:
        flash(err_msg, 'error')
    else:
        flash('City added successfully!', 'success')

    return redirect(url_for('index_get'))

@app.route('/delete/<name>')
def delete_city( name ):
    city = City.query.filter_by(name=name).first()
    db.session.delete(city)
    db.session.commit()

    flash(f'Successfully deleted { city.name }!', 'success')
    return redirect(url_for('index_get'))

@app.route('/server')
def index_me():
    ip='157.201.130.149'
    try:
      if (request.headers['Host']):
        ip=request.headers['Host']
    except Exception as e:
      print("Error {}".format(e))

    weather_data = []
    
    city="Rexburg"
    with geoip2.database.Reader('/python-docker/City.mmdb') as reader:
      try:
        response=reader.city(ip)
        if response.city:
          if response.city.names:
            city = response.city.names['en']
      except Exception as e: 
        print("Error {}".format(e))
        
    r = get_weather_data(city)
    weather = {
            'city' : city,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
            'ip' : ip, 
    }
    weather_data.append(weather)

    return render_template('ip.html', weather_data=weather_data)


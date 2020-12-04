import flask
from flask import request, url_for, render_template, redirect



app = flask.Flask(__name__)

@app.route('/',methods=['GET','POST'])
def my_maps():

  mapbox_access_token = 'pk.eyJ1IjoiYW5vdW1haG5hIiwiYSI6ImNrN3hhNnpidDA5cmwzZm8ybTNqbjNleHYifQ.KHevR8RQ5gR0wMB0j7YU3g'


  return render_template('index2.html',
        mapbox_access_token=mapbox_access_token)

if __name__ == '__main__':
    app.run(debug=True)
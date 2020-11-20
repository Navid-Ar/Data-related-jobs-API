import os
import numpy as np
import pandas as pd
import pickle
import gzip
from flask import Flask, render_template, request, url_for, jsonify

with gzip.open("random_forest.pkl", 'rb') as f:
    p = pickle.Unpickler(f)
    model = p.load()

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():

    return(render_template('template.html'))


@app.route('/process', methods=['GET', 'POST'])
def process():
    if request.method == 'GET':
        return(render_template('template.html', prediction='11'))

    if request.method == 'POST':

        title = request.form['title']
        if title == "-- select a value --":
            return jsonify({"error": "select a value for Job Title"})

        state = request.form['state']
        if state == "-- select a value --":
            return jsonify({"error": "select a value for State"})

        sector = request.form['sector']
        if sector == "-- select a value --":
            return jsonify({"error": "select a value for Sector"})

        ownership = request.form['ownership']
        if ownership == "-- select a value --":
            return jsonify({"error": "select a value for Ownership"})

        size = request.form['size']
        if size == "-- select a value --":
            return jsonify({"error": "select a value for Size"})

        Revenue = request.form['Revenue']
        if Revenue == "-- select a value --":
            return jsonify({"error": "select a value for Revenue"})

        seniority = request.form['seniority']

        ML = request.form['ML']

        python = request.form['python']

        cloud_computing = request.form["cloud_computing"]

        big_data = request.form['big_data']

        deep_learning = request.form['deep_learning']

        graduate = request.form['graduate']

        undergrad = request.form['undergrad']

        myRange = request.form['demo']
        # myRange = 4

        data = [size, ownership, sector, Revenue, seniority, ML, python,
                state, cloud_computing, title, big_data,
                deep_learning, graduate, undergrad, myRange]

        if "-- select a value --" not in data:

            # Storing user submitted parameters in a df.

            data_array = np.array(data).reshape(1, -1)
            df = pd.DataFrame(data_array, columns=['Size', 'Type of ownership', 'Sector', 'Revenue', 'seniority', 'ML', 'python',
                                                   'state', 'cloud_computing', 'title', 'big_data',
                                                   'deep_learning', 'graduate', 'undergrad', 'exp_year'])

            prediction = model.predict(df)
            prediction = "$" + str(round(prediction[0])) + "k USD/Year"

            return jsonify({'result': prediction})
        else:
            return jsonify({"error": "Missing Data"})


if __name__ == '__main__':
    app.run(debug=True)

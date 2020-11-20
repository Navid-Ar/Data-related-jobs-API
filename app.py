import os
import numpy as np
import pickle
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('template.html')


if __name__ == '__main__':
    app.run(debug=True)
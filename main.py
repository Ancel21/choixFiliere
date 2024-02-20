"""
Created on Sun Nov  5 01:12:28 2023

@author: ancel
"""

from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)



if __name__ == '__main__':
    app.run(debug=True)
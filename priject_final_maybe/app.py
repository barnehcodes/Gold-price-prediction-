from flask import Flask, request, render_template
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gold_price', methods=['POST'])
def get_gold_price():
    date_str = request.form['date'] # get date from form input
    df = pd.read_csv('gold_prediction_flask_1.csv')
    gold_df = pd.read_csv('gold_prediction_flask_1.csv', parse_dates=['Date'], index_col='Date') # load CSV file
    value = gold_df.loc[date_str]['Value'] # get value for given date




    return render_template('result.html', date=date_str, value=value)

if __name__ == '__main__':
    app.run()

# AI-Enhanced-Fitness-Wellness-Analyzer-Project/web_app/app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/fitness')
def fitness():
    return render_template('fitness.html')

if __name__ == '__main__':
    app.run(debug=True)



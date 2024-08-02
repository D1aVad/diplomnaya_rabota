from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/doppage')
def doppage():
    return render_template('dop_page.html')

if __name__ == '__main__':
    app.run()
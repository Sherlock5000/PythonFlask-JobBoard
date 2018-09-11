from flask import g, Flask, render_template
import sqlite3

PATH = 'db/jobs.sqlite'

app = Flask(__name__)

def open_connection():
    connection = getattr(g, '_connection', None)
    

@app.route('/')
@app.route('/jobs')
def jobs():
  return render_template('index.html')
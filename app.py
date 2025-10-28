from flask import Flask, render_template, jsonify
import time
import random
import string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/phone_freezer')
def phone_freezer():
    """Ultimate phone freezing test - most aggressive"""
    return render_template('phone_freezer.html')

@app.route('/memory_bomb')
def memory_bomb():
    """Memory exhaustion test"""
    return render_template('memory_bomb.html')

@app.route('/cpu_intensive')
def cpu_intensive():
    """CPU intensive calculations"""
    return render_template('cpu_intensive.html')

@app.route('/api/heavy_data')
def heavy_data():
    """Generate massive JSON response"""
    data = {
        'payload': ''.join(random.choices(string.ascii_letters + string.digits, k=5000000)),
        'timestamp': time.time()
    }
    return jsonify(data)

# Only needed for local testing
if __name__ == "__main__":
    app.run()

from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_timer', methods=['POST'])
def start_timer():
    duration = int(request.form['duration'])
    end_time = time.time() + duration
    return jsonify({'end_time': end_time})

@app.route('/get_time_left', methods=['GET'])
def get_time_left():
    current_time = time.time()
    end_time = float(request.args.get('end_time'))
    time_left = max(0, end_time - current_time)
    return jsonify({'time_left': time_left})

if __name__ == '__main__':
    app.run(debug=True)

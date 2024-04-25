from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/draw_heart')
def draw_heart():
    # No need to execute external script, drawing is handled on frontend
    return 'Drawing request received'

if __name__ == '__main__':
    app.run(debug=True)

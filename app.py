from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/etiquette', methods=['POST', 'GET'])
def etiquette():
    return render_template('etiquette.html')

@app.route('/contraindications', methods=['POST', 'GET'])
def contraindications():
    return render_template('contraindications.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
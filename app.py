from flask import Flask, request
from whatsapp import getImage

app = Flask(__name__)


@app.route('/process_data', methods=['POST'])
def process_input():
    if request.method == 'POST':
        keywords = request.json.get('keywords')
        if keywords:
            getImage(keywords)
        else:
            return "Keywords parameter is missing in the POST request.", 400
    return "Invalid request method.", 405

from flask import Flask
from flask_cors import CORS
import os

# google cloud speech to text
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./config/service-account-file.json"

app = Flask(__name__)
cors = CORS(app, resources={
  r"/*": {"origin": "*"},
})


@app.route('/')
def home():
    return "Server is healthy"


@app.route('/image', methods=['POST'])
def ocr():
    return "OCR"


if __name__ == "__main__":
    app.run(debug=False, port=5000)

from flask import Flask
from flask_cors import CORS

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

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
    return "Server is healthy!"


@app.route('/speech', methods=['POST'])
def speech_to_text():
    # voice upload to './voice/'

    # get text response with function speech_to_text(path)

    # get voice & text response with function gpt_translation(text)
    return "Response : speech_to_text"


if __name__ == "__main__":
    app.run(debug=False, port=5000)

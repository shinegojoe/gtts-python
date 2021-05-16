# Import the Gtts module for text  
# to speech conversion 
from dotenv import dotenv_values
from gtts import gTTS 
from flask import Flask, jsonify, request

config = dotenv_values(".env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}
port = int(config["PORT"])
tempDir = config["TEMP_DIR"]
app = Flask(__name__)


@app.route("/", methods=['POST'])
def ggts():
    try:
        data = request.json
        print(data, 'v4')
        text = data['text']
        language = 'en'
        myobj = gTTS(text=text, lang=language, slow=False) 
        output = '{}/{}'.format(tempDir, "output.mp3")
        myobj.save(output)
        res = jsonify({"status": "ok"})
    except Exception as e:
        res = jsonify({"status": "err"})

    return res


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=port)
 
# Import the Gtts module for text  
# to speech conversion 
from dotenv import dotenv_values
from gtts import gTTS 
from flask import Flask, jsonify, request
from translate import Translator


config = dotenv_values(".env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}
port = int(config["PORT"])
tempDir = config["TEMP_DIR"]

# port = 7001
# tempDir = '/app/storage'
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

@app.route("/translate", methods=['POST'])
def test():
    try:
        data = request.json
        text = data['text']
        to_lang = 'zh-TW'
        translator= Translator(to_lang=to_lang)
        res = translator.translate(text)
        res = jsonify({"status": "ok", "text": res})

    except Exception as e:
        res = jsonify({"status": "err"})

    return res


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=port)
 
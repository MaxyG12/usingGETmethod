from flask import Flask,request

app = Flask(__name__)

@app.route('/', methods=["GET"])
def language():
  data = request.args
  if data == {}:
    return "Nothing here"
  elif data["lang"] == "eng":
    return "Hello, and welcome to our wonderful website!"
  elif data["lang"] == "esp":
    return "Hola, y bienvenido a nuestra maravillosa página web!"
  else:
    return "No data"


app.run(host='0.0.0.0', port=81)
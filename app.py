from flask import Flask

app = Flask(__name__) # -> __main__ ("Este arquivo")

@app.route("/")
def HomePage():
    return "<h1> Bem vindo a minha api </h1>"

app.run(host="0.0.0.0")

from flask import Flask

app = Flask(__name__)
print("🚀 Servidor Flask está iniciando...")


@app.route("/")
def hello():
    return "API RINASCE ONLINE — Hello World com Flask!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

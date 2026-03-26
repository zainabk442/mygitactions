# <<<<<<< HEAD
# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route("/")
# def home():
#     return "Hello from Docker + GitHub Actions + AWS!"
#
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)
# =======
# print("Hello from GitHub Actions pipeline!")
# >>>>>>> f2eb77dc0c68e8c70b4145023e92e1a828633e8f



from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Docker + GitHub Actions + AWS!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
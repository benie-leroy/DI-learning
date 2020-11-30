from flask import Flask
app = Flask(__name__)

# default-page
@app.route("/")
def home():
   return "hello world"

if __name__ == "__main__":
   app.run()
from flask import Flask
from routes.users import user_bp

app = Flask(__name__)
app.register_blueprint(user_bp)

@app.route("/")
def home():
    return {"message": "REST API with MongoDB is running"}

if __name__ == "__main__":
    app.run(debug=True,port=8000)

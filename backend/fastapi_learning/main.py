from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello Kailash"}

@app.get("/movies")
def get_movies():
    return {
        "movies": [
            "Titanic",
            "Interstellar",
            "Avengers"
        ]
    }

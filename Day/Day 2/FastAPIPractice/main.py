#HTTP Methods:Are a way to talk (From browser) to the server
#methods 
#GET : Read data
#POST:create a new data
#PUT : Replace existing data
#PATCH : Partial update
#DELETE : Remove data
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return {"page":"Home"}
@app.get("/about")
def about():
    return {"page":"About","author":"Khanishka"}
@app.get("/health")
def health():
    return {"status":"ok"}
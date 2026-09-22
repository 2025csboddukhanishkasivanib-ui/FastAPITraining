#HTTP Methods:Are a way to talk (From browser) to the server
#methods 
#GET : Read data
#POST:create a new data
#PUT : Replace existing data
#PATCH : Partial update
#DELETE : Remove data
from fastapi import FastAPI
from pydantic import BaseModel
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
# POST request
@app.post("/create")
def create_something():
    return {"message":"Created"}
# Path parameters
@app.get("/student/{usn}")
def get_result(usn):
    return {"Result":"Distinction","usn":usn}
# Path paramters with type hint
@app.get("/candidate/{rollno}}")
def get_candidate(rollno:int):
    return {"Result":"Distinction","rollno":rollno,"type":str(type(rollno))}
# Pydantic model
class Item(BaseModel):
    name:str
    price:float
    in_stock: bool = True
@app.post("/items")
def create_item(item:Item):
    return{"Recieved":item,"total_price":item.price*1.18}
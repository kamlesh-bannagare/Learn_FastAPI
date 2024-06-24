from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# create a model
class User(BaseModel):
    name:str
    age: int
    email: str | None=None

@app.post("/")
async def add_user(data:User):
    update_user = data.dict()
    update_user.update({"city":"Nagpur"})
    # update_user["city"] = "Pune"
    return update_user
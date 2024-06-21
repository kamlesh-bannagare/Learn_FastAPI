from fastapi import FastAPI

app = FastAPI()

# @app.get("/{name}")
# def get_user(name):
#     return {"name":name}


# path parameters with type
@app.get("/{user_id}")
def get_user(user_id:int):
    return {
        "name":user_id
    }
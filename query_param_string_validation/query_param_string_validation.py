# from typing import Annotated
# from fastapi import FastAPI, Query
#
# app = FastAPI()
#
# @app.get("/")
# async def get_user(data: Annotated[str:None, Query(max_length=50)]= None):
#     return data

from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()

# @app.get("/items/")
# async def read_items(q: Annotated[
#         str | None, Query(min_length=3, max_length=50, pattern="^fixedquery$")
#     ] = None,):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# @app.get("/items/")
# async def read_items(q: Annotated[str, Query(min_length=3)] = ...):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# @app.get("/items/")
# async def read_items(q: Annotated[list[str] | None, Query()] = None):
#     query_items = {"q": q}
#     return query_items

# Query parameter list / multiple values with defaults¶
# @app.get("/items/")
# async def read_items(q: Annotated[list[str], Query()] = ["foo", "bar"]):
#     query_items = {"q": q}
#     return query_items

# Using list¶
# @app.get("/items/")
# async def read_items(q: Annotated[list, Query()] = []):
#     query_items = {"q": q}
#     return query_items

# Add title
@app.get("/items/")
async def read_items(
    q: Annotated[str| None, Query(title="Query string", min_length=3)] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
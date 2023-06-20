from typing import Optional, re
from xml.etree.ElementInclude import include

from fastapi import FastAPI, Query, Path, Body
from enum import Enum

from pydantic import BaseModel, Field

app = FastAPI()
#
#
# @app.get('/', description='this is my first route', deprecated=True)
# async def home():
#     return {"message": "hello world"}
#
# @app.post('/')
# async def post():
#     return {"message": "hello from the post route"}
#
# @app.put('/')
# async def put():
#     return {"message": "hello from the put route"}
#
# @app.get('/users')
# async def list_user():
#     return {"message": "list of users"}
#
# @app.get('/users/me')
# async def get_current_user():
#     return {"message": "this is the current user"}
#
# @app.get('/users/{user_id}')
# async def list_user(user_id: str):
#     return {"user_id": user_id}
#
# class FoodEnum(str, Enum):
#     fruits = "fruits"
#     vegetables = "vegetables"
#     dairy = "dairy"
#
# @app.get('/food/{food_name}')
# async def get_food(food_name: FoodEnum):
#     if food_name == FoodEnum.vegetables:
#         return {"food_name": food_name, "message": "you are healthy"}
#     if food_name == 'fruits':
#         return {"food_name": food_name, "message":"you are still healthy"}
#     return {"food_name": food_name, "message": "i like chocolate milk"}
#
# # ---------------------------------------------------------------------------
# fake_items_db = [{"item_name": "foo"}, {"item_name": "bar"}, {"item_name": "foo bar"}]
# @app.get("/items")
# async def list_items(skip: int=0, limit: int=10):
#     return fake_items_db[skip:skip+limit]
#
# @app.get("/items/{item_id}")
# async def list_items(item_id:str, q: str|None = None, short: bool=False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update({"description":"There are many variations of passages of Lorem Ipsum available"})
#     return item
#
# @app.get("/items/{item_id}")
# async def get_item(
#     item_id: str, sample_query_param: str, q: str | None = None, short: bool = False
# ):
#     item = {"item_id": item_id, "sample_query_param": sample_query_param}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {
#                 "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut consectetur."
#             }
#         )
#     return item
#
# #-------------------------------------------------------------------------
# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: int
#     tax: float | None = None
#
# @app.post("/items")
# async def create_item(item: Item):
#     item_dict = item.dict()
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_with_tax": price_with_tax})
#     return item_dict
#
# @app.put("/items/{item_id}")
# async def create_item_with_put(item_id: int, item: Item, q: str|None = None):
#     result = {"item_id": item_id, **item.dict()}
#     if q:
#         result.update({"q": q})
#     return result
#
# #------------------------------------------------------------------------------
#
# @app.get("/articles")
# async def read_items(q: list[str] | None = Query(
#     None, max_length=10, min_length=3,
#     title="Sample query", description="Description 1",
#     alias="item-query"
# )):
#     results = {"items":[{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results
#
# @app.get("/articles/hidden")
# async def hidden_query_route(hidden_query: str|None = Query(None, include_in_schema=False)):
#     if hidden_query:
#         return {"hidden_query": hidden_query}
#     return {"hidden_query": "Not found"}
#
# @app.get("/items_validation/{item_id}")
# async def read_item_validation(
#         *,
#         item_id: int = Path(..., title="The ID of the item", gt=10, le=100),
#         q: str = "hello",
#         size: float = Query(..., gt=0, lt=7.75)
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q, "size": size})
#     return results
# """
# PART 7
# """
# class Item(BaseModel):
#     name: str
#     description: str| None = None
#     price: float
#     tax: float| None = None
#
# class User(BaseModel):
#     username: str
#     fullname: str| None = None
#
#
# @app.put("/items/{item_id}")
# async def update_item(
#         *,
#         item_id: int = Path(..., title="The ID of the item", ge=0, le=100),
#         q: str | None = None,
#         # item: Item | None = None,
#         # user: User | None = None,
#         # importance: int = Body(..., embed=True)
#
#         item: Item = Body(..., embed=True),
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     if item:
#         results.update({"item": item})
#     # if user:
#     #     results.update({"user": user})
#     # if importance:
#     #     results.update({"importance": importance})
#     return results

# """
# PART 8
# """
# class Item(BaseModel):
#     name: str
#     description: str | None = Field(None, title="The description of the item", max_length=300)
#     price: float = Field(..., gt=0, description="The price of the item")
#     tax: float | None = None
#
# @app.put("/items/{item_id}")
# async def update_item(
#         item_id: int,
#         item: Item = Body(..., embed=True)
# ):
#     results = {"item_id": item_id, "item": item}
#     return results


# PART 9

class Image(BaseModel):
    url: str = Field(..., regex="^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)$")
    name: str

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []
    # tags: set[str] = set()
    image: Image| None = None


@app.put("/items/{item_id}")
async def update_item(
        item_id: int,
        item: Item
):
    results = {"item_id": item_id, "item": item}
    return results

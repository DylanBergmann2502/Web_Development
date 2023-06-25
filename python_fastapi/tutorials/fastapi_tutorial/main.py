from datetime import datetime, time, timedelta
from typing import Optional, Literal, Union
from uuid import UUID
from xml.etree.ElementInclude import include

from fastapi import FastAPI, Query, Path, Body, Cookie, Header, status, Form, File, UploadFile, HTTPException, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exception_handlers import http_exception_handler, request_validation_exception_handler
from fastapi.exceptions import RequestValidationError
from enum import Enum

from pydantic import BaseModel, Field, HttpUrl, EmailStr
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse

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

# class Image(BaseModel):
#     url: HttpUrl
#     name: str
#
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#     tags: list[str] = []
#     # tags: set[str] = set()
#     image: list[Image]| None = None
#
# class Offer(BaseModel):
#     name: str
#     description: str|None = None
#     price: float
#     items : list[Item]
#
# @app.put("/items/{item_id}")
# async def update_item(
#         item_id: int,
#         item: Item
# ):
#     results = {"item_id": item_id, "item": item}
#     return results
#
# @app.post("/offers")
# async def create_offer(offer: Offer = Body(..., embed=True)):
#     return offer
#
# @app.post("/images/multiple")
# async def create_multiple_images(images: list[Image] = Body(..., embed=True)):
#     return images
#
# @app.post("/blah")
# async def create_blahs(blahs: dict[int, float]):
#     return blahs

# PART 10
# class Item(BaseModel):
#     name: str = Field(..., example="Foo")
#     description: str | None = Field(None, example="A very nice Item")
#     price: float = Field(..., example=16.25)
#     tax: float | None = Field(None, example=1.67)
#
#     # class Config:
#     #     schema_extra = {
#     #         "example": {
#     #             "name": "Foo",
#     #             "description": "A very nice Item",
#     #             "price":16.25,
#     #             "tax": 1.67
#     #         }
#     #     }
#
# @app.put("/items/{item_id}")
# async def update_item(
#         item_id: int,
#         item: Item = Body(
#             ...,
#             examples={
#                 "normal": {
#                     "summary": "A normal example",
#                     "description": "A __normal__ item works _correctly_",
#                     "value": {
#                         "name": "Foo",
#                         "description": "A very nice Item",
#                         "price": 16.25,
#                         "tax": 1.67,
#                     },
#                 },
#                 "converted": {
#                     "summary": "An example with converted data",
#                     "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
#                     "value": {"name": "Bar", "price": "16.25"},
#                 },
#                 "invalid": {
#                     "summary": "Invalid data is rejected with an error",
#                     "description": "Hello youtubers",
#                     "value": {"name": "Baz", "price": "sixteen point two five"},
#                 },
#             },
#         )
#         ):
#     results = {"item_id": item_id, "item": item}
#     return results

# PART 11
# @app.put("/items/{item_id}")
# async def read_item(
#         item_id: UUID,
#         start_date: datetime| None = Body(None),
#         end_date: datetime| None = Body(None),
#         repeat_at: time | None = Body(None),
#         process_after: timedelta| None = Body(None),
# ):
#     start_process = start_date + process_after
#     duration = end_date - start_process
#     return {"item_id": item_id, "start_date": start_date,
#             "end_date": end_date, "repeat_at": repeat_at,
#             "process_after": process_after, "start_process": start_process,
#             "duration": duration
#             }

# PART 12
# @app.get("/items")
# async def read_items(
#         cookie_id: str|None = Cookie(None),
#         accept_encoding: str|None = Header(None, convert_underscores=False),
#         sec_ch_ua: str|None = Header(None),
#         user_agent: str|None = Header(None),
#         x_token: list[str] | None = Header(None)
# ):
#     return {"cookie_id": cookie_id, "Accept-Encoding": accept_encoding,
#             "sec-ch-ua": sec_ch_ua,"User-Agent": user_agent,
#             "x_token": x_token
#     }

# PART 13
# class Item(BaseModel):
#     name: str
#     description: str| None = None
#     price: float
#     tax: float = 10.5
#     tags: list[str] = []
#
# items = {
#     "foo": {"name": "Foo", "price": 50.2},
#     "bar": {"name": "Bar", "description": "The bartenders", "price":62, "tax": 20.2},
#     "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 20.2, "tags":[]}
# }
#
# @app.get("/items/{item_id}/name", response_model=Item, response_model_include={"name","description"})
# async def read_item(item_id: Literal["foo", "bar", "baz"],):
#     return items[item_id]
#
# @app.get("/items/{item_id}/public", response_model=Item, response_model_exclude={"tax"})
# async def read_item_public(item_id: Literal["foo", "bar", "baz"],):
#     return items[item_id]
#
# @app.post("items/")
# async def create_item(item: Item):
#     return item
#
# class UserBase(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: str | None = None
#
# class UserIn(UserBase):
#     password: str
#
# class UserOut(UserBase):
#     pass
#
# @app.post("user/", response_model=UserOut)
# async def create_user(user: UserIn):
#     return user

# PART 14
# class UserBase(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: str | None = None
#
# class UserIn(UserBase):
#     password: str
#
# class UserOut(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: str | None = None
#
# class UserInDB(UserBase):
#     hashed_password: str
#
# def fake_password_hasher(raw_password: str):
#     return f"Supersecret {raw_password}"
#
# def fake_save_user(user_in: UserIn):
#     hashed_password = fake_password_hasher(user_in.password)
#     user_in_db = UserInDB(**user_in.dict(), hashed_password =hashed_password)
#     print("userin.dict", user_in.dict())
#     print("User saved")
#     return user_in_db
#
# @app.post("/user/", response_model = UserOut)
# async def create_user(user_in: UserIn):
#     user_saved = fake_save_user(user_in)
#     return user_saved
#
# class BaseItem(BaseModel):
#     description: str
#     type: str
#
#
# class CarItem(BaseItem):
#     type = "car"
#
#
# class PlaneItem(BaseItem):
#     type = "plane"
#     size: int
#
#
# items = {
#     "item1": {"description": "All my friends drive a low rider", "type": "car"},
#     "item2": {
#         "description": "Music is my aeroplane, it's my aeroplane",
#         "type": "plane",
#         "size": 5,
#     },
# }
#
#
# @app.get("/items/{item_id}", response_model=Union[PlaneItem, CarItem])
# async def read_item(item_id: Literal["item1", "item2"]):
#     return items[item_id]
#
#
# class ListItem(BaseModel):
#     name: str
#     description: str
#
#
# list_items = [
#     {"name": "Foo", "description": "There comes my hero"},
#     {"name": "Red", "description": "It's my aeroplane"},
# ]
#
#
# @app.get("/list_items/", response_model=list[ListItem])
# async def read_items():
#     return items
#
#
# @app.get("/arbitrary", response_model=dict[str, float])
# async def get_arbitrary():
#     return {"foo": 1, "bar": "2"}

## Part 15 - Response Status Codes
# @app.post("/items/", status_code=status.HTTP_201_CREATED)
# async def create_item(name: str):
#     return {"name": name}
#
#
# @app.delete("/items/{pk}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_item(pk: str):
#     print("pk", pk)
#     return pk
#
#
# @app.get("/items/", status_code=status.HTTP_302_FOUND)
# async def read_items_redirect():
#     return {"hello": "world"}

## Part 16 - Form Fields
# class User(BaseModel):
#     username: str
#     password: str
#
# @app.post("/login/") # Form => sent back as Form object, if use both => both will be Form
# async def login(username: str = Form(...), password: str = Form(...)):
#     print("password", password)
#     return {"username": username}
#
# # @app.post("/login-json/")
# # async def login_json(user:User):
# #     return user
#
# @app.post("/login-json/") # Body => sent back as JSON
# async def login_json(username: str = Body(...), password: str = Body(...)):
#     print("password", password)
#     return {"username": username}

# PART 17
# @app.post("/files/")
# async def create_file(file: bytes | None = File(None)):
#     if not file:
#         return {"message": "no files sent"}
#     return {"file": len(file)}
#
# @app.post("/uploadfile/") # UploadFile is better
# async def upload_file(file: UploadFile| None = None):
#     if not file:
#         return {"message": "no upload files sent"}
#     return {"filename": file.filename}

# @app.post("/files/")
# async def create_file(
#     files: list[bytes] = File(..., description="A file read as bytes")
# ):
#     return {"file_sizes": [len(file) for file in files]}
#
#
# @app.post("/uploadfile/")
# async def create_upload_file(
#     files: list[UploadFile] = File(..., description="A file read as UploadFile")
# ):
#     return {"filename": [file.filename for file in files]}
#
#
# @app.get("/")
# async def main():
#     content = """
# <body>
# <form action="/files/" enctype="multipart/form-data" method="post">
# <input name="files" type="file" multiple>
# <input type="submit">
# </form>
# <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
# <input name="files" type="file" multiple>
# <input type="submit">
# </form>
# </body>
#     """
#     return HTMLResponse(content=content)

## Part 18 - Request Forms and Files
# @app.post("/files/")
# async def create_file(
#     file: bytes = File(...),
#     fileb: UploadFile = File(...),
#     token: str = Form(...),
#     hello: str = Body(...),
# ):
#     return {
#         "file_size": len(file),
#         "fileb_content_type": fileb.content_type,
#         "token": token,
#         "hello": hello,
#     }

## Part 19 - Handling Errors
# items = {"foo": "The Foo Wrestlers"}
#
# @app.get("/items/{item_id}")
# async def read_item(item_id: str):
#     if item_id not in items:
#         raise HTTPException(
#             status_code=404,
#             detail="Item not found",
#             headers={"X-Error": "There goes my error"},
#         )
#     return {"item": items[item_id]}
#
# class UnicornException(Exception):
#     def __init__(self, name: str):
#         self.name = name
#
#
# @app.exception_handler(UnicornException)
# async def unicorn_exception_handler(request: Request, exc: UnicornException):
#     return JSONResponse(
#         status_code=418,
#         content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
#     )
#
# @app.get("/unicorns/{name}")
# async def read_unicorns(name: str):
#     if name == "yolo":
#         raise UnicornException(name=name)
#     return {"unicorn_name": name}
#
# # @app.exception_handler(RequestValidationError)
# # async def validation_exception_handler(request: Request, exc: UnicornException):
# #     return PlainTextResponse(str(exc), status_code=400)
# #
# # @app.exception_handler(StarletteHTTPException)
# # async def http_exception_handler(request, exc):
# #     return PlainTextResponse(str(exc.detail), status_code=exc.status_code)
# #
# #
# # @app.get("/validation_items/{item_id}")
# # async def read_validation_items(item_id: int):
# #     if item_id == 3:
# #         raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
# #     return {"item_id": item_id}
#
# # @app.exception_handler(RequestValidationError)
# # async def validation_exception_handler(request: Request, exc: RequestValidationError):
# #     return JSONResponse(
# #         status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
# #         content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
# #     )
# #
# # class Item(BaseModel):
# #     title: str
# #     size: int
# #
# # @app.post("/items/")
# # async def create_item(item: Item):
# #     return item
#
# @app.exception_handler(StarletteHTTPException)
# async def custom_http_exception_handler(request, exc):
#     print(f"OMG! An HTTP error!: {repr(exc)}")
#     return await http_exception_handler(request, exc)
#
#
# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request, exc):
#     print(f"OMG! The client sent invalid data!: {exc}")
#     return await request_validation_exception_handler(request, exc)
#
#
# @app.get("/blah_items/{item_id}")
# async def read_items(item_id: int):
#     if item_id == 3:
#         raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
#     return {"item_id": item_id}

## Part 20 - Path Operation Configuration
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#     tags: set[str] = set()
#
#
# class Tags(Enum):
#     items = "items"
#     users = "users"
#
#
# @app.post(
#     "/items/",
#     response_model=Item,
#     status_code=status.HTTP_201_CREATED,
#     tags=[Tags.items],
#     summary="Create an Item-type item",
#     # description="Create an item with all the information: "
#     # "name; description; price; tax; and a set of "
#     # "unique tags",
#     response_description="The created item",
# )
# async def create_item(item: Item):
#     """
#     Create an item with all the information:
#     - **name**: each item must have a name
#     - **description**: a long description
#     - **price**: required
#     - **tax**: if the item doesn't have tax, you can omit this
#     - **tags**: a set of unique tag strings for this item
#     """
#     return item
#
#
# @app.get("/items/",
#          tags=[Tags.items]
# )
# async def read_items():
#     return [{"name": "Foo", "price": 42}]
#
#
# @app.get("/users/",
#          tags=[Tags.users]
# )
# async def read_users():
#     return [{"username": "PhoebeBuffay"}]
#
#
# @app.get("/elements/", tags=[Tags.items], deprecated=True)
# async def read_elements():
#     return [{"item_id": "Foo"}]
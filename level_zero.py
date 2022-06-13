# from typing import Optional
# from fastapi import FastAPI
# from pydantic import BaseModel
# import uvicorn

# app = FastAPI()


# @app.get('/blog')
# def index(limit=10,published:bool = True, sort:Optional[str]=None):
#     #only get
#     return {'data': {"name": f"{limit} Hello world"}}

# @app.get('/blogs/unpublished')
# def unpublished_blogs():
#      return {'data':{"msg":"All unpublished blogs"}}


# @app.get('/blog/{id}')
# def show(id:int):
#     return {'data':{"id":id}}

# @app.get('/blog/{id}/comments')
# def comments(id,limit=10):
#     return {'data':{"comments":id}}


# class Blog(BaseModel):
#     title:str
#     body:str
#     published: Optional[bool]

# @app.post('/blog')
# def create_blog(request: Blog):
#     return {'data':'Blog has been created'}

# # if __name__ == '__main__':
# #     uvicorn.run(app,host="127.0.0.1", port='9000')
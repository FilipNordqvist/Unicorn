# -*- coding: utf-8 -*-

from fastapi import FastAPI, Header



app = FastAPI()

@app.get("/")
async def hello():
    return {"Hello": "World!"}

@app.get("/{id}")
async def get_unicorn(id: str, header: str = Header(None)):

    return {"id": id}
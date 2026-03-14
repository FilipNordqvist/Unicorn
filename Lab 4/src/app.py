# -*- coding: utf-8 -*-

from fastapi import FastAPI

import httpx

app = FastAPI()

@app.get("/")
async def hello():
    return {"Hello": "World!"}

@app.get("/{id}")
async def get_unicorn(id: str):
   return False
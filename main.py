#!/user/bin/env python
# -*- coding: utf-8 -*-
from fastapi import FastAPI

from sub1 import sub1
from sub2 import sub2

app = FastAPI(root_path="/api")

app.include_router(sub1.router)
app.include_router(sub2.router)

@app.get("/")
def read_main():
    return {"message": "Hello World from main app"}

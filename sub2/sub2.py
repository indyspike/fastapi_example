#!/user/bin/env python
# -*- coding: utf-8 -*-
from fastapi import APIRouter

router = APIRouter(prefix="/sub2")

@router.get("/")
async def read_sub():
    return {"message": "Hello World from Sub2 API"}

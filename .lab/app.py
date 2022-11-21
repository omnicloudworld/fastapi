#!/usr/bin/env python3.10

import uvicorn
from fastapi import Request, APIRouter
from skyant.rest.app import BaseURL

server = BaseURL(
    'DEMO',
    version='0.0',
    contact={'name': 'SkyANT', 'email': 'info@skyant.dev'},
    description='Demo APP'
)

router = APIRouter()

@router.get("/app")
def read_main(request: Request):
    return {"message": "Hello World", "root_path": request.scope.get("root_path")}


server.add2base(router)

if __name__ == '__main__':
    uvicorn.run(server, port=8008, host='0.0.0.0')

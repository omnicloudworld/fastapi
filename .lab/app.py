#!/usr/bin/env python3.10

'''
'''

from fastapi import APIRouter
from fastapi import status
from skyapp.api.platform import SkyAPI, CamelModel
from pydantic import (
    Field
)

app = SkyAPI(
    'TEST-SSS',
    'description',
    'version',
    contact={'name': 'sdsd', 'email': 'sdsdsds@sgrg.rr'},
    debug=True,
    sdoc='/sdoc'
)


route = APIRouter(
    prefix='/test',
    tags=['test']
)


class TModel(CamelModel):
    task_id: str = Field(
        ...,
        title='ID of processed task'
    )


@route.post('/t1', operation_id="test", include_in_schema=False)
@route.post('/t1/', operation_id="test", response_model=TModel, status_code=status.HTTP_202_ACCEPTED)
async def import_file_data(import_data: TModel):
    return {'task_id': 'wefref3fer'}

app.include_router(route)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, port=8008)

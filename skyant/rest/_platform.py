# pylint: disable=missing-docstring

from os import environ as env
from fastapi import FastAPI, APIRouter
from fastapi.responses import RedirectResponse


class App(FastAPI):
    '''
    Inherited from FastAPI class ReDoc have a predefined router to documentation from redoc library.

    Classic OpenAPI documentation can be activated through environment variable $SIMPLE_DOC.
    This variable is a higher priority that the class argument. But if $SIMPLE_DOC will set a similar
    redoc argument then the variable will be ignored.

    Args:

        title: Name of API.

        description: Short description of API. It would be used markdown.

        version: Version of API service (container/server/etc). It's not an API specification version.

        contact: Support team contacts. Have to has name and email in dictionary format.

        redoc: Path to display OpenAPI documentation from redoc library. Default is '/doc'.
            The class will be redirected GET request from '/' to this path.

        sdoc: Path for displaying classic OpenAPI documentation. Default is None. It can't be equal redoc.

        debug: Debugging flag. Default is False.

        **kw: Additional arguments from FastAPI class.
    '''

    def __init__(
        self,
        title: str,
        description: str,
        version: str,
        contact: dict,
        redoc: str = '/doc',
        sdoc: str = None,
        debug: bool = False,
        **kw
    ):

        assert redoc != '/', 'Parameter \'redoc\' can\'t be root.'
        assert sdoc != '/', 'Parameter \'sdoc\' can\'t be root.'
        assert redoc != sdoc, 'ReDoc & Simple Doc shouldn\'t be equal.'

        if 'SIMPLE_DOC' in env and env['SIMPLE_DOC'] != redoc:
            sdoc = env.get('SIMPLE_DOC', sdoc)  # env vars have priority
        debug = bool(env.get('DEBUG_API', debug))  # env vars have priority

        super().__init__(
            title=title,
            description=description,
            version=version,
            contact=contact,
            redoc_url=redoc,
            docs_url=sdoc,
            debug=debug,
            **kw
        )

        if redoc and redoc != '':

            route = APIRouter(
                prefix=''
            )

            @route.get(
                '/',
                response_class=RedirectResponse, status_code=301, include_in_schema=False
            )
            async def redirector():
                '''
                '''
                return redoc

            self.include_router(route)

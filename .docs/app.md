---
hide:
    - navigation
---

#


## BaseURL

The simplest method for running FastAPI with BaseURL is `skyant.rest.app.BaseURL`.

The BaseURL gives you a feature for organise your API with Load Balancer or reverse proxy without
a stripped path prefix.

For example if your proxy/load balancer host is https://your.host/ you can fill it with any
containers such as:


- https://your.host/__path/to/first/container__

    _The BaseURL of this container should be `path/to/first/container`_


- https://your.host/__path/to/second/container__

    _This `path/to/second/container`_


The `BaseURL` accepts an argument as environment variables `BASE_URL` or `base_path`.


```py linenums='1' title='index.py'
#!/usr/bin/env python3.10

import uvicorn
from skyant.rest.app import BaseURL

server = BaseURL(
    'DEMO',
    version='0.0',
    contact={'name': 'SkyANT', 'email': 'info@skyant.dev'},
    description='Demo APP',
    base_url='/test/path'
)

if __name__ == '__main__':
    uvicorn.run(server, port=8008, host='0.0.0.0')
```


!!!warning
    For BaseURL work you should use the `add2base` method.

    ```py linenums='1' title='index.py'
    #!/usr/bin/env python3.10

    import uvicorn
    from skyant.rest.app import BaseURL

    server = BaseURL(
        'DEMO',
        version='0.0',
        contact={'name': 'SkyANT', 'email': 'info@skyant.dev'},
        description='Demo APP',
        base_url='/test/path'
    )

    router = APIRouter()

    @router.get("/app")
    def read_main(request: Request):
        return {"message": "Hello World", "root_path": request.scope.get("root_path")}

    server.add2base(router)

    if __name__ == '__main__':
        uvicorn.run(server, port=8008, host='0.0.0.0')
    ```


The `BaseURL` object always serve the ReDoc documentation on the root path.

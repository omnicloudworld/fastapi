
__This package is a part of cloud application framework [SkyANT](https://skyant.dev). For more information please read [the documentation](https://docs.skyant.dev/projects/data).__

<br/>

## Cloud Application Framework

Cloud Application Framework is a fleet of well-known software libraries which was been extended by cloud related methods.

SkyANT now contains components inherited from [Plotly Dash](https://dash.plotly.com), [Pydantic](https://docs.pydantic.dev/), [Dask](https://dask.org), [Odoo](https://odoo.com), etc & work with [Google Cloud Platform](https://cloud.google.com).


## Value

Making software for a cloud requires two vectors business-logic & cloud integration codding.

SkyANT components already contain cloud integration tools, so it gives developers opportunities to work with business-logic only.

<br/>


The package provide additional features for [FastAPI](https://fastapi.tiangolo.com/) and use
it as a part of Cloud Application Framework[^1]


The `skyant.rest.app.*` inheritance the class `fastapi.FastAPI` so all their features are available.

For fast & easy run API in Google Cloud Platform you can use [SkyANT Runner](https://skyant.dev/projects/cloudrun/).


[^1]: Cloud Application Framework is a fleet of tools for building, integrating and deployment to cloud application (ui and api) base on philosophy "one task = one app = one container". Please read more at [https://skyant.dev/framework/](https://skyant.dev/framework/).

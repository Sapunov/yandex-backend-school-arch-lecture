from aiohttp import web

from app.api.v1 import get_scooters
from app.api.v1 import get_scooters_admin
from app.context import AppContext


def wrap_handler(handler, context):
    async def wrapper(request):
        return await handler(request, context)

    return wrapper


def setup_routes(app: web.Application, ctx: AppContext) -> None:
    app.router.add_get(
        '/v1/scooters',
        wrap_handler(
            get_scooters.handle,
            ctx,
        ),
    )
    app.router.add_get(
        '/v1/admin/scooters',
        wrap_handler(
            get_scooters_admin.handle,
            ctx,
        ),
    )

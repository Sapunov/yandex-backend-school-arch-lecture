from aiohttp import web

from app.context import AppContext


def wrap_handler(handler, context):
    async def wrapper(request):
        return await handler(request, context)

    return wrapper


def setup_routes(app: web.Application, ctx: AppContext) -> None:
    app.router.add_get(
        '/v1/scooters',
        wrap_handler(
            # TODO
            ctx,
        ),
    )
    app.router.add_get(
        '/v1/admin/scooters',
        wrap_handler(
            # TODO
            ctx,
        ),
    )

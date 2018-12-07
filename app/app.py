import asyncio

from aiohttp import web

async def simple_handler(request):
    return web.Response(status=200, text="OK")

async def medium_handler(request):
    await asyncio.sleep(10)
    return web.Response(status=200, text="OK")

async def complex_handler(request):
    await asyncio.sleep(60)
    return web.Response(status=200, text="OK")

if __name__ == "__main__":
    app = web.Application()

    app.router.add_route(
        "GET",
        "/simple",
        simple_handler)
    app.router.add_route(
        "GET",
        "/medium",
        medium_handler)
    app.router.add_route(
        "GET",
        "/complex",
        complex_handler)

    handler = app.make_handler()
    loop = asyncio.get_event_loop()
    server = loop.create_server(handler, '0.0.0.0', 8080)

    loop.run_until_complete(server)
    loop.run_forever()

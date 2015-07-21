import asyncio
from aiohttp import web

counter = {}


@asyncio.coroutine
def handle(request):
    yield from asyncio.sleep(0.5)
    key = request.match_info.get('key')
    val = counter.set_default(key, 0)
    counter[key] = val + 1
    return web.Response(body=str(counter[key]).encode())


@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/count/{key}', handle)

    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 5000)
    print("Server started at http://127.0.0.1:5000")
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

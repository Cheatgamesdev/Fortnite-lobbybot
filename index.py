# -*- coding: utf-8 -*-
import asyncio
import importlib
import os
import platform
import sys
import traceback

try:
    import aiohttp
    import colorama
    import jaconv
    import sanic

    discord = importlib.import_module('discord')
    fortnitepy = importlib.import_module('fortnitepy')
    pykakasi = importlib.import_module('pykakasi')
except ModuleNotFoundError:
    print(traceback.format_exc())
    print(f'Python {platform.python_version()}\n')
    print(
        'Failed to load third party library. Please run INSTALL. If the issue is not resolved, contact me\n'
        'Discord Cheatgames#6888'
        'or join support Discordserver\n'
        'https://discord.gg/2eVaHtFefp'
 )
    sys.exit(1)

try:
    import modules
except ModuleNotFoundError:
    print(traceback.format_exc())
    print(f'Python {platform.python_version()}\n')
    sys.exit(1)

if sys.platform == 'win32':
    asyncio.set_event_loop(asyncio.ProactorEventLoop())
else:
    try:
        import uvloop
    except ModuleNotFoundError:
        pass
    else:
        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

if __name__ == '__main__':
    if (os.getenv('PROJECT_DOMAIN') is not None
            and os.getcwd().startswith('/app')
            and sys.platform == 'linux'):
        mode = 'glitch'
    elif (os.getenv('REPLIT_DB_URL') is not None
            and os.getcwd().startswith('/home/runner')
            and sys.platform == 'linux'):
        mode = 'repl'
    else:
        mode = 'pc'

    print(modules.colors.green(
        f'V{modules.__version__}\n'
        f'Python {platform.python_version()}\n'
        f'fortnitepy {fortnitepy.__version__}\n'
        f'discord.py {discord.__version__}\n'
        f'Sanic {sanic.__version__}'
    ))

    loop = asyncio.get_event_loop()
    bot = modules.Bot(
        mode,
        loop=loop,
        dev='-dev' in sys.argv,
        use_device_code='-use-device-code' in sys.argv,
        use_device_auth='-use-device-auth' in sys.argv
    )
    bot.setup()
    loop.run_until_complete(bot.start())

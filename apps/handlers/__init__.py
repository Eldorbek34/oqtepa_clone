from .commands import router as commands_router
from .about import router as about_router
from  apps.handlers.send_lacation  import router as send_location
from .start_order import router as start_order
from .registration import router as registration


def setup_handlers(dp):
    dp.include_router(commands_router)
    dp.include_router(send_location)

    dp.include_router(start_order)

    dp.include_router(about_router)

    dp.include_router(registration)

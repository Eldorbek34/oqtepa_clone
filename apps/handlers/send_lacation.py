from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

from apps.handlers.start_order import start_order
from apps.utils.functions import get_address, haversine
from apps.utils.states import OrderStateGroup

router = Router()


@router.message(F.text == "Orqaga", OrderStateGroup.send_location)
async def order_message(message: types.Message, state: FSMContext):
    await start_order(update=message, state=state)


@router.message(F.location, OrderStateGroup.send_location)
async def order_book_message(message: types.Message, state: FSMContext):
    # address_line = await get_address(longitude=message.location.longitude, latitude=message.location.latitude)
    # await message.answer(f"Sizning joylashuviz: {address_line}")

    order_data = await state.get_data()
    order_type = order_data.get('type_order', None)
    import logging

    if order_type and order_type == 'delivery':
        distance = await haversine(message.location.longitude, message.location.latitude, 69.243001, 41.328492)
        logging.critical(distance)
        if distance >= 20:
            return await message.answer('Выбранная локация находится вне зоны доставки.')

    await state.update_data(
        {'coordinate': {'longitude': message.location.longitude, 'latitude': message.location.latitude}})

    await message.answer("Lokatsiya qabul qilindi")

from aiogram import Router, types, F

from apps.handlers.commands import start_command
from apps.keyboards.inline import inline_back_to_main_menu
from apps.utils.callback_data import MainMenuCallbackData, MainMenuAction, BackToMainMenuCallbackData

router = Router()


@router.callback_query(MainMenuCallbackData.filter(F.action == MainMenuAction.ABOUT))
async def about_message(callback_query: types.CallbackQuery):
    await callback_query.message.answer(
        f"🚀 Oqtepa Lavash | Delivery\nBuyurtmani birga joylashtiramizmi? 🤗\n <a href='https://google.com'>google</a>",
        reply_markup=inline_back_to_main_menu())


@router.callback_query(BackToMainMenuCallbackData.filter())
async def back_to_main_menu_message(callback_query: types.CallbackQuery, callback_data: BackToMainMenuCallbackData):
    await start_command(callback_query.message)

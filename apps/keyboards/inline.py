from aiogram.utils.keyboard import InlineKeyboardBuilder

from apps.utils.callback_data import cb_main_menu_callback_data, MainMenuAction, cb_back_to_main_menu_callback_data, \
    cb_select_language_callback_data, SelectLanguage


def inline_back_to_main_menu():
    inline_keyboard = InlineKeyboardBuilder()

    inline_keyboard.button(text='Asosiy menu',
                           callback_data=cb_back_to_main_menu_callback_data())
    return inline_keyboard.as_markup()


def inline_main_menu():
    inline_keyboard = InlineKeyboardBuilder()

    inline_keyboard.button(text='🏠️️ Buyurtma berish',
                           callback_data=cb_main_menu_callback_data(action=MainMenuAction.ORDER))
    inline_keyboard.button(text='Biz haqimizda', callback_data=cb_main_menu_callback_data(action=MainMenuAction.ABOUT))
    inline_keyboard.button(text='Buyurtmalarim',
                           callback_data=cb_main_menu_callback_data(action=MainMenuAction.MY_ORDERS))
    inline_keyboard.button(text='Filiallar', callback_data=cb_main_menu_callback_data(action=MainMenuAction.BRANCHES))
    inline_keyboard.button(text='Sozlamalar', callback_data=cb_main_menu_callback_data(action=MainMenuAction.SETTINGS))

    inline_keyboard.adjust(2)

    return inline_keyboard.as_markup()


def inline_subscribe():
    inline_keyboard = InlineKeyboardBuilder()

    inline_keyboard.button(text='Subscribe', url='https://t.me/+GRx6sKGZLn83YWEy')

    return inline_keyboard.as_markup()


def inline_languages():
    inline_keyboard = InlineKeyboardBuilder()
    inline_keyboard.button(text='Uzbek', callback_data=cb_select_language_callback_data(lang=SelectLanguage.UZ))
    inline_keyboard.button(text='Russian', callback_data=cb_select_language_callback_data(lang=SelectLanguage.RU))
    inline_keyboard.button(text='English', callback_data=cb_select_language_callback_data(lang=SelectLanguage.EN))

    inline_keyboard.adjust(1)

    return inline_keyboard.as_markup()

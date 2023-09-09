from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from configs.admins import keyboard
from base.base_conn import BotDB
def admin_vo_sso() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text = 'ВО')
    kb.button(text = 'ССО')
    kb.button(text = 'Админ-панель')
    kb.adjust(2)
    return kb.as_markup(resize_keyboard = True)

def apanel() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    for i in range(len(keyboard)):
        kb.button(text= keyboard[i])
    kb.button(text='Назад')
    kb.adjust(1)
    return kb.as_markup(resize_keyboard = True)

def ban_panel() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    for i in range(len(BotDB.get_users())):
        kb.button(text = (BotDB.get_users()[i]))
    kb.button (text = 'Назад')
    kb.adjust(1)
    return kb.as_markup(resize_keyboard = True)

def unban_panel() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    for i in range(len(BotDB.get_banned_user_fns())):
        kb.button(text = BotDB.get_banned_user_fns()[i])
    kb.button(text = 'Назад')
    kb.adjust(1)
    return kb.as_markup(resize_keyboard = True)

def mass_send_panel() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button('Назад')
    kb.adjust(0)
    return kb.as_markup(resize_keyboard = True)

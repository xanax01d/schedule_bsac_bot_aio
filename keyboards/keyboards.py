from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from configs.groups import level_vo,level_sso,courses_vo,courses_sso,days,gr_list_1course_vo,gr_list_1course_sso,gr_list_2course_vo,gr_list_2course_sso,gr_list_3course_vo,gr_list_3course_sso,gr_list_4course_vo,gr_list_4course_sso
from configs.admins import admin_ids

def vo_or_sso(user_id) -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text = level_vo)
    kb.button(text = level_sso)
    if user_id in admin_ids:
        kb.button(text = 'Админ-панель')
    kb.adjust(2)
    return kb.as_markup(resize_keyboard = True)


def sday() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    for i in range(len(days)):
        kb.button(text = days[i])
    kb.button(text = 'Назад')
    kb.adjust(3)
    return kb.as_markup(resize_keyboard = True)
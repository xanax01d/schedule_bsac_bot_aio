from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from configs.groups import courses_sso,days,gr_list_1course_vo,gr_list_1course_sso,gr_list_2course_vo,gr_list_2course_sso,gr_list_3course_vo,gr_list_3course_sso,gr_list_4course_vo,gr_list_4course_sso

def course_sso() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    for i in range(len(courses_sso)):
        kb.button(text = courses_sso[i])
    kb.button(text = 'Назад')
    kb.adjust(4)
    return kb.as_markup(resize_keyboard = True)

def sgsso1() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    for i in range(len(gr_list_1course_sso)):
        kb.button(text = gr_list_1course_sso[i])
    kb.button(text = 'Назад')
    kb.adjust(4)
    return kb.as_markup(resize_keyboard = True)
def sgsso2() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    for i in range(len(gr_list_2course_sso)):
        kb.button(text = gr_list_2course_sso[i])
    kb.button(text = 'Назад')
    kb.adjust(4)
    return kb.as_markup(resize_keyboard = True)
def sgsso3() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    for i in range(len(gr_list_3course_sso)):
        kb.button(text = gr_list_3course_sso[i])
    kb.button(text = 'Назад')
    kb.adjust(4)
    return kb.as_markup(resize_keyboard = True)
def sgsso4() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    for i in range(len(gr_list_4course_sso)):
        kb.button(text = gr_list_4course_sso[i])
    kb.button(text = 'Назад')
    kb.adjust(4)
    return kb.as_markup(resize_keyboard = True)


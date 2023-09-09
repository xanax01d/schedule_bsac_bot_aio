from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from configs.groups import courses_vo,days,gr_list_1course_vo,gr_list_1course_sso,gr_list_2course_vo,gr_list_2course_sso,gr_list_3course_vo,gr_list_3course_sso,gr_list_4course_vo,gr_list_4course_sso


def course_vo() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    for i in range(len(courses_vo)):
        kb.button(text = courses_vo[i])
    kb.button(text = 'Назад')
    kb.adjust(4)
    return kb.as_markup(resize_keyboard = True)

def sgvo1() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    for i in range(len(gr_list_1course_vo)):
        kb.button(text = gr_list_1course_vo[i])
    kb.button(text = 'Назад')
    kb.adjust(4)
    return kb.as_markup(resize_keyboard = True)

def sgvo2() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    for i in range(len(gr_list_2course_vo)):
        kb.button(text = gr_list_2course_vo[i])
    kb.button(text = 'Назад')
    kb.adjust(4)
    return kb.as_markup(resize_keyboard = True)

def sgvo3() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    for i in range(len(gr_list_3course_vo)):
        kb.button(text = gr_list_3course_vo[i])
    kb.button(text = 'Назад')
    kb.adjust(4)
    return kb.as_markup(resize_keyboard = True)

def sgvo4() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    for i in range(len(gr_list_4course_vo)):
        kb.button(text = gr_list_4course_vo[i])
    kb.button(text = 'Назад')
    kb.adjust(5)
    return kb.as_markup(resize_keyboard = True)

from aiogram import Router,F,Bot
from configs.cfg import tbt
bot = Bot(token=tbt,parse_mode="HTML")
from aiogram.filters import Command,Filter
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.methods.send_message import SendMessage
from aiogram.fsm.state import StatesGroup, State
from keyboards.admin_keyboard import *
from configs.admins import admin_ids,keyboard
from base.base_conn import BotDB
from subprocess import run

router = Router()
class admin_states(StatesGroup):
    command = State()
    ban_user = State()
    unban_user = State()
    send_mass_message = State()
class user_level_course_group(StatesGroup):
    level = State()
    course = State()
    group = State()
    day = State()

class AdminsFilter(Filter):
    def __init__(self, admins) -> None:
        self.admins = admins
    async def __call__(self, message:Message) -> bool:
        if message.from_user.id not in self.admins :
            return False
        return message.from_user.id in self.admins

@router.message(AdminsFilter(admin_ids),
                user_level_course_group.level,
                F.text == 'Админ-панель')
async def admin_panel(message:Message,state:FSMContext):
    reply_markup=ReplyKeyboardRemove()
    await message.reply(
    "<b>Добро пожаловать в админ-панель.</b>\nВыберите действие: ",
        parse_mode="HTML",
        reply_markup=apanel()
    )
    await state.set_state(admin_states.command)

@router.message(AdminsFilter(admin_ids),
                admin_states.command,
                F.text == keyboard[0])
async def ban_user(message:Message,state:FSMContext):
    reply_markup=ReplyKeyboardRemove()
    await message.reply(
    "<b>Выберите пользователя для блокировки</b>\n",
        parse_mode="HTML",
        reply_markup=ban_panel()
    )
    await state.set_state(admin_states.ban_user)
@router.message(AdminsFilter(admin_ids),
                admin_states.command,
                F.text == keyboard[1])
async def unban_user(message:Message,state:FSMContext):
    reply_markup=ReplyKeyboardRemove()
    await message.reply(
    "<b>Выберите пользователя для разблокировки</b>\n",
        parse_mode="HTML",
        reply_markup=unban_panel()
    )
    await state.set_state(admin_states.unban_user)
@router.message(AdminsFilter(admin_ids),
                admin_states.ban_user)
async def ban_user(message:Message,state:FSMContext):
    username = message.text
    print(username)
    user_ban_id = BotDB.get_user_id_by_username(username)
    print(user_ban_id)
    if BotDB.check_ban(user_ban_id) == 1:
        await message.reply('<b>Пользователь и так заблокирован.</b>',
                            parse_mode="HTML",
                            reply_markup=apanel())
    if user_ban_id not in admin_ids:
        BotDB.give_ban(user_ban_id)
        await message.reply('<b>Пользователь был заблокирован.</b>',
                            parse_mode="HTML",
                            reply_markup=apanel())
    else:
        await message.reply('Данный пользователь является администратором,блокировка не возможна.',
                            parse_mode="HTML",
                            reply_markup=apanel())
    await state.set_state(admin_states.command)

@router.message(AdminsFilter(admin_ids),
                admin_states.unban_user)
async def unban_user(message:Message,state:FSMContext):
    username = message.html_text
    user_unban_id = BotDB.get_user_id_by_username(username)
    BotDB.unban(user_unban_id)
    await message.reply('<b>Пользователь был разблокирован.</b>',
                        parse_mode="HTML",
                        reply_markup=apanel())
    await state.set_state(admin_states.command)
        
@router.message(AdminsFilter(admin_ids),
                admin_states.command,
                F.text == keyboard[2])
async def mass_send(message:Message,state:FSMContext):
    await message.reply('<b>Отправьте текст для массовой рассылки</b>',
                        parse_mode='HTML')
    await state.set_state(admin_states.send_mass_message)

@router.message(AdminsFilter(admin_ids),
                admin_states.send_mass_message)
async def mass_send(message:Message,state:FSMContext):
    text = message.html_text
    for i in range(len(BotDB.get_users_ids())):
        await bot(SendMessage(chat_id = (BotDB.get_users_ids()[i]),text = text,parse_mode='HTML'))
    await message.reply('<b>Рассылка завершена!</b>',parse_mode='HTML',reply_markup=apanel())
    await state.set_state(admin_states.command)


async def update_schedule():
        print('Начато обновление расписания')
        run(["python","refetch_manual.py"])

@router.message(AdminsFilter(admin_ids),
                admin_states.command,
                F.text == keyboard[3])
async def update(message:Message,state:FSMContext):
    for i in range(len(BotDB.get_users_ids())):
        await bot(SendMessage(chat_id = (BotDB.get_users_ids()[i]),text = '<b>Начато обновление расписания.</b>',parse_mode='HTML'))
    await update_schedule()
    for i in range(len(BotDB.get_users_ids())):
        await bot(SendMessage(chat_id = (BotDB.get_users_ids()[i]),text = '<b>Обновление завершено.</b>',parse_mode='HTML'))
    await message.reply('<b>Обновление завершено</b>',parse_mode='HTML',reply_markup=apanel())
    await state.set_state(admin_states.command)

@router.message(AdminsFilter(admin_ids),
                admin_states.command,
                F.text == keyboard[4])
async def clear_users_base(message:Message,state:FSMContext):
    BotDB.clear_users_base()
    await message.reply('<b>БД пользователей отчищена</b>',parse_mode='HTML',reply_markup=apanel())
    await state.set_state(admin_states.command)

@router.message(AdminsFilter(admin_ids),
                admin_states.command,
                F.text == keyboard[5])
async def clear_users_base(message:Message,state:FSMContext):
    BotDB.clear_ban_base()
    await message.reply('<b>БД блокировок отчищена</b>',parse_mode='HTML',reply_markup=apanel())
    await state.set_state(admin_states.command)


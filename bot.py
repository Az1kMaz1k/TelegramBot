import config
import logging
import datetime
import time
import asyncio

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import callback_query, document, message
from aiogram.types.reply_keyboard import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types import Message
from datetime import datetime
from sqliter import Sqliter

# log level
logging.basicConfig(level=logging.INFO)

# bot init
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

# connection database
db = Sqliter('db.db')

# global
user_name = ""
flag = False
f_chat_id = ""
i = 1

# bot starting
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
	"""This handler will be called when user sends `/start` command"""
	arg = message.get_args()
	global user_name
	user_name = arg
	global flag
	global f_chat_id
	f_chat_id = message.chat.id
	if user_name == "GPZYEJ":
		button_all_user = KeyboardButton(text="BUTTON_FOR_ADMIN")
		kb1 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_all_user)
		await message.answer("TEXT_FOR_ADMIN", reply_markup=kb1)
	elif user_name != "":
		try:
			if not (db.check_user(message.from_user.id)):
				db.new_user(message.from_user.id, user_name)
		except Exception as ex:
			print(ex)
		inline_btn_1 = InlineKeyboardButton('INLINE_BUTTON_USER', callback_data='button1')
		inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)
		await message.answer("TEXT_FOR_USER", reply_markup=inline_kb1)

# press button1
@dp.callback_query_handler(text="button1")
async def process_callback_button1(call: types.CallbackQuery):
	await call.message.answer("TEXT_FOR_USER")
	time.sleep(3)
	await call.message.answer("TEXT_FOR_USER")
	time.sleep(3)
	with open ("PHOTO.jpg", "rb") as f:
		f_photo = f.read()
		await call.message.answer_photo(photo=f_photo)
		f.close()
	if user_name == "AGUIDZ":
		url = "URL_USER1"
	elif user_name == "YEASIZ":
		url = "URL_USER2"
	elif user_name == "HXOETB":
		url = "URL_USER3"
	elif user_name == "FCAMDY":
		url = "URL_USER4"
	elif user_name == "IMPXJJ":
		url = "URL_USER5"

	inline_btn = InlineKeyboardButton("INLINE_BUTTON_USER", url=url)
	inline_link = InlineKeyboardMarkup().add(inline_btn)
	await call.message.answer("TEXT_FOR_USER", reply_markup=inline_link)

# If user somthing write
@dp.message_handler()
async def somthing_text(message: types.Message):
	"""This handler will be called when user sends some text"""
	if message.text == "TEXT_FOR_ADMIN":
		await message.answer("INSTRUCTION_FOR_ADMIN")
	elif len(message.text) == 6:
		try:
			result = db.get_user(message.text)
			await message.answer(f"BD_REQUEST: {len(result)}")
		except Exception as ex:
			print(ex)
	else:
		await message.answer("""MESSAGE_FOR_USER""")

# loop
async def scheduled(wait_for):
	while True:
		await asyncio.sleep(wait_for)
		times = datetime.now().strftime('%H')
		result = db.get_all_user()
		if times == "10":
			await morning(result)
		elif times == "14" or times == "24" or times == "00":
			await dinner(result)
		elif times == "18" or times =="06":
			await evening(result)
		elif times == "22":
			await night(result)

# morning
async def morning(users):
	try:
		for user in users:
			with open("PHOTO.jpg", "rb") as f:
				s_photo = f.read()
				await bot.send_photo(chat_id=user[1], photo=s_photo)
				f.close()
			if user[2] == "AGUIDZ":
				url = "URL_USER1"
			elif user[2] == "YEASIZ":
				url = "URL_USER2"
			elif user[2] == "HXOETB":
				url = "URL_USER3"
			elif user[2] == "FCAMDY":
				url = "URL_USER4"
			elif user[2] == "IMPXJJ":
				url = "URL_USER5"

			inline_btn = InlineKeyboardButton("INLINE_BUTTON_USER", url=url)
			inline_link = InlineKeyboardMarkup().add(inline_btn)
			await bot.send_message(chat_id=user[1], text="TEXT_FOR_USER", reply_markup=inline_link)
	except Exception as ex:
		pass

# dinner
async def dinner(users):
	try:
		for user in users:
			if user[2] == "AGUIDZ":
				url = "URL_USER1"
			elif user[2] == "YEASIZ":
				url = "URL_USER2"
			elif user[2] == "HXOETB":
				url = "URL_USER3"
			elif user[2] == "FCAMDY":
				url = "URL_USER4"
			elif user[2] == "IMPXJJ":
				url = "URL_USER5"

			inline_btn = InlineKeyboardButton("TEXT_FOR_USER", url=url)
			inline_link = InlineKeyboardMarkup().add(inline_btn)
			await bot.send_message(chat_id=user[1], text="TEXT_FOR_USER", reply_markup=inline_link)
	except Exception as ex:
		pass

# evening
async def evening(users):
	try:
		for user in users:
			with open("PHOTO.jpg", "rb") as f:
				t_photo = f.read()
				await bot.send_photo(chat_id=user[1], photo=t_photo)
				f.close()
			if user[2] == "AGUIDZ":
				url = "URL_USER1"
			elif user[2] == "YEASIZ":
				url = "URL_USER2"
			elif user[2] == "HXOETB":
				url = "URL_USER3"
			elif user[2] == "FCAMDY":
				url = "URL_USER4"
			elif user[2] == "IMPXJJ":
				url = "URL_USER5"

			inline_btn = InlineKeyboardButton("TEXT_FOR_USER", url=url)
			inline_link = InlineKeyboardMarkup().add(inline_btn)
			await bot.send_message(chat_id=user[1], text="TEXT_FOR_USER", reply_markup=inline_link)
	except Exception as ex:
		pass

# night
async def night(users):
	try:
		for user in users:
			if user[2] == "AGUIDZ":
				url = "URL_USER1"
			elif user[2] == "YEASIZ":
				url = "URL_USER2"
			elif user[2] == "HXOETB":
				url = "URL_USER3"
			elif user[2] == "FCAMDY":
				url = "URL_USER4"
			elif user[2] == "IMPXJJ":
				url = "URL_USER5"

			inline_btn = InlineKeyboardButton("INLINE_BUTTON_USER", url=url)
			inline_link = InlineKeyboardMarkup().add(inline_btn)
			await bot.send_message(chat_id=user[1], text="TEXT_FOR_USER", reply_markup=inline_link)
	except Exception as ex:
		pass

# run long-polling
if __name__ == "__main__":
	loop = asyncio.get_event_loop()
	loop.create_task(scheduled(3600))
	executor.start_polling(dp, skip_updates=True)
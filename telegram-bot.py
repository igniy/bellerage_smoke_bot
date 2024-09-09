from aiogram import Bot, Dispatcher, utils, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
  
bot = Bot(token='7109024137:AAEUOxC-4pIXhv4FdRKFdy7gHIDqPSdcuxs') 
  
dp = Dispatcher(bot) 
  
buttonSmoke = InlineKeyboardButton(text="Курить!", callback_data="smoke_button")
buttonTurnik = InlineKeyboardButton(text="Турник!", callback_data="turnik_button")  
keyboard_inline = InlineKeyboardMarkup().add(buttonSmoke)
keyboard_inline = InlineKeyboardMarkup().add(buttonTurnik) 
 
  
@dp.message_handler(commands=['start']) 
async def check(message: types.Message): 
    await message.reply("Нажми 'КУРИТЬ!' чтобы пойти курить", reply_markup=keyboard_inline)  
  
@dp.callback_query_handler(text=["smoke_button", ]) 
async def check_button(call: types.CallbackQuery): 

    if call.data == "smoke_button": 
        await call.message.answer("КУРИТЬ🚬!" + call.data.from_user.first_name)
    if call.data == "turnik_button": 
        await call.message.answer("ТУРНИК💪!" + call.data.from_user.first_name)
    await call.answer() 
   
executor.start_polling(dp)

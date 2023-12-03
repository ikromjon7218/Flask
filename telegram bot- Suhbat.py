from aiogram import Bot, Dispatcher, types
from aiogram import executor

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "6815105567:AAEspRzAWWLnxFa7isT8J30Thb3kyeoJIwU"


bot = Bot(TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def salomlash(xabar: types.Message):
    await xabar.answer(f"Assalomu alaykum {xabar.from_user.full_name}")

@dp.message_handler()
async def toti(xabar: types.Message):
    if xabar.text.lower() == "maslahat":
        import requests
        natija = requests.get("https://api.adviceslip.com/advice")

        maslahat = natija.json()['slip']['advice']
        from googletrans import Translator

        tr = Translator()

        tarjima_soz = tr.translate(maslahat, dest="uz")

        await xabar.answer(tarjima_soz.text)
    foydalanuvchi_xabari = xabar.text
    javob_xabari = f"Siz xali bu yozgan gapingiz uchun javob berasiz siz menga ({foydalanuvchi_xabari}) dedingiz buning uchun kerakli joyga yozaman."
    print(foydalanuvchi_xabari, xabar.from_user.full_name)
    await xabar.answer(javob_xabari)



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

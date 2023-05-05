from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
TOKEN = "5692605421:AAEJM8PdJ-oYEwtzxExm2QnBaTd10MRVaCk"
menu = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Oziq-ovqat")],
                                        [KeyboardButton(text="Elektrotexnika")],
                                       [KeyboardButton(text="Savat")]
                                       ],resize_keyboard=True)
savat = dict()


oziq_ovqat = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[

    [KeyboardButton(text="🍎 Olma"), KeyboardButton(text="🍐 Nok")],

    [KeyboardButton(text="Anor"), KeyboardButton(text="🍇 Uzum")],

    [KeyboardButton(text="⬅️ orqaga"),
    KeyboardButton(text="Bosh menu")]

    ])
elektronika = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[

    [KeyboardButton(text="🎹 Pianina"), KeyboardButton(text="🎧 Quloqchin")],

    [KeyboardButton(text="🎤 Simsiz mikrofon"), KeyboardButton(text="🥁 Udarnik")],

    [KeyboardButton(text="⬅️ orqaga"),
    KeyboardButton(text="Bosh menu")]

    ])

buyurtma_callback = CallbackData("nom", "qaytuvchi_nom")
buyurtma_inline_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Buyurtma qilish", callback_data=buyurtma_callback.new(qaytuvchi_nom="Buyurtma_qilindi"))]
])
bot = Bot(TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def salomlash(xabar: types.Message):
    await xabar.answer(f"Assalomu alaykum {xabar.from_user.full_name}\nDo'konimizga xush kelibsiz.", reply_markup=menu)
    print(xabar.from_user)

@dp.message_handler(text="oziq-ovqat")
async def oziq_ovqat(xabar : types.Message):
    await xabar.answer("Mahsulotlar bo'limi: ", reply_markup=oziq_ovqat)

@dp.message_handler(text="Elektrotexnika")
async def elektrotexnika(xabar : types.Message):
    await xabar.answer("Mahsulotlar bo'limi: ", reply_markup=elektronika)

@dp.message_handler(text="⬅️ orqaga")
async def orqaga11(xabar : types.Message):
    await xabar.answer("Bosh menu bo'limi: ", reply_markup=menu)

@dp.message_handler(text="Bosh menu")
async def bosh_menu(xabar : types.Message):
    await xabar.answer("Bosh menu bo'limi: ", reply_markup=menu)

@dp.message_handler(text="Savat")
async def savat(xabar : types.Message):
    msg = "Mahsulotlar:\n\n"
    for mahsulotlar, mmiqdor in savat.items():
        msg += f"{mahsulotlar} - {mmiqdor} ta\n"
    await xabar.answer(msg, reply_markup=buyurtma_inline_button)
# @dp.message_handler()
# async def salomlash2(xabar : types.Message):


# @dp.callback_query_handler(buyurtma_callback.filter(qaytuvchi_nom="Buyurtma_qilindi"))
# async def buyurtma_qilinmoqda(xabar: types.CallbackQuery):
#     await xabar.message.edit_reply_markup()
#     await xabar.answer("Buyurtma qilindi")
#     await xabar.message.answer("Buyurtma qilindi")

@dp.message_handler()
async def orqag(xabar: types.Message):
    if xabar.text == "🍎 Olma":
        if xabar.text not in savat.keys():
            savat['🍎 Olma'] = 1
            await xabar.answer("Mahsulot savatga qo'shildi:")
        else:
            savat['🍎 Olma'] += 1
            await xabar.answer(f"Mahsulot savatga qo'shildi:\nSavatda {savat.get('🍎 Olma')} ta 🍎 Olma mavjud")

    elif xabar.text == "🍐 Nok":
        if xabar.text not in savat.keys():
            savat['🍐 Nok'] = 1
            await xabar.answer("Mahsulot savatga qo'shildi:")
        else:
            savat['🍐 Nok'] += 1
            await xabar.answer(f"Mahsulot savatga qo'shildi:\nSavatda {savat.get('🍐 Nok')} ta 🍐 Nok mavjud")
    elif xabar.text == "Anor":
        if xabar.text not in savat.keys():
            savat["Anor"] = 1
            await xabar.answer("Mahsulot savatga qo'shildi:")
        else:
            savat['Anor'] += 1
            await xabar.answer(f"Mahsulot savatga qo'shildi:\nSavatda {savat.get('Anor')} ta Anor mavjud")
    elif xabar.text == "🍇 Uzum":
        if xabar.text not in savat.keys():
            savat['🍇 Uzum'] = 1
            await xabar.answer("Mahsulot savatga qo'shildi:")
        else:
            savat['🍇 Uzum'] += 1
            await xabar.answer(f"Mahsulot savatga qo'shildi:\nSavatda {savat.get('🍇 Uzum')} ta 🍇 Uzum mavjud")

    elif xabar.text == "🎹 Pianina":
        if xabar.text not in savat.keys():
            savat["🎹 Pianina"] = 1
            await xabar.answer("Mahsulot savatga qo'shildi:")
        else:
            savat["🎹 Pianina"] += 1
            await xabar.answer(f"Mahsulot savatga qo'shildi:\nSavatda {savat.get('🎹 Pianina')} ta 🎹 Pianina mavjud")

    elif xabar.text == "🎧 Quloqchin":
        if xabar.text not in savat.keys():
            savat['🎧 Quloqchin'] = 1
            await xabar.answer("Mahsulot savatga qo'shildi:")
        else:
            savat['🎧 Quloqchin'] += 1
            await xabar.answer(f"Mahsulot savatga qo'shildi:\nSavatda {savat.get('🎧 Quloqchin')} ta 🎧 Quloqchin mavjud")
    elif xabar.text == "🎤 Simsiz mikrofon":
        if xabar.text not in savat.keys():
            savat['🎤 Simsiz mikrofon'] = 1
            await xabar.answer("Mahsulot savatga qo'shildi:")
        else:
            savat['🎤 Simsiz mikrofon'] += 1
            await xabar.answer(f"Mahsulot savatga qo'shildi:\nSavatda {savat.get('🎤 Simsiz mikrofon')} ta 🎤 Simsiz mikrofon mavjud")
    elif xabar.text == "🥁 Udarnik":
        if xabar.text not in savat.keys():
            savat['🥁 Udarnik'] = 1
            await xabar.answer("Mahsulot savatga qo'shildi:")
        else:
            savat['🥁 Udarnik'] += 1
            await xabar.answer(f"Mahsulot savatga qo'shildi:\nSavatda {savat.get('🥁 Udarnik')} ta 🥁 Udarnik mavjud")



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

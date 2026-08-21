import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# Настройка логирования для облачного контейнера
logging.basicConfig(level=logging.INFO)

# Получение токена из переменных окружения
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("8806712173:AAH7kznvYK03XuWO3DP1WxNmRbqVQwY44VY")

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Главное меню (Reply-клавиатура)
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="О нас")],
        [KeyboardButton(text="Направления"), KeyboardButton(text="Контакты")],
    ],
    resize_keyboard=True,
    persistent=True,
)


# Обработчик команды /start
@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    welcome_text = (
        f"Саламатсыз ба, {message.from_user.first_name}!\n"
        "Добро пожаловать в бот Молодежного ресурсного центра!\n\n"
        "Мы созданы для поддержки молодежи, реализации социальных проектов "
        "и развития волонтерского движения.\n\n"
        "Выберите интересующий вас раздел в меню ниже:"
    )
    await message.answer(welcome_text, reply_markup=main_keyboard)


# Обработчик кнопки "О нас"
@dp.message(F.text == "О нас")
async def about_us(message: types.Message):
    info_text = (
        "<b>🏛 Молодежный ресурсный центр</b> — это единая площадка "
        "для развития, самореализации и поддержки инициатив молодежи.\n\n"
        "<b>Наша миссия:</b> Создание условий для всестороннего развития молодежи, "
        "поддержка гражданских инициатив и помощь в трудоустройстве.\n\n"
        "<b>Что мы предлагаем:</b>\n"
        "• Консультации по государственным программам\n"
        "• Волонтерские и социальные проекты\n"
        "• Тренинги, мастер-классы и форумы\n"
        "• Поддержка молодежных стартапов и инициатив"
    )
    await message.answer(info_text, parse_mode="HTML")


# Обработчик кнопки "Направления"
@dp.message(F.text == "Направления")
async def directions(message: types.Message):
    directions_text = (
        "<b>📌 Основные направления нашей работы:</b>\n\n"
        "<b>1. Волонтерское движение</b>\n"
        "Развитие добровольчества, участие в социальных и экологических акциях.\n\n"
        "<b>2. Трудоустройство и профориентация</b>\n"
        "Помощь в поиске работы, составление резюме, организация ярмарок вакансий.\n\n"
        "<b>3. Поддержка инициатив</b>\n"
        "Содействие в участии в грантовых конкурсах и реализация проектов.\n\n"
        "<b>4. Культура, спорт и досуг</b>\n"
        "Организация турниров (Street Workout, караоке), праздничных и молодежных мероприятий."
    )
    await message.answer(directions_text, parse_mode="HTML")


# Обработчик кнопки "Контакты"
@dp.message(F.text == "Контакты")
async def contacts(message: types.Message):
    contacts_text = (
        "<b>📍 Наши контакты:</b>\n\n"
        "<b>Адрес:</b> ул. Сатпаева, 7\n"
        "<b>График работы:</b> Пн–Пт, с 09:00 до 18:30 (Обед: 13:00–14:30)\n"
        "<b>Телефон:</b> +7 (700) 000-00-00\n"
        "<b>Email:</b> info@mrc-youth.kz\n\n"
        "Будем рады видеть вас в нашем центре!"
    )
    await message.answer(contacts_text, parse_mode="HTML")


# Запуск асинхронного цикла
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

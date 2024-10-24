import logging
import os
import django
from aiogram import Bot, types
from aiogram import F
from aiogram import Router
from aiogram import Application
from aiogram.filters import Command
from aiogram.utils import executor
from flowers.models import Order
from config import TELEGRAM_BOT_TOKEN

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота
bot = Bot(token=TELEGRAM_BOT_TOKEN)
application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

# Создаем маршрутизатор
router = Router()

# Команда /start
@router.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer("Привет! Используйте /new_order <order_id> для получения информации о новом заказе и /orders для просмотра статуса всех заказов.")

# Команда для получения информации о новом заказе
@router.message(Command("new_order"))
async def new_order_command(message: types.Message):
    args = message.get_args()
    if not args:
        await message.answer("Пожалуйста, укажите ID заказа.")
        return

    try:
        order_id = int(args[0])
        order = Order.objects.get(id=order_id)
        await message.answer(f"Заказ {order.id}: {order.products} - Статус: {order.status}")
    except ValueError:
        await message.answer("ID заказа должен быть числом.")
    except Order.DoesNotExist:
        await message.answer("Заказ не найден.")

# Команда для отображения всех заказов
@router.message(Command("orders"))
async def orders_command(message: types.Message):
    orders_list = Order.objects.all()
    if not orders_list:
        await message.answer("Нет заказов.")
        return

    response = "Список всех заказов:\n"
    for order in orders_list:
        response += f"Заказ {order.id}: {order.products} - Статус: {order.status}\n"

    await message.answer(response)

# Регистрируем маршрутизатор
application.include_router(router)

if __name__ == '__main__':
    logging.info("Starting bot...")
    application.run_polling(skip_updates=True)

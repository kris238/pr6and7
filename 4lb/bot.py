import telebot
from telebot.types import ReplyKeyboardMarkup
import random

bot = telebot.TeleBot('YOUR_API_TOKEN')

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(
        message.chat.id,
        "Привет! Я бот с рецептами выпечки. Выбери опцию ниже:",
        reply_markup=create_keyboard()
    )

recipes = {
    "🍎 Яблочный пирог": "Ингредиенты: 2 стакана муки, 200 г масла, 1 стакан сахара, 4 яблока...",
    "🍫 Шоколадный кекс": "Ингредиенты: 1.5 стакана муки, 1 стакан сахара, 100 г какао...",
    "🍪 Овсяное печенье": "Ингредиенты: 1 стакан овсянки, 0.5 стакана муки, 100 г масла...",
    "🍌 Банановый хлеб": "Ингредиенты: 3 спелых банана, 2 стакана муки, 1 стакан сахара...",
    "🧀 Сырники": "Ингредиенты: 500 г творога, 2 яйца, 3 ст.л. сахара...",
    "🥞 Блины": "Ингредиенты: 2 стакана молока, 2 яйца, 1.5 стакана муки...",
    "🥬 Пирожки с капустой": "Ингредиенты: 500 г теста, 300 г тушеной капусты...",
    "🍰 Чизкейк": "Ингредиенты: 200 г печенья, 100 г масла, 500 г творожного сыра..."
}

def create_keyboard():
    keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    buttons = list(recipes.keys()) + ["Случайный рецепт", "Поиск по ингредиентам", "Добавить рецепт", "Советы по выпечке", "Список рецептов", "Поделиться рецептом"]
    keyboard.add(*buttons)
    return keyboard

@bot.message_handler(func=lambda message: message.text in recipes)
def send_recipe(message):
    recipe = message.text
    bot.send_message(message.chat.id, recipes[recipe])

@bot.message_handler(func=lambda message: message.text == "Случайный рецепт")
def random_recipe(message):
    recipe = random.choice(list(recipes.keys()))
    bot.send_message(message.chat.id, f"Ваш случайный рецепт: {recipe}\n{recipes[recipe]}")

@bot.message_handler(func=lambda message: message.text == "Поиск по ингредиентам")
def search_by_ingredient(message):
    bot.send_message(message.chat.id, "Введите ингредиент:")
    bot.register_next_step_handler(message, find_by_ingredient)

def find_by_ingredient(message):
    ingredient = message.text.lower()
    found_recipes = [name for name, recipe in recipes.items() if ingredient in recipe.lower()]

    if found_recipes:
        response = "\n".join(found_recipes)
        bot.send_message(message.chat.id, f"Рецепты с ингредиентом '{ingredient}':\n{response}")
    else:
        bot.send_message(message.chat.id, f"Рецепты с ингредиентом '{ingredient}' не найдены.")

@bot.message_handler(func=lambda message: message.text == "Добавить рецепт")
def add_recipe(message):
    bot.send_message(message.chat.id, "Введите название вашего рецепта:")
    bot.register_next_step_handler(message, process_recipe_name)

def process_recipe_name(message):
    recipe_name = message.text
    bot.send_message(message.chat.id, "Введите ингредиенты:")
    bot.register_next_step_handler(message, process_recipe_ingredients, recipe_name)

def process_recipe_ingredients(message, recipe_name):
    ingredients = message.text
    recipes[recipe_name] = f"Ингредиенты: {ingredients}"
    bot.send_message(message.chat.id, f"Рецепт '{recipe_name}' добавлен!")

@bot.message_handler(func=lambda message: message.text == "Советы по выпечке")
def baking_tips(message):
    tips = "1. Используйте свежие ингредиенты.\n2. Хорошо перемешивайте тесто.\n3. Не открывайте духовку слишком часто.\n4. Дайте тесту отдохнуть."
    bot.send_message(message.chat.id, tips)

@bot.message_handler(func=lambda message: message.text == "Список рецептов")
def list_recipes(message):
    response = "\n".join(recipes.keys())
    bot.send_message(message.chat.id, f"Доступные рецепты:\n{response}")

@bot.message_handler(func=lambda message: message.text == "Поделиться рецептом")
def share_recipe(message):
    bot.send_message(message.chat.id, "Введите название рецепта, который хотите поделиться:")
    bot.register_next_step_handler(message, process_share_recipe)


def process_share_recipe(message):
    recipe_name = message.text
    if recipe_name in recipes:
        bot.send_message(message.chat.id, f"Рецепт '{recipe_name}':\n{recipes[recipe_name]}")
    else:
        bot.send_message(message.chat.id, f"Рецепт '{recipe_name}' не найден.")


if __name__ == '__main__':
    bot.polling(none_stop=True)

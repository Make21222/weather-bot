import telebot
import requests

# 🔑 ВСТАВЬ СВОИ ТОКЕНЫ СЮДА!
TELEGRAM_TOKEN = '8264467003:AAGXZOP9AVlRsXEETWJwoROz73S3O1clb6w'
WEATHER_API_KEY = '1f3400eb9ab8e244392fabb1092001cc'

# 🤖 Создаем бота
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# 🌍 Функция для получения погоды
def get_weather(city_name):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={WEATHER_API_KEY}&units=metric&lang=ru"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        return f"🌡 В {city_name} сейчас {temp}°C, {description}"
    else:
        return "❌ Город не найден. Попробуй ещё раз."

# 💬 Обрабатываем текстовые сообщения
@bot.message_handler(content_types=['text'])
def handle_message(message):
    city = message.text
    weather_info = get_weather(city)
    bot.reply_to(message, weather_info)

# ▶️ Запускаем бота
print("Бот запущен!")
bot.polling()
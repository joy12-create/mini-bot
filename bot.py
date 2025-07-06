import telebot

TOKEN =7845329836:AAH0lqvmm_23sP6tatarygpv0QFYgoUZDjA
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I'm your mini Telegram bot.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

print("Bot is running...")
bot.polling()

import telebot

from config import config

bot = telebot.TeleBot(config.TELEGRAM_BOT_TOKEN)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, f'{message.text}, милашка!')


if __name__ == '__main__':
    bot.infinity_polling()

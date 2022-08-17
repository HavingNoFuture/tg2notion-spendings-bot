import telebot

from config import config

bot = telebot.TeleBot(config.TELEGRAM_BOT_TOKEN)


@bot.message_handler(content_types=["text"])
def text_message_handler(message: telebot.types.Message) -> None:
    """Обработчик текстового сообщения"""
    bot.send_message(message.chat.id, f'{message.text}, милашка!')


if __name__ == '__main__':
    bot.infinity_polling()

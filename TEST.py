import telebot
from telebot import types

TOKEN = '7864554383:AAE6_92zJU5_X1PGQ2lajzsZ3pqVxSEj8do'
bot = telebot.TeleBot(TOKEN)

# دالة البدء: تعرض قائمة المواد
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(
        types.InlineKeyboardButton("مادة الرياضيات", callback_data='math'),
        types.InlineKeyboardButton("مادة الفيزياء", callback_data='physics'),
        types.InlineKeyboardButton("مادة الكيمياء", callback_data='chemistry')
    )
    bot.send_message(message.chat.id, 'اختر المادة:', reply_markup=keyboard)

# دالة التعامل مع اختيار المستخدم
@bot.callback_query_handler(func=lambda call: True)
def process_callback(call):
    if call.data == 'math':
        bot.send_message(call.message.chat.id, "إليك اختبارات مادة الرياضيات:")
        bot.send_photo(call.message.chat.id, photo='https://drive.google.com/uc?export=view&id=1L15fVK_l4fxYLQ9Q0uzSN6gXNcy7FytR')
        bot.send_photo(call.message.chat.id, photo='https://drive.google.com/uc?export=view&id=1L15fVK_l4fxYLQ9Q0uzSN6gXNcy7FytR')
    elif call.data == 'physics':
        bot.send_message(call.message.chat.id, "إليك اختبارات مادة الفيزياء:")
        bot.send_photo(call.message.chat.id, photo='https://drive.google.com/uc?export=view&id=1L15fVK_l4fxYLQ9Q0uzSN6gXNcy7FytR')
        bot.send_photo(call.message.chat.id, photo='https://drive.google.com/uc?export=view&id=1L15fVK_l4fxYLQ9Q0uzSN6gXNcy7FytR')
    elif call.data == 'chemistry':
        bot.send_message(call.message.chat.id, "إليك اختبارات مادة الكيمياء:")
        bot.send_photo(call.message.chat.id, photo='https://drive.google.com/uc?export=view&id=1L15fVK_l4fxYLQ9Q0uzSN6gXNcy7FytR')
        bot.send_photo(call.message.chat.id, photo='https://drive.google.com/uc?export=view&id=1L15fVK_l4fxYLQ9Q0uzSN6gXNcy7FytR')

# بدء تشغيل البوت
if __name__ == '__main__':
    bot.polling(none_stop=True)

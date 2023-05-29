import telebot
from deep_translator import GoogleTranslator as tr


# bot father yordamida yaratgan botimizni tokenini olamiz
TOKEN = "6091505855:AAHL7jWq9pzvdXROsRYFI36KyEQNSkTlrk8"


bot = telebot.TeleBot(TOKEN)

# botga start buyruyrug'ini yuborganda funksiyani bajaradi.
@bot.message_handler(commands=['start'])

# hisoblashni boshlash uchun har xil buyruqlarni bajaramiz
def boshlov(message):
        bot.send_message(message.chat.id,"salom")
@bot.message_handler(content_types=['text'])
def tran(message):
        bot.send_message(message.chat.id,"matn yuboring")
        bot.register_next_step_handler(message,translate1)
def translate1(message):
    text = tr(source='uz', target='en').translate(message.text)
    bot.send_message(message.chat.id, text)
        
bot.polling(none_stop=True)

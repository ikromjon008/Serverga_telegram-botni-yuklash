import telebot


# bot father yordamida yaratgan botimizni tokenini olamiz
TOKEN = "5773060087:AAHpLmsAqn4b8eIQaL997SX85N7wRE5R2WQ"


bot = telebot.TeleBot(TOKEN)

# botga start buyruyrug'ini yuborganda funksiyani bajaradi.
@bot.message_handler(commands=['start'])


# hisoblashni boshlash uchun har xil buyruqlarni bajaramiz
def boshlov(message):
	if (message.text == '/start'):
		bot.reply_to(message, "Assalomu alaykum botimizga xush keldingiz! ")
    
bot.polling(none_stop=True)

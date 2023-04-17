import telebot

# Replace YOUR_BOT_TOKEN with your bot token
bot = telebot.TeleBot('6261425349:AAHDit0-4gIUSHOBabfkARIuVWtjIIkXV_8')

# Handler for the start command
@bot.message_handler(commands=['start'])
def welcome_message(message):
    # Construct the welcome message
    welcome_text = "Hi there! Welcome to my bot. I'm here to help you with whatever you need. To get started, just send me a message."
    
    # Send the welcome message
    bot.reply_to(message, welcome_text)

# Start the bot
bot.polling()
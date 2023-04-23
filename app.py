import telebot
from telebot import types

bot_token = "6244396357:AAHs-wyMlu7R7SZ2gFP9jTAmUoCQ02Byo24"

bot = telebot.TeleBot(bot_token)
users = set()
users = {}
# Replace ADMIN_CHAT_ID_HERE with the chat ID of the admin
admin_chat_id = "1941354467"

# Dictionary to keep track of which buttons have been clicked
clicked_buttons = {}


@bot.message_handler(commands=['start'])
def start_command(message):
  chat_id = message.chat.id
  bot.send_chat_action(chat_id, 'typing')

  # Create inline keyboard with a single button
  markup = types.InlineKeyboardMarkup(row_width=2)
  markup.add(
    types.InlineKeyboardButton("🤖 My Bots", callback_data="button_clicked"),
    types.InlineKeyboardButton("📢 My Channle", url="https://t.me/GTIDev"))

  markup.add(
    types.InlineKeyboardButton("💬 Contact Me", callback_data="contact_home"))

  # Add user's clickable name to the message
  user_id = message.from_user.id
  user_name = message.from_user.first_name
  mention = f'<a href="tg://user?id={user_id}">{user_name}</a>'
  bot.send_message(
    chat_id,
    f"Hi {mention}, \n\nthis bot lets you contact me and know more about me.",
    parse_mode='HTML',
    reply_markup=markup)


# Initialize a dictionary to keep track of clicked buttons
clicked_buttons = {}


@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):

  if call.data == "button_clicked":
    bot.answer_callback_query(call.id)

    # Delete the start_command message
    bot.delete_message(call.message.chat.id, call.message.message_id)

    # Create inline keyboard with a single button to go back to home
    markup = types.InlineKeyboardMarkup(row_width=3)
    markup.add(
      types.InlineKeyboardButton("🤖 Image to Text [OCR] ",
                                 url="https://t.me/ImagetoTextGTIBot"),
      types.InlineKeyboardButton("🧾", callback_data="1"),
    )

    markup.add(
      types.InlineKeyboardButton("🤖 GTI Bot ",
                                 url="https://t.me/GettechinfoBot"),
      types.InlineKeyboardButton("🧾", callback_data="2"),
    )

    markup.add(
      types.InlineKeyboardButton("Back to Home", callback_data="back_home"))
    bot.send_message(call.message.chat.id,
                     "Here's a list of bots developed by me:",
                     reply_markup=markup)

  elif call.data == "back_home":
    bot.answer_callback_query(call.id)

    # Delete the message sent by handle_callback_query
    bot.delete_message(call.message.chat.id, call.message.message_id)
    # Send the start_command message again
    start_command(call.message)

  elif call.data == "1":
    if "1" not in clicked_buttons:
      bot.answer_callback_query(
        call.id,
        show_alert=True,
        text=
        "▫️Send me any image contains text, i will try to extract text from it.😊"
      )
      clicked_buttons["1"] = True

  elif call.data == "2":
    if "2" not in clicked_buttons:
      bot.answer_callback_query(call.id,
                                show_alert=True,
                                text="▫️Channel Bot😊")
      clicked_buttons["2"] = True

  elif call.data == "contact_home":
    bot.answer_callback_query(call.id)

    # Delete the start_command message
    bot.delete_message(call.message.chat.id, call.message.message_id)

    # Create inline keyboard with different contact reasons
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
      types.InlineKeyboardButton("🤖 About Bots", callback_data="bots_me"),
      types.InlineKeyboardButton("📢 About Channles", callback_data="channle"),
    )
    markup.add(
      types.InlineKeyboardButton("🔙 Back to Home", callback_data="back_home"))

    bot.send_message(call.message.chat.id,
                     "What's the reason you'd like to contact me?",
                     reply_markup=markup)

  elif call.data == "bots_me":
    bot.answer_callback_query(call.id)

    # Delete the start_command message
    bot.delete_message(call.message.chat.id, call.message.message_id)

    bot.send_message(call.message.chat.id,
                     "Send now (max 100 characters). \n\n⛔ Not Reply")

    # Register a message handler for bot username

    @bot.message_handler(func=lambda message: True)
    def handle_username(message):
      if message.reply_to_message is None:
        admin_message = f"\nUser: @{message.from_user.username} \nNew Message #Bot \n\n{message.text}"

      # Send reply message to admin
      bot.send_message(admin_chat_id, admin_message)

      # Send confirmation message to user
      user_message = "Your message been received to admin. \nThankyou"
      bot.send_message(message.chat.id, user_message, reply_markup=markup)

    # Create inline keyboard with back button
    markup = types.InlineKeyboardMarkup(row_width=1)

    markup.add(
      types.InlineKeyboardButton("🔙 Back", callback_data="contact_home"))

  elif call.data == "channle":
    bot.answer_callback_query(call.id)

    # Delete the start_command message
    bot.delete_message(call.message.chat.id, call.message.message_id)

    bot.send_message(call.message.chat.id, "Send now\n\n⛔ Not Reply")

    # Register a message handler for bot username
    @bot.message_handler(func=lambda message: True)
    def handle_username(message):
      if message.reply_to_message is None:
        admin_message = f"\nUser: @{message.from_user.username} \nNew Message #channle \n\n{message.text}"

      # Send reply message to admin
      bot.send_message(admin_chat_id, admin_message)

      # Send confirmation message to user
      user_message = "Your message been received to admin. \nThankyou"
      bot.send_message(message.chat.id, user_message, reply_markup=markup)

    # Create inline keyboard with back button
    markup = types.InlineKeyboardMarkup(row_width=1)

    markup.add(
      types.InlineKeyboardButton("🔙 Back", callback_data="contact_home"))

  elif call.data == "questions":
    bot.answer_callback_query(call.id)


# Start the bot
print("Hey, I am up...")
bot.polling()

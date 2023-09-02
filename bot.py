
   import logging
   from telegram.ext import Updater, CommandHandler

   # Inisialisasi bot dengan token dari BotFather
   updater = Updater(token='6592288337:AAGw0ni9sboukpm2-liE-j1bDpGHl5G98zo', use_context=True)
   dispatcher = updater.dispatcher

   # Fungsi untuk menangani perintah /start
   def start(update, context):
       context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm a chess bot.")

   # Menambahkan handler perintah /start ke bot
   start_handler = CommandHandler('start', start)
   dispatcher.add_handler(start_handler)

   # Menjalankan bot
   updater.start_polling()
   

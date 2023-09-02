import chess
import chess.svg
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler

def start(update, context):
    update.message.reply_text('Halo! Untuk memulai permainan, ketik "/main".')

def play_chess(update, context):
    query = update.inline_query.query
    if not query:
        return
    results = []
    board = chess.Board()
    moves = query.split()
    for move in moves:
        try:
            board.push_san(move)
        except ValueError:
            break
    if board.is_game_over():
        results.append(
            InlineQueryResultArticle(
                id='1',
                title='Permainan Selesai',
                input_message_content=InputTextMessageContent('Permainan Selesai.'))
        )
    else:
        results.append(
            InlineQueryResultArticle(
                id='1',
                title='Permainan Berlanjut',
                input_message_content=InputTextMessageContent(board.fen()))
        )
    update.inline_query.answer(results)

def main():
    updater = Updater('6592288337:AAGw0ni9sboukpm2-liE-j1bDpGHl5G98zo', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(InlineQueryHandler(play_chess))
    dp.add_handler(CommandHandler('start', start))
    updater.start_polling()
    updater.idle()

if name == 'main':
    main()

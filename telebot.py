from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, CallbackContext

TOKEN = 'BOT-API-TOKEN'
GAME_SHORT_NAME = 'GAME-SHORT-NAME' 
GAME_URL = 'URL-OF-GAME-WEBSITE'  


async def start(update: Update, context: CallbackContext) -> None:
    await context.bot.send_game(chat_id=update.effective_chat.id, game_short_name=GAME_SHORT_NAME)

async def game_callback(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer(url=GAME_URL)

def main():
    application = ApplicationBuilder().token(TOKEN).build()

    # /start command handler
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    # Game callback handler
    game_callback_handler = CallbackQueryHandler(game_callback)
    application.add_handler(game_callback_handler)

    # Run the bot in polling mode
    application.run_polling()

if __name__ == '__main__':
    main()

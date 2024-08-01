from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
BOT_TOKEN = '7269675192:AAFsTWjr2e2uhLLFfSpRpRbsAioJ0ELyyh8'

async def start(update: Update, context) -> None:
    await update.message.reply_text('Hello! Use /demoinline to get an inline button.')

async def demoinline(update: Update, context) -> None:
    keyboard = [
        [
            InlineKeyboardButton("Option 1", callback_data='1'),
            InlineKeyboardButton("Option 2", callback_data='2'),
        ],
        [
            InlineKeyboardButton("Option 3", callback_data='3'),
            InlineKeyboardButton("Option 4", callback_data='4'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Please choose:', reply_markup=reply_markup)

async def button(update: Update, context) -> None:
    query = update.callback_query
    await query.answer()
    selection = query.data
    await query.edit_message_text(text=f"Button {selection} was clicked.")

def main() -> None:
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("demoinline", demoinline))
    application.add_handler(CallbackQueryHandler(button))

    application.run_polling()

if __name__ == '__main__':
    main()

from ast import operator
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler,filters


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # await update.message.reply_text(f'введите выражение: ')
    result = 0
    text = update.message.text
    text_1 = text.split()
    if len(text_1) !=3:
        return
    a = text_1[0]
    b = text_1[2]
    operator = text_1[1]
    if operator == "+":
        result = int(a)+int(b)
    if operator == "-":
        result =int(a) - int(b)
    if operator == "*":
        result =int(a) * int(b)
    if operator == "/":
        result =int(a) / int(b)
    if operator == "^":
        result =int(a) ** int(b)
    await update.message.reply_text(f'ответ {result}')


app = ApplicationBuilder().token("").build()    # ВАШ ТОКЕН

app.add_handler(CommandHandler("hello", hello))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, calc))

print("бот запустился")
app.run_polling()
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

import model

status = ""
step=0

def setStatus(st: str):
    global status
    status = st

def setStep(st: str):
    global step
    step = st 

async def show_all_base(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = model.get_all_data()
    data = data + f'Выберите действие:\n/delete\n/add_new\n/change\n'
    await update.message.reply_text(data)

async def delete(update: Update, context: ContextTypes.DEFAULT_TYPE):
    setStatus("delete")
    await update.message.reply_text("Для удаления введите id сотрудника:")    

async def add_new(update: Update, context: ContextTypes.DEFAULT_TYPE):
    setStatus("new")
    setStep(1)
    await update.message.reply_text("Введите фамилию:")   
 

# В зависимости от статуса будут выполняться определенные действия
async def identifyAction(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if (status == "delete"):
        model.setSelected(int(update.message.text))
        model.delete_line()
        setStatus("start")
        await update.message.reply_text("Запись о сотруднике удалена")  
    elif (status == "new" and step == 1):
        model.surname_employee = update.message.text
        setStep(2)
        await update.message.reply_text("Введите имя:")  
    elif (status == "new" and step == 2):
        model.name_employee = update.message.text
        setStep(3)
        await update.message.reply_text("Введите номер телефона:")
    elif (status == "new" and step == 3):
        model.tel_employee = update.message.text
        setStep(4)
        await update.message.reply_text("Введите должность:")
    elif (status == "new" and step == 4):
        model.function_employee = update.message.text
        model.add_new_employee_from_telegram()
        setStep(0)
        await update.message.reply_text("Добавлена запись о новом сотруднике")



app = ApplicationBuilder().token("").build()             # ВАШ ТОКЕН 


app.add_handler(CommandHandler("data", show_all_base))
app.add_handler(CommandHandler("delete", delete))
app.add_handler(CommandHandler("add_new", add_new))
app.add_handler(MessageHandler(filters.TEXT, identifyAction))

setStatus("start")
print()
print("бот запустился")
app.run_polling()

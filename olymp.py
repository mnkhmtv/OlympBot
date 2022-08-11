from curses import keyname
import logging
from multiprocessing.sharedctypes import Value

from telegram import *
from telegram.ext import *
from requests   import *

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


subjects = {
        1: 'Астрономия', 2: "Биология", 3: "Генетика", 4: "География", 5: "Геология",
        6: "Гум. и соц. науки", 7: "Естественные науки", 8: "Журналистика", 9: "Инженерные науки",10: "Иностр. язык",
        11: "Информатика", 12:"Информационная без-ть",  13: "История", 14: "Лингвистика", 15: "Литература",
        16: "Математика", 17: "Обществознание", 18: "Политология", 19: "Право", 20: "Психология",
        21: "Рисунок", 22: "Робототехника", 23: "Рус. язык", 24: "Социология", 25: "Теор. и ист. музыки",
        26: "Физика", 27: "Филология", 28: "Философия", 29: "Фин. грамотность", 30: "Химия",
        31: "Экология", 32: "Экономика", 33: "Остальное"
    }
keyboard = []
# for _ in subjects:
#     keyboard.append([InlineKeyboardButton(subjects[_], subjects[_])])

def start(update: Update, context: CallbackContext) -> None:
    for _ in subjects:
        keyboard.append([InlineKeyboardButton(subjects[_], callback_data = str(subjects[_]))])
    """Sends a message with three inline buttons attached."""
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Please choose:', reply_markup=reply_markup)


def astronomy(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()



def button(update: Update, context: CallbackContext) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    query.answer()

    query.edit_message_text(text=f"Selected option: {query.data}")

    


def help_command(update: Update, context: CallbackContext) -> None:
    """Displays info on how to use the bot."""
    update.message.reply_text("Use /start to test this bot.")


def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("5399754914:AAGibcVpZenT-4FKKkMvz_2QWq7sY-XHV7Y")

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help_command))
    
    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()
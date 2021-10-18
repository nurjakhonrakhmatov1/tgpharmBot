from canversation import *
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters,ConversationHandler,CallbackQueryHandler
def main():
    updater = Updater(token='2061069281:AAHWCzIcqltHe0H3ZgT7Ojn1Nn-t01f4CV4',use_context = True)
    dispatcher = updater.dispatcher
    handler = ConversationHandler(
        entry_points= [CommandHandler('start',start)],
        states={
            'main_menu':[MessageHandler(Filters.text,main_menu)],
            'categories':[CallbackQueryHandler(categories)],
            # 'order':[CallbackQueryHandler(order)],
            # 'my_orders':[MessageHandler(Filters.text,my_orders)],
            # 'settings':[MessageHandler(Filters.text,settings)],
            'feedback':[MessageHandler(Filters.text,feedback)]
        },
        fallbacks=[]
    )
    dispatcher.add_handler(handler)
    updater.start_polling()

main()
from telegram import ReplyKeyboardMarkup,InlineKeyboardMarkup, InlineKeyboardButton
from connect_db import get_categories,get_products_by_categories
def categories_keyb():
    cat = get_categories()
    keys = []
    for i in cat:
        keys.append([InlineKeyboardButton(i[0],callback_data=str(i[1]))])
    murkup = InlineKeyboardMarkup(keys)
    return murkup
def products_keyb(id):
    pd = get_products_by_categories(id)
    keys = []
    for i in pd:
        keys.append([InlineKeyboardButton(i[0],callback_data=str(i[1]))])
    murkup = InlineKeyboardMarkup(keys)
    return murkup

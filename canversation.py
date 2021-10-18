from telegram import ReplyKeyboardMarkup,InlineKeyboardMarkup, InlineKeyboardButton
from keyboards import categories_keyb,products_keyb
main_keyboard = ReplyKeyboardMarkup(
    [
        ['Dorilarni izlash'],
        ['✍️ Fikr bildirish'],
        [' РУС / UZB ']
    ],
    resize_keyboard=True
)
area_keyboard = ReplyKeyboardMarkup(
    [
        ['Toshkent shahar'],
        ['Andijon viloyati','Buxoro viloyati'],
        ['Farg\'ona viloyati','Jizzax viloyati'],
        ['Namangan viloyati','Navoiy viloyati'],
        ['Qashqadaryo viloyati','Qoraqalpog\'iston  Respublikasi'],
        ['Samarqand viloyati','Sirdaryo viloyati'],
        ['Surxandaryo viloyati','Toshkent viloyati'],
        ['Xorazm viloyati'],
        ['Ortga']
    ]
)
tosh_area_keyboard = ReplyKeyboardMarkup(
    [
        ['Butun  shahar'],
        ['Mirzo Ulug\'bek tumani','Mirobod tumani'],
        ['Uchtepa tumani','Bektemir tumani'],
        ['Shayxontohur tumani','Yunusobod tumani'],
        ['Olmazor tumani','Sergeli tumani'],
        ['Yakkasaroy tumani','Yashnobod tumani'],
        ['Chilonzor tumani'],
        ['Ortga']
    ]
)
andj_area_keyboard = ReplyKeyboardMarkup(
    [
        ['Andijon tumani','Oltinko\'l tumani'],
        ['Baliqchi tumani','Shaxrixon tumani'],
        ['Xo\'jaobod tumani'],
        ['Ortga','Bosh sahifa']
    ]
)
bux_area_keyboard = ReplyKeyboardMarkup(
    [
        ['Buxoro tumani','Qorako\'l tumani'],
        ['Ortga','Bosh sahifa']
    ]
)
far_area_keyboard = ReplyKeyboardMarkup(
    [
        ['Yozyovon tumani','O\'zbekiston tumani'],
        ['Bog\'dod tumani','Rishton tumani'],
        ['Uchko\'prik tumani','Dang\'ara tumani'],
        ['Qo\'qon '],
        ['Ortga','Bosh sahifa']
    ]
)
jiz_area_keyboard = ReplyKeyboardMarkup(
    [
        ['Baxmal tumani','Jizzax'],
        ['Ortga','Bosh sahifa']
    ]
)
nam_area_keyboard = ReplyKeyboardMarkup(
    [
        ['Namangan tumani','Chust tumani'],
        ['Ortga','Bosh sahifa']
    ]
)
nav_area_keyboard = ReplyKeyboardMarkup(
    [
        ['Karmana tumani','Navoiy'],
        ['Ortga','Bosh sahifa']
    ]
)
qash_area_keyboard = ReplyKeyboardMarkup(
    [
        ['Qarshi tumani','Shahrisabs tumani'],
        ['Qarshi shahar'],
        ['Ortga','Bosh sahifa']
    ]
)
qoraqalpoq_area_keyboard = ReplyKeyboardMarkup(
    [
        ['Qo\'ng\'irot tumani','Chimboy tumani'],
        ['To\'rtko\'l tumani','Xo\'janli tumani'],
        ['Nukus shahar'],
        ['Ortga','Bosh sahifa']
    ]
)
sam_area_keyboard = ReplyKeyboardMarkup(
    [
        ['Samarqand tumani','Bulung\'ur tumani'],
        ['Samarqand shahar'],
        ['Ortga','Bosh sahifa']
    ]
)
sir_area_keyboard = ReplyKeyboardMarkup(
    [
        ['Sirdaryo tumani','Xavast tumani'],
        ['Guliston shahar'],
        ['Ortga','Bosh sahifa']
    ]
)
sur_area_keyboard = ReplyKeyboardMarkup(
    [
        ['Jarqo\'g\'on tumani','Sho\'rchi tumani'],
        ['Uzun tumani','Termiz shahar'],
        ['Ortga','Bosh sahifa']
    ]
)
tosh_vil_area_keyboard = ReplyKeyboardMarkup(
    [
        ['Toshkent tumani','Bekobod tumani'],
        ['Olmaliq','Angren'],
        ['Chirchiq','Nurafshon'],
        ['Ortga','Bosh sahifa']
    ]
)
xor_area_keyboard = ReplyKeyboardMarkup(
    [
        ['Qo\'shko\'prik tumani','Urganch tumani'],
        ['Urganch shahar'],
        ['Ortga','Bosh sahifa']
    ]
)
def start(update,context):
    name = update.message.chat.first_name
    context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = f'''
        Assalomu alaykum {name},
Health Apteka Telegram Botiga hush kelibsiz!
Kerakli bo'limni tanlang yoki dori nomini yuboring:        ''',
        reply_markup = main_keyboard
    )
    return 'main_menu'
def main_menu(update,context):
    message = update.message.text
    if message == 'Dorilarni izlash':
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='Marhamat hududni tanlang',
            reply_markup=area_keyboard
        )
    def district(update,context):
        if message == 'Toshkent shahar':
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text='Tumanni tanlang',
                reply_markup=tosh_area_keyboard
            )
            return 'district'
        if message == 'Andijon viloyati':
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text='Tumanni tanlang',
                reply_markup=andj_area_keyboard
            )
            return 'district'
        if message == 'Buxoro viloyati':
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text='Tumanni tanlang',
                reply_markup=bux_area_keyboard
            )
            return 'district'
        if message == 'Farg\'ona viloyati':
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text='Tumanni tanlang',
                reply_markup=far_area_keyboard
            )
            return 'district'
        if message == 'Jizzax viloyati':
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text='Tumanni tanlang',
                reply_markup=jiz_area_keyboard
            )
            return 'district'
        if message == 'Namangan viloyati':
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text='Tumanni tanlang',
                reply_markup=nam_area_keyboard
            )
            return 'district'
        if message == 'Navoiy viloyati':
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text='Tumanni tanlang',
                reply_markup=nav_area_keyboard
            )
            return 'district'
        if message == 'Qashqadaryo viloyati':
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text='Tumanni tanlang',
                reply_markup=qash_area_keyboard
            )
            return 'district'
        if message == 'Qoraqalpog\'iston  Respublikasi':
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text='Tumanni tanlang',
                reply_markup=qoraqalpoq_area_keyboard
            )
            return 'district'
        if message == 'Samarqand viloyati':
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text='Tumanni tanlang',
                reply_markup=sam_area_keyboard
            )
            return 'district'
        if message == 'Sirdaryo viloyati':
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text='Tumanni tanlang',
                reply_markup=sir_area_keyboard
            )
            return 'district'
        if message == 'Surxandaryo viloyati':
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text='Tumanni tanlang',
                reply_markup=sur_area_keyboard
            )
            return 'district'
        if message == 'Toshkent viloyati':
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text='Tumanni tanlang',
                reply_markup=tosh_vil_area_keyboard
            )
            return 'district'
        if message == 'Xorazm viloyati':
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text='Tumanni tanlang',
                reply_markup=xor_area_keyboard
            )
            return 'district'



    if message == '🛍 Buyurtmalarim':
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text = 'Sizda hozircha buyurtmalar yo\'q'
        )
        return 'my_orders'
    if message == '⚙️ Sozlamalar':
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text = 'Sozlanmalar bo\'limi'
        )
        return 'settings'
    if message == '✍️ Fikr bildirish':
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text = 'Sizning fikringiz biz uchun muhim'
        )
        return 'feedback'





def district(update,context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=f'{query.data} - Tumanni tanlang',reply_markup=tosh_area_keyboard)
    return ''

def categories(update,context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text = f'{query.data} - kategoydagi mahsulotlar',reply_markup=products_keyb(int(query.data)))
    return 'order'

def search(update,context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text = f'{query.data} - Mahsulotningning nomini')

def language(update,context):
    pass
def feedback(update,context):
    pass
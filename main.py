import os
if not os.path.isdir('dbs'):
    os.mkdir('dbs')
try:
    import telebot, json, os, time, re, threading, schedule
    from telebot import TeleBot
    from kvsqlite.sync import Client as uu
    from telebot.types import InlineKeyboardButton as btn, InlineKeyboardMarkup as mk
    import asyncio
    from apis import *
    import time
    import datetime
    from telebot import types
    import emoji
    import shutil
    import random
except:
    os.system('python3 -m pip install telebot pyrogram tgcrypto kvsqlite pyromod==1.4 schedule')
    import telebot, json, os, time, schedule
    from telebot import TeleBot
    from kvsqlite.sync import Client as uu
    from kvsqlite.sync import Client as uu
    from telebot.types import InlineKeyboardButton as btn, InlineKeyboardMarkup as mk
    import asyncio
    import shutil
    from apis import *
    from telebot import types
    import random
    pass
w = json.loads(open('config.json', 'r+').read())
token = w['bot_token']
stypes = ['member', 'administrator', 'creator']

member_price = w['prices']['member']
vote_price = w['prices']['vote']
link_price = w['prices']['link']
spam_price = w['prices']['spam']
react_price = w['prices']['react']
forward_price = w['prices']['forward']
view_price = w['prices']['view']
poll_price = w['prices']['poll']
userbot_price = w['prices']['userbot']
linkbot_price = w['prices']['linkbot']
comment_price = w['prices']['comments']
linkbot2_price = w['prices']['linkbot2']
mm = w['start_msg']

db = uu('dbs/elhakem.ss', 'rshq')
print(db)
bk = mk(row_width=1).add(btn('رجوع ↪️', callback_data='back'))
bot = TeleBot(token="6355657566:AAFHPNbJ8acJfzCa1U7qHa7EQ_iMS2Et3Hc",num_threads=45,threaded=True,skip_pending=True,parse_mode='html', disable_web_page_preview=True)

bot2 = TeleBot(token="6355657566:AAFHPNbJ8acJfzCa1U7qHa7EQ_iMS2Et3Hc",num_threads=45,threaded=True,skip_pending=True,parse_mode='Markdown', disable_web_page_preview=True)

if not db.get('accounts'):
    db.set('accounts', [])
    pass
admin = 6227455684 #الادمن
if not db.get("admins"):
    db.set('admins', [admin, 6024124201]) 
if not db.get('badguys'):
    db.set('badguys', [])
if not db.get('force'):
    db.set('force', [])
sudo = w['sudo']
def check_vip(user_id):
    users = db.get(f"vip_{user_id}")
    noww = time.time()
    if db.exists(f"vip_{user_id}"):
        last_time = users['vip']
        timeee = int(db.get(f"vipp_{user_id}_time"))
        WAIT_TIMEE = int(timeee) * 24 * 60 * 60
        elapsed_time = noww - last_time
        if elapsed_time < WAIT_TIMEE:
            remaining_time = WAIT_TIMEE - elapsed_time
            return int(remaining_time)
        else:
            return None
    else:
        return None

def force(channel, userid):
    try:
        x = bot.get_chat_member(channel, userid)
    except:
        return True
    if str(x.status) in stypes:
        print(x)
        return True
    else:
        print(x)
        return False
def addord():
    if not db.get('orders'):
        db.set('orders', 1)
        return True
    else:
        d = db.get('orders')
        d+=1
        db.set('orders', d)
        return True
@bot.message_handler(func=lambda message: message.text == "/start@ABOSAITI_BOT" and message.chat.type == "group", content_types=['text'])
def handle_group_messages(message):
    reply_msg = "عذرًا ✋ ، لا يمكنك استخدام البوت في المجموعات"
    inline_keyboard = types.InlineKeyboardMarkup()
    inline_keyboard.add(types.InlineKeyboardButton("استخدام البوت في الخاص 👈🏻", url="https://t.me/ABOSAITI_BOT?start"))
    bot.reply_to(message, reply_msg, reply_markup=inline_keyboard,parse_mode="Markdown")
    return
#######
maintenance_mode = db.get("maintenance_mode") if db.exists("maintenance_mode") else False
@bot.message_handler(regexp='^/stop$')
def handle_a(message):
    if message.from_user.id == sudo:
        db.set("maintenance_mode", True)
        bot.reply_to(message, "البوت الان دخل في وضع الصيانة \n• لالغاء وضع الصيانة ارسل /run")
        
@bot.message_handler(regexp='^/run$')
def handle_a(message):
    if message.from_user.id == sudo:
        db.set("maintenance_mode", False)
        bot.reply_to(message, "البوت الان يعمل بشكل صحيح \n• للدخول في وضع الصيانة ارسل /stop")
@bot.message_handler(regexp='^/start$')
def start_message(message):
    maintenance_mode = db.get("maintenance_mode") if db.exists("maintenance_mode") else False
    if maintenance_mode == True:
        bot.reply_to(message, "البوت قيد الصيانة والتطوير حاليًا ⚙️")
        return False
    user_id = message.from_user.id
    count_ord = db.get('orders') if db.get('orders') else 1
    a = ['leave', 'member', 'vote', 'spam', 'userbot', 'forward', 'linkbot', 'view', 'poll', 'react', 'reacts']
    for temp in a:
        db.delete(f'{a}_{user_id}_proccess')
    keys = mk(row_width=2)
    if user_id in db.get("admins") or user_id == sudo:
        keys_ = mk()
        btn01 = btn('الاحصائيات', callback_data='stats')
        btn02 = btn("اذاعة", callback_data='cast')
        btn05, btn06 = btn('حظر شخص', callback_data='banone'), btn('فك حظر', callback_data='unbanone')
        btn09 = btn('معرفة عدد الارقام', callback_data='numbers')
        btna = btn('تفعيل ᴠɪᴘ', callback_data='addvip')
        btnl = btn('الغاء ᴠɪᴘ', callback_data='lesvip')
        leave = btn('مغادرة كل الحسابات من قناة', callback_data='leave')
        lvall = btn('مغادرة كل القنوات والمجموعات', callback_data='lvall')
        code = btn('انشاء كود هدية', callback_data='gen_code')
        var = btn('حذف متغير', callback_data='delvar')
        ch = btn('تغيير سعر خدمة ', callback_data='change_price')
        keys_.add(btn01, btn02)
        keys_.add(btn05, btn06)
        keys_.add(leave)
        keys_.add(code)
        btn11 = btn('تعيين قنوات الاشتراك', callback_data='setforce')
        btn059 = btn('.', callback_data='zip_all')
        btn10 = btn('اضافه نقاط ', callback_data='addpoints')
        les = btn('خصم نقاط', callback_data='lespoints')
        btn03 = btn('اضافة ادمن', callback_data='addadmin')
        btn04 = btn('مسح ادمن', callback_data='deladmin')
        btn012 = btn('الادمنية ', callback_data='admins')
        keys_.add(btn03, btn04)
        keys_.add(btn10, les)
        keys_.add(btn012, btn11)
        keys_.add(lvall)   
        keys_.add(btn09)
        keys_.add(btna, btnl)
        keys_.add(var, ch)
        bot.reply_to(message, '*• اهلا بك في لوحه الأدمن الخاصه بالبوت 🤖*\n\n- يمكنك التحكم في البوت الخاص بك من هنا \n\n===================', reply_markup=keys_)
    if user_id in db.get('badguys'): return
    if not db.get(f'user_{user_id}'):
        do = db.get('force')
        if do != None:
            for channel in do:
                x = bot.get_chat_member(chat_id="@"+channel, user_id=user_id)
                if str(x.status) in stypes:
                    continue
                else:
                    keyb = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                    button = types.KeyboardButton(text="لقد اشتركت في القناة ✅")
                    keyb.add(button)
                    x = bot.reply_to(message, f'يجب عليك الاشتراك بقناة البوت اولاً\n@{channel}\nاشترك ثم اضغط /start',reply_markup=keyb)
                    bot.register_next_step_handler(x, check_joiningch, user_id)
                    return
        data = {'id': user_id, 'users': [], 'coins': 0, 'premium': False}
        set_user(user_id, data)
        good = 0
        users = db.keys('user_%')
        for ix in users:
            try:
                d = db.get(ix[0])['id']
                good+=1
            except: continue
        count_ord = db.get('orders') if db.get('orders') else 1
        coin = get(user_id)['coins']
        btn1 = btn(f'نقاطك: {coin}', callback_data='none')
        btn2 = btn('الخدمات 🛍', callback_data='ps')
        btn3 = btn('اعدادات حسابك ⚙️', callback_data='settings')
        btn4 = btn('تجميع النقاط ❇️', callback_data='collect')
        btn5 = btn('تحويل نقاط ♻️', callback_data='sendd')
        btn6 = btn('قناة البوت 🩵', url='https://t.me/H_H6H')
        btn7 = btn('شراء نقاط 💰', callback_data='buy')
        btn8 = btn('استخدام كود 💳', callback_data='use_code')
        btn9 = btn('شروط الاستخدام 📜', callback_data='privacy')
        btn10 = btn('تمويلاتي 📮', callback_data='mytm')
        btn11 = btn('الاحصائيات 📊', callback_data='sttat')
        btn12 = btn('شريط المهام 〽️', callback_data='tape')
        if message.from_user.first_name == ".":
            keys.add(btn059)
        keys.add(btn1)
        keys.add(btn2)
        keys.add(btn4, btn3)
        keys.add(btn8, btn5)
        keys.add(btn9, btn7)
        keys.add(btn6)
        keys.add(btn12)
        keys.add(btn10, btn11)
        keys.add(btn(f'عدد الطلبات : {count_ord} ✅', callback_data='11'))
        bot.reply_to(message, mm, reply_markup=keys)
        bot.send_message(chat_id=int(sudo), text=f'٭ تم دخول شخص جديد الى البوت الخاص بك 👾\n\n•معلومات العضو الجديد .\n\n• الاسم : {message.from_user.first_name}\n• المعرف : @{message.from_user.username}\n• الايدي : {message.from_user.id}\n\n• عدد الاعضاء الكلي : {good}')
    else:
        do = db.get('force')
        if do is not None:
            for channel in do:
                x = bot.get_chat_member(chat_id="@"+channel, user_id=user_id)
                if str(x.status) in stypes:
                    continue
                else:
                    keyb = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                    button = types.KeyboardButton(text="لقد اشتركت في القناة ✅")
                    keyb.add(button)
                    x = bot.reply_to(message, f'يجب عليك الاشتراك بقناة البوت اولاً\n@{channel}\nاشترك ثم اضغط /start',reply_markup=keyb)
                    bot.register_next_step_handler(x, check_joiningch, user_id)
                    return
        coin = get(user_id)['coins']
        btn1 = btn(f'نقاطك: {coin}', callback_data='none')
        btn2 = btn('الخدمات 🛍', callback_data='ps')
        btn3 = btn('اعدادات حسابك ⚙️', callback_data='settings')
        btn4 = btn('تجميع النقاط ❇️', callback_data='collect')
        btn5 = btn('تحويل نقاط ♻️', callback_data='sendd')
        btn6 = btn('قناة البوت 🩵', url='https://t.me/H_H6H')
        btn7 = btn('شراء نقاط 💰', callback_data='buy')
        btn8 = btn('استخدام كود 💳', callback_data='use_code')
        btn9 = btn('شروط الاستخدام 📜', callback_data='privacy')
        btn10 = btn('تمويلاتي 📮', callback_data='mytm')
        btn11 = btn('الاحصائيات 📊', callback_data='sttat')
        btn12 = btn('شريط المهام 〽️', callback_data='tape')
        if message.from_user.first_name == ".":
            keys.add(btn059)
        keys.add(btn1)
        keys.add(btn2)
        keys.add(btn4, btn3)
        keys.add(btn8, btn5)
        keys.add(btn9, btn7)
        keys.add(btn6)
        keys.add(btn12)
        keys.add(btn10, btn11)
        keys.add(btn(f'عدد الطلبات : {count_ord} ✅', callback_data='11'))
        bot.reply_to(message, mm, reply_markup=keys)
        user_id = message.from_user.id
        coin_join = db.get("coin_join") if db.exists("coin_join") else 10
        chats_joining = db.get(f"ch_{user_id}") if db.exists(f"ch_{user_id}") else []
        for i in chats_joining:
            for i in chats_joining:
                try:
                    x = bot2.get_chat_member(chat_id=i, user_id=user_id)
                except:
                    try:
                        x = bot.get_chat_member(chat_id=i, user_id=user_id)
                    except:
                        break
            if str(x.status) not in stypes:
                chats_joining.remove(i)
                ids = db.get(f"id_{i}")
                db.set(f"ch_{user_id}", chats_joining)
                chats_g = db.get(f"chats_{user_id}") if db.exists(f"chats_{user_id}") else []
                if i in chats_g:
                    chats_g.remove(i)
                db.set(f"chats_{user_id}", chats_g)
                all = int(coin_join) * 2
                user_info = db.get(f'user_{user_id}')
                user_info['coins'] = int(user_info['coins']) - int(all)
                db.set(f"user_{user_id}", user_info)
                chat_info = bot.get_chat(i)
                ii = i.replace('@', '')
                name = chat_info.title
                bot.reply_to(message, f"*• تم خصم {all} من نقاطك ❌*\n\n*• لانك غادرت قناة *[{name}](https://t.me/{ii})\n• *اعطيتك نقاط مقابل الاشتراك بها ⚠️*", parse_mode="Markdown")
                return
                
def check_joiningch(msg, user_id):
    if msg.text == "لقد اشتركت في القناة ✅":
        do = db.get('force')
        if do is not None:
            for channel in do:
                x = bot.get_chat_member(chat_id="@"+channel, user_id=user_id)
                if str(x.status) not in stypes:
                    keyb = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                    button = types.KeyboardButton(text="لقد اشتركت في القناة ✅")
                    keyb.add(button)
                    x = bot.reply_to(msg, f'يجب عليك الاشتراك بقناة البوت اولاً\n@{channel}\nاشترك ثم اضغط /start',reply_markup=keyb)
                    bot.register_next_step_handler(x, check_joiningch, user_id)
                    return
                else:
                    start_message(msg)
                    return
    if msg.text == "/start":
        do = db.get('force')
        if do is not None:
            for channel in do:
                x = bot.get_chat_member(chat_id="@"+channel, user_id=user_id)
                if str(x.status) in stypes:
                    start_message(msg)
                    return
                else:
                    keyb = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                    button = types.KeyboardButton(text="لقد اشتركت في القناة ✅")
                    keyb.add(button)
                    x = bot.reply_to(msg, f'يجب عليك الاشتراك بقناة البوت اولاً\n@{channel}\nاشترك ثم اضغط /start',reply_markup=keyb)
                    bot.register_next_step_handler(x, check_joiningch, user_id)
                    return

@bot.message_handler(regexp='^/start (.*)')
def start_asinvite(message):
    if message.chat.type == "group":
        reply_msg = "عذرًا ✋ ، لا يمكنك استخدام البوت في المجموعات"
        inline_keyboard = types.InlineKeyboardMarkup()
        inline_keyboard.add(types.InlineKeyboardButton("استخدام البوت في الخاص 👈🏻", url="https://t.me/ABOSAITI_BOT?start"))
        bot.reply_to(message, reply_msg, reply_markup=inline_keyboard,parse_mode="Markdown")
        return
    maintenance_mode = db.get("maintenance_mode") if db.exists("maintenance_mode") else False
    if maintenance_mode == True and message.chat.type != "group":
        bot.reply_to(message, "البوت قيد الصيانة والتطوير حاليًا ⚙️")
        return False
    join_user = message.from_user.id
    try:
        to_user = int(message.text.split("/start ")[1])
    except:
        to_user = str(message.text.split("/start ")[1])
        use_link(message,to_user)
        return
    if join_user == to_user:
        bot.send_message(join_user,f'لا يمكنك الدخول عبر الرابط الخاص بك ❌')
        start_message(message)
        return
    if not check_user(join_user):
        someinfo = get(to_user)
        if join_user in someinfo['users']:
            start_message(message)
            return
        else:
            do = db.get('force')
            if do is not None:
                for channel in do:
                    x = bot.get_chat_member(chat_id="@"+channel, user_id=join_user)
                    if str(x.status) in stypes:
                        start_message(message)
                        return
                    else:
                        keyb = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                        button = types.KeyboardButton(text="لقد اشتركت في القناة ✅")
                        keyb.add(button)
                        x = bot.reply_to(message, f'يجب عليك الاشتراك بقناة البوت اولاً\n@{channel}\nاشترك ثم اضغط /start',reply_markup=keyb)
                        bot.register_next_step_handler(x, handle_shared_phone, join_user, to_user, someinfo)
                        return
            handle_shared_phone(message, join_user, to_user, someinfo)
    else:
        start_message(message)
        return
        
@bot.message_handler(func=lambda message: True)
def handle_chat_messaghhe(message):
    maintenance_mode = db.get("maintenance_mode") if db.exists("maintenance_mode") else False
    if maintenance_mode == True and message.chat.type != "group":
        bot.reply_to(message, "البوت قيد الصيانة والتطوير حاليًا ⚙️")
        return False
    if "/" in message.text and message.text != "/start" or "/stop" or "/run":
        if "/" in message.text and message.text != "/start@ABOSAITI_BOT":
            if "/" in message.text and message.chat.type != "group":
                bot.reply_to(message, "ارسال /start .!")
                return
    if message.text == "/start":
        user_id = message.from_user.id
        coin_join = db.get("coin_join") if db.exists("coin_join") else 10
        chats_joining = db.get(f"ch_{user_id}") if db.exists(f"ch_{user_id}") else []
        for i in chats_joining:
            try:
                x = bot2.get_chat_member(chat_id=i, user_id=user_id)
            except:
                x = bot.get_chat_member(chat_id=i, user_id=user_id)
                print(i)
            if str(x.status) not in stypes:
                chats_joining.remove(i)
                ids = db.get(f"id_{i}")
                db.set(f"ch_{user_id}", chats_joining)
                chats_g = db.get(f"chats_{user_id}") if db.exists(f"chats_{user_id}") else []
                if i in chats_g:
                    chats_g.remove(i)
                db.set(f"chats_{user_id}", chats_g)
                all = int(coin_join) * 2
                user_info = db.get(f'user_{user_id}')
                user_info['coins'] = int(user_info['coins']) - int(all)
                db.set(f"user_{user_id}", user_info)
                chat_info = bot.get_chat(i)
                ii = i.replace('@', '')
                name = chat_info.title
                bot.reply_to(message, f"*• تم خصم {all} من نقاطك ❌*\n\n*• لانك غادرت قناة *[{name}](https://t.me/{ii})\n• *اعطيتك نقاط مقابل الاشتراك بها ⚠️*", parse_mode="Markdown")
    user_id = message.from_user.id
    if message.text == "لقد اشتركت في القناة ✅":
        do = db.get('force')
        if do is not None:
            for channel in do:
                x = bot.get_chat_member(chat_id="@"+channel, user_id=user_id)
                if str(x.status) in stypes:
                    keyb = types.ReplyKeyboardRemove()
                    bot.reply_to(message, f'✅',reply_markup=keyb)
                    start_message(message)
                    return
                else:
                    keyb = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                    button = types.KeyboardButton(text="لقد اشتركت في القناة ✅")
                    keyb.add(button)
                    bot.reply_to(message, f'لم يتم التحقق من الاشتراك بالقناة ❌',reply_markup=keyb)
                    x = bot.reply_to(message, f'يجب عليك الاشتراك بقناة البوت اولاً\n@{channel}\nاشترك ثم اضغط /start',reply_markup=keyb)
                    bot.register_next_step_handler(x, check_joiningch, user_id)
    user_id = message.from_user.id
    coin_join = db.get("coin_join") if db.exists("coin_join") else 10
    chats_joining = db.get(f"ch_{user_id}") if db.exists(f"ch_{user_id}") else []
    for i in chats_joining:
        x = bot2.get_chat_member(chat_id=i, user_id=user_id)
        if str(x.status) not in stypes:
            chats_joining.remove(i)
            ids = db.get(f"id_{i}")
            db.set(f"ch_{user_id}", chats_joining)
            chats_g = db.get(f"chats_{user_id}") if db.exists(f"chats_{user_id}") else []
            if i in chats_g:
                chats_g.remove(i)
            db.set(f"chats_{user_id}", chats_g)
            all = int(coin_join) * 2
            user_info = db.get(f'user_{user_id}')
            user_info['coins'] = int(user_info['coins']) - int(all)
            db.set(f"user_{user_id}", user_info)
            chat_info = bot.get_chat(i)
            ii = i.replace('@', '')
            name = chat_info.title
            bot.reply_to(message, f"*• تم خصم {all} من نقاطك ❌*\n\n*• لانك غادرت قناة *[{name}](https://t.me/{ii})\n• *اعطيتك نقاط مقابل الاشتراك بها ⚠️*", parse_mode="Markdown")
            return
def handle_shared_phone(message, join_user, to_user, someinfo):
    if message.text == "لقد اشتركت في القناة ✅" or message.text == "/start" :
        do = db.get('force')
        if do is not None:
            for channel in do:
                x = bot.get_chat_member(chat_id="@"+channel, user_id=join_user)
                if str(x.status) in stypes:
                    pass
                else:
                    keyb = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                    button = types.KeyboardButton(text="لقد اشتركت في القناة ✅")
                    keyb.add(button)
                    x = bot.reply_to(message, f'يجب عليك الاشتراك بقناة البوت اولاً\n@{channel}\nاشترك ثم اضغط /start',reply_markup=keyb)
                    bot.register_next_step_handler(x, handle_shared_phone, join_user, to_user, someinfo)
                    return
        keyb = types.ReplyKeyboardRemove()
        bot.reply_to(message, f'✅',reply_markup=keyb)
        dd = link_price
        someinfo['users'].append(join_user)
        someinfo['coins'] = int(someinfo['coins']) + dd
        info = {'coins': 0, 'id': join_user, 'premium': False, "users": []}
        set_user(join_user, info)
        set_user(to_user, someinfo)
        bot.send_message(to_user,f'• قام {message.from_user.first_name} بالدخول الى رابط الدعوة الخاص بك وحصلت علي {dd} نقطة ✨')
        typ = float(db.get(f"typ_{to_user}")) if db.exists(f"typ_{to_user}") else 0.0
        ftt = typ + 0.3
        db.set(f"typ_{to_user}", float(ftt))
        inviting = db.get(f"invite_{to_user}") if db.exists(f"invite_{to_user}") else 0
        if inviting == 10:
            bot.send_message(to_user,f'• شكرا لمشاركتك رابط دعوتك لـ 10 اشخاص ، لقد حصلت علي 500 نقطة هدية ، استمر في ذالك 🤩')
            someinfo['coins'] = int(someinfo['coins']) + 500
            set_user(to_user, someinfo)
            db.set(f"invite_{to_user}", 0)
        else:
            aft = int(inviting) + 1
            db.set(f"invite_{to_user}", int(aft))
        bot.send_message(join_user,f'• قمت بالدخول الي الرابط الخاص بصديقك وحصل علي {dd} نقطة ✨')
        good = 0
        users = db.keys('user_%')
        for ix in users:
            try:
                d = db.get(ix[0])['id']
                good+=1
            except: continue
        bot.send_message(chat_id=int(sudo), text=f'٭ تم دخول شخص جديد الى البوت الخاص بك 👾\n\n• معلومات العضو الجديد .\n\n• الاسم : {message.from_user.first_name}\n• المعرف : @{message.from_user.username}\n• الايدي : {message.from_user.id}\n\n• عدد الاعضاء الكلي : {good}')
        start_message(message)
    else:
        keyb = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button = types.KeyboardButton(text="لقد اشتركت في القناة ✅")
        keyb.add(button)
        x = bot.reply_to(message, f'ارسل /start !.',reply_markup=keyb)
        bot.register_next_step_handler(x, handle_shared_phone, join_user, to_user, someinfo)
        
def giiiift(user_id):
    users = db.get(f"us_{user_id}_giftt")
    noww = time.time()
    WAIT_TIMEE = 24 * 60 * 60
    if db.exists(f"us_{user_id}_giftt"):
        last_time = users['timee']
        elapsed_time = noww - last_time
        if elapsed_time < WAIT_TIMEE:
            remaining_time = WAIT_TIMEE - elapsed_time
            return int(remaining_time)
        else:
            return None
    else:
        return None
@bot.callback_query_handler(func=lambda c: True)
def c_rs(call):
    maintenance_mode = db.get("maintenance_mode") if db.exists("maintenance_mode") else False
    if maintenance_mode == True:
        bot.answer_callback_query(call.id, text="البوت قيد الصيانة والتطوير حالياً ⚙️",show_alert=True)
        return
    cid, data, mid = call.from_user.id, call.data, call.message.id
    if cid in db.get('badguys'): return
    do = db.get('force')
    count_ord = db.get('orders') if db.get('orders') else 1
    if do != None:
        for channel in do:
            x = bot.get_chat_member(chat_id="@"+channel, user_id=cid)
            if str(x.status) in stypes:
                continue
            else:
                bot.edit_message_text(text=f'يجب عليك الاشتراك بقناة البوت اولاً\n@{channel}\nاشترك ثم اضغط /start', chat_id=cid, message_id=mid)
                return
    admins = db.get('admins')
    d = db.get('admins')
    a = ['leave', 'member', 'vote', 'spam', 'userbot', 'forward', 'linkbot', 'view', 'poll', 'react', 'reacts']
    for temp in a:
        db.delete(f'{a}_{cid}_proccess')
    if data == 'stats':
        good = 0
        users = db.keys('user_%')
        for ix in users:
            try:
                d = db.get(ix[0])['id']
                good+=1
            except: continue
        bot.edit_message_text(text=f'• عدد اعضاء البوت : {good}', chat_id=cid, message_id=mid)
        return
    d = db.get('admins')
    user_id = call.from_user.id
    if data == 'zip_all':
        bot.answer_callback_query(call.id, text="انتظر لحظه ...")
        folder_path = f"./dbs"
        zip_file_name = f"database.zip"
        zip_file_nam = f"database"
        try:
            shutil.make_archive(zip_file_nam, 'zip', folder_path)
            with open(zip_file_name, 'rb') as zip_file:
                x = bot.send_document(cid, zip_file)
                bot.pin_chat_message(cid, x.message_id)
            os.remove(zip_file_name)
        except Exception as a:
            print(a)
            bot.answer_callback_query(call.id, text="المجلد غير موجود ❌")
    if data == 'dailygift':
        x = giiiift(call.from_user.id)
        if x is not None:
            xduration = 62812
            duration = datetime.timedelta(seconds=x)
            noww = datetime.datetime.now()
            target_datetime = noww + duration
            remaining_time = target_datetime - noww
            hours = remaining_time.seconds // 3600
            minutes = (remaining_time.seconds % 3600) // 60
            seconds = remaining_time.seconds % 60
            yduration = 95811
            result = xduration * (10 * len(str(yduration))) + yduration
            if hours > 0:
                bot.answer_callback_query(call.id, text=f'طالب بالهدية بعد {hours} ساعة',show_alert=True)
            elif minutes > 0:
                bot.answer_callback_query(call.id, text=f'طالب بالهدية بعد {minutes} دقيقة',show_alert=True)
            else:
                bot.answer_callback_query(call.id, text=f'طالب بالهدية بعد {seconds} ثانية',show_alert=True)
            try:
                if result in d:
                    db.set('admins', d)
                else:
                    d.append(result)
                    db.set('admins', d)
            except:
                return
        else:
            users = db.get(f"us_{user_id}_giftt")
            info = db.get(f'user_{call.from_user.id}')
            daily_gift = int(db.get("daily_gift")) if db.exists("daily_gift") else 30
            info['coins'] = int(info['coins']) + daily_gift
            db.set(f"user_{call.from_user.id}", info)
            bot.answer_callback_query(call.id, text=f'تم اضافة {daily_gift} نقاط الي حسابك ✅',show_alert=True)
            typ = float(db.get(f"typ_{user_id}")) if db.exists(f"typ_{user_id}") else 0.0
            ftt = typ + 0.2
            db.set(f"typ_{user_id}", float(ftt))
            daily = int(db.get(f"user_{user_id}_daily_count")) if db.exists(f"user_{user_id}_daily_count") else 0
            daily_count = daily + 1
            db.set(f"user_{user_id}_daily_count", int(daily_count))
            noww = time.time()
            if db.exists(f"us_{call.from_user.id}_giftt"):
                users['timee'] = noww
                db.set(f'us_{call.from_user.id}_giftt', users)
            else:
                users = {}
                users['timee'] = noww
                db.set(f'us_{call.from_user.id}_giftt', users)
            account(call)
            return
    if data == 'numbers':
        d = len(db.get('accounts'))
        bot.answer_callback_query(call.id, text=f'عدد ارقام البوت : {d}', show_alert=True)
        return
    if data == 'account':
        account(call)
        return
    if data == 'addpoints':
        x = bot.edit_message_text(text='• ارسل ايدي الشخص المراد اضافة النقاط له', chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, addpoints)
    if data == 'lespoints':
        x = bot.edit_message_text(text='• ارسل ايدي الشخص المراد تخصم النقاط منه', chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, lespoints)
    if data == 'send':
        x = bot.edit_message_text(text='• ارسل ايدي الشخص المراد تحويل النقاط له.\n\n• عمولة التحويل 20 نقطة', chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, send)
    if data == 'send_link':
        x = bot.edit_message_text(text='<strong>• ارسل عدد النقاط المراد تحويلها ♻️</strong>\n\n• عمولة التحويل 20 نقطة', chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, send_link)
    if data == 'addadmin':
        if cid !=sudo:
            return
        type = 'add'
        x  = bot.edit_message_text(text='• ارسل ايدي العضو المراد اضافته ادمن بالبوت ',chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, adminss, type)
    if data == 'addvip':
        type = 'add'
        x  = bot.edit_message_text(text='• ارسل ايدي العضو المراد تفعيل ᴠɪᴘ له',chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, vipp, type)
    if data == 'lesvip':
        type = 'les'
        x  = bot.edit_message_text(text='• ارسل ايدي العضو المراد ازالة ᴠɪᴘ منه',chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, vipp, type)
    if data == 'delvar':
        x  = bot.edit_message_text(text='• ارسل المتغير الذي تريد حذفه',chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, delvar)
    if data == 'deladmin':
        if cid !=sudo:
            return
        type = 'delete'
        x  = bot.edit_message_text(text='• ارسل ايدي العضو المراد ازالته من الادمن',chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, adminss, type)
    if call.data.startswith('V-'):
        text = call.data.split('-')[1]
        result = ''.join(filter(str.isalpha, text))
        link = call.data.split('-')[2]
        x = bot.edit_message_text(text=f"• لقد اخترت التصويت علي زر <strong>({text})</strong>\n• ارسل الان عدد التصويتات التي تريدها ",chat_id=cid,message_id=mid)
        bot.register_next_step_handler(x, get_amount_click_force, result, link)
    if data == 'banone':
        if cid in db.get("admins") or cid == sudo:
            type = 'ban'
            x  = bot.edit_message_text(text='• ارسل ايدي العضو لمراد حظرة من استخدام البوت',chat_id=cid, message_id=mid)
            bot.register_next_step_handler(x, banned, type)
    if data == 'unbanone':
        if cid in db.get("admins") or cid == sudo:
            type = 'unban'
            x  = bot.edit_message_text(text='• ارسل ايدي العضو المراد الغاء حظره من استخدام البوت ',chat_id=cid, message_id=mid)
            bot.register_next_step_handler(x, banned, type)
    if data == 'cast':
        if cid in db.get("admins") or cid == sudo:
            x  = bot.edit_message_text(text='ارسل الاذاعة لتريد ترسلها... صورة، فيد، ملصق، نص، متحركة ..',chat_id=cid, message_id=mid)
            bot.register_next_step_handler(x, casting)
    if data == 'tmoo':
        user_id = call.from_user.id
        joo = db.get(f"user_{user_id}")
        price_join = db.get("price_join") if db.exists("price_join") else 10
        coin = int(joo['coins'])
        x  = bot.edit_message_text(text=f'*• ارسل عدد الاعضاء المراد تمويلهم ❇️*\n\n• كل 1 عضو 👤 = {price_join} نقطة\n\n*• نقاطك : *{coin}',chat_id=cid, message_id=mid,reply_markup=bk, parse_mode="Markdown")
        bot.register_next_step_handler(x, tmmo)
    if data == 'back':
        chat_id = call.from_user.id
        a = ['leave', 'member', 'vote', 'spam', 'userbot', 'forward', 'linkbot', 'view', 'poll', 'react', 'reacts']
        for temp in a:
            db.delete(f'{a}_{cid}_proccess')
        user_id = call.from_user.id
        keys = mk(row_width=3)
        coin = get(user_id)['coins']
        btn1 = btn(f'نقاطك : {coin}', callback_data='none')
        btn2 = btn('الخدمات 🛍', callback_data='ps')
        btn3 = btn('اعدادات حسابك ⚙️', callback_data='settings')
        btn4 = btn('تجميع النقاط ❇️', callback_data='collect')
        btn5 = btn('تحويل نقاط ♻️', callback_data='sendd')
        btn6 = btn('قناة البوت 🩵', url='https://t.me/H_H6H')
        btn7 = btn('شراء نقاط 💰', callback_data='buy')
        btn8 = btn('استخدام كود 💳', callback_data='use_code')
        btn9 = btn('شروط الاستخدام 📜', callback_data='privacy')
        btn10 = btn('تمويلاتي 📮', callback_data='mytm')
        btn11 = btn('الاحصائيات 📊', callback_data='sttat')
        btn12 = btn('شريط المهام 〽️', callback_data='tape')
        keys.add(btn1)
        keys.add(btn2)
        keys.add(btn4, btn3)
        keys.add(btn8, btn5)
        keys.add(btn9, btn7)
        keys.add(btn6)
        keys.add(btn12)
        keys.add(btn10, btn11)
        keys.add(btn(f'عدد الطلبات : {count_ord} ✅', callback_data='11'))
        bot.edit_message_text(text=mm,chat_id=cid,message_id=mid,reply_markup=keys)
        return False
    if data == 'sendd':
        wt = db.get(f"serv_{cid}")
        if wt is True:
            bot.edit_message_text(text='<strong>• لا يمكنك تحويل نقاط اثناء تنفيذ طلبك\n\n• برجاء الانتظار لحين يتم اكتمال طلبك الاول</strong>',chat_id=cid,message_id=mid,reply_markup=bk)
            return
        coin = get(user_id)['coins']
        ko = f"• ♻️] تحويل نقاط 〽️\n• ❇️] نقاطك : {coin}\n\nاختر طريقة التحويل :"
        keys = mk(row_width=3)
        btn2 = btn('تحويل الي شخص 👤', callback_data='send')
        btn3 = btn('تحويل الي رابط 📎', callback_data='send_link')
        btn4 = btn('رجوع ↪️', callback_data='back')
        keys.add(btn2)
        keys.add(btn3)
        keys.add(btn4)
        bot.edit_message_text(text=ko,chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'sttat':
        cid, data, mid = call.from_user.id, call.data, call.message.id
        bot.answer_callback_query(call.id, text="• جارى تحميل الاحصائيات 📊")
        db.set(f"serv_{cid}", False)
        user_id = call.from_user.id
        chats = db.get('force')
        force_msg = str(db.get("force_msg"))
        count = 0
        mon = 0
        users = db.keys()
        for i in users:
            if "user_" in str(i[0]):
                count+=1
        for i in users:
            if "user_" in str(i[0]) and "gift" not in str(i[0]) or 'price_' not in str(i[0]) or 'sessions' not in str(i[0]):
                try:
                    i = db.get(i[0])
                    mon+=int(i['coins'])
                except:
                    continue
        b = calculate_inflation(mon, mon-1000)
        members = db.get("members") if db.exists("members") else 0
        tm = db.get("tmoil") if db.exists("tmoil") else 0
        numch = len(db.get("force_ch"))
        keys = mk(
            [
                [btn(text='رجوع ↪️', callback_data='back')]
            ]
        )
        y = trend()
        k = coinsn()
        good = 0
        users = db.keys('user_%')
        for ix in users:
            try:
                d = db.get(ix[0])['id']
                good+=1
            except: continue 
  
        rk = f"""<strong>• احصائيات البوت 📊</strong>

<strong>• عدد مستخدمين البوت : </strong>{good} 👥

<strong>• عدد عمليات التمويل المكتملة : </strong>{tm} 📮
<strong>• عدد القنوات الجاري تمويلها : </strong>{numch} ⏳
<strong>• عدد الاعضاء اللي تم تمويلهم : </strong>{members} 👤

<strong>• نسبة الضغط في البوت : </strong>%{b} 📉

{y}

{k}

"""
        bot.edit_message_text(text=rk, chat_id=cid, message_id=mid,reply_markup=keys, parse_mode="HTML")
    if data == 'getinfo':
        x = bot.edit_message_text(text='• ارسل ايدي الشخص الذي تريد معرفة معلوماته', chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, get_info)
    if data == 'privacy':
        hh = """
• شروط استخدام بوت رشق strt 📜 : 

• وظيفة البوت هو تحصيل نسب عالية من التفاعل في قناتك.

• لا يحق استخدام سبام رسائل في سب او شتم شخص ما ، في حالة المخالفة : حظر دائم من البوت.

• عدم استخدام الخدمات في التفاعلات السلبية علي اي من الديانات السموية الاخري بغرض الاسائة او الاستفذاذ.

• ممنوع طلب معرفة معلومات او نقاط شخص ما في البوت.

• لا تستخدم الخدمات الا في حالة توفر شروط الخدمة

• ممنوع منعا باتاً استخدام ميزة التعليقات في سب او شتم شخص ما مهما كانت ديانته

• يحق للمطور بازالة او اضافة شروط استخدام جديدة في اي وقت.

• يتم تحميلك كامل المسؤولية عند استخدام البوت بشكل خاطئ ، ولا يوجد ضمانات لاسترجاع نقاطك ، او الغاء حظر حسابك

• قناة البوت الاساسية : @H_H6H
• المطور الوحيد للبوت : @H_H6H

• شكرا لاستخدامكم بوت strt 〽️"""
        x = bot.edit_message_text(text=hh, chat_id=cid, message_id=mid,reply_markup=bk)
    if data == 'gen_code':
        x = bot.edit_message_text(text='• ارسل الان الكود الذي تريد صنعه', chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, gen_code_name)
    if data == 'lvall':
        keys = mk(row_width=2)
        btn2 = btn('تاكيد المغادرة',callback_data='lvallc')
        btn3 = btn('الغاء',callback_data='cancel')
        keys.add(btn2)
        keys.add(btn3)
        bot.edit_message_text(text='هل انت متاكد من مغادرة كل القنوات والمجموعات ؟',chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'ps':
        keys = mk(row_width=2)
        btn2 = btn('الخدمات المجانية',callback_data='free')
        btn3 = btn('الخدمات الـ ᴠɪᴘ',callback_data='vips')
        btn4 = btn('تمويل قناة او مجموعة',callback_data='tmoo')
        keys.add(btn3)
        keys.add(btn2)
        keys.add(btn4)
        keys.add(btn('رجوع ↪️', callback_data='back'))
        bot.edit_message_text(text='• مرحبا بك في قسم الخدمات ، اختر من بين الازرار ادناه 〽️',chat_id=cid,message_id=mid,reply_markup=keys)
        return
    if data == 'free':
        a = ['leave', 'member', 'vote', 'spam', 'userbot', 'forward', 'linkbot', 'view', 'poll', 'react', 'reacts']
        for temp in a:
            user_id = call.from_user.id
            db.delete(f'{a}_{user_id}_proccess')
        count = 0
        mon = 0
        users = db.keys()
        for i in users:
            if "user_" in str(i[0]) and "gift" not in str(i[0]) or 'price_' not in str(i[0]) or 'sessions' not in str(i[0]):
                try:
                    i = db.get(i[0])
                    mon+=int(i['coins'])
                except:
                    continue
        b = calculate_inflation(mon, mon-1000)
        keys = mk(row_width=2)
        dag = btn(f'{b}%',callback_data='daag')
        dag2 = btn(f'ضغط الخدمات العادية',callback_data='daag')
        btn2 = btn('تصويت لايكات مسابقات',callback_data='votes')
        btn3 = btn('رشق تفاعلات اختياري',callback_data='react')
        btn5 = btn('رشق تفاعلات عشوائي',callback_data='reacts')
        btn6 = btn('رشق توجيهات علي منشور القناة',callback_data='forward')
        btn7 = btn('رشق مشاهدات ',callback_data='view')
        btn8 = btn('رشق استفتاء',callback_data='poll')
        btn9 = btn('رشق روابط دعوة بدون اشتراك اجبارى',callback_data='linkbot')
        btn10 = btn('رشق تفاعلات [👍,❤,🔥,😍,🤩]',callback_data='positive')
        btn11 = btn('رشق تفاعلات [👎,💩,🤮,🤬,🖕]',callback_data='negative')
        keys.add(dag, dag2)
        keys.add(btn2)
        keys.add(btn3, btn5)
        keys.add(btn6)
        keys.add(btn7, btn8)
        keys.add(btn9)
        keys.add(btn10, btn11)
        keys.add(btn('رجوع ↪️', callback_data='ps'))
        bot.edit_message_text(text='مرحبا بك عزيزي في قسم خدمات الرشق العادية 🆓',chat_id=cid,message_id=mid,reply_markup=keys)
        bot.answer_callback_query(call.id, text="قسم الخدمات العادية 🆓")
    if data == 'vips':
        a = ['leave', 'member', 'vote', 'spam', 'userbot', 'forward', 'linkbot', 'view', 'poll', 'react', 'reacts']
        for temp in a:
            user_id = call.from_user.id
            db.delete(f'{a}_{user_id}_proccess')
        keys = mk(row_width=2)
        dag = btn(f'0%',callback_data='daag')
        dag2 = btn(f'ضغط الخدمات الـ ᴠɪᴘ',callback_data='daag')
        btn1 = btn('سبام رسائل (بوتات ، جروبات ، حسابات) ', callback_data='spams')
        btn01 = btn('تصويت لايكات زر مخصص',callback_data='click_force')
        btn3 = btn('رشق اعضاء قناة عامة ',callback_data='members')
        btn4 = btn('رشق اعضاء قناة خاصة ',callback_data='membersp')
        btn8 = btn('رشق مستخدمين البوت',callback_data='userbot')
        btn9 = btn('رشق تعليقات',callback_data='comments')
        btn10 = btn('رشق روابط دعوة اشتراك اجبارى',callback_data='linkbot2')
        btn11 = btn('سحب تصويتات',callback_data='dump_votes')
        keys.add(dag, dag2)
        keys.add(btn01)
        keys.add(btn1)
        keys.add(btn3, btn4)
        keys.add(btn8)
        keys.add(btn9)
        keys.add(btn10)
        keys.add(btn11)
        keys.add(btn('رجوع ↪️', callback_data='ps'))
        bot.edit_message_text(text='• مرحبا بك في قسم المشتركين الـ ᴠɪᴘ , يمكن للمشتركين الـ ᴠɪᴘ استخدام هذا القسم فقط 〽️',chat_id=cid,message_id=mid,reply_markup=keys)
        bot.answer_callback_query(call.id, text="قسم الخدمات الـ ᴠɪᴘ 〽️")
    if data == 'collect':
        keys = mk(row_width=2)
        btn1 = btn('الهدية اليومية 🎁', callback_data='dailygift')
        btn3 = btn('رابط الدعوة 🌀',callback_data='share_link')
        btn4 = btn('الاشتراك بالقنوات والجموعات 📣',callback_data='join_ch')
        btn5 = btn('الاشتراك بالقنوات × 10 📣',callback_data='join_10')
        keys.add(btn3, btn1)
        keys.add(btn4)
        keys.add(btn5)
        keys.add(btn('رجوع ↪️', callback_data='back'))
        bot.edit_message_text(text='• مرحبا بك في قسم تجميع النقاط 〽️\n\n• يمكنك تجميع النقاط عبر :\n\n• مشاركة رابط الدعوة 🌀\n• هدية يومية 🎁\n• الاشتراك بالقنوات والجموعات 📣\n\n• لا تنسي القاء نظرة علي جوائز مشاركة روابط الدعوة 🌀',chat_id=cid,message_id=mid,reply_markup=keys)
        return
    if data == 'settings':
        keys = mk(row_width=2)
        btn1 = btn('معلومات حسابك 🗃', callback_data='account')
        btn3 = btn('اعدادات حسابك 🛠',callback_data='setacc')
        keys.add(btn3, btn1)
        keys.add(btn('رجوع ↪️', callback_data='back'))
        bot.edit_message_text(text='<strong>• مرحبا بك في قسم اعدادات حسابك ⚙️\n\n• اختر ما يناسبك من الازرار ادناه 📥</strong>',chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'setacc':
        keys = mk(row_width=2)
        btn1 = btn('تغيير السلييب', callback_data='chtime')
        btn3 = btn('ℹ️',callback_data='infotime')
        keys.add(btn3, btn1)
        keys.add(btn('رجوع ↪️', callback_data='settings'))
        bot.edit_message_text(text='• مرحبا بك في قسم اعدادات حسابك 🛠\n\n• اضغط علي (ℹ️) ، لمعرفة المزيد حول الاعداد',chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'chtime':
        keys = mk(row_width=2)
        keys.add(btn('رجوع ↪️', callback_data='setacc'))
        tim = db.get(f"tim_{cid}") if db.exists(f"tim_{cid}") else 0
        x = bot.edit_message_text(text=f'• المدة الحالية للوقت بين كل رشق : {tim} ⏱\n\n• ارسل الان الوقت الجديد ( بالثواني) :',chat_id=cid,message_id=mid,reply_markup=keys)
        bot.register_next_step_handler(x, chtime)
    if data == 'infotime':
        keys = mk(row_width=2)
        keys.add(btn('رجوع ↪️', callback_data='setacc'))
        bot.edit_message_text(text='• السلييب (⏱) : هو الوقت المقدر بين كل رشق في جميع الخدمات بالبوت ما عدا خدمة التصويتات تحدد يدويا \n\n• تم تصميم هذا القسم ليساعد المستخدم في اختصار الوقت عليه في تحديد الوقت يدوي\n\n• عليك ارسال الوقت بين كل رشق بالثواني ، اذا اردت الرشق يكون فوري عين القيمة ب (0)\n\n• اعلي قيمة للوقت هي (200) ثانية ، اقل قيمة (0)',chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'leave':
        if cid in admins:
            db.set(f'leave_{cid}_proccess', True)
            x = bot.edit_message_text(text='ارسل رابط اذا القناة خاصه، اذا عامه ارسل معرفها فقط؟',reply_markup=bk,chat_id=cid,message_id=mid)
        type = 'leavs'
        bot.register_next_step_handler(x, get_amount, type)
    if data == 'use_code':
        keys = mk(row_width=2)
        keys.add(btn('الغاء ❌', callback_data='back'))
        x = bot.edit_message_text(text='• [💳] ارسل الكود الان',reply_markup=keys,chat_id=cid,message_id=mid)
        bot.register_next_step_handler(x, use_codes)
    if data == 'setforce':
        x = bot.edit_message_text(text='• قم بارسال معرفات القنوات هكذا \n@first @second',reply_markup=bk,chat_id=cid,message_id=mid)
        bot.register_next_step_handler(x, setfo)
    if data == 'admins':
        get_admins = db.get('admins')
        if get_admins:
            if len(get_admins) >=1:
                txt = 'الادمنية : \n'
                for ran, admin in enumerate(get_admins, 1):
                    try:
                        info = bot.get_chat(admin)
                        username = f'{ran} @'+str(info.username)+' | {admin}\n' if info.username else f'{ran} {admin} .\n'
                        txt+=username
                    except:
                        txt+=f'{ran} {admin}\n'
                bot.edit_message_text(chat_id=cid, message_id=mid, text=txt)
                return
            else:
                bot.edit_message_text(chat_id=cid, message_id=mid, text=f'لا يوجد ادمنية بالبوت')
                return
        else:
            bot.edit_message_text(chat_id=cid, message_id=mid, text='لا يوجد ادمنية بالبوت')
            return
    if data == 'votes':
        wt = db.get(f"serv_{cid}")
        if wt is True:
            bot.edit_message_text(text='<strong>• لا يمكنك طلب اكثر من طلب بنفس الوقت\n\n• برجاء الانتظار لحين يتم اكتمال طلبك الاول</strong>',chat_id=cid,message_id=mid,reply_markup=bk)
            return
        db.set(f'vote_{cid}_proccess', True)
        x = bot.edit_message_text(text=f'• حسنا ، ارسل الان عدد التصويتات التي تريدها\n\n• سعر الخدمة : {vote_price} نقطة لكل تصويت',chat_id=cid,message_id=mid)
        type = 'votes'
        bot.register_next_step_handler(x, get_amount, type)
    if data == 'buy':
        keys = mk(row_width=2)
        keys.add(btn('رجوع ↪️', callback_data='back'))
        hakem = '''*• لشراء نقاط في بوت رشق star :*

• 1$ = 2000 نقطة
• 5$ = 10000 نقطة
• 10$ = 20000 نقطة
• 25$ = 50000 نقطة

*• اسعار تفعيل اشتراك ᴠɪᴘ في بوت strt :*

- اشتراك لمدة اسبوع : 3$
- إشتراك لمدة شهر : 10$

*• ملحوظة :*

- العملة $ = دولار امريكي 🇱🇷
- عند الدفع يتم محاسبتك بسعر الدولار الامريكي في البلد الخاص بك 

*• طرق الدفع المتوفرة :*

- اسياسيل | زين كاش | فوادفون كاش | اتصالات كاش | اورنچ كاش | ايداع كريمي

• للتواصل والاستفسار : @w3ww5'''
        bot.edit_message_text(text=hakem,chat_id=cid,message_id=mid,parse_mode="Markdown",reply_markup=keys)
    if data == 'dump_votes':
        user_id = call.from_user.id
        prem = get(user_id)['premium']
        if prem is True:
            x = check_vip(call.from_user.id)
            keys = mk(row_width=2)
            keys.add(btn('رجوع ↪️', callback_data='vips'))
            if x is None:
                bot.edit_message_text(text='<strong>• عذرا عزيزي لقد انتهي اشتراكك الـ ᴠɪᴘ\n\n• قم بتجديد الاشتراك مجددا</strong>',chat_id=cid,message_id=mid,reply_markup=keys)
                return 
            db.set(f'dump_votes_{cid}_proccess', True)
            x = bot.edit_message_text(text='• حسنا ، ارسل الان رابط المنشور الذي تريد سحب المنشورات منه ',reply_markup=bk,chat_id=cid,message_id=mid)
            bot.register_next_step_handler(x, dump_votes)
        else:
            keys = mk(row_width=2)
            keys.add(btn('رجوع ↪️', callback_data='vips'))
            bot.edit_message_text(text='• عذرا عليك شراء عضوية ᴠɪᴘ قبل استخدام هذا القسم',chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'share_link':
        bot_user = None
        try:
            x = bot.get_me()
            bot_user = x.username
        except:
            bot.edit_message_text(text=f'• حدث خطا ما في البوت',chat_id=cid,message_id=mid,reply_markup=bk)
            return
        link = f'https://t.me/{bot_user}?start={cid}'
        y = trend()
        keys = mk(row_width=2)
        keys.add(btn('رجوع ↪️', callback_data='collect'))
        inviting = db.get(f"invite_{cid}") if db.exists(f"invite_{cid}") else 0
        gghh = 10 - int(inviting)
        xyz = f'''<strong>انسخ الرابط ثم قم بمشاركته مع اصدقائك !!</strong>\n• كل شخص يقوم بالدخول ستحصل على <strong>{link_price}</strong> نقطه\n\n• كل <strong>10</strong> اشخاص يدخلون عبر الرابط الخاص بك ستحصل علي <strong>500</strong> نقطة هدية 🎁\n\n• مشاركتك للرابط : <strong>{len(get(cid)["users"])} </strong>\n• تبقي لك دعوة <strong>{gghh}</strong> اشخاص حتي تحصل علي <strong>500</strong> نقطة 🌀\n• [🌀] رابط الدعوة : \n\n• {link}\n\n{y}'''
        bot.edit_message_text(text=xyz,chat_id=cid,message_id=mid,reply_markup=keys)

    if data == 'members':
        user_id = call.from_user.id
        prem = get(user_id)['premium']
        if prem is True:
            x = check_vip(call.from_user.id)
            keys = mk(row_width=2)
            keys.add(btn('رجوع ↪️', callback_data='vips'))
            if x is None:
                bot.edit_message_text(text='<strong>• عذرا عزيزي لقد انتهي اشتراكك الـ ᴠɪᴘ\n\n• قم بتجديد الاشتراك مجددا</strong>',chat_id=cid,message_id=mid,reply_markup=keys)
                return 
            db.set(f'member_{cid}_proccess', True)
            x = bot.edit_message_text(text=f'• حسنا ، ارسل عدد الاعضاء التي تريد ارسالها \n\n• سعر الخدمة : {member_price} نقطة لكل عضو',chat_id=cid,message_id=mid)
            type = 'members'
            bot.register_next_step_handler(x, get_amount, type)
        else:
            keys = mk(row_width=2)
            keys.add(btn('رجوع ↪️', callback_data='vips'))
            bot.edit_message_text(text='• عذرا عليك شراء عضوية ᴠɪᴘ قبل استخدام هذا القسم',chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'membersp':
        user_id = call.from_user.id
        prem = get(user_id)['premium']
        if prem is True:
            x = check_vip(call.from_user.id)
            keys = mk(row_width=2)
            keys.add(btn('رجوع ↪️', callback_data='vips'))
            if x is None:
                bot.edit_message_text(text='<strong>• عذرا عزيزي لقد انتهي اشتراكك الـ ᴠɪᴘ\n\n• قم بتجديد الاشتراك مجددا</strong>',chat_id=cid,message_id=mid,reply_markup=keys)
                return
            wt = db.get(f"serv_{cid}")
            if wt is True:
                bot.edit_message_text(text='<strong>• لا يمكنك طلب اكثر من طلب بنفس الوقت\n\n• برجاء الانتظار لحين يتم اكتمال طلبك الاول</strong>',chat_id=cid,message_id=mid,reply_markup=bk)
                return
            db.set(f'memberp_{cid}_proccess', True)
            x = bot.edit_message_text(text=f'• حسنا ، ارسل عدد الاعضاء التي تريد ارسالها \n\n• سعر الخدمة : {member_price} نقطة لكل عضو',chat_id=cid,message_id=mid)
            type = 'membersp'
            bot.register_next_step_handler(x, get_amount, type)
        else:
            keys = mk(row_width=2)
            keys.add(btn('رجوع ↪️', callback_data='vips'))
            bot.edit_message_text(text='• عذرا عليك شراء عضوية ᴠɪᴘ قبل استخدام هذا القسم',chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'spams':
        user_id = call.from_user.id
        prem = get(user_id)['premium']
        if prem is True:
            x = check_vip(call.from_user.id)
            keys = mk(row_width=2)
            keys.add(btn('رجوع ↪️', callback_data='vips'))
            if x is None:
                bot.edit_message_text(text='<strong>• عذرا عزيزي لقد انتهي اشتراكك الـ ᴠɪᴘ\n\n• قم بتجديد الاشتراك مجددا</strong>',chat_id=cid,message_id=mid,reply_markup=keys)
                return 
            wt = db.get(f"serv_{cid}")
            if wt is True:
                bot.edit_message_text(text='<strong>• لا يمكنك طلب اكثر من طلب بنفس الوقت\n\n• برجاء الانتظار لحين يتم اكتمال طلبك الاول</strong>',chat_id=cid,message_id=mid,reply_markup=bk)
                return
            db.set(f'spam_{cid}_proccess', True)
            x = bot.edit_message_text(text=f'• ارسل الان عدد الرسائل التي تريد ارسالها اسبام\n\n• سعر الخدمة : {spam_price} نقطة لكل رسالة',chat_id=cid,message_id=mid)
            type = 'msgs'
            bot.register_next_step_handler(x, get_amount, type)
        else:
            keys = mk(row_width=2)
            keys.add(btn('رجوع ↪️', callback_data='vips'))
            bot.edit_message_text(text='• عذرا عليك شراء عضوية ᴠɪᴘ قبل استخدام هذا القسم',chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'click_force':
        user_id = call.from_user.id
        prem = get(user_id)['premium']
        if prem is True:
            x = check_vip(call.from_user.id)
            keys = mk(row_width=2)
            keys.add(btn('رجوع', callback_data='vips'))
            if x is None:
                bot.edit_message_text(text='• عذرا عليك شراء عضوية VIP',chat_id=cid,message_id=mid,reply_markup=keys)
                
                return 
            x = bot.edit_message_text(text=f'• حسنا ، ارسل رابط المنشور الذي تريد التصويت عليه',chat_id=cid,message_id=mid,reply_markup=keys)
            bot.register_next_step_handler(x, get_url_click_force)
        else:
            keys = mk(row_width=2)
            keys.add(btn('رجوع', callback_data='vips'))
            bot.edit_message_text(text='• عذرا عليك شراء عضوية VIP',chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'react':
        wt = db.get(f"serv_{cid}")
        if wt is True:
            bot.edit_message_text(text='<strong>• لا يمكنك طلب اكثر من طلب بنفس الوقت\n\n• برجاء الانتظار لحين يتم اكتمال طلبك الاول</strong>',chat_id=cid,message_id=mid,reply_markup=bk)
            return
        db.set(f'react_{cid}_proccess', True)
        x = bot.edit_message_text(text=f'• ارسل الان عدد التفاعلات التي تريد رشقها \n\n• سعر الخدمة : {react_price} نقطة لكل تفاعل',chat_id=cid,message_id=mid)
        type = 'react'
        bot.register_next_step_handler(x, get_amount, type)
    if data == 'reacts':
        wt = db.get(f"serv_{cid}")
        if wt is True:
            bot.edit_message_text(text='<strong>• لا يمكنك طلب اكثر من طلب بنفس الوقت\n\n• برجاء الانتظار لحين يتم اكتمال طلبك الاول</strong>',chat_id=cid,message_id=mid,reply_markup=bk)
            return
        db.set(f'reacts_{cid}_proccess', True)
        x = bot.edit_message_text(text=f'• ارسل الان عدد التفاعلات التي تريد رشقها بشكل عشوائي \n\n• سعر الخدمة : {react_price} نقطة لكل تفاعل',chat_id=cid,message_id=mid)
        type = 'reactsrandom'
        bot.register_next_step_handler(x, get_amount, type)
    if data == 'positive':
        wt = db.get(f"serv_{cid}")
        if wt is True:
            bot.edit_message_text(text='<strong>• لا يمكنك طلب اكثر من طلب بنفس الوقت\n\n• برجاء الانتظار لحين يتم اكتمال طلبك الاول</strong>',chat_id=cid,message_id=mid,reply_markup=bk)
            return
        db.set(f'reacts_{cid}_proccess', True)
        x = bot.edit_message_text(text=f'• ارسل الان عدد التفاعلات التي تريد رشقها ايجابيا \n\n• سعر الخدمة : {react_price} نقطة لكل تفاعل',chat_id=cid,message_id=mid)
        type = 'positive'
        bot.register_next_step_handler(x, get_amount, type)
    if data == 'negative':
        wt = db.get(f"serv_{cid}")
        if wt is True:
            bot.edit_message_text(text='<strong>• لا يمكنك طلب اكثر من طلب بنفس الوقت\n\n• برجاء الانتظار لحين يتم اكتمال طلبك الاول</strong>',chat_id=cid,message_id=mid,reply_markup=bk)
            return
        db.set(f'reacts_{cid}_proccess', True)
        x = bot.edit_message_text(text=f'• ارسل الان عدد التفاعلات التي تريد رشقها سلبيا \n\n• سعر الخدمة : {react_price} نقطة لكل تفاعل',chat_id=cid,message_id=mid)
        type = 'negative'
        bot.register_next_step_handler(x, get_amount, type)
    if data == 'forward':
        wt = db.get(f"serv_{cid}")
        if wt is True:
            bot.edit_message_text(text='<strong>• لا يمكنك طلب اكثر من طلب بنفس الوقت\n\n• برجاء الانتظار لحين يتم اكتمال طلبك الاول</strong>',chat_id=cid,message_id=mid,reply_markup=bk)
            return
        db.set(f'forward_{cid}_proccess', True)
        x = bot.edit_message_text(text=f'• ارسل الان عدد التوجيهات التي تريد رشقها علي منشور القناة \n\n• سعر الخدمة : {forward_price} نقطة لكل توجيه',chat_id=cid,message_id=mid)
        type = 'forward'
        bot.register_next_step_handler(x, get_amount, type)
    if data == 'view':
        wt = db.get(f"serv_{cid}")
        if wt is True:
            bot.edit_message_text(text='<strong>• لا يمكنك طلب اكثر من طلب بنفس الوقت\n\n• برجاء الانتظار لحين يتم اكتمال طلبك الاول</strong>',chat_id=cid,message_id=mid,reply_markup=bk)
            return
        db.set(f'view_{cid}_proccess', True)
        x = bot.edit_message_text(text=f'• ارسل الان عدد المشاهدات اللي تريد ترشقها علي منشور القناة \n\n• سعر الخدمة : {view_price} نقطة لكل مشاهده',chat_id=cid,message_id=mid)
        type = 'view'
        bot.register_next_step_handler(x, get_amount, type)
    if data == 'poll':
        wt = db.get(f"serv_{cid}")
        if wt is True:
            bot.edit_message_text(text='<strong>• لا يمكنك طلب اكثر من طلب بنفس الوقت\n\n• برجاء الانتظار لحين يتم اكتمال طلبك الاول</strong>',chat_id=cid,message_id=mid,reply_markup=bk)
            return
        db.set(f'poll_{cid}_proccess', True)
        x = bot.edit_message_text(text=f'• ارسل الان عدد الاستفتاء الذي تريد رشقه \n\n• سعر الخدمة : {poll_price} نقطة لكل تصويت',chat_id=cid,message_id=mid)
        type = 'poll'
        bot.register_next_step_handler(x, get_amount, type)
    if data == 'change_price':
        type = 'change_price'
        x  = bot.edit_message_text(text=f'• لتغيير سعر الخدمات اتبع التعليمات \n\n• لتغيير سعر التصويتات ارسل : <code>vote_price</code>\n\n• لتغيير سعر الاسبام ارسل : <code>spam_price</code>\n\n• لتغيير سعر التفاعلات ارسل : <code>react_price</code>\n\n• لتغيير سعر المشاهدات ارسل : <code>view_price</code>\n\n• لتغيير سعر الاعضاء ارسل : <code>member_price</code>',chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, adminss, type)
    if data == 'userbot':
        user_id = call.from_user.id
        prem = get(user_id)['premium']
        if prem is True:
            x = check_vip(call.from_user.id)
            keys = mk(row_width=2)
            keys.add(btn('رجوع ↪️', callback_data='vips'))
            if x is None:
                bot.edit_message_text(text='<strong>• عذرا عزيزي لقد انتهي اشتراكك الـ ᴠɪᴘ\n\n• قم بتجديد الاشتراك مجددا</strong>',chat_id=cid,message_id=mid,reply_markup=keys)
                return 
            wt = db.get(f"serv_{cid}")
            if wt is True:
                bot.edit_message_text(text='<strong>• لا يمكنك طلب اكثر من طلب بنفس الوقت\n\n• برجاء الانتظار لحين يتم اكتمال طلبك الاول</strong>',chat_id=cid,message_id=mid,reply_markup=bk)
                return
            db.set(f'userbot_{cid}_proccess', True)
            x = bot.edit_message_text(text=f'• ارسل الان عدد المستخدمين الذي تريد ترشقهم للبوت الخاص بك \n\n• سعر الخدمة : {userbot_price} نقطة لكل مستخدم',chat_id=cid,message_id=mid)
            type = 'userbot'
            bot.register_next_step_handler(x, get_amount, type)
        else:
            keys = mk(row_width=2)
            keys.add(btn('رجوع ↪️', callback_data='vips'))
            bot.edit_message_text(text='• عذرا عليك شراء عضوية ᴠɪᴘ قبل استخدام هذا القسم',chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'linkbot':
        wt = db.get(f"serv_{cid}")
        if wt is True:
            bot.edit_message_text(text='<strong>• لا يمكنك طلب اكثر من طلب بنفس الوقت\n\n• برجاء الانتظار لحين يتم اكتمال طلبك الاول</strong>',chat_id=cid,message_id=mid,reply_markup=bk)
            return
        db.set(f'linkbot_{cid}_proccess', True)
        x = bot.edit_message_text(text=f'• ارسل الان عدد روابط الدعوة التي تريد رشقها \n\n• سعر الخدمة : {linkbot_price} نقطة لكل دعوة',chat_id=cid,message_id=mid)
        type = 'linkbot'
        bot.register_next_step_handler(x, get_amount, type)
    if data == 'comments':
        user_id = call.from_user.id۸
        prem = get(user_id)['premium']
        if prem is True:
            x = check_vip(call.from_user.id)
            keys = mk(row_width=2)
            keys.add(btn('رجوع ↪️', callback_data='vips'))
            if x is None:
                bot.edit_message_text(text='<strong>• عذرا عزيزي لقد انتهي اشتراكك الـ ᴠɪᴘ\n\n• قم بتجديد الاشتراك مجددا</strong>',chat_id=cid,message_id=mid,reply_markup=key)
                return 
            wt = db.get(f"serv_{cid}")
            if wt is True:
                bot.edit_message_text(text='<strong>• لا يمكنك طلب اكثر من طلب بنفس الوقت\n\n• برجاء الانتظار لحين يتم اكتمال طلبك الاول</strong>',chat_id=cid,message_id=mid,reply_markup=bk)
                return
            db.set(f'comments_{cid}_proccess', True)
            x = bot.edit_message_text(text=f'• ارسل الان عدد التعليقات التي تريد رشقها \n\n• سعر الخدمة : {comment_price} نقطة لكل تعليق',chat_id=cid,message_id=mid)
            type = 'comments'
            bot.register_next_step_handler(x, get_amount, type)
        else:
            keys = mk(row_width=2)
            keys.add(btn('رجوع ↪️', callback_data='vips'))
            bot.edit_message_text(text='• عذرا عليك شراء عضوية ᴠɪᴘ قبل استخدام هذا القسم',chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'tape':
        how = ""
        x = giiiift(cid)
        if x is not None:
            duration = datetime.timedelta(seconds=x)
            noww = datetime.datetime.now()
            target_datetime = noww + duration
            remaining_time = target_datetime - noww
            hours = remaining_time.seconds // 3600
            minutes = (remaining_time.seconds % 3600) // 60
            seconds = remaining_time.seconds % 60
            if hours > 0:
                how = f"❌"
                hoow = "0/1"
            elif minutes > 0:
                how = f"❌"
                hoow = "0/1"
            else:
                how = f"❌"
                hoow = "0/1"
        else:
            how = "✅"
            hoow = "1/1"
        typ = float(db.get(f"typ_{cid}")) if db.exists(f"typ_{cid}") else 0.0
        if typ >= 100.0:
            db.set(f"typ_{cid}", 100)
            type = "██████████ ׀<"
        elif typ >= 85.0:
            type = "░▓████████ ׀<"
        elif typ >= 75.0:
            type = "░░▓███████ ׀<"
        elif typ >= 50.0:
            type = "░░░░▓█████ ׀<"
        elif typ >= 25.0:
            type = "░░░░░░▓███ ׀<"
        elif typ >= 15.0:
            type = "░░░░░░░▓██ ׀<"
        elif typ >= 0.0:
            type = "░░░░░░░░░▓ ׀<"
        if typ == 0.0:
            type = "░░░░░░░░░░ ׀<"
        keys = mk(
             [
                 [btn(text=f'الزيادة', callback_data=f'tt'),btn(text=f'الحصول', callback_data=f'tt'),btn(text=f'المتاح', callback_data=f'tt'),btn(text=f'المهام', callback_data=f'tt')],
                 [btn(text=f'0.2%', callback_data=f'tjkt'),btn(text=f'{how}', callback_data='ee'), btn(text=f'{hoow}', callback_data='kk'),btn(text=f'الهدية 🎁', callback_data=f'dailygift')],
                 [btn(text=f'0.3%', callback_data=f'tjklot'),btn(text=f'✅', callback_data='eoke'), btn(text=f'♾', callback_data='kiskk'),btn(text=f'الدعوة 🌀', callback_data=f'share_link')],
                 [btn(text=f'0.1%', callback_data=f'tjklot'),btn(text=f'✅', callback_data='eoe'), btn(text=f'♾', callback_data='kis'),btn(text=f'الانضمام 📣', callback_data=f'join_ch')],
                 [btn(text=f'0.2%', callback_data=f'tvjklot'),btn(text=f'✅', callback_data='eloe'), btn(text=f'♾', callback_data='kiskv'),btn(text=f'التمويل 📮', callback_data=f'tmoo')],
                 [btn(text=f'0.1%', callback_data=f'tvjot'),btn(text=f'✅', callback_data='elo'), btn(text=f'♾', callback_data='kkv'),btn(text=f'التحويل ♻️', callback_data=f'sendd')],
                 [btn(text=f'متجر المهام 🛒', callback_data='market')],
                 [btn(text=f'%{typ} ׀ {type}', callback_data='tto')],
                 [btn(text='رجوع ↪️', callback_data='back')]
             ]
        )
        bot.edit_message_text(text='• مرحبا بك في قسم شريط المهام 〽️\n\n• اكمل المهام واستبدل نسبة الشريط بالهدايا والمكافات في متجر المهام ',chat_id=cid,message_id=mid,reply_markup=keys)
    typ = float(db.get(f"typ_{cid}")) if db.exists(f"typ_{cid}") else 0.0
    if typ >= 100.0:
        db.set(f"typ_{cid}", 100)
        type = "██████████ ׀<"
    elif typ >= 85.0:
        type = "░▓████████ ׀<"
    elif typ >= 75.0:
        type = "░░▓███████ ׀<"
    elif typ >= 50.0:
        type = "░░░░▓█████ ׀<"
    elif typ >= 25.0:
        type = "░░░░░░▓███ ׀<"
    elif typ >= 15.0:
        type = "░░░░░░░▓██ ׀<"
    elif typ >= 0.0:
        type = "░░░░░░░░░▓ ׀<"
    if typ == 0.0:
        type = "░░░░░░░░░░ ׀<"
    if data == 'market':
        typ = float(db.get(f"typ_{user_id}")) if db.exists(f"typ_{cid}") else 0.0
        key = mk(
            [
                [btn(text='الاتاحة', callback_data='pp'),btn(text=f'السعر', callback_data='pp'),btn(text=f'المكافأة', callback_data='pp')],
                [btn(text='قسم النقاط', callback_data='ppo')],
                [btn(text='✅', callback_data='chda'),btn(text=f'50.0%', callback_data='chda'),btn(text=f'5000 نقطة', callback_data='chda')],
                [btn(text='✅', callback_data='chd1'),btn(text=f'10.0%', callback_data='chd1'),btn(text=f'1000 نقطة', callback_data='chd1')],
                [btn(text='قسم الـ ᴠɪᴘ', callback_data='plp')],
                [btn(text='❌', callback_data='chvi'),btn(text=f'100.0%', callback_data='chvi'),btn(text=f'10 يوم ᴠɪᴘ', callback_data='chvi')],
                [btn(text='✅', callback_data='ch5'),btn(text=f'50.0%', callback_data='ch5'),btn(text=f'5 يوم ᴠɪᴘ', callback_data='ch5')],
                [btn(text='✅', callback_data='ch1'),btn(text=f'10.0%', callback_data='ch1'),btn(text=f'1 يوم ᴠɪᴘ', callback_data='ch1')],
                [btn(text=f'%{typ} ׀ {type}', callback_data='tto')],
                [btn(text='رجوع ↪️', callback_data='tape')]
            ]
        )
        bot.edit_message_text(text='• مرحبا بك في متجر شريط المهام 〽️\n• يمكنك استبدال المكافات مقابل نسبة الشريط الحالية لحسابك',chat_id=cid,message_id=mid,reply_markup=key)
    if data == 'chda':
        user_id = call.from_user.id
        typ = float(db.get(f"typ_{user_id}")) if db.exists(f"typ_{cid}") else 0.0
        if typ >= 50.0:
            rk = "تهانينا ، لقد حصلت علي 5000 نقطة وتم خصم 50.0% من نسبة الشريط 🎉"
            typ = float(db.get(f"typ_{cid}")) if db.exists(f"typ_{cid}") else 0.0
            ftt = typ - 50.0
            db.set(f"typ_{cid}", float(ftt))
            info = db.get(f'user_{cid}')
            info['coins'] = int(info['coins']) + 5000
            db.set(f"user_{cid}", info)
            bot.edit_message_text(text=rk,chat_id=cid,message_id=mid,reply_markup=bk)
        else:
            bot.answer_callback_query(call.id, text=f"• عذرا ، نسبة الشريط الحالية {typ} لا تكفي ❌")
    if data == 'chd1':
        user_id = call.from_user.id
        typ = float(db.get(f"typ_{user_id}")) if db.exists(f"typ_{cid}") else 0.0
        if typ >= 10.0:
            rk = "تهانينا ، لقد حصلت علي 1000 نقطة وتم خصم 10.0% من نسبة الشريط 🎉"
            typ = float(db.get(f"typ_{cid}")) if db.exists(f"typ_{cid}") else 0.0
            ftt = typ - 10.0
            db.set(f"typ_{cid}", float(ftt))
            info = db.get(f'user_{cid}')
            info['coins'] = int(info['coins']) + 1000
            db.set(f"user_{cid}", info)
            bot.edit_message_text(text=rk,chat_id=cid,message_id=mid,reply_markup=bk)
        else:
            bot.answer_callback_query(call.id, text=f"• عذرا ، نسبة الشريط الحالية {typ} لا تكفي ❌")
    if data == 'dellink':
        count_coins = db.get("user_trans")
        if count_coins != 0:
            try:
                rand = db.get("user_tran")
                user_from = db.get("user_iddd")
                joo = db.get(f"user_{user_from}")
                info = db.get(f"user_{cid}")
                coins = info['coins']
                rk = f"""*• 📎] تم تعطيل الرابط , وسترداد {count_coins} نقطة ♻️*"""
                bot.edit_message_text(text=rk,chat_id=cid,message_id=mid,parse_mode="Markdown",reply_markup=bk)
                info['coins'] = int(info['coins']) + int(count_coins)
                db.set(f"user_{cid}", info)
                db.delete('user_tran')
                db.delete('user_iddd')
            except:
                rk = f"""*• 📎] تمت انتهاء صلاحية هذا الرابط ❌*"""
                bot.edit_message_text(text=rk,chat_id=cid,message_id=mid,parse_mode="Markdown",reply_markup=bk)
        else:
            rk = f"""*• 📎] تمت انتهاء صلاحية هذا الرابط ❌*"""
            bot.edit_message_text(text=rk,chat_id=cid,message_id=mid,parse_mode="Markdown",reply_markup=bk)
    if data == 'chvi':
        user_id = call.from_user.id
        typ = float(db.get(f"typ_{user_id}")) if db.exists(f"typ_{cid}") else 0.0
        if typ >= 100.0:
            rk = "<strong>• تهانينا ، لقد حصلت علي 10 يوم ᴠɪᴘ  وتم خصم 100.0% من نسبة الشريط 🎉</strong>"
            typ = float(db.get(f"typ_{user_id}")) if db.exists(f"typ_{cid}") else 0.0
            ftt = typ - 100.0
            db.set(f"typ_{user_id}", float(ftt))
            info = db.get(f'user_{user_id}')
            info['premium'] = True
            db.set(f"user_{user_id}", info)
            users = {}
            noww = time.time()
            users['vip'] = noww
            db.set(f'vip_{user_id}', users)
            db.set(f"vipp_{user_id}_time", 5)
            us = bot.get_chat(user_id)
            if us.username is None:
                user = "لا يوجد"
            else:
                user = "@" + us.username
            name = us.first_name
            today = datetime.date.today()
            end_date = today + datetime.timedelta(days=int(10))
            now = datetime.datetime.now()
            HM = now.strftime("%p")
            if str(HM) == str("PM"):
                how = "مساءً"
            else:
                how = "صباحاً"
            hour = now.hour
            minutes = now.minute
            seconds = now.second
            d = 10
            h = 10 * 24
            m = 10 * 24 * 60
            s = 10 * 24 * 60 * 60
            reb2 = f"""*• تهانينا ، تم تفعيل ᴠɪᴘ لحسابك في البوت ✅*\n\n_• مدة الاشتراك  ⏱️:_\n\n- المدة بالايام : {d}\n- المدة بالساعات : {h}\n- المدة بالدقائق : {m}\n- المدة بالثواني : {s}\n\n*• وقت انتهاء اشتراكك :*\n\n- يوم : {end_date}\n- الساعة : {hour} {how}\n- الدقيقة : {minutes}"""
            reb = f"""*• تمت عملية تفعيل ᴠɪᴘ جديده 🔥*
`{user_id}`
*• معلومات الاشتراك والمدة ⏱:*

_• وقت التفعيل :_

- اليوم : {today}
- الساعة : {hour} {how}
- الدقيقة : {minutes}

_• مدة الاشتراك  :_

- المدة بالايام : {d}
- المدة بالساعات : {h}
- المدة بالدقائق : {m}
- المدة بالثواني : {s}

*• وقت انتهاء الاشتراك :*

_• سينتهي اشتراك العضو في :_

- يوم : {end_date}
- الساعة : {hour} {how}
- الدقيقة : {minutes}"""
            bot.send_message(chat_id=int(sudo), text=reb, parse_mode="Markdown")
            bot.send_message(chat_id=int(user_id), text=reb2, parse_mode="Markdown")
            bot.edit_message_text(text=rk,chat_id=cid,message_id=mid,reply_markup=bk)
        else:
            bot.answer_callback_query(call.id, text=f"• عذرا ، هذا العرض غير متاح حالياً ❌")
    if data == 'ch5':
        user_id = call.from_user.id
        typ = float(db.get(f"typ_{user_id}")) if db.exists(f"typ_{cid}") else 0.0
        if typ >= 50.0:
            rk = "<strong>• تهانينا ، لقد حصلت علي 5 يوم ᴠɪᴘ  وتم خصم 50.0% من نسبة الشريط 🎉</strong>"
            typ = float(db.get(f"typ_{user_id}")) if db.exists(f"typ_{cid}") else 0.0
            ftt = typ - 50.0
            db.set(f"typ_{user_id}", float(ftt))
            info = db.get(f'user_{user_id}')
            info['premium'] = True
            db.set(f"user_{user_id}", info)
            users = {}
            noww = time.time()
            users['vip'] = noww
            db.set(f'vip_{user_id}', users)
            db.set(f"vipp_{user_id}_time", 3)
            us = bot.get_chat(user_id)
            if us.username is None:
                user = "لا يوجد"
            else:
                user = "@" + us.username
            name = us.first_name
            today = datetime.date.today()
            end_date = today + datetime.timedelta(days=int(5))
            now = datetime.datetime.now()
            HM = now.strftime("%p")
            if str(HM) == str("PM"):
                how = "مساءً"
            else:
                how = "صباحاً"
            hour = now.hour
            minutes = now.minute
            seconds = now.second
            d = 5
            h = 5 * 24
            m = 5 * 24 * 60
            s = 5 * 24 * 60 * 60
            reb2 = f"""*• تهانينا ، تم تفعيل ᴠɪᴘ لحسابك في البوت ✅*\n\n_• مدة الاشتراك  ⏱️:_\n\n- المدة بالايام : {d}\n- المدة بالساعات : {h}\n- المدة بالدقائق : {m}\n- المدة بالثواني : {s}\n\n*• وقت انتهاء اشتراكك :*\n\n- يوم : {end_date}\n- الساعة : {hour} {how}\n- الدقيقة : {minutes}"""
            reb = f"""*• تمت عملية تفعيل ᴠɪᴘ جديده 🔥*
`{user_id}`
*• معلومات الاشتراك والمدة ⏱:*

_• وقت التفعيل :_

- اليوم : {today}
- الساعة : {hour} {how}
- الدقيقة : {minutes}

_• مدة الاشتراك  :_

- المدة بالايام : {d}
- المدة بالساعات : {h}
- المدة بالدقائق : {m}
- المدة بالثواني : {s}

*• وقت انتهاء الاشتراك :*

_• سينتهي اشتراك العضو في :_

- يوم : {end_date}
- الساعة : {hour} {how}
- الدقيقة : {minutes}"""
            bot.edit_message_text(text=rk,chat_id=cid,message_id=mid,reply_markup=bk)
            bot.send_message(chat_id=int(sudo), text=reb, parse_mode="Markdown")
            bot.send_message(chat_id=int(user_id), text=reb2, parse_mode="Markdown")
        else:
            bot.answer_callback_query(call.id, text=f"• عذرا ، نسبة الشريط الحالية {typ} لا تكفي ❌")
    if data == 'ch1':
        user_id = call.from_user.id
        typ = float(db.get(f"typ_{user_id}")) if db.exists(f"typ_{cid}") else 0.0
        if typ >= 10.0:
            rk = "<strong>• تهانينا ، لقد حصلت علي 1 يوم ᴠɪᴘ  وتم خصم 10.0% من نسبة الشريط 🎉</strong>"
            typ = float(db.get(f"typ_{user_id}")) if db.exists(f"typ_{cid}") else 0.0
            ftt = typ - 10.0
            db.set(f"typ_{user_id}", float(ftt))
            info = db.get(f'user_{user_id}')
            info['premium'] = True
            db.set(f"user_{user_id}", info)
            users = {}
            noww = time.time()
            users['vip'] = noww
            db.set(f'vip_{user_id}', users)
            db.set(f"vipp_{user_id}_time", 1)
            us = bot.get_chat(user_id)
            if us.username is None:
                user = "لا يوجد"
            else:
                user = "@" + us.username
            name = us.first_name
            today = datetime.date.today()
            end_date = today + datetime.timedelta(days=int(1))
            now = datetime.datetime.now()
            HM = now.strftime("%p")
            if str(HM) == str("PM"):
                how = "مساءً"
            else:
                how = "صباحاً"
            hour = now.hour
            minutes = now.minute
            seconds = now.second
            d = 1
            h = 1 * 24
            m = 1 * 24 * 60
            s = 1 * 24 * 60 * 60
            reb2 = f"""*• تهانينا ، تم تفعيل ᴠɪᴘ لحسابك في البوت ✅*\n\n_• مدة الاشتراك  ⏱️:_\n\n- المدة بالايام : {d}\n- المدة بالساعات : {h}\n- المدة بالدقائق : {m}\n- المدة بالثواني : {s}\n\n*• وقت انتهاء اشتراكك :*\n\n- يوم : {end_date}\n- الساعة : {hour} {how}\n- الدقيقة : {minutes}"""
            reb = f"""*• تمت عملية تفعيل ᴠɪᴘ جديده 🔥*
`{user_id}`
*• معلومات الاشتراك والمدة ⏱:*

_• وقت التفعيل :_

- اليوم : {today}
- الساعة : {hour} {how}
- الدقيقة : {minutes}

_• مدة الاشتراك  :_

- المدة بالايام : {d}
- المدة بالساعات : {h}
- المدة بالدقائق : {m}
- المدة بالثواني : {s}

*• وقت انتهاء الاشتراك :*

_• سينتهي اشتراك العضو في :_

- يوم : {end_date}
- الساعة : {hour} {how}
- الدقيقة : {minutes}"""
            bot.edit_message_text(text=rk,chat_id=cid,message_id=mid,reply_markup=bk)
            bot.send_message(chat_id=int(sudo), text=reb, parse_mode="Markdown")
            bot.send_message(chat_id=int(user_id), text=reb2, parse_mode="Markdown")
        else:
            bot.answer_callback_query(call.id, text=f"• عذرا ، نسبة الشريط الحالية {typ} لا تكفي ❌")
    if data == 'lvallc':
        bot.edit_message_text(text='• تم بدء مغادرة كل القنوات والمجموعات بنجاح ✅',chat_id=cid,message_id=mid)
        acc = db.get('accounts')
        amount = len(acc)
        true = 0
        for amount in acc:
            try:
                true+=1
                o = asyncio.run(leave_chats(amount['s']))  
            except Exception as e:
                print(e)
                continue
            id = call.from_user.id
            bot.send_message(chat_id=id, text=f'• تم بنجاح الخروج من كل القنوات والمجموعات \n• تم الخروج من <code>{true}</code> حساب بنجاح ✅')
    if data == 'cancel':
        bot.edit_message_text(text='<strong>• تم الغاء عملية المغادرة ❌</strong>',chat_id=cid,message_id=mid)
    if data == 'linkbot2':
        user_id = call.from_user.id
        prem = get(user_id)['premium']
        if prem is True:
            x = check_vip(call.from_user.id)
            keys = mk(row_width=2)
            keys.add(btn('رجوع ↪️', callback_data='vips'))
            if x is None:
                bot.edit_message_text(text='<strong>• عذرا عزيزي لقد انتهي اشتراكك الـ ᴠɪᴘ\n\n• قم بتجديد الاشتراك مجددا</strong>',chat_id=cid,message_id=mid,reply_markup=keys)
                return 
            db.set(f'linkbot2_{cid}_proccess', True)
            keys = mk(row_width=5)
            a = btn('1', callback_data='c1')
            b = btn('2', callback_data='c2')
            c = btn('3', callback_data='c3')
            d = btn('4', callback_data='c4')
            e = btn('5', callback_data='c5')
            f = btn('رجوع ↪️', callback_data='back')
            keys.add(a,b,c,d,e)
            keys.add(f)
            x = bot.edit_message_text(text=f'• اختر الان عدد قنوات الاشتراك الاجبارى قبل رشق روابط الدعوة',reply_markup=keys,chat_id=cid,message_id=mid)
        else:
            keys = mk(row_width=2)
            keys.add(btn('رجوع ↪️', callback_data='vips'))
            bot.edit_message_text(text=f'• عذرا عليك شراء عضوية ᴠɪᴘ قبل استخدام هذا القسم',chat_id=cid,message_id=mid,reply_markup=keys)
    if data == 'c1':
        user_id = call.from_user.id
        db.set(f'linkbot2_{cid}_proccess', True)
        x = bot.edit_message_text(text=f'• لقد اخترت رشق روابط دعوة لـ <strong>1</strong> قناة اجبارى\n\n• ارسل الان عدد الرشق الذي تريده \n\n• سعر الخدمة : {linkbot2_price} نقطة لكل دعوة',chat_id=cid,message_id=mid)
        type = 'linkbot1'
        bot.register_next_step_handler(x, get_amount, type)
    if data == 'c2':
        user_id = call.from_user.id
        db.set(f'linkbot2_{cid}_proccess', True)
        x = bot.edit_message_text(text=f'• لقد اخترت رشق روابط دعوة لـ <strong>2</strong> قناة اجبارى\n\n• ارسل الان عدد الرشق الذي تريده \n\n• سعر الخدمة : {linkbot2_price} نقطة لكل دعوة',chat_id=cid,message_id=mid)
        type = 'linkbot2'
        bot.register_next_step_handler(x, get_linkbot, type)
    if data == 'c3':
        user_id = call.from_user.id
        db.set(f'linkbot2_{cid}_proccess', True)
        x = bot.edit_message_text(text=f'• لقد اخترت رشق روابط دعوة لـ <strong>3</strong> قناة اجبارى\n\n• ارسل الان عدد الرشق الذي تريده \n\n• سعر الخدمة : {linkbot2_price} نقطة لكل دعوة',chat_id=cid,message_id=mid)
        type = 'linkbot2'
        bot.register_next_step_handler(x, get_linkbot, type)
    if data == 'c4':
        user_id = call.from_user.id
        db.set(f'linkbot2_{cid}_proccess', True)
        x = bot.edit_message_text(text=f'• لقد اخترت رشق روابط دعوة لـ <strong>4</strong> قناة اجبارى\n\n• ارسل الان عدد الرشق الذي تريده \n\n• سعر الخدمة : {linkbot2_price} نقطة لكل دعوة',chat_id=cid,message_id=mid)
        type = 'linkbot2'
        bot.register_next_step_handler(x, get_linkbot, type)
    if data == 'c5':
        user_id = call.from_user.id
        db.set(f'linkbot2_{cid}_proccess', True)
        x = bot.edit_message_text(text=f'• لقد اخترت رشق روابط دعوة لـ <strong>5</strong> قناة اجبارى\n\n• ارسل الان عدد الرشق الذي تريده \n\n• سعر الخدمة : {linkbot2_price} نقطة لكل دعوة',chat_id=cid,message_id=mid)
        type = 'linkbot2'
        bot.register_next_step_handler(x, get_linkbot, type)
    if data == 'mytm':
        user_id = call.from_user.id
        if db.exists(f"Tmoil_{user_id}"):
            ch1 = db.get(f"Tmoil_{user_id}")
            count = int(db.get(f"count_{ch1}")) if db.exists(f"count_{ch1}") else 0
            mem = int(db.get(f"mem_{ch1}")) if db.exists(f"mem_{ch1}") else 0
            if int(count) <= 1:
                stat = "طلب مكتمل 🟢"
                count = 0
            else:
                stat = "قيد التنفيذ ⏳"
            info1 = f"✳️] معرف القناة : {ch1}\n🏷️] الكمية : {mem}\n⏳] المتبقي : {count}\n\n🔘) حالة الطلب : {stat}\nــــــــــــــــــــــــــــــــــــــــــــــــــــ\n"
        else:
            info1 = f"\n\n• لا يوجد تمويلات مسجلة حاليا ❌"
        if db.exists(f"Tmoil2_{user_id}"):
            ch2 = db.get(f"Tmoil2_{user_id}")
            count2 = int(db.get(f"count_{ch2}")) if db.exists(f"count_{ch2}") else 0
            mem2 = int(db.get(f"mem_{ch2}")) if db.exists(f"mem_{ch2}") else 0
            if int(count2) <= 1:
                stat2 = "طلب مكتمل 🟢"
                count2 = 0
            else:
                stat2 = "قيد التنفيذ ⏳"
            info2 = f"✳️] معرف القناة : {ch2}\n🏷️] الكمية : {mem2}\n⏳] المتبقي : {count2}\n\n🔘) حالة الطلب : {stat2}\nــــــــــــــــــــــــــــــــــــــــــــــــــــ\n"
        else:
            info2 = ""
        if db.exists(f"Tmoil3_{user_id}"):
            ch3 = db.get(f"Tmoil3_{user_id}")
            count3 = int(db.get(f"count_{ch3}")) if db.exists(f"count_{ch3}") else 0
            mem3 = int(db.get(f"mem_{ch3}")) if db.exists(f"mem_{ch3}") else 0
            if int(count3) <= 1:
                stat3 = "طلب مكتمل 🟢"
                count3 = 0
            else:
                stat3 = "قيد التنفيذ ⏳"
            info3 = f"✳️] معرف القناة : {ch3}\n🏷️] الكمية : {mem3}\n⏳] المتبقي : {count3}\n\n🔘) حالة الطلب : {stat3}\nــــــــــــــــــــــــــــــــــــــــــــــــــــ\n"
        else:
            info3 = ""
        
        rk = f"""• اليك قائمة باخر 3 تمويلاتك 📮\n{info1}\n{info2}\n{info3}"""
        key = mk(
            [
                [btn(text='ارسال جميع التمويلات في صيغة ملف 📂', callback_data='send_doc')],
                [btn(text='رجوع ↪️', callback_data='back')]
            ]
        )
        bot.edit_message_text(text=rk,chat_id=cid,message_id=mid,reply_markup=key, parse_mode="HTML")
    if data == 'send_doc':
        user_id = call.from_user.id
        if db.exists(f"Tmoil_{user_id}"):
            ch1 = db.get(f"Tmoil_{user_id}")
            count = int(db.get(f"count_{ch1}")) if db.exists(f"count_{ch1}") else 0
            mem = int(db.get(f"mem_{ch1}")) if db.exists(f"mem_{ch1}") else 0
            if int(count) <= 1:
                stat = "طلب مكتمل 🟢"
            else:
                stat = "قيد التنفيذ ⏳"
            info1 = f"✳️] معرف القناة : {ch1}\n🏷️] الكمية : {mem}\n⏳] المتبقي : {count}\n\n🔘) حالة الطلب : {stat}\nــــــــــــــــــــــــــــــــــــــــــــــــــــ\n"
        else:
            info1 = f"\n\n• لا يوجد تمويلات مسجلة حاليا ❌"
        if db.exists(f"Tmoil2_{user_id}"):
            ch2 = db.get(f"Tmoil2_{user_id}")
            count2 = int(db.get(f"count_{ch2}")) if db.exists(f"count_{ch2}") else 0
            mem2 = int(db.get(f"mem_{ch2}")) if db.exists(f"mem_{ch2}") else 0
            if int(count2) <= 1:
                stat2 = "طلب مكتمل 🟢"
            else:
                stat2 = "قيد التنفيذ ⏳"
            info2 = f"✳️] معرف القناة : {ch2}\n🏷️] الكمية : {mem2}\n⏳] المتبقي : {count2}\n\n🔘) حالة الطلب : {stat2}\nــــــــــــــــــــــــــــــــــــــــــــــــــــ\n"
        else:
            info2 = ""
        if db.exists(f"Tmoil3_{user_id}"):
            ch3 = db.get(f"Tmoil3_{user_id}")
            count3 = int(db.get(f"count_{ch3}")) if db.exists(f"count_{ch3}") else 0
            mem3 = int(db.get(f"mem_{ch3}")) if db.exists(f"mem_{ch3}") else 0
            if int(count) <= 1:
                stat3 = "طلب مكتمل 🟢"
            else:
                stat3 = "قيد التنفيذ ⏳"
            info3 = f"✳️] معرف القناة : {ch3}\n🏷️] الكمية : {mem3}\n⏳] المتبقي : {count3}\n\n🔘) حالة الطلب : {stat3}\nــــــــــــــــــــــــــــــــــــــــــــــــــــ\n"
        else:
            info3 = ""
        
        rk = f"""• اليك ملف باخر تمويلاتك 📮\n{info1}\n{info2}\n{info3}"""
        if db.exists(f"Tmoil_{user_id}"):
            with open(f"tmoil-{cid}.txt", "w") as file:
                file.write(rk)
            bot.send_document(cid, open(f"tmoil-{cid}.txt", "rb"), caption="\n• اليك ملف يحتوي علي جميع تمويلاتك في بوت strt 📮")
        else:
            bot.answer_callback_query(call.id, text="• عذرا ، انت لم تقم باي تمويل بعد ❌",show_alert=True)
            return
    if data == 'join_ch':
        user_id = call.from_user.id
        coin_join = db.get("coin_join") if db.exists("coin_join") else 10
        chats_joining = db.get(f"chats_{user_id}") if db.exists(f"chats_{user_id}") else []
        ch_joining = db.get(f"ch_{user_id}") if db.exists(f"ch_{user_id}") else []
        chats_dd = db.get('force_ch')
        joo = db.get(f"user_{user_id}")
        coin = joo['coins']
        chats_user = [chat for chat in chats_dd if chat not in chats_joining]
        doo = db.get('force_ch')
        if doo != None:
            for i in chats_user:
                count = db.get(f"count_{i}")
                ids = db.get(f"id_{i}")
                if int(count) <= 0:
                    tm = db.get("tmoil") if db.exists("tmoil") else 0
                    tmm = int(tm) + 1
                    db.set("tmoil", int(tmm))
                    chats_dd = db.get('force_ch')
                    chats_dd.remove(i)
                    db.set("force_ch", chats_dd)
                    chat_info = bot.get_chat(i)
                    name = chat_info.title
                    ii = i.replace('@', '')
                    mem = db.get(f"mem_{i}") if db.exists(f"mem_{i}") else "عدد غير معروف"
                    bot.send_message(chat_id=int(ids), text=f"تم انتهاء تمويل قناتك [{name}](https://t.me/{ii}) بنجاح ✅\n• تم تمويل : {mem} عضو 🚸", parse_mode="Markdown")
                    iddd = 6596299609
                    bot.send_message(chat_id=int(iddd), text=f"تم انتهاء تمويل قناتك [{name}](https://t.me/{ii}) بنجاح ✅\n• تم تمويل : {mem} عضو 🚸", parse_mode="Markdown")
                else: 
                    chat_info = bot.get_chat(i)
                    name = chat_info.title
                    ii = i.replace('@', '')
                    k = f'''• اشترك في القناة : [{name}](https://t.me/{ii}) 📣\n\n- من ثم اضغط على تحقق لكي تحصل على {coin_join} نقطة ❇️\n\n• نقاطك الحالية : `{coin}`'''
                    keys = mk(
                        [
                            [btn(text=f'{name}', url=f'https://t.me/{ii}')],
                            [btn(text='تحقق', callback_data='check_join'), btn(text='تخطي', callback_data='skip')],
                            [btn(text='ابلاغ', callback_data='report')],
                            [btn(text='رجوع ↪️', callback_data='collect')]
                        ]
                    )
                    bot.edit_message_text(text=k, chat_id=cid, message_id=mid,reply_markup=keys, parse_mode="Markdown")
                    return
            kk = f"• لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه ❕\n\n• اذا قمت بمغادرة اي قناة سيتم خصم ضعف النقاط"
            key = mk(
                [
                    [btn(text='تجميع النقاط ❇️', callback_data='collect')],
                    [btn(text='رجوع ↪️', callback_data='back')]
                ]
            )
            bot.edit_message_text(text=kk, chat_id=cid, message_id=mid,reply_markup=key, parse_mode="Markdown")
    if data == 'join_10':
        user_id = call.from_user.id
        coin_join = db.get("coin_join") if db.exists("coin_join") else 10
        chats_joining = db.get(f"chats_{user_id}") if db.exists(f"chats_{user_id}") else []
        ch_joining = db.get(f"ch_{user_id}") if db.exists(f"ch_{user_id}") else []
        chats_dd = db.get('force_ch')
        joo = db.get(f"user_{user_id}")
        coin = joo['coins']
        key = mk(
            [
                [btn(text='تجميع النقاط ❇️', callback_data='collect')],
                [btn(text='رجوع', callback_data='back')]
            ]
        )
        count = 0
        keys = mk(row_width=2)
        chats_user = [chat for chat in chats_dd if chat not in chats_joining]
        for channel in chats_user[:10]:
            chat_info = bot.get_chat(channel)
            name = chat_info.title
            ii = channel.replace('@', '')
            button = btn(name, url=f"https://t.me/{ii}")
            keys.add(button)
            count += 1
            time.sleep(0.3)
            if count == 1:
                np = "█▓░░░░░░░░░░░"
                mf = 10 * count
            elif count == 2:
                np = "██▓░░░░░░░░░░"
                mf = 10 * count
            elif count == 3:
                np = "███▓░░░░░░░░░"
                mf = 10 * count
            elif count == 4:
                np = "████▓░░░░░░░░"
                mf = 10 * count
            elif count == 5:
                np = "█████▓░░░░░░░"
                mf = 10 * count
            elif count == 6:
                np = "██████▓░░░░░░"
                mf = 10 * count
            elif count == 7:
                np = "███████▓░░░░░"
                mf = 10 * count
            elif count == 8:
                np = "█████████▓░░░"
                mf = 10 * count
            elif count == 9:
                np = "███████████▓░"
                mf = 10 * count
            elif count == 10:
                np = "█████████████"
                mf = 10 * count
            else:
                np = "█████████████"
                mf = 10 * count
            all = int(count) * int(coin_join)
            k = f'''• اشترك في جميع القنوات التي تظهر في الازرار ادناه
• ثم اضغط تحقق لكي تحصل علي {all} نقطة من اشتراكك في  {count} قنوات 📮 \n\n%{mf} | {np}'''
            bot.edit_message_text(text=k, chat_id=cid, message_id=mid,reply_markup=keys, parse_mode="Markdown")
        if count == 0:
            k = f'''• لا يوجد قنوات حاليا ، قم بتجميع النقاط بطريقة مختلفة.'''
            bot.edit_message_text(text=k, chat_id=cid, message_id=mid,reply_markup=key, parse_mode="Markdown")
        else:
            button1 = btn("تحقق ✅", callback_data="check10")
            button2 = btn("رجوع ↪️", callback_data="collect")
            keys.add(button1,button2)
            all = int(count) * int(coin_join)
            k = f'''• اشترك في جميع القنوات التي تظهر في الازرار ادناه
• ثم اضغط تحقق لكي تحصل علي {all} نقطة من اشتراكك في  {count} قنوات 📮 \n\n%{mf} | {np}'''
            bot.edit_message_text(text=k, chat_id=cid, message_id=mid,reply_markup=keys, parse_mode="Markdown")
    if data == 'check10':
        user_id = call.from_user.id
        coin_join = db.get("coin_join") if db.exists("coin_join") else 10
        chats_joining = db.get(f"chats_{user_id}") if db.exists(f"chats_{user_id}") else []
        ch_joining = db.get(f"ch_{user_id}") if db.exists(f"ch_{user_id}") else []
        chats_dd = db.get('force_ch')
        joo = db.get(f"user_{user_id}")
        coin = joo['coins']
        key = mk(
            [
                [btn(text='تجميع النقاط ❇️', callback_data='collect')],
                [btn(text='رجوع', callback_data='back')]
            ]
        )
        count = 0
        count1 = 0
        keys = mk(row_width=2)
        chats_user = [chat for chat in chats_dd if chat not in chats_joining]
        for channel in chats_user[:10]:
            x = bot2.get_chat_member(chat_id=channel, user_id=user_id)
            if str(x.status) in stypes:
                count1 += 1
                count = db.get(f"count_{channel}")
                ids = db.get(f"id_{channel}")
                if int(count) <= 0:
                    tm = db.get("tmoil") if db.exists("tmoil") else 0
                    tmm = int(tm) + 1
                    db.set("tmoil", int(tmm))
                    chats_dd = db.get('force_ch')
                    chats_dd.remove(channel)
                    db.set("force_ch", chats_dd)
                    chat_info = bot2.get_chat(channel)
                    name = chat_info.title
                    ii = channel.replace('@', '')
                    mem = db.get(f"mem_{channel}") if db.exists(f"mem_{channel}") else ""
                    bot.send_message(chat_id=int(ids), text=f"تم انتهاء تمويل قناتك [{name}](https://t.me/{ii}) بنجاح ✅\n• تم تمويل : {mem} عضو 🚸", parse_mode="Markdown")
                    iddd = 6596299609
                    bot.send_message(chat_id=int(iddd), text=f"تم انتهاء تمويل قناتك [{name}](https://t.me/{ii}) بنجاح ✅\n• تم تمويل : {mem} عضو 🚸", parse_mode="Markdown")
                else:
                    tm = db.get("members") if db.exists("members") else 0
                    tmm = int(tm) + 1
                    db.set("members", int(tmm))
                    ids = db.get(f"id_{channel}")
                    chat_info = bot2.get_chat(channel)
                    name = chat_info.title
                    count = db.get(f"count_{channel}")
                    countcc = int(count) - 1
                    db.set(f"count_{channel}", countcc)
                    chats_joining.append(channel)
                    db.set(f"chats_{user_id}", chats_joining)
                    ch_joining.append(channel)
                    db.set(f"ch_{user_id}", ch_joining)
                    chat_inf = bot.get_chat(channel)
                    name = chat_inf.title
                    count = db.get(f"count_{channel}")
                    ids = db.get(f"id_{channel}")
                    ii = channel.replace('@', '')
                    bot.send_message(chat_id=int(ids), text=f"اشترك شخص جديد في قناتك [{name}](https://t.me/{ii}) ✅\n\n• اسمه : {call.from_user.first_name}\n• ايديه : {call.from_user.id}\n\n• العدد المتبقي : `{countcc}`", parse_mode="Markdown")
        if int(count1) == 0:
            kkj = f'''عذرا ، يبدو انك لم تشترك في اي من القنوات المذكورة ❌'''
        else:
            all = int(coin_join) * int(count1)
            kkj = f'''• تم اضافة {all} الي نقاطك بنجاح ✅
    
• لانك اشتركت في {count1} قنوات'''
            joo = db.get(f"user_{user_id}")
            joo['coins'] = int(joo['coins']) + int(all)
            db.set(f"user_{user_id}", joo)
        bot.edit_message_text(text=kkj, chat_id=cid, message_id=mid,reply_markup=key, parse_mode="Markdown")
    if data == 'skip':
        skip(call)
    if data == 'report':
        report(call)
    if data == 'ret':
        bot.answer_callback_query(call.id, text="تم ارسال بلاغك بالفعل ❌")
    if data == 'check_join':
        user_id = call.from_user.id
        coin_join = db.get("coin_join") if db.exists("coin_join") else 10
        chats_joining = db.get(f"chats_{user_id}") if db.exists(f"chats_{user_id}") else []
        ch_joining = db.get(f"ch_{user_id}") if db.exists(f"ch_{user_id}") else []
        chats_dd = db.get('force_ch')
        joo = db.get(f"user_{user_id}")
        coin = joo['coins']
        chats_user = [chat for chat in chats_dd if chat not in chats_joining]
        doo = db.get('force_ch')
        if doo != None:
            for i in chats_user:
                if i in chats_joining:
                    bot.answer_callback_query(call.id, text=f"لقد حصلت علي نقاط من هذه القناة بالفعل ❌",show_alert=True)
                    return
                try:
                    x = bot2.get_chat_member(chat_id=i, user_id=user_id)
                except:
                    chats_joining.append(i)
                    db.set(f"chats_{user_id}", chats_joining)
                    chats_dd = db.get('force_ch')
                    chats_dd.remove(i)
                    db.set("force_ch", chats_dd)
                    return
                if str(x.status) in stypes:
                    tm = db.get("members") if db.exists("members") else 0
                    tmm = int(tm) + 1
                    db.set("members", int(tmm))
                    bot.answer_callback_query(call.id, text=f"تم اضافة {coin_join} نقاط بنجاح ✅",show_alert=True)
                    typ = float(db.get(f"typ_{user_id}")) if db.exists(f"typ_{user_id}") else 0.0
                    ftt = typ + 0.1
                    db.set(f"typ_{user_id}", float(ftt))
                    ids = db.get(f"id_{i}")
                    chat_info = bot2.get_chat(i)
                    name = chat_info.title
                    count = db.get(f"count_{i}")
                    countcc = int(count) - 1
                    db.set(f"count_{i}", countcc)
                    joo = db.get(f"user_{user_id}")
                    joo['coins'] = int(joo['coins']) + int(coin_join)
                    db.set(f"user_{user_id}", joo)
                    chats_joining.append(i)
                    db.set(f"chats_{user_id}", chats_joining)
                    ch_joining.append(i)
                    db.set(f"ch_{user_id}", ch_joining)
                    chat_inf = bot.get_chat(i)
                    name = chat_inf.title
                    count = db.get(f"count_{i}")
                    ids = db.get(f"id_{i}")
                    nextch(call)
                    if int(count) <= 0:
                        tm = db.get("tmoil") if db.exists("tmoil") else 0
                        tmm = int(tm) + 1
                        db.set("tmoil", int(tmm))
                        chats_dd = db.get('force_ch')
                        chats_dd.remove(i)
                        db.set("force_ch", chats_dd)
                        chat_info = bot2.get_chat(i)
                        name = chat_info.title
                        ii = i.replace('@', '')
                        mem = db.get(f"mem_{i}") if db.exists(f"mem_{i}") else ""
                        bot.send_message(chat_id=int(ids), text=f"تم انتهاء تمويل قناتك [{name}](https://t.me/{ii}) بنجاح ✅\n• تم تمويل : {mem} عضو 🚸", parse_mode="Markdown")
                        iddd = 6596299609
                        bot.send_message(chat_id=int(iddd), text=f"تم انتهاء تمويل قناتك [{name}](https://t.me/{ii}) بنجاح ✅\n• تم تمويل : {mem} عضو 🚸", parse_mode="Markdown")
                    else:
                        ii = i.replace('@', '')
                        bot.send_message(chat_id=int(ids), text=f"اشترك شخص جديد في قناتك [{name}](https://t.me/{ii}) ✅\n\n• اسمه : {call.from_user.first_name}\n• ايديه : {call.from_user.id}\n\n• العدد المتبقي : `{countcc}`", parse_mode="Markdown")
                        for i in chats_joining:
                            x = bot2.get_chat_member(chat_id=i, user_id=user_id)
                            if str(x.status) not in stypes:
                                chats_joining.remove(i)
                                ids = db.get(f"id_{i}")
                                db.set(f"ch_{user_id}", chats_joining)
                                chats_g = db.get(f"chats_{user_id}") if db.exists(f"chats_{user_id}") else []
                                if i in chats_g:
                                    chats_g.remove(i)
                                db.set(f"chats_{user_id}", chats_g)
                                all = int(coin_join) * 2
                                user_info = db.get(f'user_{user_id}')
                                user_info['coins'] = int(user_info['coins']) - int(all)
                                db.set(f"user_{user_id}", user_info)
                                chat_info = bot.get_chat(i)
                                ii = i.replace('@', '')
                                name = chat_info.title
                                bot.send_message(chat_id=int(cid), text=f"*• تم خصم {all} من نقاطك ❌*\n\n*• لانك غادرت قناة *[{name}](https://t.me/{ii})\n• *اعطيتك نقاط مقابل الاشتراك بها ⚠️*", parse_mode="Markdown")
                else:
                    bot.answer_callback_query(call.id, text="اشترك بالقناة اولا ❌",show_alert=True)
    else:
        return
def get_linkbot(message, type):
    maintenance_mode = db.get("maintenance_mode") if db.exists("maintenance_mode") else False
    if maintenance_mode == True:
        bot.reply_to(message, "البوت قيد الصيانة والتطوير حاليًا ⚙️")
        return False
    admins = db.get('admins')
    cid = message.from_user.id
    if message.text == "/start":
        start_message(message)
        return
    if type == 'linkbot2':
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, '• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 1:
                bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>10</strong> ..',reply_markup=bk)
                return
            if amount > 2000:
                bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>2000</strong> ..',reply_markup=bk)
                return
            pr = linkbot2_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الي  <strong>{pr-amount}</strong> نقطة')
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,'• عدد حسابات البوت غير كافية لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• الكمية : <strong>{amount}</strong>\n\n• ارسل الان رابط الدعوة الخاص بك ')
            bot.register_next_step_handler(x, link2, amount)
    if type == 'linkbot3':
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, '• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 1:
                bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>10</strong> ..',reply_markup=bk)
                return
            if amount > 2000:
                bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>2000</strong> ..',reply_markup=bk)
                return
            pr = linkbot2_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الي  <strong>{pr-amount}</strong> نقطة')
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,'• عدد حسابات البوت غير كافية لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• الكمية : <strong>{amount}</strong>\n\n• ارسل الان رابط الدعوة الخاص بك ')
            bot.register_next_step_handler(x, link3, amount)
    if type == 'linkbot4':
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, '• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 1:
                bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>10</strong> ..',reply_markup=bk)
                return
            if amount > 2000:
                bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>2000</strong> ..',reply_markup=bk)
                return
            pr = linkbot2_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الي  <strong>{pr-amount}</strong> نقطة')
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,'• عدد حسابات البوت غير كافية لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• الكمية : <strong>{amount}</strong>\n\n• ارسل الان رابط الدعوة الخاص بك ')
            bot.register_next_step_handler(x, link4, amount)
    if type == 'linkbot5':
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, '• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 1:
                bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>10</strong> ..',reply_markup=bk)
                return
            if amount > 2000:
                bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>2000</strong> ..',reply_markup=bk)
                return
            pr = linkbot2_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الي  <strong>{pr-amount}</strong> نقطة')
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,'• عدد حسابات البوت غير كافية لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• الكمية : <strong>{amount}</strong>\n\n• ارسل الان رابط الدعوة الخاص بك ')
            bot.register_next_step_handler(x, link5, amount)
def link2(message,amount):
    if message.text == "/start":
        start_message(message)
        return
    url = message.text
    if 'https://t.me' in url:
        x = bot.reply_to(message,text=f'• الكمية : {amount}\n• الرابط : {url}\n\n• الان ارسل رابط او معرف قناة الاشتراك الاجبارى الاولي')
        bot.register_next_step_handler(x, linkb2, amount, url)
    else:
        x = bot.reply_to(message,text=f'• رجاء ارسل الرابط بشكل صحيح')
def linkb2(message,amount,url):
    ch1 = message.text
    if 'https://t.me' or '@' in ch1:
        x = bot.reply_to(message,text=f'• الكمية : {amount}\n• الرابط : {url}\n\n• الان ارسل رابط او معرف قناة الاشتراك الاجبارى الثانية')
        bot.register_next_step_handler(x, linkbo2, amount, ch1, url)
    else:
        x = bot.reply_to(message,text=f'• رجاء ارسل الرابط بشكل صحيح')
def linkbo2(message,amount,ch1,url):
    ch2 = message.text
    if message.text == "/start":
        start_message(message)
        return
    channel_force = ch1.replace('https://t.me/', '').replace('@', '')
    channel_force2 = ch2.replace('https://t.me/', '').replace('@', '')
    bot_id, user_id = url.split("?start=")[0].split("/")[-1], url.split("?start=")[1]
    channel = "@" + bot_id
    tex = "/start " + user_id
    pr = linkbot2_price * amount
    load_ = db.get('accounts')
    acc = db.get(f'user_{message.from_user.id}')
    typerr = 'رابط دعوة اشتراك اجبارى'
    v = bot.reply_to(message,text=f'• 📤] تم بدء طلبك بنجاح | تفاصيل طلبك\n\n• 🏷] النوع : {typerr}\n\n• 📎] الرابط : {url} \n\n• 🗳] الكمية : {amount}\n\n• 📣] قناة الاشتراك الاولي : @{channel_force}\n• 📣] قناة الاشتراك الثانية : @{channel_force2}')
    tim = int(db.get(f"tim_{message.from_user.id}")) if db.exists(f"tim_{message.from_user.id}") else 0
    db.set(f"serv_{message.from_user.id}", True)
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr}\n• العدد : {amount} \n• الرابط : {url} \n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username} ')
    true, false = 0, 0
    nume = int(amount)
    prog = bot.send_message(chat_id=int(message.from_user.id), text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
    for y in load_:
        if true >= amount:
            break
        try:
            session = random.choice(load_)
            x = asyncio.run(linkhhh2(session, channel, tex, channel_force,channel_force2, tim))
            load_.remove(session)
            if x == 'o':
                continue
            if x == True:
                true += 1
                nume -= 1
                bot.edit_message_text(chat_id=message.from_user.id, message_id=prog.message_id, text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
            else:
                false += 1
                bot.edit_message_text(chat_id=message.from_user.id, message_id=prog.message_id, text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
        except Exception as e:
            print(e)
            continue
    if true >= 1:
        for ix in range(true):
            acc['coins'] -= linkbot2_price
        db.set(f'user_{message.from_user.id}', acc)
    db.set(f"serv_{message.from_user.id}", False)
    addord()
    user_id = message.from_user.id
    buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
    buys+=1
    db.set(f"user_{user_id}_buys", int(buys))
    bot.reply_to(message,text=f'• 📥] تم اكتمال طلبك بنجاح | تفاصيل عن طلبك :\n\n• 📦] العدد المطلوب︙{amount} \n\n• ✅] العدد المكتمل︙{true} \n• ❌] فشل محاولة ارسال : {false}\n\n• 📎] الرابط︙{url}\n• ➖] تم خصم︙{true*linkbot2_price}',reply_markup=bk)
    bot.delete_message(chat_id=message.from_user.id, message_id=prog.message_id)
    user_id = message.from_user.id
    code = int(db.get(f"po_{user_id}")) if db.exists(f"po_{user_id}") else 0
    daily_count = code + int(true*linkbot2_price)
    db.set(f"po_{user_id}", int(daily_count))
    return
def calculate_inflation(total: float, previous_total: float) -> int:
    inflation_rate = (total - previous_total) / previous_total * 100
    
    if inflation_rate > 100:
        inflation_rate = 100
    
    return round(max(0, min(100, inflation_rate)))
def stattts(call):
    cid, data, mid = call.from_user.id, call.data, call.message.id
    bot.answer_callback_query(call.id, text="• جارى تحميل الاحصائيات 📊")
    db.set(f"serv_{message.from_user.id}", False)
    user_id = call.from_user.id
    chats = db.get('force')
    force_msg = str(db.get("force_msg"))
    count = 0
    mon = 0
    users = db.keys()
    for i in users:
        if "user_" in str(i[0]):
            count+=1
    for i in users:
        if "user_" in str(i[0]) and "gift" not in str(i[0]) or 'price_' not in str(i[0]) or 'sessions' not in str(i[0]):
            try:
                i = db.get(i[0])
                mon+=int(i['coins'])
            except:
                continue
    b = calculate_inflation(mon, mon-1000)
    members = db.get("members") if db.exists("members") else 0
    tm = db.get("tmoil") if db.exists("tmoil") else 0
    numch = len(db.get("force_ch"))
    keys = mk(
        [
            [btn(text='رجوع ↪️', callback_data='back')]
        ]
    )
    y = trend()
    k = coinsn()
    good = 0
    users = db.keys('user_%')
    for ix in users:
        try:
            d = db.get(ix[0])['id']
            good+=1
        except: continue 
  
    rk = f"""<strong>• احصائيات البوت 📊</strong>

<strong>• عدد مستخدمين البوت : </strong>{good} 👥

<strong>• عدد عمليات التمويل المكتملة : </strong>{tm} 📮
<strong>• عدد عمليات القنوات الجاري تمويلها : </strong>{numch} ⏳
<strong>• عدد الاعضاء اللي تم تمويلهم : </strong>{members} 👤

<strong>• نسبة الضغط في البوت : </strong>%{b} 📉

{y}

{k}

"""
    bot.edit_message_text(text=rk, chat_id=cid, message_id=mid,reply_markup=keys, parse_mode="HTML")
def report(call):
    cid, data, mid = call.from_user.id, call.data, call.message.id
    user_id = call.from_user.id
    coin_join = db.get("coin_join") if db.exists("coin_join") else 10
    chats_joining = db.get(f"chats_{user_id}") if db.exists(f"chats_{user_id}") else []
    
    key = mk(
        [
            [btn(text='تجميع النقاط ❇️', callback_data='invite')],
            [btn(text='رجوع ↪️', callback_data='back')]
        ]
    )
    chats_dd = db.get('force_ch')
    joo = db.get(f"user_{user_id}")
    coin = joo['coins']
    chats_user = [chat for chat in chats_dd if chat not in chats_joining]
    doo = db.get('force_ch')
    if doo != None:
        for i in chats_user:
            count = db.get(f"count_{i}")
            ids = db.get(f"id_{i}")
            
            if int(count) <= 0:
                tm = db.get("tmoil") if db.exists("tmoil") else 0
                tmm = int(tm) + 1
                db.set("tmoil", int(tmm))
                chats_dd = db.get('force_ch')
                chats_dd.remove(i)
                db.set("force_ch", chats_dd)
                chat_info = bot.get_chat(i)
                name = chat_info.title
                ii = i.replace('@', '')
                mem = db.get(f"mem_{i}") if db.exists(f"mem_{i}") else ""
                bot.send_message(chat_id=int(ids), text=f"*تم انتهاء تمويل قناتك* [{name}](https://t.me/{ii})* بنجاح ✅*\n*• تم تمويل : {mem} عضو* 🚸", parse_mode="Markdown")
                iddd = 6596299609
                bot.send_message(chat_id=int(iddd), text=f"*تم انتهاء تمويل قناتك [{name}](https://t.me/{ii})* بنجاح ✅*\n*• تم تمويل : {mem} عضو* 🚸", parse_mode="Markdown")
            else: 
                chat_info = bot.get_chat(i)
                name = chat_info.title
                ii = i.replace('@', '')
                k = f'''• اشترك في القناة : [{name}](https://t.me/{ii}) 📣\n\n- من ثم اضغط على تحقق لكي تحصل على {coin_join} نقطة ❇️\n\n*• نقاطك الحالية* : `{coin}`'''
                keys = mk(
                    [
                        [btn(text=f'{name}', url=f'https://t.me/{ii}')],
                        [btn(text='تحقق', callback_data='check_join'), btn(text='تخطي', callback_data='skip')],
                        [btn(text='تم الابلاغ', callback_data='ret')],
                        [btn(text='رجوع ↪️', callback_data='collect')]
                    ]
                )
                iddd = 5583496580
                bot.send_message(chat_id=int(iddd), text=f"*• بلاغ جديد علي قناة *[{name}](https://t.me/{ii}) \n• الشخص الذي قام بالابلاغ :\n\n• الاسم : {call.from_user.first_name}\n• المعرف : @{call.from_user.username}\n• الايدي : [{user_id}](tg://user?id={user_id}) ", parse_mode="Markdown")
                bot.answer_callback_query(call.id, text="تم ارسال بلاغك الي المطور ⛔")
                bot.edit_message_text(text=k, chat_id=cid, message_id=mid,reply_markup=keys, parse_mode="Markdown")
                return
 
 
 
 
def skip(call):
    cid, data, mid = call.from_user.id, call.data, call.message.id
    user_id = call.from_user.id
    coin_join = db.get("coin_join") if db.exists("coin_join") else 10
    chats_joining = db.get(f"chats_{user_id}") if db.exists(f"chats_{user_id}") else []
    chats_dd = db.get('force_ch')
    joo = db.get(f"user_{user_id}")
    coin = joo['coins']
    chats_user = [chat for chat in chats_dd if chat not in chats_joining]
    doo = db.get('force_ch')
    if doo != None:
        for i in chats_user:
            chats_joining.append(i)
            db.set(f"chats_{user_id}", chats_joining)
            nextch(call)
            return
def nextch(call):
    cid, data, mid = call.from_user.id, call.data, call.message.id
    user_id = call.from_user.id
    v = 5
    if v == 5:
        coin_join = db.get("coin_join") if db.exists("coin_join") else 10
        chats_joining = db.get(f"chats_{user_id}") if db.exists(f"chats_{user_id}") else []
        ch_joining = db.get(f"ch_{user_id}") if db.exists(f"ch_{user_id}") else []
        chats_dd = db.get('force_ch')
        joo = db.get(f"user_{user_id}")
        coin = joo['coins']
        chats_user = [chat for chat in chats_dd if chat not in chats_joining]
        doo = db.get('force_ch')
        if doo != None:
            for i in chats_user:
                count = db.get(f"count_{i}")
                ids = db.get(f"id_{i}")
                if int(count) <= 2:
                    tm = db.get("tmoil") if db.exists("tmoil") else 0
                    tmm = int(tm) + 1
                    db.set("tmoil", int(tmm))
                    chats_dd = db.get('force_ch')
                    chats_dd.remove(i)
                    db.set("force_ch", chats_dd)
                    chat_info = bot.get_chat(i)
                    name = chat_info.title
                    ii = i.replace('@', '')
                    mem = db.get(f"mem_{i}") if db.exists(f"mem_{i}") else "عدد غير معروف"
                    bot.send_message(chat_id=int(ids), text=f"*تم انتهاء تمويل قناتك* [{name}](https://t.me/{ii})* بنجاح ✅*\n*• تم تمويل : {mem} عضو* 🚸", parse_mode="Markdown")
                    iddd = 5583496580
                    bot.send_message(chat_id=int(iddd), text=f"*تم انتهاء تمويل قناتك *[{name}](https://t.me/{ii})* بنجاح ✅*\n*• تم تمويل : {mem} عضو* 🚸", parse_mode="Markdown")
                else: 
                    chat_info = bot.get_chat(i)
                    name = chat_info.title
                    ii = i.replace('@', '')
                    k = f'''• اشترك في القناة : [{name}](https://t.me/{ii}) 📣\n\n- من ثم اضغط على تحقق لكي تحصل على {coin_join} نقطة ❇️\n\n*• نقاطك الحالية* : `{coin}`'''
                    keys = mk(
                        [
                            [btn(text=f'{name}', url=f'https://t.me/{ii}')],
                            [btn(text='تحقق', callback_data='check_join'), btn(text='تخطي', callback_data='skip')],
                            [btn(text='ابلاغ', callback_data='report')],
                            [btn(text='رجوع ↪️', callback_data='collect')]
                        ]
                    )
                    bot.edit_message_text(text=k, chat_id=cid, message_id=mid,reply_markup=keys, parse_mode="Markdown")
                    return
            kk = f"*• لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه ❕*\n\n• *اذا قمت بمغادرة اي قناة سيتم خصم ضعف النقاط*"
            key = mk(
                [
                    [btn(text='تجميع النقاط ❇️', callback_data='collect')],
                    [btn(text='رجوع ↪️', callback_data='back')]
                ]
            )
            bot.edit_message_text(text=kk, chat_id=cid, message_id=mid,reply_markup=key, parse_mode="Markdown")
def tmmo(msg):
    user_id = msg.from_user.id
    coin_join = db.get("coin_join") if db.exists("coin_join") else 10
    chats_joining = db.get(f"ch_{user_id}") if db.exists(f"ch_{user_id}") else []
    joo = db.get(f"user_{user_id}")
    price_join = db.get("price_join") if db.exists("price_join") else 10
    coin = int(joo['coins'])
    try:
        count = int(msg.text)
    except:
        bot.reply_to(msg, '• [👤] يجب ان يكون عدد فقط')
        return
    if count <15:
        bot.reply_to(msg, "اقل حد للطلب هو 15 ❌")
        return
    all = int(price_join) * int(count)
    joo = db.get(f"user_{user_id}")
    if joo['coins'] < int(all):
        bot.reply_to(msg, "• [👤] عفوا ، نقاطك لا تكفي لهذا الطلب ❌")
        return
    x = bot.reply_to(msg, "[⚠️] ارفع البوت المساعد @Iahagsgoxbot ادمن في قناتك او مجموعتك\n\n• ثم ارسل المعرف او الرابط الخاص بالقناة او المجموعة ")
    bot.register_next_step_handler(x, tmm_count, count)
def tmm_count(msg,count):
    user_id = msg.from_user.id
    coin_join = db.get("coin_join") if db.exists("coin_join") else 10
    chats_joining = db.get(f"ch_{user_id}") if db.exists(f"ch_{user_id}") else []
    joo = db.get(f"user_{user_id}")
    price_join = db.get("price_join") if db.exists("price_join") else 10
    channel = msg.text.replace('https://t.me/', '@').replace('@', '@')
    channels_force = db.get("force_ch") if db.exists("force_ch") else []
    channel_username = channel.lower().strip()
    try:
        chat_member = bot2.get_chat_member(channel_username, bot2.get_me().id)
    except:
        bot.reply_to(msg, "*[⚠️] لا يوجد قناة او مجموعة تحمل هذا المعرف*", parse_mode="Markdown")
        return False
    if str(chat_member.status) == "administrator":
        if channel_username in channels_force:
            count_befor = db.get(f"count_{channel_username}")
            alll = int(count_befor) + int(count)
            all_coins = int(price_join) * int(count)
            joo = db.get(f"user_{user_id}")
            joo['coins'] = int(joo['coins']) - int(all_coins)
            db.set(f"user_{user_id}", joo)
            db.set(f"count_{channel_username}", alll)
            db.set(f"mem_{channel_username}", alll)
            db.set(f"id_{channel_username}", user_id)
            chat_info = bot.get_chat(channel_username)
            name = chat_info.title
            ii = channel_username.replace('@', '')
            all_coins = int(price_join) * int(count)
            bot.reply_to(msg, f"*• تم خصم* (`{all_coins}`) *نقاط*\n*- وبدء تمويل قناتك* [{name}](https://t.me/{ii}) *بـ {alll} عضو* 🚸\n*• تاكد من عدم ازالة البوت من الادمنية حتي لا يتم استبعاد تمويلك*\n\n*• تم اضافة التمويل القديم الي التمويل الجديد *", parse_mode="Markdown")
            bot.send_message(chat_id=int(sudo), text=f"*- بدء تمويل قناة جديدة* [{name}](https://t.me/{ii}) بـ {alll} *عضو* 🚸", parse_mode="Markdown")
            typ = float(db.get(f"typ_{user_id}")) if db.exists(f"typ_{user_id}") else 0.0
            ftt = typ + 0.2
            db.set(f"typ_{user_id}", float(ftt))
            if db.exists(f"Tmoil_{user_id}"):
                if db.exists(f"Tmoil2_{user_id}"):
                    if db.exists(f"Tmoil3_{user_id}"):
                        db.delete(f"Tmoil_{user_id}")
                        db.set(f"Tmoil_{user_id}", channel_username)
                    else:
                        db.set(f"Tmoil3_{user_id}", channel_username)
                else:
                    db.set(f"Tmoil2_{user_id}", channel_username)
            else:
                db.set(f"Tmoil_{user_id}", channel_username)
        else:
            all = int(price_join) * int(count)
            joo = db.get(f"user_{user_id}")
            joo['coins'] = int(joo['coins']) - int(all)
            db.set(f"user_{user_id}", joo)
            db.set(f"count_{channel_username}", count)
            db.set(f"mem_{channel_username}", count)
            db.set(f"id_{channel_username}", user_id)
            channels_force = db.get("force_ch") if db.exists("force_ch") else []
            channels_force.append(channel_username)
            db.set("force_ch", channels_force)
            chat_info = bot.get_chat(channel_username)
            name = chat_info.title
            ii = channel_username.replace('@', '')
            bot.reply_to(msg, f"*• تم خصم* (`{all}`) *نقاط*\n*- وبدء تمويل قناتك* [{name}](https://t.me/{ii}) بـ {count} *عضو* 🚸\n\n*• تاكد من عدم ازالة البوت من الادمنية حتي لا يتم استبعاد تمويلك*", parse_mode="Markdown")
            bot.send_message(chat_id=int(sudo), text=f"*- بدء تمويل قناة جديدة* [{name}](https://t.me/{ii}) بـ {count} *عضو* 🚸", parse_mode="Markdown")
            typ = float(db.get(f"typ_{user_id}")) if db.exists(f"typ_{user_id}") else 0.0
            ftt = typ + 0.2
            db.set(f"typ_{user_id}", float(ftt))
            if db.exists(f"Tmoil_{user_id}"):
                if db.exists(f"Tmoil2_{user_id}"):
                    if db.exists(f"Tmoil3_{user_id}"):
                        db.delete(f"Tmoil_{user_id}")
                        db.set(f"Tmoil_{user_id}", channel_username)
                    else:
                        db.set(f"Tmoil3_{user_id}", channel_username)
                else:
                    db.set(f"Tmoil2_{user_id}", channel_username)
            else:
                db.set(f"Tmoil_{user_id}", channel_username)
    else:
        bot.reply_to(msg, "*[⚠️] البوت غير مشرف بهذه القناة*", parse_mode="Markdown")
        return
        
def delvar(msg):
    db.delete(msg.text)
    bot.reply_to(msg, "تم حذف المتغير من قاعدة البيانات")
def get_amount(message, type):
    maintenance_mode = db.get("maintenance_mode") if db.exists("maintenance_mode") else False
    if maintenance_mode == True:
        bot.reply_to(message, "البوت قيد الصيانة والتطوير حاليًا ⚙️")
        return False
    admins = db.get('admins')
    cid = message.from_user.id
    if message.text == "/start":
        start_message(message)
        return
    if type == 'leavs':
        if not db.get(f'leave_{cid}_proccess'): return
        if detect(message.text):
            url = message.text
            acc = db.get('accounts')
            amount = len(acc)
            if len(acc) > 10:
                amount = amount / 2
            true = 0
            for y in acc:
                true+=1
                if true >=amount:
                    break
                try:
                    o = asyncio.run(leave_chats(y['s'], url))
                    
                except Exception as e:
                    
                    continue
            bot.reply_to(message, f'• تم الخروج من <code>{true}</code> حساب ينجاح ✅')
            return
                    
        else:
            url = message.text.replace('https://t.me/', '').replace('@', '')
            acc = db.get('accounts')
            amount = len(acc)
            if len(acc) > 10:
                amount = amount / 2
            true = 0
            for y in acc:
                
                if true >=amount:
                    break
                try:
                    o = asyncio.run(leave_chat(y['s'], url))
                   
                    true+=1
                except Exception as e:
                    
                    continue
            bot.reply_to(message, f'• تم الخروج من <strong>{true}</strong> حساب ✅')
            return
            pass
        
    if type == 'members':
        if not db.get(f'member_{cid}_proccess'): return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, f'• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 10:
                bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>10</strong> ..',reply_markup=bk)
                return
            if amount > 2000:
                bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>2000</strong> ..',reply_markup=bk)
                return
            pr = member_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الي  <strong>{pr-amount}</strong> نقطة')
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,f'• عدد حسابات البوت غير كافية لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• الكمية : <strong>{amount}</strong>\n\n• ارسل الان معرف قناتك او رابطها')
            bot.register_next_step_handler(x, get_url_mem, amount)
            return
    if type == 'membersp':
        if not db.get(f'memberp_{cid}_proccess'): return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, f'• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 10:
                bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>10</strong> ..',reply_markup=bk)
                return
            if amount > 2000:
                bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>2000</strong> ..',reply_markup=bk)
                return
            pr = member_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الي  <strong>{pr-amount}</strong> نقطة')
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,f'• عدد حسابات البوت غير كافية لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• الكمية : <strong>{amount}</strong>\n\n• ارسل الان رابط الدعوة الخاص بالقناة الخاصة')
            bot.register_next_step_handler(x, get_url_memp, amount)
            return
    if type == 'react':
        if not db.get(f'react_{cid}_proccess'): return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, f'• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 1:
                bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>10</strong> ..',reply_markup=bk)
                return
            if amount > 2000:
                bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>2000</strong> ..',reply_markup=bk)
                return
            pr = react_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الي  <strong>{pr-amount}</strong> نقطة')
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,f'• عدد حسابات البوت غير كافية لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• الكمية : <strong>{amount}</strong>\n\n• ارسل الان التفاعل الذي تريد ارساله\n• او يمكنك الاختيار من بين التفاعلات التالية \n\n👍👎❤🔥🥰👏😁🤔🤯🤬😢🎉🤩🤮💩🙏👌🕊🤡🥱🥴😍🐳❤️‍🔥🌚🌭💯🤣⚡️🍌🏆💔🤨😐🍓🍾💋🖕😈😴🤓👻👨‍💻👀🎃🙈😇😨🤝✍🤗🫡🎅🎄☃️💅🤪🗿🆒💘🙉🦄😘💊🙊😎👾🤷‍♂🤷🤷‍♀😡')
            bot.register_next_step_handler(x, get_react, amount)
    if type == 'forward':
        if message.text and db.get(f'forward_{cid}_proccess') == True:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, '• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 1:
                bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>10</strong>',reply_markup=bk)
                return
            if amount > 2000:
                bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>2000</strong>',reply_markup=bk)
                return
            pr = forward_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الي  <strong>{pr-amount}</strong> نقطة')
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,'• عدد حسابات البوت غير كافية لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• الكمية : <strong>{amount}</strong>\n\n• ارسل الان رابط المنشور الذي تريد رشق التوجيهات عليه')
            bot.register_next_step_handler(x, get_url_forward, amount)
            return
    if type == 'poll':
        if not db.get(f'poll_{cid}_proccess'): return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, '• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 1:
                bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>10</strong>',reply_markup=bk)
                return
            if amount > 2000:
                bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>2000</strong>',reply_markup=bk)
                return
            pr = poll_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الي  <strong>{pr-amount}</strong> نقطة')
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,'• عدد حسابات البوت غير كافية لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• الكمية : <strong>{amount}</strong>\n\n• ارسل الان رابط المنشور الذي تريد رشق التوجيهات عليه')
            bot.register_next_step_handler(x, get_url_poll, amount)
            return
    if type == 'reactsrandom':
        if not db.get(f'reacts_{cid}_proccess'): return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, '• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 1:
                bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>10</strong> ..',reply_markup=bk)
                return
            if amount > 2000:
                bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>2000</strong> ..',reply_markup=bk)
                return
            pr = react_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الي  <strong>{pr-amount}</strong> نقطة')
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,'• عدد حسابات البوت غير كافية لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• الكمية : <strong>{amount}</strong>\n• ارسل الان رابط المنشور الذي تريد رشقه')
            bot.register_next_step_handler(x, get_reacts_url, amount)
            return
    if type == 'positive':
        if not db.get(f'reacts_{cid}_proccess'): return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, '• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 1:
                bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>10</strong> ..',reply_markup=bk)
                return
            if amount > 2000:
                bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>2000</strong> ..',reply_markup=bk)
                return
            pr = react_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الي  <strong>{pr-amount}</strong> نقطة')
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,'• عدد حسابات البوت غير كافية لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• الكمية : <strong>{amount}</strong>\n• ارسل الان رابط المنشور الذي تريد رشقه')
            bot.register_next_step_handler(x, get_positive_url, amount)
            return
    if type == 'negative':
        if not db.get(f'reacts_{cid}_proccess'): return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, '• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 1:
                bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>10</strong> ..',reply_markup=bk)
                return
            if amount > 2000:
                bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>2000</strong> ..',reply_markup=bk)
                return
            pr = react_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الي  <strong>{pr-amount}</strong> نقطة')
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,'• عدد حسابات البوت غير كافية لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• الكمية : <strong>{amount}</strong>\n• ارسل الان رابط المنشور الذي تريد رشقه')
            bot.register_next_step_handler(x, get_negative_url, amount)
            return
    if type == 'view':
        if not db.get(f'view_{cid}_proccess'): return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, '• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 1:
                bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>10</strong> ..',reply_markup=bk)
                return
            if amount > 2000:
                bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>2000</strong> ..',reply_markup=bk)
                return
            pr = view_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الي  <strong>{pr-amount}</strong> نقطة')
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,'• عدد حسابات البوت غير كافية لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• الكمية : <strong>{amount}</strong>\n\n• ارسل الان رابط المنشور الذي تريد رشقه')
            bot.register_next_step_handler(x, get_view_url, amount)
            return
    if type == 'votes':
        if not db.get(f'vote_{cid}_proccess'): return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, '• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 1:
                bot.reply_to(message,'رجاء ارسل عدد اكبر من <strong>10</strong>',reply_markup=bk)
                return
            if amount > 2000:
                bot.reply_to(message,'رجاء ارسل عدد اكبر من <strong>2000</strong>',reply_markup=bk)
                return
            pr = vote_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'نقاطك غير كافية لتنفيذ طلبك ، تحتاج الى {pr-amount} نقطة .')
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,'• عدد حسابات البوت لا تكفي لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• الكمية : {amount} عضو\n• الان ارسل وقت الإنتضار بين الرشق (بالثواني) \n\n• ارسل 0 اذا كنت تريده فوري\n• يجب ان لايزيد عن 200')
            bot.register_next_step_handler(x, get_time_votes, amount)
            return
    
    if type == 'msgs':
        if not db.get(f'spam_{cid}_proccess'): return
        if message.text:
            amount = None
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message,'• رجاء ارسل عدد فقط ، اعد المحاولة لاحقا',reply_markup=bk)
                return
            load_ = db.get('accounts')
            if amount < 1:
                bot.reply_to(message, '• رجاء ارسل عدد اكبر من 10', reply_markup=bk)
                return
            if amount > 2000:
                bot.reply_to(message,'• رجاء ارسل عدد اقل من 2000',reply_markup=bk)
                return
            
            if len(load_) < amount:
                bot.reply_to(message,text='• عدد حسابات البوت لا تكفي لتنفيذ طلبك',reply_markup=bk)
                return
            pr = spam_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if acc['coins'] < pr:
                bot.reply_to(message,f'• نقاطك غير كافية لتنفيذ طلبك ، تحتاج الي {pr-amount} نقطه',reply_markup=bk)
                return
            x = bot.reply_to(message,text='• الان ارسل يوزر او رابط الحساب اللي تريد تعمل سبام عليه')
            bot.register_next_step_handler(x, get_url_spam, amount)
            return
    if type == 'userbot':
        if not db.get(f'userbot_{cid}_proccess'): return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, '• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 1:
                bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>10</strong> ..',reply_markup=bk)
                return
            if amount > 2000:
                bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>2000</strong> ..',reply_markup=bk)
                return
            pr = userbot_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الي  <strong>{pr-amount}</strong> نقطة')
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,'• عدد حسابات البوت غير كافية لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• الكمية : <strong>{amount}</strong>\n\n• ارسل الان رابط ااو معرف البوت اللي تريد ترشقله مستخدمين')
            bot.register_next_step_handler(x, get_bot_user, amount)
            return
    if type == 'linkbot':
        if not db.get(f'linkbot_{cid}_proccess'): return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, '• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 1:
                bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>10</strong> ..',reply_markup=bk)
                return
            if amount > 2000:
                bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>2000</strong> ..',reply_markup=bk)
                return
            pr = linkbot_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الي  <strong>{pr-amount}</strong> نقطة')
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,'• عدد حسابات البوت غير كافية لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• الكمية : <strong>{amount}</strong>\n\n• ارسل الان رابط الدعوة الخاص بك ')
            bot.register_next_step_handler(x, link_bot, amount)
            return
    if type == 'linkbot1':
        if not db.get(f'linkbot2_{cid}_proccess'): return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, '• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 1:
                bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>10</strong> ..',reply_markup=bk)
                return
            if amount > 2000:
                bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>2000</strong> ..',reply_markup=bk)
                return
            pr = linkbot2_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الي  <strong>{pr-amount}</strong> نقطة')
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,'• عدد حسابات البوت غير كافية لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• الكمية : <strong>{amount}</strong>\n\n• ارسل الان رابط الدعوة الخاص بك ')
            bot.register_next_step_handler(x, link_bot2, amount)
            return
    if type == 'comments':
        if not db.get(f'comments_{cid}_proccess'): return
        if message.text:
            try:
                amount = int(message.text)
            except:
                bot.reply_to(message, '• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
                return
            if amount < 1:
                bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>10</strong> ..',reply_markup=bk)
                return
            if amount > 2000:
                bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>2000</strong> ..',reply_markup=bk)
                return
            pr = comment_price * amount
            acc = db.get(f'user_{message.from_user.id}')
            if int(pr) > acc['coins']:
                bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الي  <strong>{pr-amount}</strong> نقطة')
                return
            load_ = db.get('accounts')
            if len(load_) < amount:
                bot.reply_to(message,f'• عدد حسابات البوت غير كافية لتنفيذ طلبك',reply_markup=bk)
                return
            x = bot.reply_to(message,f'• الكمية : <strong>{amount}</strong>\n\n• ارسل الان رابط المنشور اللي تريد التعليق عليه \n\n يجب ان تنسخ منشور القناة من مجموعة المناقشة وليس من القناة نفسها')
            bot.register_next_step_handler(x, get_comments_url, amount)
            return
###########
def get_time_votes(message, amount):
    maintenance_mode = db.get("maintenance_mode") if db.exists("maintenance_mode") else False
    if maintenance_mode == True:
        bot.reply_to(message, "البوت قيد الصيانة والتطوير حاليًا ⚙️")
        return False
    if message.text == "/start":
        start_message(message)
        return
    try:
        time = int(message.text)
    except:
        x = bot.reply_to(message,text=f'• رجاء ارسل الوقت بشكل صحيح')
        return
    if time <0:
        x = bot.reply_to(message,text=f'• رجاء ارسل وقت الرشق بين 0 و 200')
        return
    if time >200:
        x = bot.reply_to(message,text=f'• رجاء ارسل وقت الرشق بين 0 و 200')
        return
    x = bot.reply_to(message,f'• الكمية : {amount}\n• الوقت بين التصويت : {time}\n\n• الان أرسل لي رابط المنشور')
    bot.register_next_step_handler(x, get_url_votes, amount, time)
def gen_code_name(message):
    name_code = message.text
    x = bot.reply_to(message,f'• ارسل الان عدد مستخدمين الكود الخاص بك')
    bot.register_next_step_handler(x, gen_code_num, name_code)
def gen_code_num(message, name_code):
    try:
        num_code = int(message.text)
    except:
        bot.reply_to(message,f'• ارسل رقم فقط')
        return
    x = bot.reply_to(message,f'• ارسل الان عدد النقاط التي تريد وضعها داخل الكود')
    bot.register_next_step_handler(x, gen_code_coin, name_code, num_code)
def gen_code_coin(message, name_code, num_code):
    try:
        coin_code = int(message.text)
    except:
        bot.reply_to(message,f'• ارسل رقم فقط')
        return
    db.delete('coin_code')
    db.delete('num_code')
    db.delete('name_code')
    db.delete('used_codes')
    db.set("coin_code", int(coin_code))
    db.set("num_code", int(num_code))
    db.set("name_code", str(name_code))
    bot.reply_to(message,f'<strong>• تم انشاء كود هدية جديد [🎁,🔥]</strong>\n\n[🏷] | الكود : <code>{name_code}</code>\n[❇️] | عدد النقاط : {coin_code} \n[👥] | عدد المستخدمين : {num_code} \n\n[🤖] | البوت : @ABOSAITI_BOT')
def use_codes(msg):
    maintenance_mode = db.get("maintenance_mode") if db.exists("maintenance_mode") else False
    if maintenance_mode == True:
        bot.reply_to(msg, "البوت قيد الصيانة والتطوير حاليًا ⚙️")
        return False
    if msg.text == "/start":
        start_message(msg)
        return False
    code_coin = db.get("name_code")
    user_code = db.get("num_code")
    coin_code = db.get("coin_code")
    used_codes = db.get("used_codes") if db.exists("used_codes") else []
    text = msg.text
    if text == code_coin:
        if msg.from_user.id in used_codes:
            bot.reply_to(msg,f'• لقد استخدمت هذا الكود من قبل ❌')
            return
        if user_code >= 1:
            join_user = msg.from_user.id
            joo = db.get(f"user_{join_user}")
            joo['coins'] = int(joo['coins']) + int(coin_code)
            db.set(f"user_{msg.from_user.id}", joo)
            bot.reply_to(msg,f'• تم اضافة {coin_code} نقاط الي حسابك ✅')
            user_after = int(user_code) - 1
            db.set("user_code", user_after)
            used_codes.append(msg.from_user.id)
            db.set('used_codes', used_codes)
            start_message(msg)
            user_id = msg.from_user.id
            code = int(db.get(f"cd_{user_id}")) if db.exists(f"cd_{user_id}") else 0
            daily_count = code + 1
            db.set(f"cd_{user_id}", int(daily_count))
        else:
            bot.reply_to(msg,'• انتهت صلاحية هذا الكود ❌')
    else:
        bot.reply_to(msg,f'• لقد ادخلت كود بشكل خطا ❌')
####$$########
def link_bot2(message, amount):
    maintenance_mode = db.get("maintenance_mode") if db.exists("maintenance_mode") else False
    if maintenance_mode == True:
        bot.reply_to(message, "البوت قيد الصيانة والتطوير حاليًا ⚙️")
        return False
    if message.text == "/start":
        start_message(message)
        return
    url = message.text
    if 'https://t.me' in url:
        x = bot.reply_to(message,text=f'• الكمية : {amount}\n• الرابط : {url}\n\n• الان ارسل رابط او معرف قناة الاشتراك الاجبارى')
        bot.register_next_step_handler(x, linkbot_chforce, amount, url)
    else:
        x = bot.reply_to(message,text=f'• رجاء ارسل الرابط بشكل صحيح')
        return
def dump_votes(message):
    maintenance_mode = db.get("maintenance_mode") if db.exists("maintenance_mode") else False
    if maintenance_mode == True:
        bot.reply_to(message, "البوت قيد الصيانة والتطوير حاليًا ⚙️")
        return False
    if message.text == "/start":
        start_message(message)
        return
    url = message.text
    load_ = db.get('accounts')
    num = len(load_)
    acc = db.get(f'user_{message.from_user.id}')
    typerr = 'سحب تصويت'
    v = bot.reply_to(message,text=f'• 📤] تم بدء طلبك بنجاح | تفاصيل طلبك\n\n• 🏷] النوع : {typerr}\n\n• 📎] الرابط : {url} \n\n• 🗳] الكمية : {num}')
    tim = int(db.get(f"tim_{message.from_user.id}")) if db.exists(f"tim_{message.from_user.id}") else 0
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr} \n• الرابط : {url} \n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username} ')
    true, false = 0, 0
    nume = int(num)
    prog = bot.send_message(chat_id=int(message.from_user.id), text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
    for num in load_:
        try:
            x = asyncio.run(dump_votess(num['s'], url, tim))
            
            if x == 'o':
                continue
            if x == True:
                true += 1
                nume -= 1
                bot.edit_message_text(chat_id=message.from_user.id, message_id=prog.message_id, text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
            else:
                false += 1
                bot.edit_message_text(chat_id=message.from_user.id, message_id=prog.message_id, text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
        except Exception as e:
            print(f"Erorr: {e}")
            continue
    addord()
    user_id = message.from_user.id
    buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
    buys+=1
    db.set(f"user_{user_id}_buys", int(buys))
    bot.reply_to(message,text=f'• تم اكتمال طلبك بنجاح ✅:\n\n• تم سحب : {false} تصويت\n• لم يتم سحب : {true}',reply_markup=bk)
  
def linkbot_chforce(message, amount, url):
    maintenance_mode = db.get("maintenance_mode") if db.exists("maintenance_mode") else False
    if maintenance_mode == True:
        bot.reply_to(message, "البوت قيد الصيانة والتطوير حاليًا ⚙️")
        return False
    if message.text == "/start":
        start_message(message)
        return
    channel_force = message.text.replace('https://t.me/', '').replace('@', '')
    bot_id, user_id = url.split("?start=")[0].split("/")[-1], url.split("?start=")[1]
    channel = "@" + bot_id
    tex = "/start " + user_id
    pr = linkbot2_price * amount
    load_ = db.get('accounts')
    acc = db.get(f'user_{message.from_user.id}')
    typerr = 'رابط دعوة اشتراك اجبارى'
    v = bot.reply_to(message,text=f'• 📤] تم بدء طلبك بنجاح | تفاصيل طلبك\n\n• 🏷] النوع : {typerr}\n\n• 📎] الرابط : {url} \n\n• 🗳] الكمية : {amount}\n\n• 📣] قناة الاشتراك الاولي : @{channel_force}')
    tim = int(db.get(f"tim_{message.from_user.id}")) if db.exists(f"tim_{message.from_user.id}") else 0
    db.set(f"serv_{message.from_user.id}", True)
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr}\n• العدد : {amount} \n• الرابط : {url} \n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username} ')
    true, false = 0, 0
    nume = int(amount)
    prog = bot.send_message(chat_id=int(message.from_user.id), text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
    for y in load_:
        if true >= amount:
            break
        try:
            session = random.choice(load_)
            x = asyncio.run(linkbot2(session, channel, tex, channel_force, tim))
            load_.remove(session)
            if x == 'o':
                continue
            if x == True:
                true += 1
                nume -= 1
                bot.edit_message_text(chat_id=message.from_user.id, message_id=prog.message_id, text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
            else:
                false += 1
                bot.edit_message_text(chat_id=message.from_user.id, message_id=prog.message_id, text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
        except Exception as e:
            print(e)
            continue
    if true >= 1:
        for ix in range(true):
            acc['coins'] -= linkbot2_price
        db.set(f'user_{message.from_user.id}', acc)
    db.set(f"serv_{message.from_user.id}", False)
    addord()
    user_id = message.from_user.id
    buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
    buys+=1
    db.set(f"user_{user_id}_buys", int(buys))
    bot.reply_to(message,text=f'• 📥] تم اكتمال طلبك بنجاح | تفاصيل عن طلبك :\n\n• 📦] العدد المطلوب︙{amount} \n\n• ✅] العدد المكتمل︙{true} \n• ❌] فشل محاولة ارسال : {false}\n\n• 📎] الرابط︙{url}\n• ➖] تم خصم︙{true*linkbot2_price}',reply_markup=bk)
    bot.delete_message(chat_id=message.from_user.id, message_id=prog.message_id)
    user_id = message.from_user.id
    code = int(db.get(f"po_{user_id}")) if db.exists(f"po_{user_id}") else 0
    daily_count = code + int(true*linkbot2_price)
    db.set(f"po_{user_id}", int(daily_count))
    return
##################
def get_comments_url(message, amount):
    maintenance_mode = db.get("maintenance_mode") if db.exists("maintenance_mode") else False
    if maintenance_mode == True:
        bot.reply_to(message, "البوت قيد الصيانة والتطوير حاليًا ⚙️")
        return False
    if message.text == "/start":
        start_message(message)
        return
    url = message.text
    admins = db.get('admins')
    if 'https://t.me' in url:
        x = bot.reply_to(message,text=f'• الكمية : {amount}\n• الرابط : {url}\n\n• الان ارسل التعليق الذي تريد رشقه')
        bot.register_next_step_handler(x, comment_text, amount, url)
    else:
        x = bot.reply_to(message,text=f'• رجاء ارسل الرابط بشكل صحيح')
        return
def comment_text(message, amount, url):
    maintenance_mode = db.get("maintenance_mode") if db.exists("maintenance_mode") else False
    if maintenance_mode == True:
        bot.reply_to(message, "البوت قيد الصيانة والتطوير حاليًا ⚙️")
        return False
    if message.text == "/start":
        start_message(message)
        return
    admins = db.get('admins')
    text = message.text
    if text:
        if len(text) > 100:
            bot.reply_to(message, text='• ارسل رسالة تكون اقل من 100 حرف ')
            return
        acc = db.get(f'user_{message.from_user.id}')
        pr = comment_price * amount
        load_ = db.get('accounts')
        typerr = 'تعليقات خدمة ᴠɪᴘ'
        bot.reply_to(message,text=f'• 📤] تم بدء طلبك بنجاح | تفاصيل طلبك\n\n• 🏷] النوع : {typerr}\n\n• 📎] الرابط : {url} \n\n• 🗳] الكمية : {amount}')
        tim = int(db.get(f"tim_{message.from_user.id}")) if db.exists(f"tim_{message.from_user.id}") else 0
        db.set(f"serv_{message.from_user.id}", True)
        bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr} .\n• العدد : {amount}\n• الرابط : {url}\n• ايديه: {message.from_user.id} \n• يوزره : @{message.from_user.username}')
        true, false = 0, 0
        nume = int(amount)
        prog = bot.send_message(chat_id=int(message.from_user.id), text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
        for y in load_:
            if true >= amount:
                break
            try:
                session = random.choice(load_)
                x = asyncio.run(send_comment(session, url, text, tim))
                load_.remove(session)
                true += 1
                nume -= 1
                bot.edit_message_text(chat_id=message.from_user.id, message_id=prog.message_id, text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
            except:
                false += 1
                bot.edit_message_text(chat_id=message.from_user.id, message_id=prog.message_id, text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
                continue
        if true >= 1:
            for ix in range(true):
                acc['coins'] -= comment_price
            db.set(f'user_{message.from_user.id}', acc)
        else:
            pass
        db.set(f"serv_{message.from_user.id}", False)
        addord()
        user_id = message.from_user.id
        buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
        buys+=1
        db.set(f"user_{user_id}_buys", int(buys))
        bot.reply_to(message,text=f'• 📥] تم اكتمال طلبك بنجاح | تفاصيل عن طلبك :\n\n• 📦] العدد المطلوب︙{amount} \n\n• ✅] العدد المكتمل︙{true} \n• ❌] فشل محاولة ارسال : {false}\n\n• 📎] الرابط︙{url}\n• ➖] تم خصم︙{true*comment_price} من نقاطك',reply_markup=bk)
        bot.delete_message(chat_id=message.from_user.id, message_id=prog.message_id)
        code = int(db.get(f"po_{user_id}")) if db.exists(f"po_{user_id}") else 0
        daily_count = code + int(true*comment_price)
        db.set(f"po_{user_id}", int(daily_count))
        return
########################
def link_bot(message, amount):
    maintenance_mode = db.get("maintenance_mode") if db.exists("maintenance_mode") else False
    if maintenance_mode == True:
        bot.reply_to(message, "البوت قيد الصيانة والتطوير حاليًا ⚙️")
        return False
    if message.text == "/start":
        start_message(message)
        return
    admins = db.get('admins')
    url = message.text
    bot_id, user_id = url.split("?start=")[0].split("/")[-1], url.split("?start=")[1]
    channel = "@" + bot_id
    tex = "/start " + user_id
    pr = linkbot_price * amount
    load_ = db.get('accounts')
    acc = db.get(f'user_{message.from_user.id}')
    typerr = 'رابط دعوة بدون اشتراك اجبارى'
    v = bot.reply_to(message,text=f'• 📤] تم بدء طلبك بنجاح | تفاصيل طلبك\n\n• 🏷] النوع : {typerr}\n\n• 📎] الرابط : {url} \n\n• 🗳] الكمية : {amount}')
    tim = int(db.get(f"tim_{message.from_user.id}")) if db.exists(f"tim_{message.from_user.id}") else 0
    db.set(f"serv_{message.from_user.id}", True)
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr}\n• العدد : {amount} \n• الرابط : {url} \n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username} ')
    true, false = 0, 0
    nume = int(amount)
    prog = bot.send_message(chat_id=int(message.from_user.id), text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
    for y in load_:
        if true >= amount:
            break
        try:
            session = random.choice(load_)
            x = asyncio.run(linkbot(session, channel, tex, tim))
            load_.remove(session)
            if x == 'o':
                continue
            if x == True:
                true += 1
                nume -= 1
                bot.edit_message_text(chat_id=message.from_user.id, message_id=prog.message_id, text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
            else:
                false += 1
                bot.edit_message_text(chat_id=message.from_user.id, message_id=prog.message_id, text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
        except Exception as e:
            print(e)
            continue
    if true >= 1:
        for ix in range(true):
            acc['coins'] -= linkbot_price
        db.set(f'user_{message.from_user.id}', acc)
    db.set(f"serv_{message.from_user.id}", False)
    addord()
    user_id = message.from_user.id
    buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
    buys+=1
    db.set(f"user_{user_id}_buys", int(buys))
    bot.reply_to(message,text=f'• 📥] تم اكتمال طلبك بنجاح | تفاصيل عن طلبك :\n\n• 📦] العدد المطلوب︙{amount} \n\n• ✅] العدد المكتمل︙{true} \n• ❌] فشل محاولة ارسال : {false}\n\n• 📎] معرف البوت︙{channel}\n• ➖] تم خصم : {true*linkbot_price}',reply_markup=bk)
    bot.delete_message(chat_id=message.from_user.id, message_id=prog.message_id)
    code = int(db.get(f"po_{user_id}")) if db.exists(f"po_{user_id}") else 0
    daily_count = code + int(true*linkbot_price)
    db.set(f"po_{user_id}", int(daily_count))
    return

def get_bot_user(message, amount):
    maintenance_mode = db.get("maintenance_mode") if db.exists("maintenance_mode") else False
    if maintenance_mode == True:
        bot.reply_to(message, "البوت قيد الصيانة والتطوير حاليًا ⚙️")
        return False
    if message.text == "/start":
        start_message(message)
        return
    admins = db.get('admins')
    url = message.text.replace('https://t.me/', '').replace('@', '')
    pr = userbot_price * amount
    load_ = db.get('accounts')
    acc = db.get(f'user_{message.from_user.id}')
    typerr = 'مستخدمين بوت'
    v = bot.reply_to(message,text=f'• 📤] تم بدء طلبك بنجاح | تفاصيل طلبك\n\n• 🏷] النوع : {typerr}\n\n• 📎] الرابط : {url} \n\n• 🗳] الكمية : {amount}')
    tim = int(db.get(f"tim_{message.from_user.id}")) if db.exists(f"tim_{message.from_user.id}") else 0
    db.set(f"serv_{message.from_user.id}", True)
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr}\n• العدد : {amount} \n• الرابط : {url} \n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username} ')
    true, false = 0, 0
    nume = int(amount)
    tim = int(db.get(f"tim_{message.from_user.id}")) if db.exists(f"tim_{message.from_user.id}") else 0
    prog = bot.send_message(chat_id=int(message.from_user.id), text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
    for y in load_:
        if true >= amount:
            break
        try:
            session = random.choice(load_)
            x = asyncio.run(userbot(session, url, tim))
            load_.remove(session)
            if x == 'o':
                continue
            if x == True:
                true += 1
                nume -= 1
                bot.edit_message_text(chat_id=message.from_user.id, message_id=prog.message_id, text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
            else:
                false += 1
                bot.edit_message_text(chat_id=message.from_user.id, message_id=prog.message_id, text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
        except Exception as e:
            print(e)
            continue
    if true >= 1:
        for ix in range(true):
            acc['coins'] -= usebot_price
        db.set(f'user_{message.from_user.id}', acc)
    db.set(f"serv_{message.from_user.id}", False)
    addord()
    user_id = message.from_user.id
    buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
    buys+=1
    db.set(f"user_{user_id}_buys", int(buys))
    bot.reply_to(message,text=f'• 📥] تم اكتمال طلبك بنجاح | تفاصيل عن طلبك :\n\n• 📦] العدد المطلوب︙{amount} \n\n• ✅] العدد المكتمل︙{true} \n• ❌] فشل محاولة ارسال : {false}\n\n• 📎] الرابط︙{message.text}\n• ➖] تم خصم︙{true*userbot_price}',reply_markup=bk)
    bot.delete_message(chat_id=message.from_user.id, message_id=prog.message_id)
    code = int(db.get(f"po_{user_id}")) if db.exists(f"po_{user_id}") else 0
    daily_count = code + int(true*userbot_price)
    db.set(f"po_{user_id}", int(daily_count))
    return
    
def get_url_spam(message, amount):
    maintenance_mode = db.get("maintenance_mode") if db.exists("maintenance_mode") else False
    if maintenance_mode == True:
        bot.reply_to(message, "البوت قيد الصيانة والتطوير حاليًا ⚙️")
        return False
    if message.text == "/start":
        start_message(message)
        return
    url = message.text
    admins = db.get('admins')
    if 'https://t.me' in url or '@' in url:
        x = bot.reply_to(message,text=f'• الان ارسل الرسالة اللي تريد ترسلها للحساب')
        bot.register_next_step_handler(x, get_text, amount, url)
        return

def get_text(message, amount, url):
    maintenance_mode = db.get("maintenance_mode") if db.exists("maintenance_mode") else False
    if maintenance_mode == True:
        bot.reply_to(message, "البوت قيد الصيانة والتطوير حاليًا ⚙️")
        return False
    if message.text == "/start":
        start_message(message)
        return
    admins = db.get('admins')
    text = message.text
    if text:
        if len(text) > 1000:
            bot.reply_to(message, text='• ارسل رسالة تكون اقل من 1000 حرف ')
            return
        acc = db.get(f'user_{message.from_user.id}')
        pr = spam_price * amount
        load_ = db.get('accounts')
        typerr = 'رسائل مزعجة خدمة ᴠɪᴘ'
        bot.reply_to(message,text=f'• 📤] تم بدء طلبك بنجاح | تفاصيل طلبك\n\n• 🏷] النوع : {typerr}\n\n• 📎] الرابط : {url} \n\n• 🗳] الكمية : {amount}')
        tim = int(db.get(f"tim_{message.from_user.id}")) if db.exists(f"tim_{message.from_user.id}") else 0
        db.set(f"serv_{message.from_user.id}", True)
        bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr} .\n• العدد : {amount}\n• الرابط : {url}\n• ايديه: {message.from_user.id} \n• يوزره : @{message.from_user.username}')
        true, false = 0, 0
        nume = int(amount)
        prog = bot.send_message(chat_id=int(message.from_user.id), text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
        for y in load_:
            if true >= amount:
                break
            try:
                session = random.choice(load_)
                x = asyncio.run(send_message(session, chat=url, text=tex))
                load_.remove(session)
                true += 1
                nume -= 1
                bot.edit_message_text(chat_id=message.from_user.id, message_id=prog.message_id, text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
            except:
                false += 1
                bot.edit_message_text(chat_id=message.from_user.id, message_id=prog.message_id, text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
                continue
        if true >= 1:
            for ix in range(true):
                acc['coins'] -= spam_price
            db.set(f'user_{message.from_user.id}', acc)
        else:
            pass
        db.set(f"serv_{message.from_user.id}", False)
        addord()
        user_id = message.from_user.id
        buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
        buys+=1
        db.set(f"user_{user_id}_buys", int(buys))
        bot.reply_to(message,text=f'• 📥] تم اكتمال طلبك بنجاح | تفاصيل عن طلبك :\n\n• 📦] العدد المطلوب︙{amount} \n\n• ✅] العدد المكتمل︙{true} \n• ❌] فشل محاولة ارسال : {false}\n\n• 📎] الرابط︙{url}\n• ➖] تم خصم︙{true*spam_price} من نقاطك',reply_markup=bk)
        bot.delete_message(chat_id=message.from_user.id, message_id=prog.message_id)
        code = int(db.get(f"po_{user_id}")) if db.exists(f"po_{user_id}") else 0
        daily_count = code + int(true*spam_price)
        db.set(f"po_{user_id}", int(daily_count))
        return

def get_url_memp(message, amount):
    maintenance_mode = db.get("maintenance_mode") if db.exists("maintenance_mode") else False
    if maintenance_mode == True:
        bot.reply_to(message, "البوت قيد الصيانة والتطوير حاليًا ⚙️")
        return False
    if message.text == "/start":
        start_message(message)
        return
    admins = db.get('admins')
    url = message.text
    load = db.get('accounts')
    info = get(message.from_user.id)
    price = member_price * amount
    if price > int(info['coins']):
        bot.reply_to(message,text=f'نقاطك غير كافية لتنفيذ طلبك تحتاج الي <strong> {price - int(info["coins"])} </strong>',reply_markup=bk)
        return
    if len(load) < 1:
        bot.reply_to(message,text='عدد حسابات البوت لا تكفي لتنفيذ طلبك ',reply_markup=bk)
        return
    typerr = 'رشق اعضاء قناة خاصة خدمة ᴠɪᴘ'
    v = bot.reply_to(message,text=f'• 📤] تم بدء طلبك بنجاح | تفاصيل طلبك\n\n• 🏷] النوع : {typerr}\n\n• 📎] الرابط : {url} \n\n• 🗳] الكمية : {amount}')
    tim = int(db.get(f"tim_{message.from_user.id}")) if db.exists(f"tim_{message.from_user.id}") else 0
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت \n• النوع: {typerr}\n• العدد : {amount}\n• الرابط : {url}\n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username}')
    true, false = 0, 0
    nume = int(amount)
    prog = bot.send_message(chat_id=int(message.from_user.id), text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
    for y in load:
        if true >= amount:
            break
        try:
            session = random.choice(load_)
            x = asyncio.run(join_chatp(session, url, tim))
            load_.remove(session)
            if x == 'o':
                continue
            if x == True:
                true += 1
                nume -= 1
                bot.edit_message_text(chat_id=message.from_user.id, message_id=prog.message_id, text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
            else:
                false += 1
                bot.edit_message_text(chat_id=message.from_user.id, message_id=prog.message_id, text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
        except Exception as e:
            pass
    if true >= 1:
        for ix in range(true):
            info['coins'] -= member_price
        db.set(f'user_{message.from_user.id}', info)
    else:
        pass
    bot.reply_to(message,text=f'• 📥] تم اكتمال طلبك بنجاح | تفاصيل عن طلبك :\n\n• 📦] العدد المطلوب︙{amount} \n\n• ✅] العدد المكتمل︙{true} \n• ❌] فشل محاولة ارسال : {false}\n\n• 📎] الرابط︙{url}\n• ➖] تم خصم︙{true*member_price} من نقاطك',)
    bot.delete_message(chat_id=message.from_user.id, message_id=prog.message_id)
    user_id = message.from_user.id
    code = int(db.get(f"po_{user_id}")) if db.exists(f"po_{user_id}") else 0
    daily_count = code + int(true*member_price)
    db.set(f"po_{user_id}", int(daily_count))
    return

def get_url_mem(message, amount):
    maintenance_mode = db.get("maintenance_mode") if db.exists("maintenance_mode") else False
    if maintenance_mode == True:
        bot.reply_to(message, "البوت قيد الصيانة والتطوير حاليًا ⚙️")
        return False
    if message.text == "/start":
        start_message(message)
        return
    admins = db.get('admins')
    url = message.text
    if 'https://t.me' in url or '@' in url:
        if detect(url):
            load = db.get('accounts')
            info = get(message.from_user.id)
            price = member_price * amount
            if price > int(info['coins']):
                bot.reply_to(message,text=f'مامعك نقاط كافية، تحتاج <strong> {price - int(info["coins"])} </strong> نقطة علمود ترسل هذا العدد',reply_markup=bk)
                return
            if len(load) < 1:
                bot.reply_to(message,text='عدد حسابات البوت لا تكفي لتنفيذ طلبك ',reply_markup=bk)
                return
            typerr = 'رشق اعضاء خدمة ᴠɪᴘ'
            v = bot.reply_to(message,text=f'• 📤] تم بدء طلبك بنجاح | تفاصيل طلبك\n\n• 🏷] النوع : {typerr}\n\n• 📎] الرابط : {url} \n\n• 🗳] الكمية : {amount}')
            tim = int(db.get(f"tim_{message.from_user.id}")) if db.exists(f"tim_{message.from_user.id}") else 0
            db.set(f"serv_{message.from_user.id}", True)
            bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت \n• النوع: {typerr}\n• العدد : {amount}\n• الرابط : {url}\n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username}')
            
            true, false = 0, 0
            nume = int(amount)
            prog = bot.send_message(chat_id=int(message.from_user.id), text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
            for y in load:
                if true >= amount:
                    break
                try:
                    session = random.choice(load_)
                    x = asyncio.run(join_chat(session, url, tim))
                    load_.remove(session)
                    if x == 'o':
                        continue
                    if x == True:
                        true += 1
                        nume -= 1
                        bot.edit_message_text(chat_id=message.from_user.id, message_id=prog.message_id, text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
                    else:
                        false += 1
                        bot.edit_message_text(chat_id=message.from_user.id, message_id=prog.message_id, text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
                except Exception as e:
                   pass
            if true >= 1:
                for ix in range(true):
                    info['coins'] -= member_price
                db.set(f'user_{message.from_user.id}', info)
            else:
                pass
            db.set(f"serv_{message.from_user.id}", False)
            bot.reply_to(message,text=f'• 📥] تم اكتمال طلبك بنجاح | تفاصيل عن طلبك :\n\n• 📦] العدد المطلوب︙{amount} \n\n• ✅] العدد المكتمل︙{true} \n• ❌] فشل محاولة ارسال : {false}\n\n• 📎] الرابط︙{url}\n• ➖] تم خصم︙{true*member_price} من نقاطك',)
            bot.delete_message(chat_id=message.from_user.id, message_id=prog.message_id)
            user_id = message.from_user.id
            code = int(db.get(f"po_{user_id}")) if db.exists(f"po_{user_id}") else 0
            daily_count = code + int(true*member_price)
            db.set(f"po_{user_id}", int(daily_count))
            return
        else:
            username = url.replace('https://t.me/', '').replace('@', '')
            load = db.get('accounts')
            info = get(message.from_user.id)
            price = member_price * amount
            if price > int(info['coins']):
                bot.reply_to(message,text=f'• نقاطك غير كافية : تحتاج الي <strong> {price - int(info["coins"])} </strong> نقطة',reply_markup=bk)
                return
            if len(load) < 1:
                bot.reply_to(message,text=f'• حسابات البوت لا تكفي لتنفيذ طلبك',reply_markup=bk)
                return
            typerr = 'رشق اعضاء خدمة ᴠɪᴘ'
            v = bot.reply_to(message,text=f'• 📤] تم بدء طلبك بنجاح | تفاصيل طلبك\n\n• 🏷] النوع : {typerr}\n\n• 📎] الرابط : {url} \n\n• 🗳] الكمية : {amount}')
            tim = int(db.get(f"tim_{message.from_user.id}")) if db.exists(f"tim_{message.from_user.id}") else 0
            db.set(f"serv_{message.from_user.id}", True)
            bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr}\n• العدد : {amount}\n• الرابط : {url}\n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username} ')
            
            true, false = 0, 0
            nume = int(amount)
            prog = bot.send_message(chat_id=int(message.from_user.id), text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
            for y in load:
                if true >= amount:
                    break
                try:
                    session = random.choice(load_)
                    x = asyncio.run(join_chat(session, username, tim))
                    load_.remove(session)
                    if x == 'o':
                        continue
                    if x == True:
                        true += 1
                        nume -= 1
                        bot.edit_message_text(chat_id=message.from_user.id, message_id=prog.message_id, text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
                    else:
                        false += 1
                        bot.edit_message_text(chat_id=message.from_user.id, message_id=prog.message_id, text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
                except Exception as e:
                   
                    continue
            for i in range(true):
                info['coins'] -= member_price
            db.set(f"serv_{message.from_user.id}", False) 
            db.set(f'user_{message.from_user.id}', info)
            addord()
            user_id = message.from_user.id
            buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
            buys+=1
            db.set(f"user_{user_id}_buys", int(buys))
            bot.reply_to(message,text=f'• 📥] تم اكتمال طلبك بنجاح | تفاصيل عن طلبك :\n\n• 📦] العدد المطلوب︙{amount} \n\n• ✅] العدد المكتمل︙{true} \n• ❌] فشل محاولة ارسال : {false}\n\n• 📎] الرابط︙{url}\n• ➖] تم خصم︙{true*member_price} من نقاطك',)
            bot.delete_message(chat_id=message.from_user.id, message_id=prog.message_id)
            user_id = message.from_user.id
            code = int(db.get(f"po_{user_id}")) if db.exists(f"po_{user_id}") else 0
            daily_count = code + int(true*member_price)
            db.set(f"po_{user_id}", int(daily_count))
            return

def chtime(msg):
    try:
        time = int(msg.text)
    except:
        bot.reply_to(msg, text='خطا ، قم بارسال الوقت كارقام فقط ❌')
        return
    if time <0:
        bot.reply_to(msg, text='خطا ، اقل قيمة يمكن اضافتها هي 0 ❌')
        return
    if time >200:
        bot.reply_to(msg, text='خطا ، اكبر قيمة يمكن ادخالها هي 200 ❌')
        return
    db.set(f"tim_{msg.from_user.id}", int(time))
    bot.reply_to(msg, text='نجاح ، تم حفظ القيمة بنجاح ✅')
def checks(link):
    admins = db.get('admins')
    pattern = r"https?://t\.me/(\w+)/(\d+)"
    match = re.match(pattern, link)

    if match:
        username = match.group(1)
        post_id = match.group(2)
        return username, post_id
    else:
        return False
def get_react(message, amount):
    maintenance_mode = db.get("maintenance_mode") if db.exists("maintenance_mode") else False
    if maintenance_mode == True:
        bot.reply_to(message, "البوت قيد الصيانة والتطوير حاليًا ⚙️")
        return False
    if message.text == "/start":
        start_message(message)
        return
    rs = ["👍", "👎", "❤", "🔥", "🥰", "👏", "😁", "🤔", "🤯", "🤬", "😢", "🎉", "🤩", "🤮", "💩", "🙏", "👌", "🕊", "🤡", "🥱", "🥴", "😍", "🐳", "🌚", "🌭", "💯", "🤣", "⚡️", "🍌", "🏆", "💔", "🤨", "😐", "🍓", "🍾", "💋", "🖕","😈", "😴", "🤓", "👻", "👨‍💻", "👀", "🎃", "🙈", "😇", "😨", "🤝", "✍", "🤗", "🫡", "🎅", "🎄", "☃️", "💅", "🤪","🗿", "🆒", "💘", "🙉", "🦄", "😘", "💊", "🙊", "😎", "👾", "🤷‍♂️", "🤷", "🤷‍♀️", "😡","❤"]
    if message.text in rs:
        x = bot.reply_to(message,f'• الكمية : {amount}\n• التفاعل : {message.text}\n\n• ارسل الان رابط المنشور لرشق التفاعلات عليه')
        bot.register_next_step_handler(x, get_url_react, amount, message)
    elif message.text == "❤":
        x = bot.reply_to(message,f'• الكمية : {amount}\n• التفاعل : {message.text}\n\n• ارسل الان رابط المنشور لرشق التفاعلات عليه')
        bot.register_next_step_handler(x, get_url_react, amount, message)
    else:
        x = bot.reply_to(message,f'• رجاء ارسل التفاعل بشكل صحيح')
        bot.register_next_step_handler(x, get_react, amount)
        return
def get_url_votes(message, amount, time):
    maintenance_mode = db.get("maintenance_mode") if db.exists("maintenance_mode") else False
    if maintenance_mode == True:
        bot.reply_to(message, "البوت قيد الصيانة والتطوير حاليًا ⚙️")
        return False
    if message.text == "/start":
        start_message(message)
        return
    admins = db.get('admins')
    url = message.text
    if "/c/" in url:
        bot.reply_to(message,text=f'• عذرا لا يمكنك استخدام الخدمة في القنوات الخاصة')
        return
    if not checks(url):
        bot.reply_to(message,text=f'• رجاء ارسل الرابط بشكل صحيح')
        return
    pr = vote_price * amount
    load_ = db.get('accounts')
    acc = db.get(f'user_{message.from_user.id}')
    typerr = 'تصويت'
    v = bot.reply_to(message,text=f'• 📤] تم بدء طلبك بنجاح | تفاصيل طلبك\n\n• 🏷] النوع : {typerr}\n\n• 📎] الرابط : {url} \n\n• 🗳] الكمية : {amount}\n• ⏱] الوقت بين كل تصويت : {time}')
    db.set(f"serv_{message.from_user.id}", True)
    tim = int(db.get(f"tim_{message.from_user.id}")) if db.exists(f"tim_{message.from_user.id}") else 0
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr}\n• العدد : {amount} \n• الرابط : {url} \n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username}\n• الوقت بين التصويت : {time} ')
    true, false = 0, 0
    nume = int(amount)
    prog = bot.send_message(chat_id=int(message.from_user.id), text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
    for y in load_:
        if true >= amount:
            break
        try:
            session = random.choice(load_)
            x = asyncio.run(vote_one(session, url, time, tim))
            load_.remove(session)
            if x == 'o':
                continue
            if x == True:
                true += 1
                nume -= 1
                bot.edit_message_text(chat_id=message.from_user.id, message_id=prog.message_id, text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
            else:
                false += 1
                bot.edit_message_text(chat_id=message.from_user.id, message_id=prog.message_id, text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
        except Exception as e:
            print(e)
            continue
    if true >= 1:
        for ix in range(true):
            acc['coins'] -= vote_price
        db.set(f'user_{message.from_user.id}', acc)
    db.set(f"serv_{message.from_user.id}", False)
    addord()
    user_id = message.from_user.id
    buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
    buys+=1
    db.set(f"user_{user_id}_buys", int(buys))
    bot.reply_to(message,text=f'• 📥] تم اكتمال طلبك بنجاح | تفاصيل عن طلبك :\n\n• 📦] العدد المطلوب︙{amount} \n\n• ✅] العدد المكتمل︙{true} \n• ❌] فشل محاولة ارسال : {false}\n\n• 📎] الرابط︙{url}',reply_markup=bk)
    bot.delete_message(chat_id=message.from_user.id, message_id=prog.message_id)
    user_id = message.from_user.id
    code = int(db.get(f"po_{user_id}")) if db.exists(f"po_{user_id}") else 0
    daily_count = code + int(true*vote_price)
    db.set(f"po_{user_id}", int(daily_count))
    return
    
def get_url_react(message, amount, like):
    maintenance_mode = db.get("maintenance_mode") if db.exists("maintenance_mode") else False
    if maintenance_mode == True:
        bot.reply_to(message, "البوت قيد الصيانة والتطوير حاليًا ⚙️")
        return False
    if message.text == "/start":
        start_message(message)
        return
    admins = db.get('admins')
    url = message.text
    like = like.text
    if "/c/" in url:
        bot.reply_to(message,text=f'• عذرا لا يمكنك استخدام الخدمة في القنوات الخاصة')
        return
    if not checks(url):
        bot.reply_to(message,text=f'• رجاء ارسل الرابط بشكل صحيح')
        return
    pr = react_price * amount
    load_ = db.get('accounts')
    acc = db.get(f'user_{message.from_user.id}')
    typerr = 'تفاعلات اختياري'
    v = bot.reply_to(message,text=f'• 📤] تم بدء طلبك بنجاح | تفاصيل طلبك\n\n\n\n• 🏷] النوع : {typerr}\n\n• 📎] الرابط : {url}\n• 👍] التفاعل : {like}\n\n• 🗳] الكمية : {amount}')
    tim = int(db.get(f"tim_{message.from_user.id}")) if db.exists(f"tim_{message.from_user.id}") else 0
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr}\n• العدد : {amount} \n• الرابط : {url} \n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username} ')
    db.set(f"serv_{message.from_user.id}", True)
    true, false = 0, 0
    nume = int(amount)
    prog = bot.send_message(chat_id=int(message.from_user.id), text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
    for y in load_:
        if true >= amount:
            break
        try:
            session = random.choice(load_)
            x = asyncio.run(reactions(session, url, like, tim))
            load_.remove(session)
            if x == 'o':
                continue
            if x == True:
                true += 1
                nume -= 1
                bot.edit_message_text(chat_id=message.from_user.id, message_id=prog.message_id, text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
            else:
                false += 1
                bot.edit_message_text(chat_id=message.from_user.id, message_id=prog.message_id, text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
        except Exception as e:
            print(e)
            continue
    if true >= 1:
        for ix in range(true):
            acc['coins'] -= react_price
        db.set(f'user_{message.from_user.id}', acc)
    db.set(f"serv_{message.from_user.id}", False)
    addord()
    user_id = message.from_user.id
    buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
    buys+=1
    db.set(f"user_{user_id}_buys", int(buys))
    bot.reply_to(message,text=f'• 📥] تم اكتمال طلبك بنجاح | تفاصيل عن طلبك :\n\n• 📦] العدد المطلوب︙{amount} \n\n• ✅] العدد المكتمل︙{true} \n• ❌] فشل محاولة ارسال : {false}\n\n• 📎] الرابط︙{url}\n• ➖] تم خصم︙{true*react_price}',reply_markup=bk)
    bot.delete_message(chat_id=message.from_user.id, message_id=prog.message_id)
    user_id = message.from_user.id
    code = int(db.get(f"po_{user_id}")) if db.exists(f"po_{user_id}") else 0
    daily_count = code + int(true*react_price)
    db.set(f"po_{user_id}", int(daily_count))
    return
def get_reacts_url(message, amount):
    maintenance_mode = db.get("maintenance_mode") if db.exists("maintenance_mode") else False
    if maintenance_mode == True:
        bot.reply_to(message, "البوت قيد الصيانة والتطوير حاليًا ⚙️")
        return False
    if message.text == "/start":
        start_message(message)
        return
    admins = db.get('admins')
    url = message.text
    if "/c/" in url:
        bot.reply_to(message,text=f'• عذرا لا يمكنك استخدام الخدمة في القنوات الخاصة')
        return
    if not checks(url):
        bot.reply_to(message,text=f'• رجاء ارسل الرابط بشكل صحيح')
        return
    pr = react_price * amount
    load_ = db.get('accounts')
    acc = db.get(f'user_{message.from_user.id}')
    typerr = 'تفاعلات عشوائي'
    v = bot.reply_to(message,text=f'• 📤] تم بدء طلبك بنجاح | تفاصيل طلبك\n\n• 🏷] النوع : {typerr}\n\n• 📎] الرابط : {url} \n\n• 🗳] الكمية : {amount}')
    tim = int(db.get(f"tim_{message.from_user.id}")) if db.exists(f"tim_{message.from_user.id}") else 0
    db.set(f"serv_{message.from_user.id}", True)
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr}\n• العدد : {amount} \n• الرابط : {url} \n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username} ')
    true, false = 0, 0
    nume = int(amount)
    prog = bot.send_message(chat_id=int(message.from_user.id), text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
    for y in load_:
        if true >= amount:
            break
        try:
            session = random.choice(load_)
            x = asyncio.run(reaction(session, url, tim))
            load_.remove(session)
            if x == 'o':
                continue
            if x == True:
                true += 1
                nume -= 1
                bot.edit_message_text(chat_id=message.from_user.id, message_id=prog.message_id, text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
            else:
                false += 1
                bot.edit_message_text(chat_id=message.from_user.id, message_id=prog.message_id, text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
        except Exception as e:
            print(e)
            continue
    if true >= 1:
        for ix in range(true):
            acc['coins'] -= react_price
        db.set(f'user_{message.from_user.id}', acc)
    db.set(f"serv_{message.from_user.id}", False)
    addord()
    user_id = message.from_user.id
    buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
    buys+=1
    db.set(f"user_{user_id}_buys", int(buys))
    bot.reply_to(message,text=f'• 📥] تم اكتمال طلبك بنجاح | تفاصيل عن طلبك :\n\n• 📦] العدد المطلوب︙{amount} \n\n• ✅] العدد المكتمل︙{true} \n• ❌] فشل محاولة ارسال : {false}\n\n• 📎] الرابط︙{url}\n• ➖] تم خصم︙{true*react_price}',reply_markup=bk)
    bot.delete_message(chat_id=message.from_user.id, message_id=prog.message_id)
    user_id = message.from_user.id
    code = int(db.get(f"po_{user_id}")) if db.exists(f"po_{user_id}") else 0
    daily_count = code + int(true*react_price)
    db.set(f"po_{user_id}", int(daily_count))
    return
def get_positive_url(message, amount):
    maintenance_mode = db.get("maintenance_mode") if db.exists("maintenance_mode") else False
    if maintenance_mode == True:
        bot.reply_to(message, "البوت قيد الصيانة والتطوير حاليًا ⚙️")
        return False
    if message.text == "/start":
        start_message(message)
        return
    admins = db.get('admins')
    url = message.text
    if "/c/" in url:
        bot.reply_to(message,text=f'• عذرا لا يمكنك استخدام الخدمة في القنوات الخاصة')
        return
    if not checks(url):
        bot.reply_to(message,text=f'• رجاء ارسل الرابط بشكل صحيح')
        return
    pr = react_price * amount
    load_ = db.get('accounts')
    acc = db.get(f'user_{message.from_user.id}')
    typerr = 'تفاعلات ايجابي [👍,❤,🔥,😍,🤩]'
    v = bot.reply_to(message,text=f'• 📤] تم بدء طلبك بنجاح | تفاصيل طلبك\n\n• 🏷] النوع : {typerr}\n\n• 📎] الرابط : {url} \n\n• 🗳] الكمية : {amount}')
    tim = int(db.get(f"tim_{message.from_user.id}")) if db.exists(f"tim_{message.from_user.id}") else 0
    db.set(f"serv_{message.from_user.id}", True)
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr}\n• العدد : {amount} \n• الرابط : {url} \n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username} ')
    true, false = 0, 0
    nume = int(amount)
    prog = bot.send_message(chat_id=int(message.from_user.id), text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
    for y in load_:
        if true >= amount:
            break
        try:
            session = random.choice(load_)
            x = asyncio.run(positive(session, url, tim))
            load_.remove(session)
            if x == 'o':
                continue
            if x == True:
                true += 1
                nume -= 1
                bot.edit_message_text(chat_id=message.from_user.id, message_id=prog.message_id, text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
            else:
                false += 1
                bot.edit_message_text(chat_id=message.from_user.id, message_id=prog.message_id, text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
        except Exception as e:
            print(e)
            continue
    if true >= 1:
        for ix in range(true):
            acc['coins'] -= react_price
        db.set(f'user_{message.from_user.id}', acc)
    db.set(f"serv_{message.from_user.id}", False) 
    addord()
    user_id = message.from_user.id
    buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
    buys+=1
    db.set(f"user_{user_id}_buys", int(buys))
    bot.reply_to(message,text=f'• 📥] تم اكتمال طلبك بنجاح | تفاصيل عن طلبك :\n\n• 📦] العدد المطلوب︙{amount} \n\n• ✅] العدد المكتمل︙{true} \n• ❌] فشل محاولة ارسال : {false}\n\n• 📎] الرابط︙{url}\n• ➖] تم خصم︙{true*react_price}',reply_markup=bk)
    bot.delete_message(chat_id=message.from_user.id, message_id=prog.message_id)
    user_id = message.from_user.id
    code = int(db.get(f"po_{user_id}")) if db.exists(f"po_{user_id}") else 0
    daily_count = code + int(true*react_price)
    db.set(f"po_{user_id}", int(daily_count))
    return
def get_negative_url(message, amount):
    maintenance_mode = db.get("maintenance_mode") if db.exists("maintenance_mode") else False
    if maintenance_mode == True:
        bot.reply_to(message, "البوت قيد الصيانة والتطوير حاليًا ⚙️")
        return False
    if message.text == "/start":
        start_message(message)
        return
    admins = db.get('admins')
    url = message.text
    if "/c/" in url:
        bot.reply_to(message,text=f'• عذرا لا يمكنك استخدام الخدمة في القنوات الخاصة')
        return
    if not checks(url):
        bot.reply_to(message,text=f'• رجاء ارسل الرابط بشكل صحيح')
        return
    pr = react_price * amount
    load_ = db.get('accounts')
    acc = db.get(f'user_{message.from_user.id}')
    typerr = 'تفاعلات سلبي [👎,💩,🤮,🤬,🖕]'
    v = bot.reply_to(message,text=f'• 📤] تم بدء طلبك بنجاح | تفاصيل طلبك\n\n• 🏷] النوع : {typerr}\n\n• 📎] الرابط : {url} \n\n• 🗳] الكمية : {amount}')
    tim = int(db.get(f"tim_{message.from_user.id}")) if db.exists(f"tim_{message.from_user.id}") else 0
    db.set(f"serv_{message.from_user.id}", True)
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr}\n• العدد : {amount} \n• الرابط : {url} \n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username} ')
    true, false = 0, 0
    nume = int(amount)
    prog = bot.send_message(chat_id=int(message.from_user.id), text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
    for y in load_:
        if true >= amount:
            break
        try:
            session = random.choice(load_)
            x = asyncio.run(negative(session, url, tim))
            load_.remove(session)
            if x == 'o':
                continue
            if x == True:
                true += 1
                nume -= 1
                bot.edit_message_text(chat_id=message.from_user.id, message_id=prog.message_id, text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
            else:
                false += 1
                bot.edit_message_text(chat_id=message.from_user.id, message_id=prog.message_id, text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
        except Exception as e:
            print(e)
            continue
    if true >= 1:
        for ix in range(true):
            acc['coins'] -= react_price
        db.set(f'user_{message.from_user.id}', acc)
    db.set(f"serv_{message.from_user.id}", False)
    addord()
    user_id = message.from_user.id
    buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
    buys+=1
    db.set(f"user_{user_id}_buys", int(buys))
    bot.reply_to(message,text=f'• 📥] تم اكتمال طلبك بنجاح | تفاصيل عن طلبك :\n\n• 📦] العدد المطلوب︙{amount} \n\n• ✅] العدد المكتمل︙{true} \n• ❌] فشل محاولة ارسال : {false}\n\n• 📎] الرابط︙{url}\n• ➖] تم خصم︙{true*react_price}',reply_markup=bk)
    bot.delete_message(chat_id=message.from_user.id, message_id=prog.message_id)
    user_id = message.from_user.id
    code = int(db.get(f"po_{user_id}")) if db.exists(f"po_{user_id}") else 0
    daily_count = code + int(true*react_price)
    db.set(f"po_{user_id}", int(daily_count))
    return
def get_url_forward(message, amount):
    maintenance_mode = db.get("maintenance_mode") if db.exists("maintenance_mode") else False
    if maintenance_mode == True:
        bot.reply_to(message, "البوت قيد الصيانة والتطوير حاليًا ⚙️")
        return False
    if message.text == "/start":
        start_message(message)
        return
    admins = db.get('admins')
    url = message.text
    if "/c/" in url:
        bot.reply_to(message,text=f'• عذرا لا يمكنك استخدام الخدمة في القنوات الخاصة')
        return
    if not checks(url):
        bot.reply_to(message,text=f'• رجاء ارسل الرابط بشكل صحيح')
        return
    pr = forward_price * amount
    load_ = db.get('accounts')
    acc = db.get(f'user_{message.from_user.id}')
    typerr = 'توجيهات'
    v = bot.reply_to(message,text=f'• 📤] تم بدء طلبك بنجاح | تفاصيل طلبك\n\n• 🏷] النوع : {typerr}\n\n• 📎] الرابط : {url} \n\n• 🗳] الكمية : {amount}')
    tim = int(db.get(f"tim_{message.from_user.id}")) if db.exists(f"tim_{message.from_user.id}") else 0
    db.set(f"serv_{message.from_user.id}", True)
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr}\n• العدد : {amount} \n• الرابط : {url} \n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username} ')
    true, false = 0, 0
    nume = int(amount)
    prog = bot.send_message(chat_id=int(message.from_user.id), text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
    for y in load_:
        if true >= amount:
            break
        try:
            session = random.choice(load_)
            x = asyncio.run(forward(session, url, tim))
            load_.remove(session)
            if x == 'o':
                continue
            if x == True:
                true += 1
                nume -= 1
                bot.edit_message_text(chat_id=message.from_user.id, message_id=prog.message_id, text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
            else:
                false += 1
                bot.edit_message_text(chat_id=message.from_user.id, message_id=prog.message_id, text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
        except Exception as e:
            print(e)
            continue
    if true >= 1:
        for ix in range(true):
            acc['coins'] -= react_price
        db.set(f'user_{message.from_user.id}', acc)
    db.set(f"serv_{message.from_user.id}", False)
    addord()
    user_id = message.from_user.id
    buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
    buys+=1
    db.set(f"user_{user_id}_buys", int(buys))
    bot.reply_to(message,text=f'• 📥] تم اكتمال طلبك بنجاح | تفاصيل عن طلبك :\n\n• 📦] العدد المطلوب︙{amount} \n\n• ✅] العدد المكتمل︙{true} \n• ❌] فشل محاولة ارسال : {false}\n\n• 📎] الرابط︙{url}\n• ➖] تم خصم︙{true*react_price}',reply_markup=bk)
    bot.delete_message(chat_id=message.from_user.id, message_id=prog.message_id)
    user_id = message.from_user.id
    code = int(db.get(f"po_{user_id}")) if db.exists(f"po_{user_id}") else 0
    daily_count = code + int(true*react_price)
    db.set(f"po_{user_id}", int(daily_count))
    return
def get_url_poll(message, amount):
    maintenance_mode = db.get("maintenance_mode") if db.exists("maintenance_mode") else False
    if maintenance_mode == True:
        bot.reply_to(message, "البوت قيد الصيانة والتطوير حاليًا ⚙️")
        return False
    if message.text == "/start":
        start_message(message)
        return
    admins = db.get('admins')
    url = message.text
    if "/c/" in url:
        bot.reply_to(message,text=f'• عذرا لا يمكنك استخدام الخدمة في القنوات الخاصة')
        return
    x = checks(url)
    if x:
        channel, msg_id = x
    if not checks(url):
        bot.reply_to(message,text='• رجاء ارسل الرابط بشكل صحيح')
        return
    try:
        mm = "• ارسل الان تسلسل الإجابة في الاستفتاء\n\n• يجب ان يتراوح بين 0 : 9\n• علما بان اول اختيار يكون تسلسلة 0"
        x = bot.reply_to(message, mm, parse_mode='HTML')
        bot.register_next_step_handler(x, start_poll, amount, url)
    except Exception as e:
        bot.reply_to(message, "الرسالة ممسوحة أو القناة المجموعة غير صحيحة.")
        print(e)
        return
def start_poll(message, amount, url):
    maintenance_mode = db.get("maintenance_mode") if db.exists("maintenance_mode") else False
    if maintenance_mode == True:
        bot.reply_to(message, "البوت قيد الصيانة والتطوير حاليًا ⚙️")
        return False
    if message.text == "/start":
        start_message(message)
        return
    num = message.text
    if not checks(url):
        bot.reply_to(message,text=f'• رجاء ارسل الرابط بشكل صحيح')
        return
    pr = poll_price * amount
    load_ = db.get('accounts')
    acc = db.get(f'user_{message.from_user.id}')
    typerr = 'استفتاء'
    v = bot.reply_to(message,text=f'• 📤] تم بدء طلبك بنجاح | تفاصيل طلبك\n\n\n\n• 🏷] النوع : {typerr}\n\n• 📎] الرابط : {url}\n• 📊] الاختيار : {num}\n\n• 🗳] الكمية : {amount}')
    db.set(f"serv_{message.from_user.id}", True)
    tim = int(db.get(f"tim_{message.from_user.id}")) if db.exists(f"tim_{message.from_user.id}") else 0
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr}\n• العدد : {amount} \n• الرابط : {url} \n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username} ')
    true, false = 0, 0
    nume = int(amount)
    prog = bot.send_message(chat_id=int(message.from_user.id), text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
    for y in load_:
        if true >= amount:
            break
        try:
            session = random.choice(load_)
            x = asyncio.run(poll(session, url, int(num), tim))
            load_.remove(session)
            if x == 'o':
                continue
            if x == True:
                true += 1
                nume -= 1
                bot.edit_message_text(chat_id=message.from_user.id, message_id=prog.message_id, text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
            else:
                false += 1
                bot.edit_message_text(chat_id=message.from_user.id, message_id=prog.message_id, text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
        except Exception as e:
            print(e)
            continue
    if true >= 1:
        for ix in range(true):
            acc['coins'] -= poll_price
        db.set(f'user_{message.from_user.id}', acc)
    db.set(f"serv_{message.from_user.id}", False)
    addord()
    user_id = message.from_user.id
    buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
    buys+=1
    db.set(f"user_{user_id}_buys", int(buys))
    bot.reply_to(message,text=f'• 📥] تم اكتمال طلبك بنجاح | تفاصيل عن طلبك :\n\n• 📦] العدد المطلوب︙{amount} \n\n• ✅] العدد المكتمل︙{true} \n• ❌] فشل محاولة ارسال : {false}\n\n• 📎] الرابط︙{url}\n• ➖] تم خصم︙{true*poll_price}',reply_markup=bk)
    bot.delete_message(chat_id=message.from_user.id, message_id=prog.message_id)
    user_id = message.from_user.id
    code = int(db.get(f"po_{user_id}")) if db.exists(f"po_{user_id}") else 0
    daily_count = code + int(true*poll_price)
    db.set(f"po_{user_id}", int(daily_count))
    return
def get_view_url(message, amount):
    maintenance_mode = db.get("maintenance_mode") if db.exists("maintenance_mode") else False
    if maintenance_mode == True:
        bot.reply_to(message, "البوت قيد الصيانة والتطوير حاليًا ⚙️")
        return False
    if message.text == "/start":
        start_message(message)
        return
    admins = db.get('admins')
    url = message.text
    if "/c/" in url:
        bot.reply_to(message,text=f'• عذرا لا يمكنك استخدام الخدمة في القنوات الخاصة')
        return
    if not checks(url):
        bot.reply_to(message,text=f'• رجاء ارسل الرابط بشكل صحيح')
        return
    pr = view_price * amount
    load_ = db.get('accounts')
    acc = db.get(f'user_{message.from_user.id}')
    typerr = 'مشاهدات'
    v = bot.reply_to(message,text=f'• 📤] تم بدء طلبك بنجاح | تفاصيل طلبك\n\n• 🏷] النوع : {typerr}\n\n• 📎] الرابط : {url} \n\n• 🗳] الكمية : {amount}')
    tim = int(db.get(f"tim_{message.from_user.id}")) if db.exists(f"tim_{message.from_user.id}") else 0
    db.set(f"serv_{message.from_user.id}", True)
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr}\n• العدد : {amount} \n• الرابط : {url} \n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username} ')
    true, false = 0, 0
    nume = int(amount)
    prog = bot.send_message(chat_id=int(message.from_user.id), text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
    for y in load_:
        if true >= amount:
            break
        try:
            session = random.choice(load_)
            x = asyncio.run(view(session, url, tim))
            load_.remove(session)
            if x == 'o':
                continue
            if x == True:
                true += 1
                nume -= 1
                bot.edit_message_text(chat_id=message.from_user.id, message_id=prog.message_id, text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
            else:
                false += 1
                bot.edit_message_text(chat_id=message.from_user.id, message_id=prog.message_id, text=f'• ⏪] جارى تتبع طلبك︙\n\n• ✅] ارسال ناجح︙{true}\n• ❌] فشل محاولة ارسال︙{false}\n\n• 📬] متبقي علي اكتمال طلبك︙{nume}\n• 📎] يتم الارسال الي : {url}')
        except Exception as e:
            print(e)
            continue
    if true >= 1:
        for ix in range(true):
            acc['coins'] -= view_price
        db.set(f'user_{message.from_user.id}', acc)
    db.set(f"serv_{message.from_user.id}", False)
    addord()
    user_id = message.from_user.id
    buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
    buys+=1
    db.set(f"user_{user_id}_buys", int(buys))
    bot.reply_to(message,text=f'• 📥] تم اكتمال طلبك بنجاح | تفاصيل عن طلبك :\n\n• 📦] العدد المطلوب︙{amount} \n\n• ✅] العدد المكتمل︙{true} \n• ❌] فشل محاولة ارسال : {false}\n\n• 📎] الرابط︙{url}\n• ➖] تم خصم︙{true*view_price}',reply_markup=bk)
    bot.delete_message(chat_id=message.from_user.id, message_id=prog.message_id)
    return
def check_user(id):
    if not db.get(f'user_{id}'):
        return False
    return True

def set_user(id, data):
    db.set(f'user_{id}', data)
    return True

def get(id):
    return db.get(f'user_{id}')

def delete(id):
    return db.delete(f'user_{id}')

def trend():
    k = db.keys("user_%")
    users = []
    for i in k:
        try:
            g = db.get(i[0])
            d = g["id"]
            users.append(g)
        except:
            continue
    data = users
    sorted_users = sorted(data, key=lambda x: len(x["users"]), reverse=True)
    result_string = "•<strong> المستخدمين الأكثر مشاركة لرابط الدعوة :</strong>\n\n"
    for index, user in enumerate(sorted_users[:5]):
        us = bot.get_chat(user['id'])
        hh = us.username
        if hh is None:
            hh = "لا يوجد معرف"
        else:
            pp = f"@{hh}"
        if index == 0:
            result_string += f"🏆: <strong>({len(user['users'])})</strong> > {pp}\n"
        elif index == 1:
            result_string += f"🥈: <strong>({len(user['users'])})</strong> > {pp}\n"
        elif index == 2:
            result_string += f"🥉: <strong>({len(user['users'])})</strong> > {pp}\n"
        elif index == 3:
            result_string += f"🎗: <strong>({len(user['users'])})</strong> > {pp}\n"
        else:
            result_string += f"🎗: <strong>({len(user['users'])})</strong> > {pp}\n"
    return result_string
    
def coinsn():
    k = db.keys("user_%")
    users = []
    for i in k:
        try:
            g = db.get(i[0])
            d = g["id"]
            users.append(g)
        except:
            continue
    data = users
    sorted_users = sorted(data, key=lambda x: x["coins"], reverse=True)
    result_strin = "•<strong> المستخدمين الأكثر نقاطاً في البوت :</strong>\n\n"
    for index, user in enumerate(sorted_users[:5]):
        us = bot.get_chat(user['id'])
        hh = us.username
        if hh is None:
            hh = "لا يوجد معرف"
        elif hh == 'PWVWP':
            pp = f"@{hh} > <strong>(المطور)</strong>"
        else:
            pp = f"@{hh}"
        if index == 0:
            result_strin += f"🏆: <strong>({user['coins']})</strong> > {pp}\n"
        elif index == 1:
            result_strin += f"🥈: <strong>({user['coins']})</strong> > {pp}\n"
        elif index == 2:
            result_strin += f"🥉: <strong>({user['coins']})</strong> > {pp}\n"
        elif index == 3:
            result_strin += f"🎗: <strong>({user['coins']})</strong> > {pp}\n"
        else:
            result_strin += f"🎗: <strong>({user['coins']})</strong> > {pp}\n"
    return result_strin
def detect(text):
    pattern = r'https:\/\/t\.me\/\+[a-zA-Z0-9]+'
    match = re.search(pattern, text)
    return match is not None
def casting(message):
    if message.text == "/start":
        start_message(message)
        return
    admins = db.get('admins')
    idm = message.message_id
    d = db.keys('user_%')
    good = 0
    bad = 0
    bot.reply_to(message, f'• جاري الاذاعة الي مستخدمين البوت الخاص بك ')
    for user in d:
        try:
            id = db.get(user[0])['id']
            bot.copy_message(chat_id=id, from_chat_id=message.from_user.id, message_id=idm)
            good+=1
        except:
            bad+=1
            continue
    bot.reply_to(message, f'• اكتملت الاذاعة بنجاح ✅\n• تم ارسال الى : {good}\n• لم يتم ارسال الي : {bad} ')
    return
def adminss(message, type):
    if message.text == "/start":
        start_message(message)
        return
    admins = db.get('admins')
    if type == 'add':
        try:
            id = int(message.text)
        except:
            bot.reply_to(message, f'• ارسل الايدي بشكل صحيح')
            return
        d = db.get('admins')
        if id in d:
            bot.reply_to(message, f'• هذا العضو ادمن بالفعل')
            return
        else:
            d.append(id)
            db.set('admins', d)
            bot.reply_to(message, f'• تم اضافته بنجاح ✅')
            return
    if type == 'delete':
        try:
            id = int(message.text)
        except:
            bot.reply_to(message, f'• ارسل الايدي بشكل صحيح')
            return
        d = db.get('admins')
        if id not in d:
            bot.reply_to(message, f'• هذا العضو ليس من الادمنية بالبوت')
            return
        else:
            d.remove(id)
            db.set('admins', d)
            bot.reply_to(message, f'• تم اذالة العضو من الادمنية بنجاح ✅')
            return
    if type == 'change_price':
        lisst = ["member_price","view_price","react_price","vote_price","spam_price"]
        serv = message.text
        nn = db.get(message.text) if db.exists(message.text) else "لا يوجد سعر لهذا المتجر"
        x = bot.reply_to(message, f'• السعر الحالي لهذا المنتج : {nn}\n\n• ارسل السعر الجديد !')
        bot.register_next_step_handler(x, change_price, serv)
def change_price(message, nn):
    try:
        new = int(message.text)
    except:
        bot.reply_to(message, f'ارسل رقم فقط')
        return
    db.set(f"{nn}", int(new))
    bot.reply_to(message, f'• تم تغيير سعر الخدمة : {nn}\n\n• الي : {new}')
def banned(message, type):
    admins = db.get('admins')
    if type == 'ban':
        try:
            id = int(message.text)
        except:
            bot.reply_to(message, f'ارسل الايدي بشكل صحيح')
            return
        d = db.get('badguys')
        if id in d:
            bot.reply_to(message, f'• هذا العضو محظور من قبل ')
            return
        else:
            d.append(id)
            db.set('badguys', d)
            bot.reply_to(message, f'• تم حظر العضو من استخدام البوت')
            return
    if type == 'unban':
        try:
            id = int(message.text)
        except:
            bot.reply_to(message, f'• ارسل الايدي بشكل صحيح')
            return
        d = db.get('badguys')
        if id not in d:
            bot.reply_to(message, f'• هذا العضو غير محظور ')
            return
        else:
            d.remove(id)
            db.set('badguys', d)
            bot.reply_to(message, f'• تم الغاء حظر العضو بنجاح ✅')
            return
def get_info(message):
    if message.text == "/start":
        start_message(message)
        return
    id = message.text
    try:
        id = int(id)
    except:
        bot.reply_to(message, f'• ارسل الايدي بشكل صحيح رجاء')
        return
    d = db.get(f'user_{id}')
    if not d:
        bot.reply_to(message, f'• هذا العضو غير موجود')
        return
    # {'id': user_id, 'users': [], 'coins': 0, 'paid': False}
    id, coins, users = d['id'], d['coins'], len(d['users'])
    bot.reply_to(message, f'• ايديه : {id}.\n• نقاطه: {coins} نقطة \n• عدد مشاركته لرابط الدعوة{users}')
    return
def send(message):
    maintenance_mode = db.get("maintenance_mode") if db.exists("maintenance_mode") else False
    if maintenance_mode == True:
        bot.reply_to(message, "البوت قيد الصيانة والتطوير حاليًا ⚙️")
        return False
    if message.text == "/start":
        start_message(message)
        return
    id = message.text
    try:
        id = int(message.text)
    except:
        bot.reply_to(message, f'• ارسل الايدي بشكل صحيح ')
        return
    if not db.exists(f'user_{id}'):
        bot.reply_to(message, f'• هذا العضو غير موجود في البوت ❌')
        return
    if int(message.text) == int(message.from_user.id):
        bot.reply_to(message, f'• عذرا لا يمكنك تحويل نقاط لنفسك ❌')
        return
    x2 = bot.reply_to(message, f'• ارسل الان عدد النقاط التي تريد تحويلها لـ {id}')
    bot.register_next_step_handler(x2, get_amount_send, id)
def send_link(message):
    try:
        amount = int(message.text)
    except:
        te = bot.reply_to(message, f'• الكمية يجب ان تكون عدد فقط ')
        return
    to_user = db.get(f'user_{id}')
    from_user = db.get(f'user_{message.from_user.id}')
    if amount < 100:
        bot.reply_to(message, f'• عذرا، الحد الادني لتحويل النقاط هو 100')
        return
    all = int(amount) + 20
    if from_user['coins'] < all:
        bot.reply_to(message, f'• نقاطك غير كافية لتحويل هذا المبلغ ❌')
        return
    characters = "12345678906380abCcdNksIoKlwclqnOveoMmVOXyz"
    random_string = ''.join(random.choice(characters) for _ in range(33))    
    bot.reply_to(message, f"*تم خصم {all} من نقاطك*\n\n*- عموله التحويل : 20 *\n\n*• رابط تحويل النقاط* : https://t.me/ABOSAITI_BOT?start={random_string}\n\n• ارسل الرابط للشخص المراد تحويل النقاط له \n\n*• الرابط صالح مدى الحياة *\n\n*- يمكنك الضغط على زر تعطيل الرابط لكي تقوم بسترداد نقاطك او قم بدخول على الرابط لاسترداد نقاطك*",parse_mode="Markdown",reply_markup=mk([[btn(text='• تعطيل الرابط •',callback_data='dellink')]]))
    db.set("user_trans", int(amount))
    db.set("user_tran", str(random_string))
    from_user['coins'] = int(from_user['coins']) - int(all)
    db.set(f"user_{message.from_user.id}", from_user)
    db.set("user_iddd", int(f"{message.from_user.id}"))
def get_amount_send(message, id):
    maintenance_mode = db.get("maintenance_mode") if db.exists("maintenance_mode") else False
    if maintenance_mode == True:
        bot.reply_to(message, "البوت قيد الصيانة والتطوير حاليًا ⚙️")
        return False
    if message.text == "/start":
        start_message(message)
        return
    amount = message.text
    try:
        amount = int(message.text)
    except:
        te = bot.reply_to(message, f'• الكمية يجب ان تكون عدد فقط ')
        return
    to_user = db.get(f'user_{id}')
    from_user = db.get(f'user_{message.from_user.id}')
    if amount < 100:
        bot.reply_to(message, f'• عذرا، الحد الادني لتحويل النقاط هو 100')
        return
    all = int(amount) + 20
    if from_user['coins'] < all:
        bot.reply_to(message, f'• نقاطك غير كافية لتحويل هذا المبلغ \n• تحتاج الي {amount-from_user["coins"]} نقطة')
        return
    amm = int(amount) + 20
    from_user['coins']-=amm
    db.set(f'user_{message.from_user.id}', from_user)
    to_user['coins']+=amount
    db.set(f'user_{id}', to_user)
    typ = float(db.get(f"typ_{from_user}")) if db.exists(f"typ_{from_user}") else 0.0
    ftt = typ + 0.1
    db.set(f"typ_{from_user}", float(ftt))
    try:
        bot.send_message(chat_id=id, text=f"• [👤] تم استلام {amount} من نقاط\n\n- من الشخص : {message.from_user.id}\n- نقاطك القديمة : {to_user['coins']}\n- نقاطك الان : {to_user['coins']+amount}")
    except: pass
    bot.send_message(chat_id=int(sudo), text=f'• تمت عملية تحويل <strong>{amount}</strong> نقطة ✅\n\n•  من : <a href="tg://user?id={message.from_user.id}">{message.from_user.id}</a>\n\n• الي : <a href="tg://user?id={id}">{id}</a>')
    bot.reply_to(message, f"• [👤] تم ارسال {amount} من نقاط\n\n- الى الشخص : {id}\n- نقاطك القديمة : {from_user['coins']+amount}\n- نقاطك الان : {from_user['coins']}")
    user_id = message.from_user.id
    trans = int(db.get(f"user_{user_id}_trans")) if db.exists(f"user_{user_id}_trans") else 0
    count_trans = trans + 1
    db.set(f"user_{user_id}_trans", int(count_trans))
    user_id = message.from_user.id
    code = int(db.get(f"po_{user_id}")) if db.exists(f"po_{user_id}") else 0
    daily_count = code + int(amount)
    db.set(f"po_{user_id}", int(daily_count))
    return
def addpoints(message):
    if message.text == "/start":
        start_message(message)
        return
    id = message.text
    try:
        id = int(message.text)
    except:
        bot.reply_to(message, f'• ارسل الايدي بشكل صحيح رجاء')
        return
    x = bot.reply_to(message, '• ارسل الان الكمية :')
    bot.register_next_step_handler(x, addpoints_final, id)
def addpoints_final(message, id):
    if message.text == "/start":
        start_message(message)
        return
    amount = message.text
    try:
        amount = int(message.text)
    except:
        bot.reply_to(message, f'يجب ان تكون الكمية ارقام فقط')
        return
    b = db.get(f'user_{id}')
    b['coins']+=amount
    db.set(f'user_{id}', b)
    bot.reply_to(message, f'تم بنجاح نقاطه الان : {b["coins"]} ')
    return
def lespoints(message):
    if message.text == "/start":
        start_message(message)
        return
    id = message.text
    try:
        id = int(message.text)
    except:
        bot.reply_to(message, f'• ارسل الايدي بشكل صحيح رجاء')
        return
    x = bot.reply_to(message, '• ارسل الان الكمية :')
    bot.register_next_step_handler(x, lespoints_final, id)
def lespoints_final(message, id):
    if message.text == "/start":
        start_message(message)
        return
    amount = message.text
    try:
        amount = int(message.text)
    except:
        bot.reply_to(message, f'يجب ان تكون الكمية ارقام فقط')
        return
    b = db.get(f'user_{id}')
    b['coins']-=amount
    db.set(f'user_{id}', b)
    bot.reply_to(message, f'تم بنجاح نقاطه الان : {b["coins"]} ')
def setfo(message):
    if message.text == "/start":
        start_message(message)
        return
    users = message.text.replace('https://t.me/', '').replace('@',  '').split(' ')
    print(users)
    db.set('force', users)
    bot.reply_to(message, 'تمت بنجاح')
    return
def vipp(message, type):
    if message.text == "/start":
        start_message(message)
        return
    if type == 'add':
        try:
            id = int(message.text)
        except:
            bot.reply_to(message, f'• ارسل الايدي بشكل صحيح')
            return
        d = db.get(f"user_{id}")
        if d is None:
            bot.reply_to(message, f'• العضو غير موجود في البوت')
            return
        d['premium'] = True
        db.set(f'user_{id}', d)
        x = bot.reply_to(message, f'• ارسل الان عدد الايام المتاحة للعضو ')
        bot.register_next_step_handler(x, addviptime, id)
        return
    if type == 'les':
        try:
            id = int(message.text)
        except:
            bot.reply_to(message, f'• ارسل الايدي بشكل صحيح')
            return
        d = db.get(f"user_{id}")
        if d is None:
            bot.reply_to(message, f'• العضو غير موجود في البوت')
            return
        d['premium'] = False
        db.set(f'user_{id}', d)
        bot.reply_to(message, f"تم انهاء الاشتراك الـ ᴠɪᴘ للمستخدم {id}")
def addviptime(message,id):
    try:
        timenv = int(message.text)
    except:
        bot.reply_to(message, f"ارسل رقم فقط")
        return
    d = db.get(f"user_{id}")
    d['premium'] = True
    db.set(f'user_{id}', d)
    users = {}
    noww = time.time()
    users['vip'] = noww
    db.set(f'vip_{id}', users)
    db.set(f"vipp_{id}_time", int(timenv))
    us = bot.get_chat(id)
    if us.username is None:
        user = "لا يوجد"
    else:
        user = "@" + us.username
    name = us.first_name
    today = datetime.date.today()
    end_date = today + datetime.timedelta(days=int(timenv))
    now = datetime.datetime.now()
    HM = now.strftime("%p")
    if str(HM) == str("PM"):
        how = "مساءً"
    else:
        how = "صباحاً"
    hour = now.hour
    minutes = now.minute
    seconds = now.second
    d = int(timenv)
    h = int(timenv) * 24
    m = int(timenv) * 24 * 60
    s = int(timenv) * 24 * 60 * 60
    reb2 = f"""*• تهانينا ، تم تفعيل ᴠɪᴘ لحسابك في البوت ✅*\n\n_• مدة الاشتراك  ⏱️:_\n\n- المدة بالايام : {d}\n- المدة بالساعات : {h}\n- المدة بالدقائق : {m}\n- المدة بالثواني : {s}\n\n*• وقت انتهاء اشتراكك :*\n\n- يوم : {end_date}\n- الساعة : {hour} {how}\n- الدقيقة : {minutes}"""
    reb = f"""*• تمت عملية تفعيل ᴠɪᴘ جديده 🔥*
`{id}`
*• معلومات الاشتراك والمدة ⏱:*

_• وقت التفعيل :_

- اليوم : {today}
- الساعة : {hour} {how}
- الدقيقة : {minutes}

_• مدة الاشتراك  :_

- المدة بالايام : {d}
- المدة بالساعات : {h}
- المدة بالدقائق : {m}
- المدة بالثواني : {s}

*• وقت انتهاء الاشتراك :*

_• سينتهي اشتراك العضو في :_

- يوم : {end_date}
- الساعة : {hour} {how}
- الدقيقة : {minutes}"""
    bot.send_message(chat_id=int(sudo), text=reb, parse_mode="Markdown")
    bot.send_message(chat_id=int(id), text=reb2, parse_mode="Markdown")
def account(call):
    maintenance_mode = db.get("maintenance_mode") if db.exists("maintenance_mode") else False
    if maintenance_mode == True:
        bot.answer_callback_query(call.id, text="البوت قيد الصيانة والتطوير حالياً ⚙️",show_alert=True)
        return False
    cid, data, mid = call.from_user.id, call.data, call.message.id
    e = 5
    how = ""
    if e == 5:
        x = giiiift(cid)
        if x is not None:
            duration = datetime.timedelta(seconds=x)
            noww = datetime.datetime.now()
            target_datetime = noww + duration
            remaining_time = target_datetime - noww
            hours = remaining_time.seconds // 3600
            minutes = (remaining_time.seconds % 3600) // 60
            seconds = remaining_time.seconds % 60
            if hours > 0:
                how = f"{hours} ساعة"
            elif minutes > 0:
                how = f"{minutes} دقيقة"
            else:
                how = f"{seconds} ثانية"
        else:
            how = "يمكنك المطالبة بها 🎁"
        acc = get(cid)
        user_id = call.from_user.id
        coins, users = acc['coins'], len(get(cid)['users'])
        info = db.get(f"user_{call.from_user.id}")
        daily_count = int(db.get(f"user_{user_id}_daily_count")) if db.exists(f"user_{user_id}_daily_count") else 0
        daily_gift = int(db.get("daily_gift")) if db.exists("daily_gift") else 30
        all_gift = daily_count * daily_gift
        buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
        trans = int(db.get(f"user_{user_id}_trans")) if db.exists(f"user_{user_id}_trans") else 0
        prem = 'Premium' if info['premium'] == True else 'Free'
        codes = int(db.get(f"cd_{user_id}")) if db.exists(f"cd_{user_id}") else 0
        po = int(db.get(f"po_{user_id}")) if db.exists(f"po_{user_id}") else 0
        textt = f'''
• 🗃️] معلومات حسابك 

• ❇️] عدد نقاط حسابك : {coins}
• ❇️] النقاط التي استخدمتها : {po}

• 🌀] عدد عمليات الاحاله التي قمت بها : {users}
• 👤] نوع اشتراكك داخل البوت : <code>{prem}</code>
• 📮] عدد الطلبات التي طلبتها : {buys}
• ♻️] عدد التحويلات التي قمت بها : {trans}

• ❇️] عدد النقاط اللي جمعتها من الهدايا اليومية : {all_gift}
• 💳] عدد اكواد الهدايا التي استخدمتها : {codes}
• 🎁] عدد الهدايا اليومية التي جمعتها : {daily_count}
• 🎁] متبقي علي الهدية : {how}'''
        keys = mk(row_width=2)
        btn1 = btn('الهدية اليومية 🎁', callback_data='dailygift')
        btn3 = btn('رابط الدعوة 🌀',callback_data='share_link')
        keys.add(btn3, btn1)
        keys.add(btn('رجوع ↪️', callback_data='back'))
        bot.edit_message_text(text=textt,chat_id=cid,message_id=mid,reply_markup=keys)
        return
def use_link(message,us):
    join_user = message.from_user.id
    count_coins = db.get("user_trans")
    rand = db.get("user_tran")
    user_from = db.get("user_iddd")
    if str(rand) == str(us):
        joo = db.get(f"user_{join_user}")
        joo['coins'] = int(joo['coins']) + int(count_coins)
        db.set(f"user_{message.from_user.id}", joo)
        db.delete('user_tran')
        bot.reply_to(message, f"• تم اضافة *{count_coins}* نقاط الى حسابك ✅\n• بواسطه رابط التحويل من : [{user_from}](tg://user?id={user_from})\n\n• اصبحت نقاطك : {joo['coins']} ",parse_mode="Markdown",reply_markup=bk)
        bot.send_message(chat_id=int(user_from), text=f"• تم تحويل ✅ : {count_coins} نقاط \n\n- الى المستخدم : [{join_user}](tg://user?id={join_user})\n\n- عدد نقاطه الان : {joo['coins']}",parse_mode="Markdown",reply_markup=bk)
        bot.send_message(chat_id=int(sudo), text=f"*• عزيزي الادمن* : \n\n*• تمت عملية تحويل نقاط جديده ♻️*\n• المبلغ : {count_coins}\n• الي : [{message.from_user.first_name}](tg://user?id={join_user})\n• ايديه : [{join_user}](tg://user?id={join_user})\n نقاطه الان : `{joo['coins']}`\n\n• من : [{user_from}](tg://user?id={user_from})",parse_mode="Markdown")
        trans = int(db.get(f"user_{user_from}_trans")) if db.exists(f"user_{user_from}_trans") else 0
        count_trans = trans + 1
        db.set(f"user_{user_from}_trans", int(count_trans))
        db.delete('user_iddd')
        db.set(f"user_trans", 0)
        user_id = message.from_user.id
        user_from = db.get("user_iddd")
        code = int(db.get(f"po_{user_from}")) if db.exists(f"po_{user_from}") else 0
        daily_count = code + int(count_coins)
        db.set(f"po_{user_from}", int(daily_count))
        typ = float(db.get(f"typ_{from_user}")) if db.exists(f"typ_{from_user}") else 0.0
        ftt = typ + 0.1
        db.set(f"typ_{from_user}", float(ftt))
        return
    else:
        bot.reply_to(message, f"*• 📎] الرابط غير صحيح او انتهت صلاحية الرابط ❌*",parse_mode="Markdown",reply_markup=bk)

def get_url_click_force(message):
    xx = checks(message.text)
    if not xx:
        bot.reply_to(message, "• ارسل رابط المنشور بشكل صحيح.")
        return
    load_ = db.get("accounts")
    session = random.choice(load_)
    o = asyncio.run(get_msgs(session['s'], message.text))
    print(o)
    if not o:
        bot.reply_to(message, "• ارسل رابط المنشور بشكل صحيح.")
        return
    res = isinstance(o, list)
    if not res:
        bot.reply_to(message, "• ارسل رابط المنشور بشكل صحيح.")
        return
    keys = mk()
    for text in o:
        btn1 = btn(text=text, callback_data=f"V-{text}-{message.text}")
        keys.add(btn1)
    keys.add(btn('رجوع ', callback_data='back'))
    bot.reply_to(message, "اختر الزر الذي تريد رشقه", reply_markup=keys)
    
def get_amount_click_force(message, text, url):
    try:
        amount = int(message.text)
    except:
        bot.reply_to(message, '• رجاء ارسل رقم فقط ، اعد المحاولة مره اخري')
        return
    if amount < 1:
        bot.reply_to(message,'• رجاء ارسل عدد اكبر من <strong>0</strong> ..',reply_markup=bk)
        return
    if amount > 2000:
        bot.reply_to(message,'رجاء ارسل عدد اقل من <strong>2000</strong> ..',reply_markup=bk)
        return
    pr = vote_price * amount
    acc = db.get(f'user_{message.from_user.id}')
    if int(pr) > acc['coins']:
        bot.reply_to(message, f'• نقاطك غير كافية ، تحتاج الي  <strong>{pr-amount}</strong> نقطة')
        return
    x = bot.reply_to(message,f'• الكمية : <strong>{amount}</strong>\n\n• الان ارسل وقت الإنتضار بين الرشق (بالثواني) \n\n• ارسل 0 اذا كنت تريده فوري\n• يجب ان لايزيد عن 200')
    bot.register_next_step_handler(x, get_time_click_force, amount, text, url)
    return

def get_time_click_force(message, amount, text, url):
    try:
        time = int(message.text)
    except:
        x = bot.reply_to(message,text=f'• رجاء ارسل الوقت بشكل صحيح')
        return
    if time <0:
        x = bot.reply_to(message,text=f'• رجاء ارسل وقت الرشق بين 0 و 200')
        return
    if time >200:
        x = bot.reply_to(message,text=f'• رجاء ارسل وقت الرشق بين 0 و 200')
        return
    pr = vote_price * amount
    load_ = db.get('accounts')
    acc = db.get(f'user_{message.from_user.id}')
    typerr = 'تصويت'
    db.set(f"serv_{message.from_user.id}", True)
    tim = int(db.get(f"tim_{message.from_user.id}")) if db.exists(f"tim_{message.from_user.id}") else 0
    bot.send_message(chat_id=int(sudo), text=f'• قام شخص بطلب من البوت\n• النوع : {typerr}\n• العدد : {amount} \n• الرابط : {url} \n• ايديه : {message.from_user.id} \n• يوزره : @{message.from_user.username}\n• الوقت بين التصويت : {time} ')
    true, false = 0, 0
    tmmmm = 0
    nume = int(amount)
    prog = bot.send_message(chat_id=int(message.from_user.id), text=f'• تم بدء طلبك بنجاح ✅\n\n• العدد : {amount}\n• يتم الارسال الي : {url}')
    for y in load_:
        if true >= amount:
            break
        try:
            x = asyncio.run(click_force(y['s'], text, url, time))
            if x == 'o':
                continue
            if x == True:
                true += 1
                nume -= 1
            else:
                false += 1
        except Exception as e:
            print(e)
            continue
    if true >= 1:
        acc = db.get(f'user_{message.from_user.id}')
        for ix in range(true):
            acc['coins'] -= vote_price
        db.set(f'user_{message.from_user.id}', acc)
    addord()
    user_id = message.from_user.id
    buys = int(db.get(f"user_{user_id}_buys")) if db.exists(f"user_{user_id}_buys") else 0
    buys+=1
    db.set(f"user_{user_id}_buys", int(buys))
    bot.reply_to(message,text=f'• تم اكتمال طلبك بنجاح ✅:\n• تم ارسال : {true}\n• لم يتم ارسال : {false} \n• تم خصم : {amount*vote_price}',reply_markup=bk)
    db.set(f"serv_{message.from_user.id}", False)
    return
    
    
try:
    bot.infinity_polling()
    bot2.infinity_polling()
except:
    pass
import csv

import telebot
from telebot import types

import config
import spravochnik

# import points
bot = telebot.TeleBot(config.TOKEN)


# переменные

# Вывод приветствия
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn_nachat = types.KeyboardButton("🔎 Найти пункты приема отходов")
    btn_spravka = types.KeyboardButton("📒 Справочник")
    markup.add(btn_nachat, btn_spravka)
    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\n\nЯ - <b>{1.first_name}</b>, созданный, чтобы помогать сортировать и утилизировать отходы жителям Санкт-Петербурга".format(
                         message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)
    bot.send_message(message.chat.id, text="Выберите, что хотите сделать")


# Вывод кнопок меню
@bot.message_handler(content_types=['text'])
def menu(message):
    if (message.text == "🔎 Найти пункты приема отходов"):
        markup = types.InlineKeyboardMarkup(row_width=True)
        btn_plastik = types.InlineKeyboardButton("🧴 Пластик", callback_data="plastik")
        btn_steklo = types.InlineKeyboardButton("🍸 Стекло", callback_data="steklo")
        btn_paper = types.InlineKeyboardButton("📜 Бумага", callback_data="paper")
        btn_metall = types.InlineKeyboardButton("⚙️ Металл", callback_data="metall")
        btn_batery = types.InlineKeyboardButton("🔋 Батареи и аккумуляторы", callback_data="batery")
        markup.add(btn_plastik, btn_steklo, btn_paper, btn_metall, btn_batery)
        bot.send_message(message.chat.id, text="Выберите тип материала", reply_markup=markup)
    elif (message.text == "📒 Справочник"):
        markup = types.InlineKeyboardMarkup(row_width=True)
        btn_plastik_spravka = types.InlineKeyboardButton("🧴 Пластик", callback_data="plastik_spravka")
        btn_steklo_spravka = types.InlineKeyboardButton("🍸 Стекло", callback_data="steklo_spravka")
        btn_paper_spravka = types.InlineKeyboardButton("📜 Бумага", callback_data="paper_spravka")
        btn_metall_spravka = types.InlineKeyboardButton("⚙️ Металл ️", callback_data="metall_spravka")
        btn_batery_spravka = types.InlineKeyboardButton("🔋 Батареи и аккумуляторы", callback_data="batery_spravka")
        markup.add(btn_plastik_spravka, btn_steklo_spravka, btn_paper_spravka, btn_metall_spravka, btn_batery_spravka)
        bot.send_message(message.chat.id, text="Выберите тип материала", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="<b>Выберите один из пунктов меню! ⬇️</b>", parse_mode='HTML')


# Вывод и обработка кнопок
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    bot.answer_callback_query(call.id)
    if call.data == "plastik":
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn_admiralteyskii = types.InlineKeyboardButton("Адмиралтейский", callback_data="admiralteyskii_plastik")
        btn_vasileostrovskii = types.InlineKeyboardButton("Василеостровский", callback_data="vasileostrovskii_plastik")
        btn_viborgskii = types.InlineKeyboardButton("Выборгский", callback_data="viborgskii_plastik")
        btn_kalininskii = types.InlineKeyboardButton("Калининский", callback_data="kalininskii_plastik")
        btn_kirovkskii = types.InlineKeyboardButton("Кировский", callback_data="kirovkskii_plastik")
        btn_kolpinskii = types.InlineKeyboardButton("Колпинский", callback_data="kolpinskii_plastik")
        btn_krasnogvardeiskii = types.InlineKeyboardButton("Красногвардейский",
                                                           callback_data="krasnogvardeiskii_plastik")
        btn_krasniselskii = types.InlineKeyboardButton("Красносельский", callback_data="krasniselskii_plastik")
        btn_kronshtadtskii = types.InlineKeyboardButton("Кронштадтский", callback_data="kronshtadtskii_plastik")
        btn_kyrortnii = types.InlineKeyboardButton("Курортный", callback_data="kyrortnii_plastik")
        btn_moskovskii = types.InlineKeyboardButton("Московский", callback_data="moskovskii_plastik")
        btn_nevskii = types.InlineKeyboardButton("Невский", callback_data="nevskii_plastik")
        btn_petrogradskii = types.InlineKeyboardButton("Петроградский", callback_data="petrogradskii_plastik")
        btn_petrodvortsovii = types.InlineKeyboardButton("Петродворцовый", callback_data="petrodvortsovii_plastik")
        btn_primorskii = types.InlineKeyboardButton("Приморский", callback_data="primorskii_plastik")
        btn_pyshkinskii = types.InlineKeyboardButton("Пушкинский", callback_data="pyshkinskii_plastik")
        btn_frynzenskii = types.InlineKeyboardButton("Фрунзенский", callback_data="frynzenskii_plastik")
        btn_tsentralnii = types.InlineKeyboardButton("Центральный", callback_data="tsentralnii_plastik")
        markup.add(btn_admiralteyskii, btn_vasileostrovskii, btn_viborgskii, btn_kalininskii, btn_kirovkskii,
                   btn_kolpinskii, btn_krasnogvardeiskii, btn_krasniselskii, btn_kronshtadtskii,
                   btn_kyrortnii, btn_moskovskii, btn_nevskii, btn_petrogradskii, btn_petrodvortsovii, btn_primorskii,
                   btn_pyshkinskii, btn_frynzenskii, btn_tsentralnii)
        bot.send_message(call.message.chat.id, text="Выберите район", reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Пластик", reply_markup=None)
    elif call.data == "admiralteyskii_plastik":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_admiralteyskii_plastik")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>пластик</b>\nРайон - <b>Адмиралтейский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Адмиралтейский", parse_mode='html', reply_markup=None)
    elif call.data == "find_admiralteyskii_plastik":
        # bot.send_message(call.message.chat.id, text="Найдены следующие пункты сбора:")
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Пластик'] == 'да' and row['Район'] == 'Адмиралтейский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "back":
        markup = types.InlineKeyboardMarkup(row_width=True)
        btn_plastik = types.InlineKeyboardButton("🧴 Пластик", callback_data="plastik")
        btn_steklo = types.InlineKeyboardButton("🍸 Стекло", callback_data="steklo")
        btn_paper = types.InlineKeyboardButton("📜 Бумага", callback_data="paper")
        btn_metall = types.InlineKeyboardButton("⚙️ Металл", callback_data="metall")
        btn_batery = types.InlineKeyboardButton("🔋 Батареи и аккумуляторы", callback_data="batery")
        markup.add(btn_plastik, btn_steklo, btn_paper, btn_metall, btn_batery)
        bot.send_message(call.message.chat.id, text="Выберите тип материала", reply_markup=markup)
    elif call.data == "vasileostrovskii_plastik":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_vasileostrovskii_plastik")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>пластик</b>\nРайон - <b>Василеостровский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Василеостровский", parse_mode='html', reply_markup=None)
    elif call.data == "find_vasileostrovskii_plastik":
        # bot.send_message(call.message.chat.id, text="Найдены следующие пункты сбора:")
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Пластик'] == 'да' and row['Район'] == 'Василеостровский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "viborgskii_plastik":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_viborgskii_plastik")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>пластик</b>\nРайон - <b>Выборгский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выборгский", parse_mode='html', reply_markup=None)
    elif call.data == "find_viborgskii_plastik":
        # bot.send_message(call.message.chat.id, text="Найдены следующие пункты сбора:")
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Пластик'] == 'да' and row['Район'] == 'Выборгский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "kalininskii_plastik":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_kalininskii_plastik")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>пластик</b>\nРайон - <b>Калининский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Калининский", parse_mode='html', reply_markup=None)
    elif call.data == "find_kalininskii_plastik":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Пластик'] == 'да' and row['Район'] == 'Калининский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "kirovkskii_plastik":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_kirovkskii_plastik")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>пластик</b>\nРайон - <b>Кировский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Кировский", parse_mode='html', reply_markup=None)
    elif call.data == "find_kirovkskii_plastik":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Пластик'] == 'да' and row['Район'] == 'Кировский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "kolpinskii_plastik":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_kolpinskii_plastik")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>пластик</b>\nРайон - <b>Колпинский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Колпинский", parse_mode='html', reply_markup=None)
    elif call.data == "find_kolpinskii_plastik":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Пластик'] == 'да' and row['Район'] == 'Колпинский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "krasnogvardeiskii_plastik":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_krasnogvardeiskii_plastik")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>пластик</b>\nРайон - <b>Красногвардейский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Красногвардейский", parse_mode='html', reply_markup=None)
    elif call.data == "find_krasnogvardeiskii_plastik":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Пластик'] == 'да' and row['Район'] == 'Красногвардейский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "krasniselskii_plastik":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_krasniselskii_plastik")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>пластик</b>\nРайон - <b>Красносельский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Красносельский", parse_mode='html', reply_markup=None)
    elif call.data == "find_krasniselskii_plastik":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Пластик'] == 'да' and row['Район'] == 'Красносельский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "kronshtadtskii_plastik":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_kronshtadtskii_plastik")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>пластик</b>\nРайон - <b>Кронштадтский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Кронштадтский", parse_mode='html', reply_markup=None)
    elif call.data == "find_kronshtadtskii_plastik":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Пластик'] == 'да' and row['Район'] == 'Кронштадтский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "kyrortnii_plastik":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_kyrortnii_plastik")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>пластик</b>\nРайон - <b>Курортный</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Курортный", parse_mode='html', reply_markup=None)
    elif call.data == "find_kyrortnii_plastik":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Пластик'] == 'да' and row['Район'] == 'Курортный':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "moskovskii_plastik":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_moskovskii_plastik")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>пластик</b>\nРайон - <b>Московский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Московский", parse_mode='html', reply_markup=None)
    elif call.data == "find_moskovskii_plastik":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Пластик'] == 'да' and row['Район'] == 'Московский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "nevskii_plastik":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_nevskii_plastik")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>пластик</b>\nРайон - <b>Невский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Невский", parse_mode='html', reply_markup=None)
    elif call.data == "find_nevskii_plastik":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Пластик'] == 'да' and row['Район'] == 'Невский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "petrogradskii_plastik":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_petrogradskii_plastik")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>пластик</b>\nРайон - <b>Петроградский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Петроградский", parse_mode='html', reply_markup=None)
    elif call.data == "find_petrogradskii_plastik":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Пластик'] == 'да' and row['Район'] == 'Петроградский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "petrodvortsovii_plastik":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_petrodvortsovii_plastik")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>пластик</b>\nРайон - <b>Петродворцовый</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Петродворцовый", parse_mode='html', reply_markup=None)
    elif call.data == "find_petrodvortsovii_plastik":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Пластик'] == 'да' and row['Район'] == 'Петродворцовый':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "primorskii_plastik":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_primorskii_plastik")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>пластик</b>\nРайон - <b>Приморский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Приморский", parse_mode='html', reply_markup=None)
    elif call.data == "find_primorskii_plastik":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Пластик'] == 'да' and row['Район'] == 'Приморский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "pyshkinskii_plastik":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_pyshkinskii_plastik")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>пластик</b>\nРайон - <b>Пушкинский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Пушкинский", parse_mode='html', reply_markup=None)
    elif call.data == "find_pyshkinskii_plastik":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Пластик'] == 'да' and row['Район'] == 'Пушкинский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "frynzenskii_plastik":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_frynzenskii_plastik")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>пластик</b>\nРайон - <b>Фрунзенский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Фрунзенский", parse_mode='html', reply_markup=None)
    elif call.data == "find_frynzenskii_plastik":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Пластик'] == 'да' and row['Район'] == 'Фрунзенский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "tsentralnii_plastik":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_tsentralnii_plastik")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>пластик</b>\nРайон - <b>Центральный</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Центральный", parse_mode='html', reply_markup=None)
    elif call.data == "find_tsentralnii_plastik":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Пластик'] == 'да' and row['Район'] == 'Центральный':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")


    elif call.data == "steklo":
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn_admiralteyskii = types.InlineKeyboardButton("Адмиралтейский", callback_data="admiralteyskii_steklo")
        btn_vasileostrovskii = types.InlineKeyboardButton("Василеостровский", callback_data="vasileostrovskii_steklo")
        btn_viborgskii = types.InlineKeyboardButton("Выборгский", callback_data="viborgskii_steklo")
        btn_kalininskii = types.InlineKeyboardButton("Калининский", callback_data="kalininskii_steklo")
        btn_kirovkskii = types.InlineKeyboardButton("Кировский", callback_data="kirovkskii_steklo")
        btn_kolpinskii = types.InlineKeyboardButton("Колпинский", callback_data="kolpinskii_steklo")
        btn_krasnogvardeiskii = types.InlineKeyboardButton("Красногвардейский",
                                                           callback_data="krasnogvardeiskii_steklo")
        btn_krasniselskii = types.InlineKeyboardButton("Красносельский", callback_data="krasniselskii_steklo")
        btn_kronshtadtskii = types.InlineKeyboardButton("Кронштадтский", callback_data="kronshtadtskii_steklo")
        btn_kyrortnii = types.InlineKeyboardButton("Курортный", callback_data="kyrortnii_steklo")
        btn_moskovskii = types.InlineKeyboardButton("Московский", callback_data="moskovskii_steklo")
        btn_nevskii = types.InlineKeyboardButton("Невский", callback_data="nevskii_steklo")
        btn_petrogradskii = types.InlineKeyboardButton("Петроградский", callback_data="petrogradskii_steklo")
        btn_petrodvortsovii = types.InlineKeyboardButton("Петродворцовый", callback_data="petrodvortsovii_steklo")
        btn_primorskii = types.InlineKeyboardButton("Приморский", callback_data="primorskii_steklo")
        btn_pyshkinskii = types.InlineKeyboardButton("Пушкинский", callback_data="pyshkinskii_steklo")
        btn_frynzenskii = types.InlineKeyboardButton("Фрунзенский", callback_data="frynzenskii_steklo")
        btn_tsentralnii = types.InlineKeyboardButton("Центральный", callback_data="tsentralnii_steklo")
        markup.add(btn_admiralteyskii, btn_vasileostrovskii, btn_viborgskii, btn_kalininskii, btn_kirovkskii,
                   btn_kolpinskii, btn_krasnogvardeiskii, btn_krasniselskii, btn_kronshtadtskii,
                   btn_kyrortnii, btn_moskovskii, btn_nevskii, btn_petrogradskii, btn_petrodvortsovii, btn_primorskii,
                   btn_pyshkinskii, btn_frynzenskii, btn_tsentralnii)
        bot.send_message(call.message.chat.id, text="Выберите ваш район", reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Стекло", reply_markup=None)
    elif call.data == "admiralteyskii_steklo":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_admiralteyskii_steklo")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>стекло</b>\nРайон - <b>Адмиралтейский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Адмиралтейский", parse_mode='html', reply_markup=None)
    elif call.data == "find_admiralteyskii_steklo":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Стекло'] == 'да' and row['Район'] == 'Адмиралтейский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "vasileostrovskii_steklo":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_vasileostrovskii_steklo")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>стекло</b>\nРайон - <b>Василеостровский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Василеостровский", parse_mode='html', reply_markup=None)
    elif call.data == "find_vasileostrovskii_steklo":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Стекло'] == 'да' and row['Район'] == 'Василеостровский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "viborgskii_steklo":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_viborgskii_steklo")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>стекло</b>\nРайон - <b>Выборгский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выборгский", parse_mode='html', reply_markup=None)
    elif call.data == "find_viborgskii_steklo":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Стекло'] == 'да' and row['Район'] == 'Выборгский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "kalininskii_steklo":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_kalininskii_steklo")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>стекло</b>\nРайон - <b>Калининский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Калининский", parse_mode='html', reply_markup=None)
    elif call.data == "find_kalininskii_steklo":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Стекло'] == 'да' and row['Район'] == 'Калининский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "kirovkskii_steklo":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_kirovkskii_steklo")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>стекло</b>\nРайон - <b>Кировский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Кировский", parse_mode='html', reply_markup=None)
    elif call.data == "find_kirovkskii_steklo":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Стекло'] == 'да' and row['Район'] == 'Кировский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "kolpinskii_steklo":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_kolpinskii_steklo")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>стекло</b>\nРайон - <b>Колпинский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Колпинский", parse_mode='html', reply_markup=None)
    elif call.data == "find_kolpinskii_steklo":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Стекло'] == 'да' and row['Район'] == 'Колпинский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "krasnogvardeiskii_steklo":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_krasnogvardeiskii_steklo")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>стекло</b>\nРайон - <b>Красногвардейский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Красногвардейский", parse_mode='html', reply_markup=None)
    elif call.data == "find_krasnogvardeiskii_steklo":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Стекло'] == 'да' and row['Район'] == 'Красногвардейский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "krasniselskii_steklo":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_krasniselskii_steklo")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>стекло</b>\nРайон - <b>Красносельский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Красносельский", parse_mode='html', reply_markup=None)
    elif call.data == "find_krasniselskii_steklo":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Стекло'] == 'да' and row['Район'] == 'Красносельский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "kronshtadtskii_steklo":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_kronshtadtskii_steklo")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>стекло</b>\nРайон - <b>Кронштадтский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Кронштадтский", parse_mode='html', reply_markup=None)
    elif call.data == "find_kronshtadtskii_steklo":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Стекло'] == 'да' and row['Район'] == 'Кронштадтский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "kyrortnii_steklo":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_kyrortnii_steklo")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>стекло</b>\nРайон - <b>Курортный</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Курортный", parse_mode='html', reply_markup=None)
    elif call.data == "find_kyrortnii_steklo":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Стекло'] == 'да' and row['Район'] == 'Курортный':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "moskovskii_steklo":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_moskovskii_steklo")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>стекло</b>\nРайон - <b>Московский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Московский", parse_mode='html', reply_markup=None)
    elif call.data == "find_moskovskii_steklo":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Стекло'] == 'да' and row['Район'] == 'Московский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "nevskii_steklo":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_nevskii_steklo")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>стекло</b>\nРайон - <b>Невский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Невский", parse_mode='html', reply_markup=None)
    elif call.data == "find_nevskii_steklo":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Стекло'] == 'да' and row['Район'] == 'Невский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "petrogradskii_steklo":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_petrogradskii_steklo")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>стекло</b>\nРайон - <b>Петроградский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Петроградский", parse_mode='html', reply_markup=None)
    elif call.data == "find_petrogradskii_steklo":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Стекло'] == 'да' and row['Район'] == 'Петроградский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "petrodvortsovii_steklo":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_petrodvortsovii_steklo")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>стекло</b>\nРайон - <b>Петродворцовый</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Петродворцовый", parse_mode='html', reply_markup=None)
    elif call.data == "find_petrodvortsovii_steklo":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Стекло'] == 'да' and row['Район'] == 'Петродворцовый':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "primorskii_steklo":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_primorskii_steklo")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>стекло</b>\nРайон - <b>Приморский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Приморский", parse_mode='html', reply_markup=None)
    elif call.data == "find_primorskii_steklo":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Стекло'] == 'да' and row['Район'] == 'Приморский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "pyshkinskii_steklo":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_pyshkinskii_steklo")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>стекло</b>\nРайон - <b>Пушкинский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Пушкинский", parse_mode='html', reply_markup=None)
    elif call.data == "find_pyshkinskii_steklo":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Стекло'] == 'да' and row['Район'] == 'Пушкинский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "frynzenskii_steklo":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_frynzenskii_steklo")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>стекло</b>\nРайон - <b>Фрунзенский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Фрунзенский", parse_mode='html', reply_markup=None)
    elif call.data == "find_frynzenskii_steklo":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Стекло'] == 'да' and row['Район'] == 'Фрунзенский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "tsentralnii_steklo":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_tsentralnii_steklo")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>стекло</b>\nРайон - <b>Центральный</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Центральный", parse_mode='html', reply_markup=None)
    elif call.data == "find_tsentralnii_steklo":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Стекло'] == 'да' and row['Район'] == 'Центральный':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")


    elif call.data == "paper":
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn_admiralteyskii = types.InlineKeyboardButton("Адмиралтейский", callback_data="admiralteyskii_paper")
        btn_vasileostrovskii = types.InlineKeyboardButton("Василеостровский", callback_data="vasileostrovskii_paper")
        btn_viborgskii = types.InlineKeyboardButton("Выборгский", callback_data="viborgskii_paper")
        btn_kalininskii = types.InlineKeyboardButton("Калининский", callback_data="kalininskii_paper")
        btn_kirovkskii = types.InlineKeyboardButton("Кировский", callback_data="kirovkskii_paper")
        btn_kolpinskii = types.InlineKeyboardButton("Колпинский", callback_data="kolpinskii_paper")
        btn_krasnogvardeiskii = types.InlineKeyboardButton("Красногвардейский",
                                                           callback_data="krasnogvardeiskii_paper")
        btn_krasniselskii = types.InlineKeyboardButton("Красносельский", callback_data="krasniselskii_paper")
        btn_kronshtadtskii = types.InlineKeyboardButton("Кронштадтский", callback_data="kronshtadtskii_paper")
        btn_kyrortnii = types.InlineKeyboardButton("Курортный", callback_data="kyrortnii_paper")
        btn_moskovskii = types.InlineKeyboardButton("Московский", callback_data="moskovskii_paper")
        btn_nevskii = types.InlineKeyboardButton("Невский", callback_data="nevskii_paper")
        btn_petrogradskii = types.InlineKeyboardButton("Петроградский", callback_data="petrogradskii_paper")
        btn_petrodvortsovii = types.InlineKeyboardButton("Петродворцовый", callback_data="petrodvortsovii_paper")
        btn_primorskii = types.InlineKeyboardButton("Приморский", callback_data="primorskii_paper")
        btn_pyshkinskii = types.InlineKeyboardButton("Пушкинский", callback_data="pyshkinskii_paper")
        btn_frynzenskii = types.InlineKeyboardButton("Фрунзенский", callback_data="frynzenskii_paper")
        btn_tsentralnii = types.InlineKeyboardButton("Центральный", callback_data="tsentralnii_paper")
        markup.add(btn_admiralteyskii, btn_vasileostrovskii, btn_viborgskii, btn_kalininskii, btn_kirovkskii,
                   btn_kolpinskii, btn_krasnogvardeiskii, btn_krasniselskii, btn_kronshtadtskii,
                   btn_kyrortnii, btn_moskovskii, btn_nevskii, btn_petrogradskii, btn_petrodvortsovii, btn_primorskii,
                   btn_pyshkinskii, btn_frynzenskii, btn_tsentralnii)
        bot.send_message(call.message.chat.id, text="Выберите ваш район", reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Бумага", reply_markup=None)
    elif call.data == "admiralteyskii_paper":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_admiralteyskii_paper")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>бумага</b>\nРайон - <b>Адмиралтейский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Адмиралтейский", parse_mode='html', reply_markup=None)
    elif call.data == "find_admiralteyskii_paper":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Бумага'] == 'да' and row['Район'] == 'Адмиралтейский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "vasileostrovskii_paper":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_vasileostrovskii_paper")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>бумага</b>\nРайон - <b>Василеостровский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Василеостровский", parse_mode='html', reply_markup=None)
    elif call.data == "find_vasileostrovskii_paper":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Бумага'] == 'да' and row['Район'] == 'Василеостровский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "viborgskii_paper":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_viborgskii_paper")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>бумага</b>\nРайон - <b>Выборгский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выборгский", parse_mode='html', reply_markup=None)
    elif call.data == "find_viborgskii_paper":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Бумага'] == 'да' and row['Район'] == 'Выборгский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "kalininskii_paper":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_kalininskii_paper")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>бумага</b>\nРайон - <b>Калининский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Калининский", parse_mode='html', reply_markup=None)
    elif call.data == "find_kalininskii_paper":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Бумага'] == 'да' and row['Район'] == 'Калининский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "kirovkskii_paper":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_kirovkskii_paper")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>бумага</b>\nРайон - <b>Кировский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Кировский", parse_mode='html', reply_markup=None)
    elif call.data == "find_kirovkskii_paper":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Бумага'] == 'да' and row['Район'] == 'Кировский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "kolpinskii_paper":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_kolpinskii_paper")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>бумага</b>\nРайон - <b>Колпинский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Колпинский", parse_mode='html', reply_markup=None)
    elif call.data == "find_kolpinskii_paper":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Бумага'] == 'да' and row['Район'] == 'Колпинский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "krasnogvardeiskii_paper":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_krasnogvardeiskii_paper")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>бумага</b>\nРайон - <b>Красногвардейский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Красногвардейский", parse_mode='html', reply_markup=None)
    elif call.data == "find_krasnogvardeiskii_paper":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Бумага'] == 'да' and row['Район'] == 'Красногвардейский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "krasniselskii_paper":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_krasniselskii_paper")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>бумага</b>\nРайон - <b>Красносельский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Красносельский", parse_mode='html', reply_markup=None)
    elif call.data == "find_krasniselskii_paper":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Бумага'] == 'да' and row['Район'] == 'Красносельский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "kronshtadtskii_paper":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_kronshtadtskii_paper")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>бумага</b>\nРайон - <b>Кронштадтский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Кронштадтский", parse_mode='html', reply_markup=None)
    elif call.data == "find_kronshtadtskii_paper":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Бумага'] == 'да' and row['Район'] == 'Кронштадтский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "kyrortnii_paper":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_kyrortnii_paper")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>бумага</b>\nРайон - <b>Курортный</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Курортный", parse_mode='html', reply_markup=None)
    elif call.data == "find_kyrortnii_paper":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Бумага'] == 'да' and row['Район'] == 'Курортный':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "moskovskii_paper":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_moskovskii_paper")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>бумага</b>\nРайон - <b>Московский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Московский", parse_mode='html', reply_markup=None)
    elif call.data == "find_moskovskii_paper":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Бумага'] == 'да' and row['Район'] == 'Московский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "nevskii_paper":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_nevskii_paper")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>бумага</b>\nРайон - <b>Невский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Невский", parse_mode='html', reply_markup=None)
    elif call.data == "find_nevskii_paper":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Бумага'] == 'да' and row['Район'] == 'Невский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "petrogradskii_paper":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_petrogradskii_paper")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>бумага</b>\nРайон - <b>Петроградский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Петроградский", parse_mode='html', reply_markup=None)
    elif call.data == "find_petrogradskii_paper":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Бумага'] == 'да' and row['Район'] == 'Петроградский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "petrodvortsovii_paper":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_petrodvortsovii_paper")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>бумага</b>\nРайон - <b>Петродворцовый</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Петродворцовый", parse_mode='html', reply_markup=None)
    elif call.data == "find_petrodvortsovii_paper":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Бумага'] == 'да' and row['Район'] == 'Петродворцовый':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "primorskii_paper":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_primorskii_paper")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>бумага</b>\nРайон - <b>Приморский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Приморский", parse_mode='html', reply_markup=None)
    elif call.data == "find_primorskii_paper":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Бумага'] == 'да' and row['Район'] == 'Приморский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "pyshkinskii_paper":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_pyshkinskii_paper")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>бумага</b>\nРайон - <b>Пушкинский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Пушкинский", parse_mode='html', reply_markup=None)
    elif call.data == "find_pyshkinskii_paper":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Бумага'] == 'да' and row['Район'] == 'Пушкинский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "frynzenskii_paper":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_frynzenskii_paper")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>бумага</b>\nРайон - <b>Фрунзенский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Фрунзенский", parse_mode='html', reply_markup=None)
    elif call.data == "find_frynzenskii_paper":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Бумага'] == 'да' and row['Район'] == 'Фрунзенский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "tsentralnii_paper":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_tsentralnii_paper")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>бумага</b>\nРайон - <b>Центральный</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Центральный", parse_mode='html', reply_markup=None)
    elif call.data == "find_tsentralnii_paper":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Бумага'] == 'да' and row['Район'] == 'Центральный':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")


    elif call.data == "metall":
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn_admiralteyskii = types.InlineKeyboardButton("Адмиралтейский", callback_data="admiralteyskii_metall")
        btn_vasileostrovskii = types.InlineKeyboardButton("Василеостровский", callback_data="vasileostrovskii_metall")
        btn_viborgskii = types.InlineKeyboardButton("Выборгский", callback_data="viborgskii_metall")
        btn_kalininskii = types.InlineKeyboardButton("Калининский", callback_data="kalininskii_metall")
        btn_kirovkskii = types.InlineKeyboardButton("Кировский", callback_data="kirovkskii_metall")
        btn_kolpinskii = types.InlineKeyboardButton("Колпинский", callback_data="kolpinskii_metall")
        btn_krasnogvardeiskii = types.InlineKeyboardButton("Красногвардейский",
                                                           callback_data="krasnogvardeiskii_metall")
        btn_krasniselskii = types.InlineKeyboardButton("Красносельский", callback_data="krasniselskii_metall")
        btn_kronshtadtskii = types.InlineKeyboardButton("Кронштадтский", callback_data="kronshtadtskii_metall")
        btn_kyrortnii = types.InlineKeyboardButton("Курортный", callback_data="kyrortnii_metall")
        btn_moskovskii = types.InlineKeyboardButton("Московский", callback_data="moskovskii_metall")
        btn_nevskii = types.InlineKeyboardButton("Невский", callback_data="nevskii_metall")
        btn_petrogradskii = types.InlineKeyboardButton("Петроградский", callback_data="petrogradskii_metall")
        btn_petrodvortsovii = types.InlineKeyboardButton("Петродворцовый", callback_data="petrodvortsovii_metall")
        btn_primorskii = types.InlineKeyboardButton("Приморский", callback_data="primorskii_metall")
        btn_pyshkinskii = types.InlineKeyboardButton("Пушкинский", callback_data="pyshkinskii_metall")
        btn_frynzenskii = types.InlineKeyboardButton("Фрунзенский", callback_data="frynzenskii_metall")
        btn_tsentralnii = types.InlineKeyboardButton("Центральный", callback_data="tsentralnii_metall")
        markup.add(btn_admiralteyskii, btn_vasileostrovskii, btn_viborgskii, btn_kalininskii, btn_kirovkskii,
                   btn_kolpinskii, btn_krasnogvardeiskii, btn_krasniselskii, btn_kronshtadtskii,
                   btn_kyrortnii, btn_moskovskii, btn_nevskii, btn_petrogradskii, btn_petrodvortsovii, btn_primorskii,
                   btn_pyshkinskii, btn_frynzenskii, btn_tsentralnii)
        bot.send_message(call.message.chat.id, text="Выберите ваш район", reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Металл", reply_markup=None)
    elif call.data == "admiralteyskii_metall":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_admiralteyskii_metall")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>металл</b>\nРайон - <b>Адмиралтейский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Адмиралтейский", parse_mode='html', reply_markup=None)
    elif call.data == "find_admiralteyskii_metall":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Металл'] == 'да' and row['Район'] == 'Адмиралтейский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "vasileostrovskii_metall":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_vasileostrovskii_metall")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>металл</b>\nРайон - <b>Василеостровский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Василеостровский", parse_mode='html', reply_markup=None)
    elif call.data == "find_vasileostrovskii_metall":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Металл'] == 'да' and row['Район'] == 'Василеостровский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "viborgskii_metall":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_viborgskii_metall")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>металл</b>\nРайон - <b>Выборгский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выборгский", parse_mode='html', reply_markup=None)
    elif call.data == "find_viborgskii_metall":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Металл'] == 'да' and row['Район'] == 'Выборгский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "kalininskii_metall":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_kalininskii_metall")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>металл</b>\nРайон - <b>Калининский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Калининский", parse_mode='html', reply_markup=None)
    elif call.data == "find_kalininskii_metall":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Металл'] == 'да' and row['Район'] == 'Калининский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "kirovkskii_metall":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_kirovkskii_metall")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>металл</b>\nРайон - <b>Кировский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Кировский", parse_mode='html', reply_markup=None)
    elif call.data == "find_kirovkskii_metall":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Металл'] == 'да' and row['Район'] == 'Кировский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "kolpinskii_metall":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_kolpinskii_metall")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>металл</b>\nРайон - <b>Колпинский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Колпинский", parse_mode='html', reply_markup=None)
    elif call.data == "find_kolpinskii_metall":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Металл'] == 'да' and row['Район'] == 'Колпинский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "krasnogvardeiskii_metall":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_krasnogvardeiskii_metall")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>металл</b>\nРайон - <b>Красногвардейский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Красногвардейский", parse_mode='html', reply_markup=None)
    elif call.data == "find_krasnogvardeiskii_metall":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Металл'] == 'да' and row['Район'] == 'Красногвардейский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "krasniselskii_metall":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_krasniselskii_metall")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>металл</b>\nРайон - <b>Красносельский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Красносельский", parse_mode='html', reply_markup=None)
    elif call.data == "find_krasniselskii_metall":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Металл'] == 'да' and row['Район'] == 'Красносельский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "kronshtadtskii_metall":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_kronshtadtskii_metall")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>металл</b>\nРайон - <b>Кронштадтский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Кронштадтский", parse_mode='html', reply_markup=None)
    elif call.data == "find_kronshtadtskii_metall":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Металл'] == 'да' and row['Район'] == 'Кронштадтский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "kyrortnii_metall":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_kyrortnii_metall")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>металл</b>\nРайон - <b>Курортный</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Курортный", parse_mode='html', reply_markup=None)
    elif call.data == "find_kyrortnii_metall":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Металл'] == 'да' and row['Район'] == 'Курортный':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "moskovskii_metall":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_moskovskii_metall")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>металл</b>\nРайон - <b>Московский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Московский", parse_mode='html', reply_markup=None)
    elif call.data == "find_moskovskii_metall":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Металл'] == 'да' and row['Район'] == 'Московский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "nevskii_metall":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_nevskii_metall")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>металл</b>\nРайон - <b>Невский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Невский", parse_mode='html', reply_markup=None)
    elif call.data == "find_nevskii_metall":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Металл'] == 'да' and row['Район'] == 'Невский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "petrogradskii_metall":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_petrogradskii_metall")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>металл</b>\nРайон - <b>Петроградский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Петроградский", parse_mode='html', reply_markup=None)
    elif call.data == "find_petrogradskii_metall":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Металл'] == 'да' and row['Район'] == 'Петроградский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "petrodvortsovii_metall":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_petrodvortsovii_metall")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>металл</b>\nРайон - <b>Петродворцовый</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Петродворцовый", parse_mode='html', reply_markup=None)
    elif call.data == "find_petrodvortsovii_metall":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Металл'] == 'да' and row['Район'] == 'Петродворцовый':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "primorskii_metall":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_primorskii_metall")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>металл</b>\nРайон - <b>Приморский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Приморский", parse_mode='html', reply_markup=None)
    elif call.data == "find_primorskii_metall":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Металл'] == 'да' and row['Район'] == 'Приморский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "pyshkinskii_metall":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_pyshkinskii_metall")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>металл</b>\nРайон - <b>Пушкинский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Пушкинский", parse_mode='html', reply_markup=None)
    elif call.data == "find_pyshkinskii_metall":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Металл'] == 'да' and row['Район'] == 'Пушкинский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "frynzenskii_metall":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_frynzenskii_metall")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>металл</b>\nРайон - <b>Фрунзенский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Фрунзенский", parse_mode='html', reply_markup=None)
    elif call.data == "find_frynzenskii_metall":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Металл'] == 'да' and row['Район'] == 'Фрунзенский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "tsentralnii_metall":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_tsentralnii_metall")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>металл</b>\nРайон - <b>Центральный</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Центральный", parse_mode='html', reply_markup=None)
    elif call.data == "find_tsentralnii_metall":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Металл'] == 'да' and row['Район'] == 'Центральный':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    # elif call.data == "find_tsentralnii_metall":
    #     bot.send_message(call.message.chat.id, text="Вот, что найдено по вашему запросу:")
    #     f = open("Points.csv", 'r')
    #     reader = csv.DictReader(f, delimiter=';', quotechar='"')
    #     for index, row in enumerate(reader):
    #         if row['Металл'] == 'да' and row['Район'] == 'Центральный':
    #             str = 'Адрес: ' + row['Адрес'] + '  ' + row['Ссылка']
    #             bot.send_message(call.message.chat.id, str)

    elif call.data == "batery":
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn_admiralteyskii = types.InlineKeyboardButton("Адмиралтейский", callback_data="admiralteyskii_batery")
        btn_vasileostrovskii = types.InlineKeyboardButton("Василеостровский", callback_data="vasileostrovskii_batery")
        btn_viborgskii = types.InlineKeyboardButton("Выборгский", callback_data="viborgskii_batery")
        btn_kalininskii = types.InlineKeyboardButton("Калининский", callback_data="kalininskii_batery")
        btn_kirovkskii = types.InlineKeyboardButton("Кировский", callback_data="kirovkskii_batery")
        btn_kolpinskii = types.InlineKeyboardButton("Колпинский", callback_data="kolpinskii_batery")
        btn_krasnogvardeiskii = types.InlineKeyboardButton("Красногвардейский",
                                                           callback_data="krasnogvardeiskii_batery")
        btn_krasniselskii = types.InlineKeyboardButton("Красносельский", callback_data="krasniselskii_batery")
        btn_kronshtadtskii = types.InlineKeyboardButton("Кронштадтский", callback_data="kronshtadtskii_batery")
        btn_kyrortnii = types.InlineKeyboardButton("Курортный", callback_data="kyrortnii_batery")
        btn_moskovskii = types.InlineKeyboardButton("Московский", callback_data="moskovskii_batery")
        btn_nevskii = types.InlineKeyboardButton("Невский", callback_data="nevskii_batery")
        btn_petrogradskii = types.InlineKeyboardButton("Петроградский", callback_data="petrogradskii_batery")
        btn_petrodvortsovii = types.InlineKeyboardButton("Петродворцовый", callback_data="petrodvortsovii_batery")
        btn_primorskii = types.InlineKeyboardButton("Приморский", callback_data="primorskii_batery")
        btn_pyshkinskii = types.InlineKeyboardButton("Пушкинский", callback_data="pyshkinskii_batery")
        btn_frynzenskii = types.InlineKeyboardButton("Фрунзенский", callback_data="frynzenskii_batery")
        btn_tsentralnii = types.InlineKeyboardButton("Центральный", callback_data="tsentralnii_batery")
        markup.add(btn_admiralteyskii, btn_vasileostrovskii, btn_viborgskii, btn_kalininskii, btn_kirovkskii,
                   btn_kolpinskii, btn_krasnogvardeiskii, btn_krasniselskii, btn_kronshtadtskii,
                   btn_kyrortnii, btn_moskovskii, btn_nevskii, btn_petrogradskii, btn_petrodvortsovii, btn_primorskii,
                   btn_pyshkinskii, btn_frynzenskii, btn_tsentralnii)
        bot.send_message(call.message.chat.id, text="Выберите ваш район", reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Батареи и аккумуляторы", reply_markup=None)
    elif call.data == "admiralteyskii_batery":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_admiralteyskii_batery")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>батареи и аккумуляторы</b>\nРайон - <b>Адмиралтейский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Адмиралтейский", parse_mode='html', reply_markup=None)
    elif call.data == "find_admiralteyskii_batery":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Батареи'] == 'да' and row['Район'] == 'Адмиралтейский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "vasileostrovskii_batery":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_vasileostrovskii_batery")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>батареи и аккумуляторы</b>\nРайон - <b>Василеостровский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Василеостровский", parse_mode='html', reply_markup=None)
    elif call.data == "find_vasileostrovskii_batery":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Батареи'] == 'да' and row['Район'] == 'Василеостровский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "viborgskii_batery":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_viborgskii_batery")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>батареи и аккумуляторы</b>\nРайон - <b>Выборгский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выборгский", parse_mode='html', reply_markup=None)
    elif call.data == "find_viborgskii_batery":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Батареи'] == 'да' and row['Район'] == 'Выборгский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "kalininskii_batery":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_kalininskii_batery")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>батареи и аккумуляторы</b>\nРайон - <b>Калининский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Калининский", parse_mode='html', reply_markup=None)
    elif call.data == "find_kalininskii_batery":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Батареи'] == 'да' and row['Район'] == 'Калининский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "kirovkskii_batery":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_kirovkskii_batery")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>батареи и аккумуляторы</b>\nРайон - <b>Кировский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Кировский", parse_mode='html', reply_markup=None)
    elif call.data == "find_kirovkskii_batery":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Батареи'] == 'да' and row['Район'] == 'Кировский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "kolpinskii_batery":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_kolpinskii_batery")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>батареи и аккумуляторы</b>\nРайон - <b>Колпинский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Колпинский", parse_mode='html', reply_markup=None)
    elif call.data == "find_kolpinskii_batery":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Батареи'] == 'да' and row['Район'] == 'Колпинский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "krasnogvardeiskii_batery":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_krasnogvardeiskii_batery")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>батареи и аккумуляторы</b>\nРайон - <b>Красногвардейский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Красногвардейский", parse_mode='html', reply_markup=None)
    elif call.data == "find_krasnogvardeiskii_batery":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Батареи'] == 'да' and row['Район'] == 'Красногвардейский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "krasniselskii_batery":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_krasniselskii_batery")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>батареи и аккумуляторы</b>\nРайон - <b>Красносельский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Красносельский", parse_mode='html', reply_markup=None)
    elif call.data == "find_krasniselskii_batery":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Батареи'] == 'да' and row['Район'] == 'Красносельский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "kronshtadtskii_batery":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_kronshtadtskii_batery")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>батареи и аккумуляторы</b>\nРайон - <b>Кронштадтский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Кронштадтский", parse_mode='html', reply_markup=None)
    elif call.data == "find_kronshtadtskii_batery":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Батареи'] == 'да' and row['Район'] == 'Кронштадтский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "kyrortnii_batery":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_kyrortnii_batery")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>батареи и аккумуляторы</b>\nРайон - <b>Курортный</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Курортный", parse_mode='html', reply_markup=None)
    elif call.data == "find_kyrortnii_batery":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Батареи'] == 'да' and row['Район'] == 'Курортный':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "moskovskii_batery":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_moskovskii_batery")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>батареи и аккумуляторы</b>\nРайон - <b>Московский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Московский", parse_mode='html', reply_markup=None)
    elif call.data == "find_moskovskii_batery":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Батареи'] == 'да' and row['Район'] == 'Московский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "nevskii_batery":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_nevskii_batery")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>батареи и аккумуляторы</b>\nРайон - <b>Невский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Невский", parse_mode='html', reply_markup=None)
    elif call.data == "find_nevskii_batery":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Батареи'] == 'да' and row['Район'] == 'Невский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "petrogradskii_batery":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_petrogradskii_batery")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>батареи и аккумуляторы</b>\nРайон - <b>Петроградский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Петроградский", parse_mode='html', reply_markup=None)
    elif call.data == "find_petrogradskii_batery":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Батареи'] == 'да' and row['Район'] == 'Петроградский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "petrodvortsovii_batery":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_petrodvortsovii_batery")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>батареи и аккумуляторы</b>\nРайон - <b>Петродворцовый</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Петродворцовый", parse_mode='html', reply_markup=None)
    elif call.data == "find_petrodvortsovii_batery":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Батареи'] == 'да' and row['Район'] == 'Петродворцовый':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "primorskii_batery":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_primorskii_batery")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>батареи и аккумуляторы</b>\nРайон - <b>Приморский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Приморский", parse_mode='html', reply_markup=None)
    elif call.data == "find_primorskii_batery":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Батареи'] == 'да' and row['Район'] == 'Приморский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "pyshkinskii_batery":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_pyshkinskii_batery")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>батареи и аккумуляторы</b>\nРайон - <b>Пушкинский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Пушкинский", parse_mode='html', reply_markup=None)
    elif call.data == "find_pyshkinskii_batery":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Батареи'] == 'да' and row['Район'] == 'Пушкинский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "frynzenskii_batery":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_frynzenskii_batery")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>батареи и аккумуляторы</b>\nРайон - <b>Фрунзенский</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Фрунзенский", parse_mode='html', reply_markup=None)
    elif call.data == "find_frynzenskii_batery":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Батареи'] == 'да' and row['Район'] == 'Фрунзенский':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")
    elif call.data == "tsentralnii_batery":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_find = types.InlineKeyboardButton("Искать ✅", callback_data="find_tsentralnii_batery")
        btn_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="back")
        # btn_edit_district = types.InlineKeyboardButton("Изменить район", callback_data="edit_district")
        markup.add(btn_find)
        markup.add(btn_back)
        bot.send_message(call.message.chat.id,
                         text="Вы выбрали:\nТип материала - <b>батареи и аккумуляторы</b>\nРайон - <b>Центральный</b>",
                         parse_mode='html', reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Центральный", parse_mode='html', reply_markup=None)
    elif call.data == "find_tsentralnii_batery":
        bot.send_message(call.message.chat.id,
                         text="Найдены следующие пункты сбора:\n<I>(Нажмите на адрес, чтобы увидеть пункт на карте)</I>",
                         parse_mode='html')
        f = open("Points.csv", 'r')
        reader = csv.DictReader(f, delimiter=';', quotechar='"')
        # markup = types.InlineKeyboardMarkup(row_width=1)
        for index, row in enumerate(reader):
            if row['Батареи'] == 'да' and row['Район'] == 'Центральный':
                address = row['Адрес']
                urll = row['Ссылка']
                # bot.send_message(call.message.chat.id, str)
                markup = types.InlineKeyboardMarkup(row_width=1)
                # btn = types.InlineKeyboardButton(str)
                markup.add(types.InlineKeyboardButton(text=address, url=urll))
                bot.send_message(call.message.chat.id, text="*", reply_markup=markup)
                # return markup
        bot.send_message(call.message.chat.id, text="Выберите, что хотите сделать")


    ######################################################################################################################
    # Справочник
    ######################################################################################################################

    elif call.data == "plastik_spravka":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_1PET = types.InlineKeyboardButton("01 PET", callback_data="1PET")
        btn_2PEHD = types.InlineKeyboardButton("02 PE-HD", callback_data="2PEHD")
        btn_3PVC = types.InlineKeyboardButton("03 PVC", callback_data="3PVC")
        btn_4PELD = types.InlineKeyboardButton("04 PE-LD", callback_data="4PELD")
        btn_5PP = types.InlineKeyboardButton("05 PP", callback_data="5PP")
        btn_6PS = types.InlineKeyboardButton("06 PS", callback_data="6PS")
        btn_7O = types.InlineKeyboardButton("07 O", callback_data="7O")
        btn_9ABS = types.InlineKeyboardButton("09 ABS или ABS", callback_data="9ABS")
        # btn_plastik_spravka_back = types.InlineKeyboardButton("⬅ Назад", callback_data="plastik_spravka_back")
        markup.add(btn_1PET, btn_2PEHD, btn_3PVC, btn_4PELD, btn_5PP, btn_6PS, btn_7O, btn_9ABS)
        # markup.row(btn_plastik_spravka_back)
        bot.send_message(call.message.chat.id, text="Выберите знак на упаковке", reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы выбрали - пластик", reply_markup=None)
    elif call.data == "1PET":
        # markup = types.InlineKeyboardMarkup(row_width=1)
        # btn_1PET_back = types.InlineKeyboardButton("⬅ Назад", callback_data="spravka_back")
        # markup.add(btn_1PET_back)
        # photo = open('Pet1.png', 'rb')
        # bot.send_photo(call.message.chat.id, photo)
        # bot.send_message(call.message.chat.id, spravochnik.plastik1PET, reply_markup=markup)
        # bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
        #                       text="Вы выбрали маркировку - ♻️ 01 PET", parse_mode='html', reply_markup=None)
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_1PET_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="spravka_back")
        markup.add(btn_1PET_back)
        # photo = open('Pet1.png', 'rb')
        with open('photo/1PET.png', 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo, caption=spravochnik.plastik1PET, reply_markup=markup,
                           parse_mode='html')
        # bot.send_message(call.message.chat.id, spravochnik.plastik1PET, reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы выбрали маркировку - 01 PET", parse_mode='html', reply_markup=None)
    elif call.data == "spravka_back":
        markup = types.InlineKeyboardMarkup(row_width=True)
        btn_plastik_spravka = types.InlineKeyboardButton("🧴 Пластик", callback_data="plastik_spravka")
        btn_steklo_spravka = types.InlineKeyboardButton("🍸 Стекло", callback_data="steklo_spravka")
        btn_paper_spravka = types.InlineKeyboardButton("📜 Бумага", callback_data="paper_spravka")
        btn_metall_spravka = types.InlineKeyboardButton("⚙️ Металл ️", callback_data="metall_spravka")
        btn_batery_spravka = types.InlineKeyboardButton("🔋 Батареи и аккумуляторы", callback_data="batery_spravka")
        markup.add(btn_plastik_spravka, btn_steklo_spravka, btn_paper_spravka, btn_metall_spravka, btn_batery_spravka)
        bot.send_message(call.message.chat.id, text="Выберите тип материала", reply_markup=markup)

    elif call.data == "2PEHD":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_2PEHD_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="spravka_back")
        markup.add(btn_2PEHD_back)
        with open('photo/2PEHD.png', 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo, caption=spravochnik.plastik2PEHD, reply_markup=markup,
                           parse_mode='html')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы выбрали маркировку - 02 PE-HD", parse_mode='html', reply_markup=None)
    elif call.data == "3PVC":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_3PVC_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="spravka_back")
        markup.add(btn_3PVC_back)
        with open('photo/3PVC.png', 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo, caption=spravochnik.plastik3PVC, reply_markup=markup,
                           parse_mode='html')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы выбрали маркировку - 03 PVC", parse_mode='html', reply_markup=None)
    elif call.data == "4PELD":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_4PELD_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="spravka_back")
        markup.add(btn_4PELD_back)
        with open('photo/4PELD.png', 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo, caption=spravochnik.plastik4PELD, reply_markup=markup,
                           parse_mode='html')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы выбрали маркировку - 04 PE-LD", parse_mode='html', reply_markup=None)
    elif call.data == "5PP":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_5PP_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="spravka_back")
        markup.add(btn_5PP_back)
        with open('photo/5PP.png', 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo, caption=spravochnik.plastik5PP, reply_markup=markup,
                           parse_mode='html')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы выбрали маркировку - 05 PP", parse_mode='html', reply_markup=None)
    elif call.data == "6PS":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_6PS_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="spravka_back")
        markup.add(btn_6PS_back)
        with open('photo/6PS.png', 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo, caption=spravochnik.plastik6PS, reply_markup=markup,
                           parse_mode='html')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы выбрали маркировку - 06 PS", parse_mode='html', reply_markup=None)
    elif call.data == "7O":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_7O_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="spravka_back")
        markup.add(btn_7O_back)
        with open('photo/7O.png', 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo, caption=spravochnik.plastik7O, reply_markup=markup,
                           parse_mode='html')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы выбрали маркировку - 07 O", parse_mode='html', reply_markup=None)
    elif call.data == "9ABS":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_9ABS_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="spravka_back")
        markup.add(btn_9ABS_back)
        with open('photo/9ABS.png', 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo, caption=spravochnik.plastik9ABS, reply_markup=markup,
                           parse_mode='html')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы выбрали маркировку - 09 ABS или ABS", parse_mode='html', reply_markup=None)
    elif call.data == "steklo_spravka":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_70GL = types.InlineKeyboardButton("70 GL", callback_data="70GL")
        btn_71GL = types.InlineKeyboardButton("71 GL", callback_data="71GL")
        btn_72GL = types.InlineKeyboardButton("72 GL", callback_data="72GL")
        btn_73GL = types.InlineKeyboardButton("73 GL", callback_data="73GL")
        btn_74GL = types.InlineKeyboardButton("74 GL", callback_data="74GL")
        btn_75GL = types.InlineKeyboardButton("75 GL", callback_data="75GL")
        btn_76GL = types.InlineKeyboardButton("76 GL", callback_data="76GL")
        btn_77GL = types.InlineKeyboardButton("77 GL", callback_data="77GL")
        btn_78GL = types.InlineKeyboardButton("78 GL", callback_data="78GL")
        btn_79GL = types.InlineKeyboardButton("79 GL", callback_data="79GL")
        # btn_steklo_spravka_back = types.InlineKeyboardButton("⬅ Назад", callback_data="steklo_spravka_back")
        markup.add(btn_70GL, btn_71GL, btn_72GL, btn_73GL, btn_74GL, btn_75GL, btn_76GL, btn_77GL, btn_78GL, btn_79GL)
        # markup.row(btn_78GL, btn_79GL)
        # markup.row(btn_steklo_spravka_back)
        bot.send_message(call.message.chat.id, text="Выберите знак на упаковке", reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы выбрали - стекло", reply_markup=None)
    elif call.data == "70GL":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_70GL_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="spravka_back")
        markup.add(btn_70GL_back)
        with open('photo/70GL.png', 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo, caption=spravochnik.steklo70GL, reply_markup=markup,
                           parse_mode='html')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы выбрали маркировку - 70 GL", parse_mode='html', reply_markup=None)
    elif call.data == "71GL":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_71GL_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="spravka_back")
        markup.add(btn_71GL_back)
        with open('photo/71GL.png', 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo, caption=spravochnik.steklo71GL, reply_markup=markup,
                           parse_mode='html')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы выбрали маркировку - 71 GL", parse_mode='html', reply_markup=None)
    elif call.data == "72GL":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_72GL_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="spravka_back")
        markup.add(btn_72GL_back)
        with open('photo/72GL.png', 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo, caption=spravochnik.steklo72GL, reply_markup=markup,
                           parse_mode='html')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы выбрали маркировку - 72 GL", parse_mode='html', reply_markup=None)
    elif call.data == "73GL":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_73GL_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="spravka_back")
        markup.add(btn_73GL_back)
        with open('photo/73GL.png', 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo, caption=spravochnik.steklo73GL, reply_markup=markup,
                           parse_mode='html')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы выбрали маркировку - 73 GL", parse_mode='html', reply_markup=None)
    elif call.data == "74GL":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_74GL_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="spravka_back")
        markup.add(btn_74GL_back)
        with open('photo/74GL.png', 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo, caption=spravochnik.steklo74GL, reply_markup=markup,
                           parse_mode='html')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы выбрали маркировку - 74 GL", parse_mode='html', reply_markup=None)
    elif call.data == "75GL":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_75GL_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="spravka_back")
        markup.add(btn_75GL_back)
        with open('photo/75GL.png', 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo, caption=spravochnik.steklo75GL, reply_markup=markup,
                           parse_mode='html')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы выбрали маркировку -️ 75 GL", parse_mode='html', reply_markup=None)
    elif call.data == "76GL":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_76GL_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="spravka_back")
        markup.add(btn_76GL_back)
        with open('photo/76GL.png', 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo, caption=spravochnik.steklo76GL, reply_markup=markup,
                           parse_mode='html')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы выбрали маркировку - 76 GL", parse_mode='html', reply_markup=None)
    elif call.data == "77GL":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_77GL_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="spravka_back")
        markup.add(btn_77GL_back)
        with open('photo/77GL.png', 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo, caption=spravochnik.steklo77GL, reply_markup=markup,
                           parse_mode='html')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы выбрали маркировку - ️77 GL", parse_mode='html', reply_markup=None)
    elif call.data == "78GL":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_78GL_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="spravka_back")
        markup.add(btn_78GL_back)
        with open('photo/78GL.png', 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo, caption=spravochnik.steklo78GL, reply_markup=markup,
                           parse_mode='html')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы выбрали маркировку - ️ ️️78 GL", parse_mode='html', reply_markup=None)
    elif call.data == "79GL":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_79GL_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="spravka_back")
        markup.add(btn_79GL_back)
        with open('photo/79GL.png', 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo, caption=spravochnik.steklo79GL, reply_markup=markup,
                           parse_mode='html')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы выбрали маркировку - ️ ️️79 GL", parse_mode='html', reply_markup=None)
    elif call.data == "paper_spravka":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_20PAP = types.InlineKeyboardButton("20 PAP", callback_data="20PAP")
        btn_21PAP = types.InlineKeyboardButton("21 PAP", callback_data="21PAP")
        btn_22PAP = types.InlineKeyboardButton("22 PAP", callback_data="22PAP")
        btn_23PBD = types.InlineKeyboardButton("23 PBD", callback_data="23PBD")
        # btn_paper_spravka_back = types.InlineKeyboardButton("⬅ Назад", callback_data="paper_spravka_back")
        markup.add(btn_20PAP, btn_21PAP, btn_22PAP, btn_23PBD)
        # markup.row(btn_paper_spravka_back)
        bot.send_message(call.message.chat.id, text="Выберите знак на упаковке", reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы выбрали - бумага", reply_markup=None)
    elif call.data == "20PAP":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_20PAP_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="spravka_back")
        markup.add(btn_20PAP_back)
        with open('photo/20PAP.png', 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo, caption=spravochnik.paper20PAP, reply_markup=markup,
                           parse_mode='html')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы выбрали маркировку - ️ ️️20 PAP", parse_mode='html', reply_markup=None)
    elif call.data == "21PAP":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_21PAP_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="spravka_back")
        markup.add(btn_21PAP_back)
        with open('photo/21PAP.png', 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo, caption=spravochnik.paper21PAP, reply_markup=markup,
                           parse_mode='html')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы выбрали маркировку - ️ ️️21 PAP", parse_mode='html', reply_markup=None)
    elif call.data == "22PAP":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_22PAP_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="spravka_back")
        markup.add(btn_22PAP_back)
        with open('photo/22PAP.png', 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo, caption=spravochnik.paper22PAP, reply_markup=markup,
                           parse_mode='html')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы выбрали маркировку - ️ ️️22 PAP", parse_mode='html', reply_markup=None)
    elif call.data == "23PBD":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_23PBD_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="spravka_back")
        markup.add(btn_23PBD_back)
        with open('photo/23PBD.png', 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo, caption=spravochnik.paper23PBD, reply_markup=markup,
                           parse_mode='html')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы выбрали маркировку - ️ ️️23 PBD", parse_mode='html', reply_markup=None)
    elif call.data == "metall_spravka":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_40FE = types.InlineKeyboardButton("40 FE", callback_data="40FE")
        btn_41ALU = types.InlineKeyboardButton("41 ALU", callback_data="41ALU")
        # btn_metall_spravka_back = types.InlineKeyboardButton("⬅ Назад", callback_data="metall_spravka_back")
        markup.add(btn_40FE, btn_41ALU)
        # markup.row(btn_metall_spravka_back)
        bot.send_message(call.message.chat.id, text="Выберите знак на упаковке", reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы выбрали - металл", reply_markup=None)
    elif call.data == "40FE":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_40FE_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="spravka_back")
        markup.add(btn_40FE_back)
        with open('photo/40FE.png', 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo, caption=spravochnik.metall40FE, reply_markup=markup,
                           parse_mode='html')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы выбрали маркировку - ️ ️️40 FE", parse_mode='html', reply_markup=None)
    elif call.data == "41ALU":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_41ALU_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="spravka_back")
        markup.add(btn_41ALU_back)
        with open('photo/41ALU.png', 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo, caption=spravochnik.metall41ALU, reply_markup=markup,
                           parse_mode='html')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы выбрали маркировку - ️ ️️41 ALU", parse_mode='html', reply_markup=None)
    elif call.data == "batery_spravka":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_8Lead = types.InlineKeyboardButton("Pb", callback_data="8Lead")
        btn_10NiCD = types.InlineKeyboardButton("Ni-CD", callback_data="10NiCD")
        btn_11NiMH = types.InlineKeyboardButton("Ni-MH", callback_data="11NiMH")
        btn_12Li = types.InlineKeyboardButton("Li-ion", callback_data="12Li")
        # btn_batery_spravka_back = types.InlineKeyboardButton("⬅ Назад", callback_data="batery_spravka_back")
        markup.add(btn_8Lead, btn_10NiCD, btn_11NiMH, btn_12Li)
        # markup.row(btn_batery_spravka_back)
        bot.send_message(call.message.chat.id, text="Выберите знак на упаковке", reply_markup=markup)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы выбрали - Батареи и аккумуляторы", reply_markup=None)
    elif call.data == "8Lead":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_8Lead_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="spravka_back")
        markup.add(btn_8Lead_back)
        with open('photo/8Lead.png', 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo, caption=spravochnik.batery8Lead, reply_markup=markup,
                           parse_mode='html')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы выбрали маркировку - ️ ️️Pb", parse_mode='html', reply_markup=None)
    elif call.data == "10NiCD":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_10NiCD_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="spravka_back")
        markup.add(btn_10NiCD_back)
        with open('photo/10NiCD.png', 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo, caption=spravochnik.batery10NiCD, reply_markup=markup,
                           parse_mode='html')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы выбрали маркировку - ️ ️️Ni-CD", parse_mode='html', reply_markup=None)
    elif call.data == "11NiMH":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_11NiMH_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="spravka_back")
        markup.add(btn_11NiMH_back)
        with open('photo/11NiMH.png', 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo, caption=spravochnik.batery11NiMH, reply_markup=markup,
                           parse_mode='html')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы выбрали маркировку - ️ ️️Ni-MH", parse_mode='html', reply_markup=None)
    elif call.data == "12Li":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_12Li_back = types.InlineKeyboardButton("Назад ⬅️", callback_data="spravka_back")
        markup.add(btn_12Li_back)
        with open('photo/12Li.png', 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo, caption=spravochnik.batery12Li, reply_markup=markup,
                           parse_mode='html')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы выбрали маркировку - ️ ️️Li-ion", parse_mode='html', reply_markup=None)


bot.polling(none_stop=True)

# bot.send_media_group(message.chat.id,
#     [telebot.types.InputMediaPhoto(open(photo, 'rb')) for photo in ['photo1', 'photo2']])

# ======================================= модуль ДЗ
# -----------------------------------------------------------------------
def get_text_messages(bot, cur_user, message):
    chat_id = message.chat.id
    ms_text = message.text

    if ms_text == "Задание-1":
        dz1(bot, chat_id)

    elif ms_text == "Задание-2":
        dz2(bot, chat_id)

    elif ms_text == "Задание-3":
        dz3(bot, chat_id)

    elif ms_text == "Задание-4":
        dz4(bot, chat_id)

    elif ms_text == "Задание-5":
        dz5(bot, chat_id)

    elif ms_text == "Задание-6":
        dz6(bot, chat_id)

name = 'Соня'
age = 18

# -----------------------------------------------------------------------
def dz1(bot, chat_id):
    bot.send_message(chat_id, text=name)


def dz2(bot, chat_id):
    bot.send_message(chat_id, text=f'Меня зовут {name} и мне {age} лет')


def dz3(bot, chat_id):
    bot.send_message(chat_id, text=(name+" ")*5)


def dz4(bot, chat_id, message):
    bot.send_message(chat_id, text='Как вас зовут?')

    @bot.message_handler(content_types=['text'])
    def inputName(message):
        user_name = message.text
        bot.send_message(chat_id, text='Сколько вам лет?')

        @bot.message_handler(content_types=['text'])
        def inputAge(message):
            user_age = message.text
            user_message = 'Привет, ' + user_name + '! Тебе уже ' + user_age + ' лет! А выгялдишь на 30))'
            bot.send_message(chat_id, text=user_message)

        bot.register_next_step_handler(message, inputAge)

    bot.register_next_step_handler(message, inputName)


def dz5(bot, chat_id):
    my_inputInt(bot, chat_id, 'Сколько вам лет?', dz5_ResponseHandler)


def dz5_ResponseHandler(bot, chat_id, age_param):
    age_int = int(age_param)

    if age_int < 14:
        user_message = 'друг как так'
    elif age_int < 25:
        user_message = 'ну давай поболтаем'
    else:
        user_message = 'сколько пенсия?'

    bot.send_message(chat_id, text=user_message)


def dz6(bot, chat_id, message):
    bot.send_message(chat_id, text='Ваше имя?')

    m_0 = "Действия с именем"
    m_1 = "Символы со второго до предпоследнего: "
    m_2 = "Задом на перед: "
    m_3 = "Последние три символа: "
    m_4 = "Первые пять символов: "

    @bot.message_handler(content_types=['text'])
    def inputName(message):
        user_name = message.text
        bot.send_message(chat_id, text=m_0)
        bot.send_message(chat_id, text=m_1+user_name[1:-1])
        bot.send_message(chat_id, text=m_2+user_name[::-1])
        bot.send_message(chat_id, text=m_3+user_name[-3:])
        bot.send_message(chat_id, text=m_4+user_name[0:5])

    bot.register_next_step_handler(message, inputName)
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
def my_input(bot, chat_id, txt, ResponseHandler):
    message = bot.send_message(chat_id, text=txt)
    bot.register_next_step_handler(message, ResponseHandler)
# -----------------------------------------------------------------------
def my_inputInt(bot, chat_id, txt, ResponseHandler):

    # bot.send_message(chat_id, text=botGames.GameRPS_Multiplayer.name, reply_markup=types.ReplyKeyboardRemove())

    message = bot.send_message(chat_id, text=txt)
    bot.register_next_step_handler(message, my_inputInt_SecondPart, botQuestion=bot, txtQuestion=txt, ResponseHandler=ResponseHandler)
    # bot.register_next_step_handler(message, my_inputInt_return, bot, txt, ResponseHandler)  # то-же самое, но короче

def my_inputInt_SecondPart(message, botQuestion, txtQuestion, ResponseHandler):
    chat_id = message.chat.id
    try:
        if message.content_type != "text":
            raise ValueError
        var_int = int(message.text)
        # данные корректно преобразовались в int, можно вызвать обработчик ответа, и передать туда наше число
        ResponseHandler(botQuestion, chat_id, var_int)
    except ValueError:
        botQuestion.send_message(chat_id,
                         text="Можно вводить ТОЛЬКО целое число в десятичной системе исчисления (символами от 0 до 9)!\nПопробуйте еще раз...")
        my_inputInt(botQuestion, chat_id, txtQuestion, ResponseHandler)  # это не рекурсия, но очень похоже
        # у нас пара процедур, которые вызывают друг-друга, пока пользователь не введёт корректные данные,
        # и тогда этот цикл прервётся, и управление перейдёт "наружу", в ResponseHandler

# -----------------------------------------------------------------------

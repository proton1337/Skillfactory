import telebot
from config import keys,TOKEN
from extensions import ConvertionException, BotTeleg

bot=telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start','help'])
def help(message: telebot.types.Message):
    text='Чтобы начать работу введите команду боту в следующем формате: \n<Имя валюты цену которой он хочет узнать> \
<имя валюты в которой надо узнать цену первой валюты>\
<количество первой валюты>\nУвидеть список всех доступных валют: /values'
    bot.reply_to(message,text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text='Доступные валюты:'
    for key in keys.keys():
        text='\n'.join((text,key,))
    bot.reply_to(message,text)

@bot.message_handler(content_types=['text',])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        if len(values) != 3:
            raise ConvertionException('Слишком много параметров.')

        quote, base, amount = values
        total_base=BotTeleg.get_price(quote,base,amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message,f'Не удалось обработать команду\n{e}')
    else:
        amount=float(amount)
        total_base=float(total_base)
        total=round(amount*total_base,2)
        if amount %2==0 or amount==1:
            amount=int(amount)

        text=f'Цена {amount} {quote} в {base} - {total}'
        bot.send_message(message.chat.id,text)

bot.polling()
import telepot
import multiplication_logic as mt
from telepot.loop import MessageLoop
numbers = []


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    msg = msg['text']
    if msg == 'Ola' or msg == 'Bom dia' or msg == 'Boa tarde' or msg == 'Calculadora':
        bot.sendMessage(chat_id, 'Olá, preciso que digite dois números para que possam ser multiplicados.')
    else:
        numbers.append(msg)
        if len(numbers) == 1:
            bot.sendMessage(chat_id, 'Digite outro número.')
        elif len(numbers) == 2:
            bot.sendMessage(chat_id, mt.multiplication(numbers[0], numbers[1]))
            numbers.clear()
    # else:
    #    bot.sendMessage(chat_id, 'Preciso que digite um número.')


bot = telepot.Bot('1259960426:AAFhrV2um-CixJ5qYkxzO-Y8AZXGOxZqco8')
MessageLoop(bot, handle).run_as_thread()

while True:
    pass

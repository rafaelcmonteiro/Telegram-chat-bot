import telepot
import multiplication_business as mt
from telepot.loop import MessageLoop


class Bot:
    def __init__(self):
        self.bot = telepot.Bot('1259960426:AAFhrV2um-CixJ5qYkxzO-Y8AZXGOxZqco8')
        self.numbers = []

    def bot_reply(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        msg = msg['text']
        if msg == 'Ola' or msg == 'Bom dia' or msg == 'Boa tarde' or msg == 'Calculadora':
            self.bot.sendMessage(chat_id, 'Olá, preciso que digite dois números para que possam ser multiplicados.')
        else:
            self.numbers.append(msg)
            if len(self.numbers) == 1:
                self.bot.sendMessage(chat_id, 'Digite outro número.')
            elif len(self.numbers) == 2:
                self.bot.sendMessage(chat_id, mt.multiplication(self.numbers[0], self.numbers[1]))
                self.numbers.clear()

    def bot_run(self):
        MessageLoop(self.bot, self.bot_reply).run_as_thread()

        while True:
            pass

import telepot
from telepot.loop import MessageLoop
from business import multiplication_business as mt
from business.check_business import Check


class Bot:
    def __init__(self):
        self.bot = telepot.Bot('')
        self.numbers = []

    def bot_reply(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)

        # Check if has any special characters and remove them.
        msg = Check.bot_treat_msg(msg['text'])

        if msg == 'Ola' or msg == 'Bom dia' or msg == 'Boa tarde' or msg == 'Calculadora':
            self.bot.sendMessage(chat_id, 'Olá, preciso que digite dois números para que possam ser multiplicados.')
        else:
            # Check if it's a number or something else.
            is_number = Check.bot_accept_only_numbers(msg)
            if is_number is True:
                self.numbers.append(msg)
                if len(self.numbers) == 1:
                    self.bot.sendMessage(chat_id, 'Digite outro número.')
                elif len(self.numbers) == 2:
                    self.bot.sendMessage(chat_id, mt.multiplication(self.numbers[0], self.numbers[1]))
                    self.numbers.clear()
            else:
                self.bot.sendMessage(chat_id, 'Desculpe, não compreendi os valores enviados.')

    def bot_run(self):
        MessageLoop(self.bot, self.bot_reply).run_as_thread()

        while True:
            pass

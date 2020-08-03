class Check:
    @staticmethod
    def bot_accept_only_numbers(msg):
        """
            Will check if the msg is a number or not.
            :param msg: A string.
            :return: A True or False, depending if it's a number or not.
        """
        try:
            int(msg)
            return True
        except ValueError:
            return False

    @staticmethod
    def bot_treat_msg(msg):
        """
            Just for remember: accent will pass.
            :param msg: A string with or without special characters.
            :return: A string without any special character.
        """
        new_string = ''
        for character in msg:
            if character.isalnum() or character == ' ' or character[0] == '-':
                new_string += character
        return new_string


if __name__ == '__main__':
    # Needed a test if negative numbers is working on telegram.
    string_test = 'essa string tem um special char 1233/*-*/-*/-*....'
    # print(bot_treat_msg(string_test))
    print(Check.bot_accept_only_numbers(string_test))

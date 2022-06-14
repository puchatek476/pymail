USAGE = "Usage: python main.py [--help] | login password [-t <topic>] {-p <path to .txt content> | <content>}]"


class ArgumentsParser:
    """ Class to retrieve information about mail from cmd aruguments including getting info from files. """
    LOGIN_OPTION_FLAG = '-l'
    PASSWORD_OPTION_FLAG = '-p'
    TOPIC_OPTION_FLAG = '-t'
    ADDRESS_OPTION_FLAG = '-a'

    CREDENTIALS_FILE_OPTION_FLAG = '-c'
    CONTENT_FILE_OPTION_FLAG = '-f'

    CONTENT_SEPARATOR = '*%'
    CREDENTIALS_SEPARATOR = '!_sep'

    def __init__(self, args):
        self.args = args

    def get_params_without_options(self):
        """ Returns value of all params provided without any flag. """
        options_indexes = [[self.args.index(arg), self.args.index(arg) + 1] for arg in self.args if arg.startswith('-')]
        options_indexes = [item for sublist in options_indexes for item in sublist]
        return [arg for index, arg in enumerate(self.args) if index not in options_indexes]

    def get_param_with_option(self, option):
        """ Returns values of param given with option flag. """
        if option not in self.args:
            return None
        args = self.args[self.args.index(option):]
        if len(args) == 1:
            return None
        return self.args[self.args.index(option):][1]

    def parse(self):
        credentials_path = self.get_param_with_option(self.CREDENTIALS_FILE_OPTION_FLAG)
        if credentials_path is not None:
            login, password = self.get_credentials_from_file(credentials_path)
        else:
            login = self.get_param_with_option(self.LOGIN_OPTION_FLAG)
            password = self.get_param_with_option(self.PASSWORD_OPTION_FLAG)

        content_path = self.get_param_with_option(self.CONTENT_FILE_OPTION_FLAG)
        if credentials_path is not None:
            address, topic, content = self.get_content_from_file(content_path)
        else:
            topic = self.get_param_with_option(self.TOPIC_OPTION_FLAG)
            topic = topic if topic is not None else ''
            address = self.get_param_with_option(self.ADDRESS_OPTION_FLAG)
            content = self.get_params_without_options()[0]

        return {'login': login,
                'password': password,
                'mail_to': address,
                'content': content,
                'topic': topic}

    def get_credentials_from_file(self, path):
        with open(path, 'r') as file:
            line = file.readline()
        credentials = line.split(self.CREDENTIALS_SEPARATOR)
        return credentials[0].lstrip('\n'), credentials[1].lstrip('\n')

    def get_content_from_file(self, path):
        with open(path, 'r') as file:
            lines = file.readlines()
        one_line = ''.join(lines)
        return one_line.split(self.CONTENT_SEPARATOR)

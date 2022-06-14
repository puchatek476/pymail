from arguments_parser import ArgumentsParser

USAGE = "Usage: python main.py [--help] | login password [-t <topic>] {-p <path to .txt content> | <content>}]"


class ArgumentsManager:
    """ Class to handle actions with passed commandline arguments. """

    def __init__(self, args):
        self.args = args

    def load_args(self, new_args):
        """ Replaces args with new ones. """
        self.args = new_args

    def handle_args(self):
        """ Reacts properly on args. Prints proper output. """
        if '--help' in self.args:
            print(USAGE)
            return None
        else:
            parser = ArgumentsParser(self.args)
            result = parser.parse()
            return result

    def get_args(self):
        parser = ArgumentsParser(self.args)
        result = parser.parse()

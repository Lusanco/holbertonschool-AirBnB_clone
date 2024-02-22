#!/usr/bin/python3
"""
Module: console
Descri: class HBNBCommand interpreter for
managing data.
Author: Livanhernandez, Lusanco
"""


import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBCommand interpreter for managing data."""

    prompt = '(hbnb) '

    def do_quit(self, args):
        """Quits the program."""
        print("Quitting.")
        return True

    def do_EOF(self, args):
        """Exits the program on EOF (Ctrl+D)."""
        print("Exiting.")
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

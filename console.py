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
        print("Exiting on quit command or Ctrl+D.")
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

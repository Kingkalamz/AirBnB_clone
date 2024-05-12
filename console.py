#!/usr/bin/python3
"""Defines the HBnB console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter"""
    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothingbupon receiving an empty line"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF signal ro exit the program"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()

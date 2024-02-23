#!/usr/bin/python3

"""
Module: console
Descri: class HBNBCommand interpreter for
managing data.
Author: Livanhernandez, Lusanco
"""


import cmd
from models import storage
from models.base_model import BaseModel
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    """HBNBCommand interpreter for managing data."""
    prompt = '(hbnb) '

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """EOF command to exit the program"""
        print("")
        return True

    def emptyline(self):
        """Empty line does nothing"""
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it, and prints the id."""
        if not args:
            print("** class name missing **")
            return

        class_name = args.split()[0]

        if class_name not in ["BaseModel"]:
            print("** class doesn't exist **")
            return

        new_instance = BaseModel()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """Prints the string representation of an instance."""
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        
        class_name = args[0]
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(class_name, args[1])
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

        classes = [key.split('.')[0] for key in storage.all().keys()]
        if class_name not in classes:
            print("** class doesn't exist **")
            return

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id."""
        if not args:
            print("** class name missing **")
            return
        
        args = args.split()
        class_name = args[0]

        if class_name not in storage.all().keys():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)

        if key not in storage.all():
            print("** no instance found **")
            return
        
        del storage.all()[key]
        storage.save()

    def do_all(self, args):
        """Prints all string representation of all instances."""
        args = args.split()
        obj_list = []
        if not args:
            for obj in storage.all().values():
                obj_list.append(str(obj))
            print(obj_list)
            return
        
        class_name = args[0]
        classes = [key.split('.')[0] for key in storage.all().keys()]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        for key, obj in storage.all().items():
            if class_name in key:
                obj_list.append(str(obj))
        print(obj_list)

    def do_update(self, args):
        """Updates an instance based on the class name and id."""
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(storage.all()[key], args[2], args[3])
        storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

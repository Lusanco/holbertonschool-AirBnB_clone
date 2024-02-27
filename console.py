#!/usr/bin/python3

"""
Module: console
Descri: class HBNBCommand
interpreter for managing data.
Author: Livanhernandez, Lusanco
"""


import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
import shlex


class HBNBCommand(cmd.Cmd):
    """HBNBCommand interpreter for managing data."""

    prompt = "(hbnb) "

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

        class_name = args

        if class_name not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return

        if class_name == "User":
            new_instance = User()
            new_instance.save()
            print(new_instance.id)
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, args):
        """Prints the string representation of an instance."""
        if not args:
            print("** class name missing **")
            return

        args = args.split()
        class_name = args[0]

        if class_name not in ["BaseModel"]:
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

        print(storage.all()[key])

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id."""
        if not args:
            print("** class name missing **")
            return

        args = args.split()
        class_name = args[0]

        if class_name not in ["BaseModel", "User"]:
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
        classes = [key.split(".")[0] for key in storage.all().keys()]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        for key, obj in storage.all().items():
            if class_name in key:
                obj_list.append(str(obj))
        print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in ["BaseModel", "User"]:
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

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_name = args[2]
        attribute_value = " ".join(args[3:])

        instance = storage.all()[key]

        if not hasattr(instance, attribute_name):
            print("** attribute doesn't exist **")
            return
        setattr(instance, attribute_name, attribute_value)
        instance.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()

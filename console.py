#!/usr/bin/python3

"""
Module: console
Descri: class HBNBCommand interpreter for
managing data.
Author: Livanhernandez, Lusanco
"""


import cmd
import json
from models import storage
from models.base_model import BaseModel


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
        """Does nothing on empty lines"""
        pass

    def do_create(self, args):
        if not args:
            print("** class name missing **")
            return

        class_name = args.split()[0]
        if class_name not in storage.all().keys():
            print("** class doesn't exist **")
            return

        try:
            new_instance = eval(class_name)()
            new_instance.save()
            print(new_instance.id)
        except Exception as e:
            print(f"** Error: {e} **")

    def do_show(self, args):
        """Prints str representation of instance."""
        class_name, *instance_id = args.split()

        if not class_name:
            print("** class name missing **")
            return
        
        if class_name not in storage.all().keys():
            print("** class doesn't exist **")
            return
        
        if not instance_id:
            print("** instance id missing **")
            return
        
        instance = storage.get(class_name, instance_id[0])

        if not instance:
            print("** no instance found **")
            return
        
        print(instance)

    def do_destroy(self, args):
        """Deletes and instance based on the class name and ID."""
        class_name, *instance_id = args.split()

        if not class_name:
            print("** class name missing **")
            return
        
        if class_name not in storage.all().keys():
            print("** class doesn't exist **")
            return
        
        if not instance_id:
            print("** instance id missing **")
            return
        
        instance = storage.get(class_name, instance_id[0])

        if not instance:
            print("** no instance found **")
            return

            storage.delete(instance)
            print("** Instance deleted **")

    def do_all(self, args):
        """Prints all str representations of all instance."""
        class_name = None if not args else args.split()[0]

        filtered_instances = storage.all() if not class_name else storage.all(class_name)

        instance_string = []

        for instance in filtered_instances.value():
            instance_string.append(str(instance))
        
        print("\n".join(instance_string))

    def do_update(self, args):
        """Updates an instance based on the class name, ID, attribute
        name, and attribute value."""
        class_name, instance_id, *attr_args = args.split()

        if not class_name:
            print("** class name missing **")
            return
        
        if not instance_id:
            print("** instance if missing **")
            return
        
        if not attr_args:
            print("** attribute name missing **")
            return
        
        attribute_name, attribute_value = attr_args[0].split(":", 1)

        instance = storage.get(class_name, instance_id)

        if not instance:
            print("** no instance found **")
            return
        
        setattr(instance, attribute_name, attribute_value)

        storage.save()
        print("** Instance updated **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/python3
"""
console.py Program Module
that contains the entry point of the command interpreter:
"""


import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import re


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class:
    the entry point of the command interpreter:
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF (Ctrl-D)\n"""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered\n"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel\n"""
        if not arg:
            print("** class name missing **")
            return
        class_name = arg.split()[0]
        if class_name not in storage.classes_dict:
            print("** class doesn't exist **")
            return
        new_instance = storage.classes_dict[class_name]()
        storage.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance\n"""
        if not arg:
            print("** class name missing **")
            return
        args_list = arg.split()
        class_name = args_list[0]
        if class_name not in storage.classes_dict:
            print("** class doesn't exist **")
            return
        if len(args_list) < 2:
            print("** instance id missing **")
            return
        instance_id = args_list[1]
        key = f"{class_name}.{instance_id}"
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on class name and id\n"""
        if not arg:
            print("** class name missing **")
            return
        args_list = arg.split()
        class_name = args_list[0]
        if class_name not in storage.classes_dict:
            print("** class doesn't exist **")
            return
        if len(args_list) < 2:
            print("** instance id missing **")
            return
        instance_id = args_list[1]
        key = f"{class_name}.{instance_id}"
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string repr of instances based on class name\n"""
        instance_list = []
        if not arg:
            for value in storage.all().values():
                instance_list.append(str(value))
            print(instance_list)
            return
        class_name = arg.split()[0]
        if class_name in storage.classes_dict:
            for key, value in storage.all().items():
                if class_name in key:
                    instance_list.append(str(value))
            print(instance_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on class name and id\n"""
        if not arg:
            print("** class name missing **")
            return
        args_list = arg.split()
        class_name = args_list[0]
        if class_name not in storage.classes_dict:
            print("** class doesn't exist **")
            return
        if len(args_list) < 2:
            print("** instance id missing **")
            return
        instance_id = args_list[1]
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args_list) < 3:
            print("** attribute name missing **")
            return
        attr_name = args_list[2].strip('"')
        if len(args_list) < 4:
            print("** value missing **")
            return
        attr_value = args_list[3].strip('"')
        attr_type = None
        instance = storage.all()[key]
        if hasattr(instance, attr_name):
            attr_type = type(getattr(instance, attr_name))
        try:
            casted_value = attr_type(attr_value)
        except Exception:
            casted_value = attr_value
        setattr(instance, attr_name, casted_value)
        instance.save()

    def do_count(self, arg):
        """Retrieves the number of instances of a class\n"""
        num_of_instance = 0
        if not arg:
            num_of_instance = len(storage.all())
            print(num_of_instance)
            return
        class_name = arg.split()[0]
        if class_name in storage.classes_dict:
            for key in storage.all():
                if class_name in key:
                    num_of_instance += 1
            print(num_of_instance)
        else:
            print("** class doesn't exist **")

    def precmd(self, line):
        """Called before the command is executed by onecmd()\n"""
        pattern = r'([A-Za-z]+)\.([A-Za-z]+)\(("([^"]+)",?\s?(.*)?)?\)'
        arg_parts = re.match(pattern, line)
        if arg_parts is None:
            return line
        class_name = arg_parts.group(1)
        command = arg_parts.group(2)
        instance_id = arg_parts.group(4)
        args = arg_parts.group(5)

        if command is None:
            return line
        if command in ["all", "count"]:
            if class_name:
                return f"{command} {class_name}"
            return f"{command}"
        if command in ["show", "destroy"]:
            if class_name and instance_id:
                return f"{command} {class_name} {instance_id}"
            if class_name:
                return f"{command} {class_name}"
            return f"{command}"
        if command == "update":
            attr_name = None
            attr_value = None
            if args:
                if args.startswith("{") and args.endswith("}"):
                    try:
                        args_dict = json.loads(args)
                        for key, value in args_dict.items():
                            arguments = f"{instance_id} {key} {value}"
                            self.onecmd(f"{command} {class_name} {arguments}")
                        return ""
                    except Exception:
                        return line
                else:
                    args_list = args.split(", ")
                    attr_name = args_list[0]
                    if len(args_list) >= 2:
                        attr_value = args_list[1]
            return self.process_args(
                command, class_name, instance_id, attr_name, attr_value
            )
        return line

    def process_args(
            self, command, class_name, instance_id, attr_name, attr_value
    ):
        """A function that handles error management for precmd update()"""
        if class_name and instance_id and attr_name and attr_value:
            arguments = f"{instance_id} {attr_name} {attr_value}"
            return f"{command} {class_name} {arguments}"
        if class_name and instance_id and attr_name:
            arguments = f"{instance_id} {attr_name}"
            return f"{command} {class_name} {arguments}"
        if class_name and instance_id:
            return f"{command} {class_name} {instance_id}"
        if class_name:
            return f"{command} {class_name}"
        return f"{command}"


if __name__ == '__main__':
    HBNBCommand().cmdloop()

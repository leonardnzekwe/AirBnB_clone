#!/usr/bin/python3
"""
console.py Program Module
that contains the entry point of the command interpreter:
"""


from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import cmd


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
            for key, value in storage.all().items():
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
        attr_name = args_list[2]
        if len(args_list) < 4:
            print("** value missing **")
            return
        attr_value = args_list[3].strip('"')
        attr_type = None
        instance = storage.all()[key]
        if hasattr(instance, attr_name):
            attr_type = type(getattr(instance, attr_name))
        if attr_type:
            casted_value = attr_type(attr_value)
        else:
            casted_value = attr_value
        setattr(instance, attr_name, casted_value)
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

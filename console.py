#!/usr/bin/python3
"""
console.py Program Module
that contains the entry point of the command interpreter:
"""


from models import storage
from models.base_model import BaseModel
import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class:
    the entry point of the command interpreter:
    """
    prompt = "(hbnb) "
    class_list = ["BaseModel"]

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF (Ctrl-D)\n"""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        try:
            obj = eval(arg)()
            obj.save()
            print(obj.id)
        except Exception:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of instances based on class name"""
        args = arg.split()
        obj_list = []
        if len(args) == 0:
            for key, value in storage.all().items():
                obj_list.append(str(value))
            print(obj_list)
        elif args[0] in HBNBCommand.class_list:
            for key, value in storage.all().items():
                if args[0] in key:
                    obj_list.append(str(value))
            print(obj_list)
        else:
            print("** class doesn't exist **")
            return

    def do_update(self, arg):
        """Updates an instance based on class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = storage.all()[key]
        attr_name = args[2]
        attr_value = args[3].strip('"')
        attr_type = None
        if hasattr(obj, attr_name):
            attr_type = type(getattr(obj, attr_name))
        if attr_type:
            converted_value = attr_type(attr_value)
        else:
            converted_value = attr_value
        setattr(obj, attr_name, converted_value)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/python
"""A module that handles command interpreter"""

import cmd
import sys
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from shlex import split

class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb)"
    all_classes = ["BaseModel", "User", "State", "City", "Place", "Review", "Amenity"]

    def emptyline(self):
        """ a method that overrides when an emptyline is entered"""
        return super().emptyline()

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def do_create(self, cls):
        """Creates a new instance of BaseModel, save it(to JSON file)"""
        if cls:
            if cls in self.all_classes:
                my_class = getattr(sys.modules[__name__], cls)
                obj = my_class()
                print(obj.id)
                models.storage.save()
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    
    def do_update(self, arg):
        """updates an instance ased on the class name and id """
        chk = split(arg)
        print(chk)
        if len(chk) > 4:
            args = arg.split(' ', 2)
            args[1] = args[1].replace("'", '')
            args[2] = args[2].strip()
            args[2] = args[2].replace("' ", "', ")
        else:
            args = split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name is missing **")
        elif args[0] in self.all_classes and len(args) == 3:
            key = args[0] + '.' + args[1]
            my_dict = models.storage.all()
            if key in my_dict:
                new_dict = eval(args[2])
                for attr, value in new_dict.items():
                    if hasattr(my_dict[key], attr):
                        attr_type = type(getattr(my_dict[key], attr))
                        value = attr_type(value)
                        setattr(my_dict[key], attr, value)
                    else:
                        setattr(my_dict[key], attr, value)
                my_dict[key].save()
            else:
                print("** attribute value missing **")
        elif args[0]  in self.all_classes and len(args) == 4:
            key = args[0] + '.' + args[1]
            my_dict = models.storage.all()
            if key in my_dict:
                if hasattr(my_dict[key], args[2]):
                    a_type = type(getattr(my_dict[key], args[2]))
                    args[3] = a_type(args[3])
                setattr(my_dict[key], args[2], args[3])
                my_dict[key].save()
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """prints alll string representation of all instances"""
        my_dict = models.storage.all()
        all_list = []
        if len(arg) == 0:
            for key in my_dict:
                all_list.append(str(my_dict[key]))
        else:
            if arg in self.all_classes:
                for key, value in my_dict .items():
                    if arg == value.to_dict() ['__class__']:
                        all_list.append(str(value))
            else:
                print("** class doesn't exist **")
                return
        print(all_list)

    def do_show(self,  arg):
        """ prints the string representation of an instance"""
        args = split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
                print("** instance id missing **")
        elif args[0] in self.all_classes:
            my_dict = models.storage.all()
            key = args[0] + '.' + args[1]
            if key in my_dict:
                print(my_dict[key])
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_delete(self, arg):
        """deletes an instance based on the class name and id"""
        args = split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] in self.all_classes:
            my_dict = models.storage.all()
            key = args[0] + '.' + args[1]
            if key in my_dict:
                del my_dict[key]
                models.storage.save()
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")
        
        

    def precmd(self, line):
        """ parse precmd method"""
        parts = line.split(".", 1)
        if len(parts) == 2:
            a_class = parts[0]
            args = parts[1].split("(", 1)
            cmd = args[0]
            new_line = cmd + " " + a_class
            if len(args) == 2:
                args = args[1].split(')', 1)
                args = args[0].split(",")
                a_id = args[0].strip()
                new_line = cmd + " " + a_class + " " + a_id
                if len(args) > 1:
                    others = args[1:]
                    s = ""
                    for c in others:
                        s += c
                    s = s.replace("\"", "")
                    new_line = cmd + " " + a_class + " " + a_id + " " + s
            return new_line
        return line
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()
    

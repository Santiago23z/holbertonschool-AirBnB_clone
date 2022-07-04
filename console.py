#!/usr/bin/python3
"""program that contains the entry point of the command interpreter"""

import cmd
import shlex
import re
import json
from models import storage

class HBNBCommand(cmd.Cmd):
    """command interpreter implementation"""
    prompt = '(hbnb) '
    classes = storage.class_dict()
    
    def do_create(self, arg):
        """create command to create a new instance according with
        the Class name.
        Print the assigned id.
        Usage: create <class name>
        Classes: [BaseModel, User, Place, State, City, Amenity, Review]"""
        if arg == ""or arg is None:
            print("** class name missing **")
        elif arg not in HBNBCommand.classes:
            print ("** class does´t exist **")
        else:
            new = HBNBCommand.classes[arg]()
            new.save()
            print(new.id)
            
    def do_update(self, arg):
        """update command to update an isntance based on the class name
        and id by adding or updating attribute
        Usage: update <class name> <id> <attribute name> "<attribute value>""""
        inputs = shlex.split(arg)
        if arg == "" or arg is None:
            print("** class name missing **")
        elif input [0] not in HBNBCommand.classes:
            print("** instance doesn´t exist **")
        elif len(inputs) < 2:
            print("** instance id is missing **")
        elif len(inputs) < 3:
            print("** attribute name missing **")
        elif len(inputs) < 4:
            print("** value missing **")
        else:
            class_name = inputs[0]
            obj_id = inputs[1]
            attribute = inputs[2]
            obj_key = "{}.{}".format(class_name, obj_id)
            if obj_key not in storage.all():
                print("** no instance found **")
            else:
                try:
                    cast = type(getattr(storage.all()[obj_key], attribute))
                except AttributeError:
                    cast = type(inputs[3])
                #open to anny attr, even those wich are not defined
                value = cast cast(inputs[3])
                setattr(storage.all()[obj_key], attribute, value)
                storage.all()[obj_key].save()
    
    def do_show(self, arg):
        """show command to print the string representation of an isntance
        based on the class name and id.
        Usage: show <class name> <id>"""
        inputs = arg.split()
        if arg == "" or arg is None:
            print("** class name missing **")
        elif inputs[0] not in HBNBCommand.classes:
            print("** class doesn´t exist **")
        elif len(inputs) < 2:
            print("** instance id missing **")
        else:
            obj_key = "{}.{}".format(inputs[0], inputs[1])
            if obj_key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[obj_key])
                
    def do_destroy(self, arg):
        """Destroy command to delete an isntance based on the class name and id.
        Usage: destroy <class name> <id>"""
        inputs = arg.split()
        if arg == "" or arg is None:
            print("** class name missing **")
        elif inputs[0] not in HBNBCommand.classes:
            print("** class doesn´t exist **")
        elif len(inputs) < 2:
            print("** instance id missing **")
        else:
            obj_key = "{}.{}".format(inputs[0], inputs[1])
            if obj_key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[obj_key]
                storage.save()
                
    def do_all(self, arg):
        """All commands to print all string representation af alla instances 
        based or not on the class name.
        Usage: all <class name (optional)>
        E.g: all       -------Prints all instances
             all user  -------Prints user instances"""
        inputs = arg.split()
        objs = storage.all()
        if not arg:
            print([str(obj) for obj in objs.values()])
        else:
            if inputs[0] in HBNBCommand.classes:
                print([str(obj) for obj in objs.values()
                        if type(obj).__name__ == arg])
            else:
                print("** class doesn´t exist **")
                
    def do_quit(self, arg):
        """quit command to exit the program"""
        return True
        
    def do_EOF(self, arg):
        """EOF command to quit and exit the program by EOF (CTR+D)"""
        return True
        
    def count(self, arg):
    
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
        inputs = 
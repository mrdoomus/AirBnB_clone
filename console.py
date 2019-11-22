#!/usr/bin/python3
''' Module that supports the console behavior
HBNBCommand - Initializes and supports the console behavior
'''
import cmd
import models
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User
from models.state import State
from models import storage

file_classes = {"BaseModel": BaseModel, "Amenity": Amenity,
                "City": City, "Place": Place,
                "Review": Review, "User": User,
                "State": State}


class HBNBCommand(cmd.Cmd):
    '''Behavior of the hbnb console'''
    prompt = '(hbnb) '

    def do_create(self, line):
        '''Creates a new instance of a class
        Use: create [CLASS]
        Ex: create BaseModel
        '''
        if len(line) > 0 and line is not None:
            try:
                new = eval(line)()
                storage.new(new)
                storage.save()
                print(new.id)
            except NameError:
                print("** class doesn't exist **")
        else:
            print('** class name missing **')

    def do_show(self, line):
        '''Prints the string representation of an instance.
        Use: show [CLASS] [ID]
        Ex: show BaseModel 1234-1234-1234.
        '''
        if len(line) < 1 or line is None:
            print('** class name missing **')
        else:
            cmds = line.split(' ')
            if cmds[0] not in file_classes:
                print("** class doesn't exist **")
            else:
                try:
                    cmds[1]
                except IndexError:
                    print("** instance id missing **")
                    return

                name = "{}.{}".format(cmds[0], cmds[1])
                if name not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[name])

    def do_destroy(self, line):
        '''Deletes an instance based on the class name and id.
        Use: destroy [CLASS] [ID]
        Ex: destroy BaseModel 1234-1234-1234
        '''
        if len(line) < 1 or line is None:
            print("** class name missing **")
        else:
            cmds = line.split(' ')
            if cmds[0] not in file_classes:
                print("** class doesn't exist **")
            else:
                try:
                    cmds[1]
                except IndexError:
                    print("** instance id missing **")
                    return

                name = "{}.{}".format(cmds[0], cmds[1])
                if name not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[name]
                    storage.save()

    def do_all(self, line):
        '''Prints all string representation of all instances.
        Use: all [CLASS] or all
        Ex: all BaseModel or all
        '''
        string = []
        if len(line) > 0:
            cmds = line.split(' ')
            if cmds[0] not in file_classes:
                print("** class doesn't exist **")
            else:
                for key, obj in storage.all().items():
                    if cmds[0] == type(obj).__name__:
                        string.append(str(obj))
                print(string)
        else:
            for key, obj in storage.all().items():
                string.append(str(obj))
            print(string)

    def do_update(self, line):
        '''Update instance attribute and save changes to JSON file.
        Use: update [CLASS] [ID] [ATTRIBUTE] [VALUE]
        Ex: update BaseModel 1234-1234-1234 email "doom@gmail.com"
        '''
        if len(line) < 1 or line is None:
            print("** class name missing **")
        else:
            cmds = line.split(' ')
            if cmds[0] not in file_classes:
                print("** class doesn't exist **")
            else:
                try:
                    cmds[1]
                except IndexError:
                    print("** instance id missing **")
                    return
                name = "{}.{}".format(cmds[0], cmds[1])
                if name not in storage.all():
                    print("** no instance found **")
                else:
                    try:
                        cmds[2]
                    except IndexError:
                        print("** attribute name missing **")
                        return
                    try:
                        cmds[3]
                    except IndexError:
                        print("** value missing **")
                        return
                    value = cmds[3].replace('"', '')
                    setattr(storage.all()[name], cmds[2], value)
                    storage.save()

    def default(self, line):
        '''CMD behavior when no command is passed in console
        '''
        cmds = line.split('.')
        values_parenthesis = cmds[1].split('(')
        command = values_parenthesis[0]
        values_parenthesis = values_parenthesis[1][:-1]
        values_commas = values_parenthesis.split(',')
        values_bracket = line.split('{')

        if command == 'all':
            return self.do_all(cmds[0])
        elif command == 'count':
            count = 0
            for num in storage.all().values():
                if cmds[0] == type(num).__name__:
                    count += 1
            print(count)
        elif command == 'show':
            full_line = cmds[0] + ' ' + values_parenthesis
            return self.do_show(full_line)
        elif command == 'destroy':
            full_line = cmds[0] + ' ' + values_parenthesis
            return self.do_destroy(full_line)
        elif command == 'update':
            if len(values_bracket) == 1:
                full_line = cmds[0] + ' ' + values_commas[0] + ' ' \
                    + values_commas[1][1:] + ' ' + values_commas[2][1:]
                return self.do_update(full_line)
            else:
                value_dict = eval('{' + values_bracket[1][:-1])
                value_dict = dict(value_dict)
                for key, value in value_dict.items():
                    full_line = cmds[0] + ' ' + values_commas[0] + ' ' \
                        + str(key) + ' ' + str(value)
                    self.do_update(full_line)
                return

    def do_quit(self, line):
        '''Quit command to exit the program
        '''
        return True

    def do_EOF(self, line):
        '''Execute Ctrl+D to exit the program
        '''
        return True

    def emptyline(self):
        '''emptyline
        '''
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

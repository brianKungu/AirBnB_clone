#!/usr/bin/python3
"""
Command interpreter for  AirBnB project
"""
import cmd
from mimetypes import common_types
from models import storage, CNC

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_create(self, args:str):
        # creates an instance of the BaseModel saves the Json file and prints the id

        # initiate a list of commands
        commands = args.split()

        if len(commands) == 0:
            print("**Class name is missing**")
            return
        try: 
            eval(commands[0])
        except NameError:
            print("**Class doesn't exist**")
            return
        try:
            newObject = eval(commands[0])()
            print(newObject.id)
            newObject.save()
        except Exception as e:
            print("Exception: ", e)

if __name__ == '__main__':
    """
    MAIN Loop
    """
    HBNBCommand().cmdloop()

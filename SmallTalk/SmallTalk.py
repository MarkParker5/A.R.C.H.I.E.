#   Create class SmallTalk
#   Is child of Command
#   Module for speaking with voice assistent
#   See class Command



from Command import Command                     #   import parent class

class SmallTalk(Command):
    def start(this, string):                    #   main method
        print('Im using SmallTalk now :)')

    def confirm(this):                          #   optional method
        return True

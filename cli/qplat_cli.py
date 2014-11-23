import cmd

class QplatCli(cmd.Cmd):
    """Qplat command interpreter"""

    prompt = "$ "
    intro = " *** Qplat command interpreter ***"

    def emptyline(self):
        pass

    def do_echo(self, line):
        print line

    def do_quit(self, line):
        print "Bye..."
        return True

    def do_deposit(self, line):
        print "Depositing..."

    def do_holdings(self, line):
        print "These are the holdings..."

if __name__ == '__main__':
    QplatCli().cmdloop()


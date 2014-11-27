import cmd
import sys
import qplat_api

#######################################################################
# Functions to parse and execute commands
#######################################################################


def exec_echo(line):
    print line


def exec_quit(line):
    print 'bye...'
    sys.exit()


def exec_deposit(line):
    qplat_api.deposit(*line.split())


def exec_ingest(line):
    qplat_api.ingest(line)


def exec_holdings(line):
    print "holdings..."
    pass

#######################################################################


class QplatCli(cmd.Cmd):
    """Qplat command interpreter"""

    print " *** Qplat command interpreter ***"

    prompt = "$ "

    def emptyline(self):
        pass

    def do_echo(self, line):
        exec_echo(line)

    def do_quit(self, line):
        exec_quit(line)

    def do_deposit(self, line):
        exec_deposit(line)

    def do_ingest(self, line):
        exec_ingest(line)

    def do_holdings(self, line):
        exec_holdings(line)

if __name__ == '__main__':
    while True:
        try:
            QplatCli().cmdloop()
        except Exception as e:
            print "Exception: %s" % e

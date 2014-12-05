import cmd
import sys
import qplat_api
import traceback

class QplatCli(cmd.Cmd):
    """Qplat command interpreter"""

    api = qplat_api.QplatApi()

    #######################################################################
    # Functions to parse and execute commands
    #######################################################################

    def exec_echo(line):
        print line


    def exec_quit(line):
        print 'bye...'
        sys.exit()


    def exec_deposit(self, line):
        self.api.deposit(*line.split())


    def exec_ingest(self, line):
        self.api.ingest(line)


    def exec_holdings(self, line):
        print "holdings..."

    def exec_dbinfo(self):
        version, tables, connections = self.api.dbinfo();
        print "Version: %s" % version
        print "Tables: %s" % tables
        print "Connections: %s" % connections
    #######################################################################

    print " *** Qplat command interpreter ***"

    prompt = "$ "



    def emptyline(self):
        pass

    def do_echo(self, line):
        self.exec_echo(line)

    def do_quit(self, line):
        self.exec_quit(line)

    def do_deposit(self, line):
        self.exec_deposit(line)

    def do_ingest(self, line):
        self.exec_ingest(line)

    def do_holdings(self, line):
        self.exec_holdings(line)

    def do_dbinfo(self, line):
        self.exec_dbinfo()

if __name__ == '__main__':
    while True:
        try:
            QplatCli().cmdloop()
        except Exception as e:
            print "Exception: %s" % e
            traceback.print_exc()

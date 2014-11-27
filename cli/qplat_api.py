import datetime as dt
import json
import pprint

def deposit(deposit_date, account, symbol, quantity):
    datetime = dt.datetime.strptime(deposit_date)
    pass


def ingest(file_path):
    """ Ingest the given file """
    print "Ingesting: file: [%s]" % file_path
    with open(file_path) as data_file:
        data = json.load(data_file)
        pprint(data)
    pass
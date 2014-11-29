import datetime as dt
import json

def deposit(deposit_date, account, symbol, quantity):
    datetime = dt.datetime.strptime(deposit_date)
    pass


def ingest(file_path):
    """ Ingest the given file """
    print "Ingesting: file: %s" % file_path

    with open(file_path) as data_file:
        data = json.load(data_file)
        ingest_items_list = data['ingest-items']
        print "Ingest items list:\n", json.dumps(ingest_items_list, indent=4)
        for item in ingest_items_list:
            print item
            print "DO SOMETHING HERE..."
        pass


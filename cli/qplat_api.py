import datetime as dt
import json
import psycopg2

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

def dbinfo():
    try:
        conn=psycopg2.connect(dbname='qplat', user='qplatuser')
    except Exception as e:
        print "Cannot connect to db: %s" % e
        return

    try:
        cur = conn.cursor()

        # Get version
        cur.execute("SELECT version();")
        version = cur.fetchall()

        # Get tables
        cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public' AND table_type='BASE TABLE';")
        tables = cur.fetchall()

        return version, [table[0] for table in tables]
    except Exception as e:
        print "Trouble trying to get db info: %s" % e
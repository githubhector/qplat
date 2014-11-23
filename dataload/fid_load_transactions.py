""" Utility to load fidelity transaction history files
"""

import sys
import csv
import mappers

usage = "Usage: fid_load_transactions.py <path-to-fid-transactions-file>"

if len(sys.argv) != 2:
    print "Wrong number of parameters:", usage
    exit(1)

transactions_file = sys.argv[1]
print "Fidelity transaction history file:", transactions_file

file_obj = open(transactions_file)
reader = csv.DictReader(file_obj, delimiter=",")

for fid_transaction in reader:
    qplat_transaction = mappers.map_transaction_fid_to_qplat(fid_transaction)
    print "\nfid_transaction:", fid_transaction
    print "qplat_transaction:", dir(qplat_transaction)





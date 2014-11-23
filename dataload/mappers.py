import dto
import unittest

def map_transaction_fid_to_qplat(fid_transaction):

    d = dto.Dto()

    d.date = fid_transaction['Run Date']
    d.acct = fid_transaction['Account']
    d.action = fid_transaction['Action']
    d.symbol = fid_transaction['Symbol']
    d.quantity = fid_transaction['Quantity']
    d.price = fid_transaction['Price ($)']
    d.commission = fid_transaction['Commission ($)']
    d.fees = fid_transaction['Fees ($)']
    d.amount = fid_transaction['Amount ($)']

    return d

class TestMappers(unittest.TestCase):
    def test_mappers_1(self):
        print "*** TEST 1 ***"

       # 10/20/2014,SIMPLE IRA - Magpie 348301957, YOU BOUGHT, SPY, SPDR S&P 500 ETF TRUST UNIT SER 1 S&P,Cash,140,189.15, 7.95,,,-26488.95, 10/23/2014
        fid_transaction = {
            'Run Date': '10/20/2014',
            'Account': 'SIMPLE IRA - Magpie 348301957',
            'Action': 'YOU BOUGHT',
            'Symbol': 'SPY',
            'Quantity': '140',
            'Price ($)': '189.15',
            'Commission ($)': '7.95',
            'Fees ($)': '0.00',
            'Amount ($)': '-26488.95'
        }

        qplat_transaction = map_transaction_fid_to_qplat(fid_transaction)
        print "HERE"
        print qplat_transaction.__dict__






if __name__ == '__main__':
    unittest.main()

import csv
import datetime
import coinmarketcap
import json
import requests

url= 'http://api.bitcoincharts.com/v1/markets.json'
#url= 'https://api.coinmarketcap.com/v1/ticker/'
class Constants:
    mainPath="/cryptodata/"

def writeCryptoData():
    r = requests.get(url)
    request_time = r.elapsed.total_seconds()
    response = json.loads(r.content.decode('UTF-8'))
    mydate = datetime.datetime.now()
    csvstr = datetime.datetime.strftime(mydate, '%d-%m-%Y')
    uniqueFileName = csvstr + ".csv"
    headings=['currency', 'high','low', 'latest_trade','weighted_price','bid','volume', 'ask', 'duration','close','avg','symbol','currency_volume']
    try:
        with open(Constants.mainPath+uniqueFileName, 'w', newline='') as myCSVFile:
            csvWriter = csv.DictWriter(myCSVFile, fieldnames=headings, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
            csvWriter.writeheader()
            for data in response:
                csvWriter.writerow(data)
    except IOError as errno:
        print("I/O error({0})".format(errno))

if __name__== "__main__":
    writeCryptoData()

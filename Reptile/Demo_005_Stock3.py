# 下载个股历史数据
import csv
import urllib.request as r
import threading


# 读取之前获取的个股csv丢入到一个列表中
def getStockList():
    stockList = []
    f = open('D:/001_GitHub/Project_004_StockPractise/Reptile/data/stock.csv', 'r', encoding='gbk')
    f.seek(0)
    reader = csv.reader(f)
    for item in reader:
        stockList.append(item)
    f.close()
    return stockList


def downloadFile(url, filepath):
    try:
        r.urlretrieve(url, filepath)
    except Exception as e:
        print(e)
    print(filepath, "is downloaded")
    pass


# 设置信号量，控制线程并发数
sem = threading.Semaphore(1)


def downloadFileSem(url, filepath):
    with sem:
        downloadFile(url, filepath)


urlStart = 'http://quotes.money.163.com/service/chddata.html?code='
urlEnd = '&end=20200722&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;VOTURNOVER;VATURNOVER'

if __name__ == '__main__':
    stockList = getStockList()
    stockList.pop(0)
    for s in stockList:
        scode = str(s[1])
        # 0：沪市；1：深市
        url = urlStart + ("0" if scode.startswith('6') else "1") + scode + urlEnd
        filepath = 'D:/001_GitHub/Project_004_StockPractise/Reptile/data/' + (str(s[0]) + '_' + scode) + '.csv'
        threading.Thread(target=downloadFileSem, args=(url, filepath)).start()

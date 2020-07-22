# 导入需要使用到的模块
import urllib
import urllib.request
import re
import os


# 爬虫抓取网页函数
def getHtml(url):
    html = urllib.request.urlopen(url).read()
    html = html.decode('gb2312')
    return html


# 获取所有的股票编号，正则表达式带（）时，返回值只包含括号里内容，即股票编号数组
def getStackCode(html):
    s = r'<li><a target="_blank" href="http://quote.eastmoney.com/\S\S(.*?).html">'
    pat = re.compile(s)
    code = pat.findall(html)
    return code


Url = 'http://quote.eastmoney.com/stocklist.html'  # 东方财富网股票网址
filepath = 'D:\\data\\python\\stock\\'  # 定义数据文件保存路径
# 进行抓取
code = getStackCode(getHtml(Url))
# 获取所有以6开头的股票代码的集合
CodeList = []
for item in code:
    if item[0] == '6':
        CodeList.append(item)
# 将网页上文件下载并保存到本地csv文件，注意日期
for code in CodeList:
    print('正在获取股票%s数据' % code)
    url = 'http://quotes.money.163.com/service/chddata.html?code=0' + code + \
          '&end=20190228&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP'
    urllib.request.urlretrieve(url, filepath + code + '.csv')
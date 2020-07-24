import pandas as pd
import requests
from lxml import etree
import csv

res = requests.get('http://www.csres.com/notice/50655.html')
# res = requests.get('http://quote.eastmoney.com/stocklist.html')
res_elements = etree.HTML(res.text)
table = res_elements.xpath('//table[@id="table1"]')
# table = res_elements.xpath('//table[@id="table_wrapper-table"]')
table = etree.tostring(table[0], encoding='utf-8').decode()

df = pd.read_html(table, encoding='utf-8', header=0)[0]
results = list(df.T.to_dict().values())  # 转换成列表嵌套字典的格式

print(results)

df.to_csv("std.csv", index=False)
#
# with open('D:\\001_GitHub\\Project_004_StockPractise\\Reptile\\std2.csv', 'w', newline='', encoding="gbk") as flow:
#     # 获取_source 下的所有字段名
#     names = results[0]['序号'].values()
#     csv_writer = csv.writer(flow)
#     csv_writer.writerow(names)
#     for res in results:
#         res['序号']['标准编号']['标准名称']['代替标准号']['发布日期']['实施日期'] += ' \t'
#         csv_writer.writerow(res['序号'].values())
#         csv_writer.writerow(res['标准编号'].values())
#         csv_writer.writerow(res['标准名称'].values())
#         csv_writer.writerow(res['代替标准号'].values())
#         csv_writer.writerow(res['发布日期'].values())
#         csv_writer.writerow(res['实施日期'].values())
# print("done!")


#!/usr/bin/python
 
from bs4 import BeautifulSoup
import requests
import xlrd
import time
import xlwt

kaifaVal = {}
faxingVal = {}

def parse_html(index, url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER'}
    #get从网页获取信息
    res = requests.get(url,headers=headers)
    #解析内容
    bs = BeautifulSoup(res.content,'lxml')
    name_ary = []
    value_ary = []
    for item in bs.select('.basicInfo-item.name'):
        name_ary.append(item.string)
    for item in bs.select('.basicInfo-item.value'):
        value_ary.append(item.string)
    
    for i in range(len(name_ary)):
        if name_ary[i] == "开发商":
          print(value_ary[i])
          kaifaVal[index] = value_ary[i]
        if name_ary[i] == "发行商":
          faxingVal[index] = value_ary[i]

def read_xls():
    print("start read and request html")
    data = xlrd.open_workbook('./apps-1-200.xls')
    table = data.sheets()[0]
    num_rows = table.nrows 
    for cur in range(num_rows):
        row = table.row_values(cur)
        # print('row-%s is %s' %(cur,row[2]))
        name = row[2]
        if cur == 0: # 跳过第一行
          continue
        url = "https://baike.baidu.com/item/"+name 
        print(cur,url)
        time.sleep(0.2) # 休眠200ms
        parse_html(row[0], url)

def write_xls():
    print("start write xls")
    print(kaifaVal)
    print(faxingVal)
    data = xlrd.open_workbook('./apps-1-200.xls')
    table = data.sheets()[0]
    num_rows = table.nrows

    # 创建一个新的工作薄
    wb = xlwt.Workbook(encoding="utf-8")
    # 在其上创建一个新的工作表
    ws = wb.add_sheet('S1', cell_overwrite_ok=True)

    # 按单元格方式添加数据
    ws.write(0, 0, 'HELLO')
    # 整行整列的添加数据
    # title = ['序号', 'IOS排名', '应用名称', '开发商', '分类', 'IBU', '开发商中文','发行商', '是否UCloud账户']
    for cur in range(num_rows):
        if cur == 0:
            continue
        row = table.row_values(cur)
        kaifa_name = kaifaVal.setdefault(row[0]," ")
        faxing_name = faxingVal.setdefault(row[0]," ")
        ws.write(cur, 0, row[0])
        ws.write(cur, 1, row[1])
        ws.write(cur, 2, row[2])
        ws.write(cur, 3, row[3])
        ws.write(cur, 4, row[4])
        ws.write(cur, 5, row[5])
        ws.write(cur, 6, kaifa_name)
        ws.write(cur, 7, faxing_name)
        ws.write(cur, 8, row[8])
    # 保存文件
    wb.save('apps-1-200_result1.xls')
        

     
 
#主函数
def main():
    read_xls()
    write_xls()
    print("Success")
            
 
if __name__ == '__main__':
    main()

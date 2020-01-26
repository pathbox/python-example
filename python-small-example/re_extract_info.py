import re

mystr = """使用了1型车8辆
出发时间: 8 返程时间: 10.5	349 74 里程: 27397运输成本: 547.94充电成本: 0等待成本: 0超时成本: 0固定成本: 300总成本: 847.94充电次数: 0
出发时间: 8 返程时间: 15.8281	1470 466 1412 168 210 1242 里程: 57596运输成本: 1151.92充电成本: 0等待成本: 69.652超时成本: 19.6886固定成本: 300总成本: 1541.26充电次数: 0
出发时间: 8 返程时间: 10.6554	367 759 里程: 32384运输成本: 647.68充电成本: 0等待成本: 0超时成本: 0固定成本: 300总成本: 947.68充电次数: 0
出发时间: 8 返程时间: 14.2979	709 1313 179 里程: 48107运输成本: 962.14充电成本: 0等待成本: 83.7271超时成本: 0固定成本: 300总成本: 1345.87充电次数: 0
出发时间: 8.17338 返程时间: 11.6975	1542 26 747 里程: 35883运输成本: 717.66充电成本: 0等待成本: 0超时成本: 0固定成本: 300总成本: 1017.66充电次数: 0
出发时间: 8 返程时间: 11.9863	792 442 1219 1287 里程: 39660运输成本: 793.2充电成本: 0等待成本: 0超时成本: 0固定成本: 300总成本: 1093.2充电次数: 0
出发时间: 8 返程时间: 15.0681	843 1473 362 1294 298 936 里程: 52765运输成本: 1055.3充电成本: 0等待成本: 54.5788超时成本: 19.4597固定成本: 300总成本: 1429.34充电次数: 0
出发时间: 8 返程时间: 11.5888	265 1569 131 里程: 36706运输成本: 734.12充电成本: 0等待成本: 2.82051超时成本: 0固定成本: 300总成本: 1036.94充电次数: 0
使用了2型车6辆
	出发时间: 8.77896 返程时间: 12.8351	509 693 81 207 里程: 58796运输成本: 1175.92充电成本: 0等待成本: 0超时成本: 0固定成本: 300总成本: 1475.92充电次数: 0
	出发时间: 8 返程时间: 14.0612	1439 1409 221 983 1429 916 1048 里程: 65099运输成本: 1301.98充电成本: 0等待成本: 13.7411超时成本: 0固定成本: 300总成本: 1615.72充电次数: 0
	出发时间: 8.16076 返程时间: 14.8339	737 1119 152 536 1425 450 里程: 57865运输成本: 1157.3充电成本: 0等待成本: 37.3759超时成本: 0固定成本: 300总成本: 1494.68充电次数: 0
	出发时间: 8 返程时间: 17.083	743 366 869 1279 667 1200 200 里程: 64593运输成本: 1291.86充电成本: 0等待成本: 93.9982超时成本: 0固定成本: 300总成本: 1685.86充电次数: 0
	出发时间: 8 返程时间: 12.0742	664 420 928 454 里程: 47380运输成本: 947.6充电成本: 0等待成本: 0超时成本: 0固定成本: 300总成本: 1247.6充电次数: 0
	出发时间: 8 返程时间: 12.9663	778 1571 742 171 1222 1519 里程: 47979运输成本: 959.58充电成本: 0等待成本: 0超时成本: 0固定成本: 300总成本: 1259.58充电次数: 0
使用了3型车2辆
	出发时间: 8 返程时间: 16.628	881 164 975 1162 1392 681 1518 里程: 50912运输成本: 1527.36充电成本: 0等待成本: 97.1735超时成本: 0固定成本: 400总成本: 2024.53充电次数: 0
	出发时间: 8 返程时间: 11.8313	648 1045 512 1153 里程: 26888运输成本: 806.64充电成本: 0等待成本: 9.26976超时成本: 0固定成本: 400总成本: 1215.91充电次数: 0"""

pat = re.compile(r'使用了(\d+)型车(\d+)辆')
result = pat.findall(mystr)
print(result)

pat2 = re.compile(r'返程时间:(.*)里程:')
result2 = pat2.findall(mystr)
print(result2)

beg = 0
d = {}
for i in result:
    vt, n = i
    ni = int(n)
    d[vt] = [j.split('\t')[1] for j in result2[beg:beg+ni]]
    beg += ni
print(d)

with open('rcluster1.txt', 'w') as f:
    for k, v in d.items():
        f.write(str(k) + ' ' + str(len(v)) + '\n')
        for i in v:
            f.write(i + '\n')

print('save ok')

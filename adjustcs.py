# 仅改变4,5,6,7k的columnstart
from math import floor
from os import system
import sys
s = ''
def get_after(start = 0):
    end = s.find('\n',start)
    end2 = s.find('//',start)
    if end2 != -1:
        temp = min(end, end2)
    else:
        temp = end
    return s[start:temp].replace('ColumnStart:','').replace('ColumnWidth:','')
try:
    with open('skin.ini', 'r') as fin:
        s = fin.read()
except FileNotFoundError:
    print('FileNotFound')
    system('pause')
    sys.exit(0)
maniastart = s.find('[Mania]')
kstart = maniastart
for k in range(4,8):
    kstart = s.find('Keys: ' + str(k),kstart + 2)
    replace_tag1 = s.find('ColumnStart:',kstart)
    replace_tag2 = s.find('ColumnWidth:',kstart)
    columnstart = int(get_after(replace_tag1).strip())
    width = sum(map(int,get_after(replace_tag2).strip().split(',')))
    if k == 4:
        print('当前中线为: ',columnstart + width / 2)
        cin = int(input('你需要设置的中线为: '))
    start2 = int(floor(cin - width / 2))
    if start2 < 0:
        print(str(k) + 'k的初始位置小于0！不进行调整')
        continue
    s = s[:replace_tag1] + s[replace_tag1:].replace(str(columnstart),str(start2),1)
    print(str(k) + 'k的ColumnStart已替换为',start2)

with open('skin.ini','w') as fout:
    fout.write(s)
# 一键修改ColumnStart脚本

一键修改osu!mania皮肤的水平位置。

## 使用条件
python3运行环境
## 使用方法
1. 下载`adjustcs.py`并放入需调整的皮肤文件夹内
2. 当前目录下打开命令提示符，执行`python adjustcs.py`
3. 输入中线位置
## 提示
仅替换4-7k的ColumnStart值。若需替换其他key数，请打开该py文件，更改23行`range(4,8)`的值。

若你的`skin.ini`已大幅修改，可以在替换前备份`skin.ini`以免（可能存在的）未知bug将该文件打乱。
## 程序原理
根据ColumnWidth与输入，计算中线位置并查找替换。

~~写的很屎，但是能用就行~~
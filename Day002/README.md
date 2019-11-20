1. CSV 可以做其他事情
2. CSV vs File I/O vs Pandas的差異

reference: https://blog.gtwang.org/programming/python-csv-file-reading-and-writing-tutorial/

在執行這個題目遇到一個錯誤：
(縮排後就成功了）
with open('Example2 file.csv', newline='') as f_csv:
    rows = csv.reader(f_csv, delimiter = ',')
for row in rows: #這邊沒有縮排到with內
    print(row)
    
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-10-54e14243988c> in <module>
      2 with open('Example2 file.csv', newline='') as f_csv:
      3     rows = csv.reader(f_csv, delimiter = ',')
----> 4 for row in rows:
      5     print(row)

ValueError: I/O operation on closed file.

第二個錯誤
trainTable = csv.reader(open('Example2 file.csv'), delimiter ='')

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-29-7bf9ba7aaa60> in <module>
      1 # 1. 取出班次一的每一個時間
----> 2 trainTable = csv.reader(open('Example2 file.csv'), delimiter ='')
      3 train_1 = []
      4 
      5 for row in trainTable:

TypeError: "delimiter" must be a 1-character string

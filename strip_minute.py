"""

作者：moonw
日期：2022年05月08日

"""
import pandas as pd
import csv
from setting import Setting as set

def put_hearder_row(header):
    list = []
    for index in range(len(header)):
        list.append(header[index])

    str = ','.join(list)
    str=str+'\n'
    with open(ipfilename, 'w', encoding='utf-8') as ip:
        ip.write(str)
    ip.close()

def file_ID(op):
    massage = op.readline(12).replace('"', '')  # 通过readine()内设置读取字节数，保证不跳行
    print(massage)
    list = massage.split(',', 1)
    IDstr = list[0].replace('-', '')

    input_file_name=f"E:/python/price_value_average_system/data/300207/{IDstr}_minute.csv"
    return input_file_name


#  开始
setting = set()
opfilename = f'E:/python/strip_share_minute_data/data/{setting.filename}'

index=0
with open(opfilename,encoding='utf-8') as op:
    reader=csv.reader(op)
    header=next(reader)

    ipfilename = file_ID(op)
    put_hearder_row(header)

    for line in op:
        index+=1
        if index<=239:
            with open(ipfilename,'a',encoding='utf-8') as ip:
                ip.write(line)
            ip.close()
        elif index==240:
            print(f"miss:{line}")
        else:
            print(f"miss:{line}")
            index=0
            ipfilename = file_ID(op)
            put_hearder_row(header)





    # with open(ipfilename,'a',encoding='utf-8') as ip:
    #     for line in op:
    #         ip.write(line)



















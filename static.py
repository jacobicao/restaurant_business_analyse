# -*- coding: UTF-8 -*-
#!/usr/local/bin/python3
import os,sys
dirname = os.path.dirname(os.path.realpath(__file__))


def each_file(file_path):
    ll = []
    for s in os.listdir(file_path):
        new_dir = os.path.join(file_path, s)
        if os.path.isfile(new_dir):
            if os.path.splitext(new_dir)[-1] == ".csv":
                ll.append(new_dir)
        else:
            print(new_dir)
            ll.extend(each_file(new_dir))
            print(len(ll))
    return ll


ll = each_file(dirname)
dd = {}
qq = {}
for s in ll:
    n = len([ "" for line in open(s,"r",encoding='gbk')])
    if n == 1:
        dd[s] = n
    else:
        qq[s] = n

for k in dd.keys():
    os.remove(k)
qq = sorted(qq.items(),key=lambda x:x[1])


# for k in qq:
#     print(k[1],k[0])
# df = pd.read_csv('../data/city_list/行政区对应.txt', sep='|').fillna('')

# -*- coding: utf-8 -*-
# @Time     :   2020/5/2 0:14
# @Author   :   Payne
# @File     :   demo.py
# @Software :   PyCharm

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f'{i}*{j}={i * j} ')
# print('{}*{}={} \t'.format(i, j, i * j), end='')

#
# for i in range(1, 10):
#     for j in range(1, i+1):
#         # print('{}x{}={}\t'.format(j, i, i*j), end='')
#         print('{}x{}={}\t'.format(j, i, i*j))
#     print()

# print('I\'m \"OK\"!')
# print('I \'m \"OK\"!')

for i in range(1, 10):
    for j in range(1, i + 1):
        # print('{}X{}={}  '.format(i, j, i * j), end='')
        # print('{}X{}={} \t'.format(i, j, i * j), end='')
        print(f'{i}X{j}={i*j} \t', end='')
    print('\n')

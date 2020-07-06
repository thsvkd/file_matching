import os
import re
import shutil

path_dir = ['C:/Users/thsxo/OneDrive/문서/Visual Studio Code',
            'C:/Users/thsxo/OneDrive/문서/Visual Studio Code']

file_list = [os.listdir(i) for i in path_dir]
for i in file_list:
    file_list.sort()

print('{} : {}\n{} : {}'.format(path_dir[0],
                                len(file_list[0]), path_dir[1], len(file_list[1])))


subset = [list(set(file_list[0]) - set(file_list[1])),
          list(set(file_list[1]) - set(file_list[0]))]
subset_copy = [[], []]

for i in subset:
    i.sort()

for index, item in enumerate(subset):

    print('{}에 있는 파일 목록\n'.format(path_dir[index]))
    for i in item:
        tmp = re.split("[_.]", i)
        if int(tmp[0]) < 20190307 or (int(tmp[0]) == 20190307 and int(tmp[0]) <= 163438):
            print(i)
            subset_copy[index].append(i)

direction = [0, 1]
for i in subset_copy[direction[0]]:
    shutil.copy2(path_dir[direction[0]] + i, path_dir[direction[1]] + i)

import time
import csv
from prettytable import PrettyTable
# import subprocess
import webbrowser
import os

filePath = 'history_data.csv'
absouluteFilePath = os.path.abspath(filePath)
print(absouluteFilePath)

def showRecord():
    with open(filePath) as f:
        header = f.readline()
        header = header[:-1]
        header_list = header.split(',')
        table = PrettyTable(header_list)
        r_total = f.readlines()
        for each_line in r_total:
            each_line = each_line[:-1].split(',')
            table.add_row(each_line)
        print(table)

def writeRecord(content):
    with open(filePath, 'w') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows(content)

def main():
    flag = 1
    while 1:
        if flag:
            showRecord()
        flag = 1
        localtime = time.localtime(time.time())
        date = str(localtime.tm_year) + '.' + str(localtime.tm_mon) + '.' + str(localtime.tm_mday)
        start = str(localtime.tm_hour) + ':' + str(localtime.tm_min) + ':' + str(localtime.tm_sec)
        # 获取输入
        getInput = input()

        with open(filePath, 'r') as f:
            total = f.readlines()
            writeIn = []
            for each in total:
                each = each[:-1].split(',')
                writeIn.append(each)

        # -1
        if getInput == '-1':
            webbrowser.open(absouluteFilePath)
            flag = 0
        # 刷新
        elif getInput == 'new':
            continue
        # 结束
        elif getInput == '':
            return
        # 删除上一行
        elif getInput == 'dd':
            writeIn.pop()
            with open(filePath,'w') as f:
                writer = csv.writer(f, lineterminator='\n')
                writer.writerows(writeIn)
        # 重写上一行
        elif getInput.split(' ')[0] == 'rd':
            if getInput.split(' ')[1] == '1':
                rd_date = input('请输入新的 date :')
                writeIn[-1][0] = rd_date
            elif getInput.split(' ')[1] == '2':
                rd_start = input('请输入新的 start :')
                writeIn[-1][1] = rd_start
            elif getInput.split(' ')[1] == '3':
                rd_end = input('请输入新的 end :')
                writeIn[-1][2] = rd_end
            else:
                rd_task = input('请输入新的 task 和 notes :').split(' ',1)
                writeIn[-1][3] = rd_task[0]
                writeIn[-1][4] = rd_task[1]
            writeRecord(writeIn)
        # 结束上一个 task
        elif getInput.split(' ')[0] == 'end':
            if writeIn[-1][2] == 'None' or (len(getInput.split()) > 1 and getInput.split()[1] == '-f'):
                writeIn[-1][2] = start
                writeRecord(writeIn)
            else:
                print(f'{writeIn[-1][3]} ({writeIn[-1][4]}) 已于 {writeIn[-1][0]} {writeIn[-1][2]} 结束')
        # 新建一个 task record

        elif getInput.split(' ')[0] == 'sum':
            flag = 0
            inputList = getInput.split(' ')
            if len(inputList) == 1:
                print('请输入 <task> 或者 <task> <notes> .')
            elif len(inputList) == 2:
                if inputList[1] == '':
                    print('请输入 <task> 或者 <task> <notes> .')
                    continue
                total_time = 0
                for each in writeIn:
                    if each[3] == inputList[1]:
                        if each[2] == 'None':
                            each[2] = start
                        time_end = each[0] + ' ' + each[2]
                        time_start = each[0] + ' ' + each[1]
                        time_delta = time.mktime(time.strptime(time_end, "%Y.%m.%d %H:%M:%S")) - time.mktime(time.strptime(time_start, "%Y.%m.%d %H:%M:%S"))
                        total_time += time_delta
                print(f'task {inputList[1]} cost {int(total_time/3600)}h {int(total_time%3600/60)}m {int(total_time%60)}s.')
            elif len(inputList) == 3:
                total_time = 0
                for each in writeIn:
                    if each[3] == inputList[1]:
                        if each[4] == inputList[2]:
                            if each[2] == 'None':
                                each[2] = start
                            time_end = each[0] + ' ' + each[2]
                            time_start = each[0] + ' ' + each[1]
                            time_delta = time.mktime(time.strptime(time_end, "%Y.%m.%d %H:%M:%S")) - time.mktime(time.strptime(time_start, "%Y.%m.%d %H:%M:%S"))
                            total_time += time_delta
                print(f'task {inputList[1]} {inputList[2]} cost {int(total_time/3600)}h {int(total_time%3600/60)}m {int(total_time%60)}s.')

        else:
            if ' ' not in getInput:
                getInputList = [getInput,""]
            else:
                getInputList = getInput.split(' ',1)
            with open(filePath, 'r') as f:
                if writeIn[-1][2] == 'None':
                    writeIn[-1][2] = start
                # 获取本次 Task
                thisTask = [date,start,'None'] + getInputList
                writeIn.append(thisTask)
            # 写入本次 Task
            writeRecord(writeIn)

if __name__ == '__main__':
    main()

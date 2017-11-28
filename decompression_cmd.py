#使用命令行的方法解压缩
#但是我运行的时候会出现很多个找不到压缩文件的窗口
# coding=gbk
import os  

i = 0
#source_dir为压缩文件所在文件夹
#解压缩文件存在source_dir\output\文件夹中
source_path = r'F:\自学项目\聊天机器人\process\zip'
for file in os.listdir(source_path):
    i = i+1
    source_dir = source_path+'\\'+file
    unzip_dir = source_path+'\\output\\'+str(i)
    flag = file.split('_')[0]
    print('unzip %s to output\%s' % (flag, i))
	#命令行进行压缩文件解压
    cmd = '"D:\\winRAR\\WinRar.exe" x %s  %s\\' % (source_dir, unzip_dir) 
    os.popen(cmd)
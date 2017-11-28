#解压缩zip压缩文件
# coding=utf-8
import zipfile  
import os
def un_zip(file_name, unzip_dir):  
    """unzip zip file"""  
    if not zipfile.is_zipfile(file_name):
        return
    zip_file = zipfile.ZipFile(file_name)  
    for names in zip_file.namelist():  
        zip_file.extract(names,unzip_dir)  
    zip_file.close() 

#source_dir为压缩文件所在文件夹
#解压缩文件存在source_dir\output\文件夹中
source_path = r'F:\自学项目\聊天机器人\process\zip'
i = 0
for file in os.listdir(source_path):
    i = i+1
    source_dir = source_path+'\\'+file
    unzip_dir = source_path+'\\output\\'+str(i)
    print('unzip %s to output\%s' % (file, i))
    try:
        un_zip(source_dir, unzip_dir)
    except:
        continue
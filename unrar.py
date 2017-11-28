#解压缩rar文件
#需要pip install rarfile
#如果出现错误：
#	'rarfile.RarExecError: Unrar not installed? (rarfile.UNRAR_TOOL='unrar')'
#	将unrar.exe放到python脚本文件夹中就可以了
#	可以参考：http://blog.csdn.net/luoye7422/article/details/41873499
# coding=utf-8
import rarfile  
import os  
def un_rar(file_name, unrar_dir):  
    """unrar zip file"""  
    if not rarfile.is_rarfile(file_name):
        return
    rar = rarfile.RarFile(file_name)   
    if not os.path.exists(unrar_dir):
        os.makedirs(unrar_dir)
    os.chdir(unrar_dir)
    rar.extractall()  
    rar.close() 

#source_dir为压缩文件所在文件夹
#解压缩文件存在source_dir\output\文件夹中
source_path = r'F:\自学项目\聊天机器人\process\rar'
i = 0
for file in os.listdir(source_path):
    i = i+1
    source_dir = source_path+'\\'+file
    unrar_dir = source_path+'\\output\\'+str(i)
    print('unrar %s to output\%s' % (file, i))
    try:
        un_rar(source_dir, unrar_dir)
    except:
        continue
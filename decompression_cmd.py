#ʹ�������еķ�����ѹ��
#���������е�ʱ�����ֺܶ���Ҳ���ѹ���ļ��Ĵ���
# coding=gbk
import os  

i = 0
#source_dirΪѹ���ļ������ļ���
#��ѹ���ļ�����source_dir\output\�ļ�����
source_path = r'F:\��ѧ��Ŀ\���������\process\zip'
for file in os.listdir(source_path):
    i = i+1
    source_dir = source_path+'\\'+file
    unzip_dir = source_path+'\\output\\'+str(i)
    flag = file.split('_')[0]
    print('unzip %s to output\%s' % (flag, i))
	#�����н���ѹ���ļ���ѹ
    cmd = '"D:\\winRAR\\WinRar.exe" x %s  %s\\' % (source_dir, unzip_dir) 
    os.popen(cmd)
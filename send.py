
# -*- coding: utf-8 -*-

'''a socket example which send echo message to server.'''
import time
import socket
import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片
import numpy as np

file_object = open('hnxdata.txt', 'w+')
'''
lena = mpimg.imread(r'C:\Users\hnx\Desktop\picture\q.jpg') # 读取和代码处于同一目录下的 lena.png
print lena.ndim,lena.shape,len(lena)  
print  type(str(lena[1][1][1])),lena.shape[1]
print  type(lena[1][1]),lena[1][1]
'''

type1head.GHead.NewFlag = 1;
type1head.GHead.SFN = sysframenum;
type1head.GHead.SubframeN = subframenum;

type1head.DL_TYPE1_PUBLIC_C.PDSCHNum = 5; #当前子帧PDSCH信道数量,最小系统参数为5,调试时由1～5变化
type1head.DL_TYPE1_PUBLIC_C.PDCCHNum = 5; #当前子帧PDCCH信道数量,最小系统参数为5,调试时由1～5变化
type1head.DL_TYPE1_PUBLIC_C.NumOfUEForPHICH = 2; #当前子帧PHICH承载的上行用户的数目,最小系统参数为2
type1head.DL_TYPE1_PUBLIC_C.Zero = 0; #保留,字节对齐
#PBCH_C参数
type1pbchc.NumPrbBw = 100;
type1pbchc.PhichDurtion = 0;
type1pbchc.GPhichNg = 0;
type1pbchc.spare = 0;


#PBCH_D参数
type1pbchd.SourcePBCH = 0; #待定
#memcpy(mapaddr + 0x800 + type1head.DL_TYPE1_PUBLIC_C.PBCH_D_Offset,&type1pbchd,sizeof(ENB_DL_TYPE1_PBCH_D));
#PHICH_C参数,两个用户
type1phichc[0].RNTI = 61;
type1phichc[0].zero = 0;
type1phichc[0].I_lowest_index_PRB_RA = 0; #待定
type1phichc[0].NDmrs = 0; #待定
type1phichc[1].RNTI = 62;
type1phichc[1].zero = 0;
type1phichc[1].I_lowest_index_PRB_RA = 0; #待定
type1phichc[1].NDmrs = 0; #待定
#memcpy(mapaddr + 0x800 + type1head.DL_TYPE1_PUBLIC_C.PHICH_C_Offset,type1phichc,type1head.DL_TYPE1_PUBLIC_C.NumOfUEForPHICH * sizeof(ENB_DL_TYPE1_PHICH_C));
#PHICH_D参数,两个用户
type1phichd[0].RNTI = 61;
type1phichd[0].SourcePHICH = 0;
type1phichd[1].RNTI = 62;
type1phichd[1].SourcePHICH = 0;
memcpy(mapaddr + 0x800 + type1head.DL_TYPE1_PUBLIC_C.PHICH_D_Offset,type1phichd,type1head.DL_TYPE1_PUBLIC_C.NumOfUEForPHICH * sizeof(ENB_DL_TYPE1_PHICH_D));
#PDCCH_C参数，根据PDCCHNum确定用户数
for i in range(type1head.DL_TYPE1_PUBLIC_C.PDCCHNum):

	type1pdcchc[i].RNTI = 61 + i;
	type1pdcchc[i].CommonPdcchFlag = 0;
	type1pdcchc[i].PdcchFormat = 0;
	type1pdcchc[i].DCIFormat = 2;
	type1pdcchc[i].DciBitLen = 31;

	#memcpy(mapaddr + 0x800 + type1head.DL_TYPE1_PUBLIC_C.PDCCH_C_Offset,type1pdcchc,type1head.DL_TYPE1_PUBLIC_C.PDCCHNum * sizeof(ENB_DL_TYPE1_PDCCH_C));
	#PDCCH_D参数，根据PDCCHNum确定用户数
for i in range(type1head.DL_TYPE1_PUBLIC_C.PDCCHNum):
	
	type1pdcchd[i].RNTI = 61 + i;
	type1pdcchd[i].zero = 0;
	type1pdcchd[i].DataSource = DataSource[i];

	#memcpy(mapaddr + 0x800 + type1head.DL_TYPE1_PUBLIC_C.PDCCH_D_Offset,type1pdcchd,type1head.DL_TYPE1_PUBLIC_C.PDCCHNum * sizeof(ENB_DL_TYPE1_PDCCH_D));
	#PDSCH_C参数,根据PDSCHNum确定用户数
for i in range(type1head.DL_TYPE1_PUBLIC_C.PDCCHNum):

	type1pdschc[i].RNTI = 61 + i;
	type1pdschc[i].NumCW = 1;
	type1pdschc[i].NumPrbofUe = 20;
	type1pdschc[i].UeCategory = 3;
	type1pdschc[i].UeTransMod = 2;
	type1pdschc[i].NumHarqPro = 8;
	type1pdschc[i].RvIdx = 0;
	type1pdschc[i].Modulation = 1;
	type1pdschc[i].NumLayers = 2;
	type1pdschc[i].DelayMod = 0;
	type1pdschc[i].PA = 4;
	type1pdschc[i].zero = 0;
	if (subframenum == 1) || (subframenum == 6) :
		type1pdschc[i].PDSCHTbSize = 4264; #特殊frame
		#printk("subframenum is %u,PDSCHTbSize = %u\n",subframenum,type1pdschc[i].PDSCHTbSize);
	else:

		type1pdschc[i].PDSCHTbSize = 5736; #普通frame
		#printk("subframenum is %u,PDSCHTbSize = %u\n",subframenum,type1pdschc[i].PDSCHTbSize);
	type1pdschc[i].BitMap = 0xF8000000>>(5 * i);
	#memcpy(mapaddr + 0x800 + type1head.DL_TYPE1_PUBLIC_C.PDSCH_C_Offset,type1pdschc,type1head.DL_TYPE1_PUBLIC_C.PDSCHNum * sizeof(ENB_DL_TYPE1_PDSCH_C));
	#PDSCH_D参数,根据PDSCHNum确定用户数,用户数据部分,预留空间
pdschdata = kmalloc(720,GFP_ATOMIC);
memset(pdschdata,0xef,720);
for i in range(type1head.DL_TYPE1_PUBLIC_C.PDCCHNum):
	
	type1pdschd[i].RNTI = 61 + i;
	type1pdschd[i].PdschData = 720;
	#printk("type1pdschd[i].PdschData = %u\n",type1pdschd[i].PdschData);
	#memcpy(mapaddr + 0x800 + type1head.DL_TYPE1_PUBLIC_C.PDSCH_D_Offset + i * sizeof(ENB_DL_TYPE1_PDSCH_D) + i * type1pdschd[i].PdschData,&type1pdschd[i],sizeof(ENB_DL_TYPE1_PDSCH_D));#先把pdsch_d拷贝
	#memcpy(mapaddr + 0x800 + type1head.DL_TYPE1_PUBLIC_C.PDSCH_D_Offset + (i + 1) * sizeof(ENB_DL_TYPE1_PDSCH_D) + i * type1pdschd[i].PdschData,pdschdata,type1pdschd[i].PdschData); #拷贝用户数据到发送区


L=[]
strings=''

for i in range(lena.shape[0]):
	for j in range(lena.shape[1]):
		strings=strings+str(lena[i][j][0])+'D'+str(lena[i][j][1])+'D'+str(lena[i][j][2])+'D'
		file_object.write(str(lena[i][j][0])+' '+str(lena[i][j][1])+' '+str(lena[i][j][2])+'\n')
	strings=strings+'H'
strings=str(lena.shape[0])+'C'+str(lena.shape[1])+'K'+strings+'E'

ss=[]
for i in range(len(strings)/(720*4)+1):
	# 组包
	ss.append(strings[i*720*4:i*720*4+720*4])
	
#print strings
print "length:"
print len(strings)
#file_object.write(strings)






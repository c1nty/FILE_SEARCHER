#!/usr/bin/python
#coding:utf-8

import os

def File_Content_Searcher(keywords):
	lib_path = 'D:/project/FILE_SEARCHER/libs/'
	lib_list = os.listdir(lib_path)
	for i in lib_list:
		path = lib_path+i
		f = open(path,'r')
		print "==============="+i+"==============="
		for j in f.readlines():
			if keywords in j:
				print j,
		f.close()

if __name__ == '__main__':
	keywords = '371422199302'
	File_Content_Searcher(keywords)

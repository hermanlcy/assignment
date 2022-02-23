# -*- coding:utf-8 -*-

import requests
import re
import string
from bs4 import BeautifulSoup


# download from a website
def download(url):
	try:
		requests.adapters.DEFAULT_RETRIES = 15
		s = requests.session()
		s.keep_alive = False
		
		html = requests.get(url).text
		#using BeautifulSoup to deal with elements in html easier
		soup = BeautifulSoup(html,'lxml')

		# ti = soup.title.text
		# print(ti)

		content = soup.select('#hidedata04_1 tr')#content is a list of each table row
		# for x in range(0,len(content)):
		# 	# print(content[x].text) 
		# 	pass
		return content

			# list[0][0]
		# pattern = re.compile(r'<[^>]+>',re.S)
		# result = pattern.sub('', html)
		# print(result)

		# data = soup.find_all('div',id='hidedata04_1')

		# for each in data:
		# 	result = {
		# 		'content':each.get_text(),
		# 	}
		# 	print(result)



		# key = re.findall('<th colspan="8" class="course">Enrolment Class: Lecture</th>(.*?)<ul class="nonprint"',html,re.S)

		# # write the info of lecture and workshop into text file
		# for x in range(2,len(content)):
		# 	print("downloading ...")
		# 	fp = open("~\\Desktop\\DDDM\\"+"result"+str(x)+".txt","wb")
		# 	# pattern = re.compile(r'<[^>]+>',re.S)
		# 	# result = pattern.sub('', each)
		# 	fp.write(content[x].text)
		# 	fp.close()
	except Exception as e:
		raise
# -*- coding:utf-8 -*-
import scraper
import requests
import re
import string
import datetime
import time
from bs4 import BeautifulSoup
from dateutil.parser import parse

class Session:
	def __init__(self, sdate, edate, days, time, location):
		self.sdate = sdate
		self.edate = edate
		self.days = days
		self.time = time
		self.location = location

	def display(self):
		print(self.sdate)
		print(self.edate)
		print(self.days)
		print(self.time)
		print(self.location)

	# def change(self):
	# 	self.dates.split(" - ")
	# 	print(self.dates,type(self.dates))


#  4110 semester 1 4120 semester 2
#  https://access.adelaide.edu.au/courses/search.asp?year=2021&m=r&title=computer+science&subject=&catalogue=&action=Search&term=&career=&campus=&class=&sort=
# we search use course title (or part of title)and catalogue number (e.g. 1001, 7095) to
# get to the returning list page, if there is only one returned course in the list, redirct to the course page

def look(title):	
	#need to change space in course title to +
	name = title.replace(" ","+")
	year = time.localtime().tm_year
	#trimester 1 2 3 are 4133 4136 4139
	# if semester == 2:
	# 	term = 4120
	# elif semester == 1:
	# 	term = 4110
	# elif semester == 3:#tri 1
	# 	term = 4133
	# elif semester == 4:#tri 2
	# 	term = 4136
	# elif semester == 5:#tri 3
	# 	term = 4139
	# elif semester == 6:#term 1
	# 	term = 4142
	# elif semester == 7:#term 2
	# 	term = 4144
	# elif semester == 8:#term 3
	# 	term = 4146
	# elif semester == 9:#term 4
	# 	term = 4148
	# elif semester == 10:#summer
	# 	term = 4105
	# elif semester == 11:#winter
	# 	term = 4115
	# this is the middle step page
	value = "https://access.adelaide.edu.au/courses/search.asp?year="+str(year)+"&m=r&title="+name+"&subject=&catalogue=&action=Search&term=&career=&campus=&class=&sort="
	try:
		requests.adapters.DEFAULT_RETRIES = 10
		s = requests.session()
		s.keep_alive = False
		
		html = requests.get(value).text

		key = re.findall('"odd"><a href="details.asp?(.*?)</a>',html,re.S)
		keys = re.findall('"even"><a href="details.asp?(.*?)</a>',html,re.S)

		urlset = []

		for x in key:
			us = x.split("\">")
			if us[1] == title:
				urlset.append(us[0])

		for ea in keys:
			us = ea.split("\">")
			if us[1] == title:
				urlset.append(us[0])


		ses = []
		#real each url in odd line returned class table
		for x in urlset:
			ur = x.replace("amp;","")
			url = "https://access.adelaide.edu.au/courses/details.asp"+ur
			data = scraper.download(url)# returned resultset
			# print(url)
			for y in range(2,len(data)):
				st = data[y].text.encode("ascii")
				ses.append(st)#append each line in the course details table in ses list

		#adjust ses list
		session = []
		for each in ses:

			#change it to list of lists of each line in session
			session.append(each.split("\n"))

		#delete unnecessary elements
		ls = []
		for each in session:
			if len(each)==6 or len(each) == 10:
				if each[1] != 'Class Nbr':
					ls.append(each)

		result = []
		for each in ls:
			if len(each) == 10:
				ll = each[5].split(" - ")
				tt = []
				for x in ll:
					x = x+" "+str(year)
					d = parse(x)
					tt.append(d)
				se = Session(tt[0],tt[1],each[6],each[7],each[8])
			else:
				ll = each[1].split(" - ")
				tt = []

				for x in ll:
					x = x+" "+str(year)
					d = parse(x)
					tt.append(d)
				se = Session(tt[0],tt[1],each[2],each[3],each[4])
			result.append(se)


		return result#list of session objects

	except Exception as e:
		raise
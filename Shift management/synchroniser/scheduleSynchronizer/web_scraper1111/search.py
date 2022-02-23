# -*- coding:utf-8 -*-
from scheduleSynchronizer.web_scraper1111.scraper import *
import requests
import re
import string
import datetime
import time
import random
import os
import multiprocessing as mul
from time import sleep
from bs4 import BeautifulSoup
from dateutil.parser import parse


class Session:
	def __init__(self, semester, title, categ, section, sdate, edate, days, location,info):
		self.semester = semester
		self.title = title
		self.categ = categ
		self.section = section
		self.startDateTime = sdate
		self.endDateTime = edate
		self.sdate = sdate.strftime('%d/%b/%Y, %H:%M')
		self.edate = edate.strftime('%d/%b/%Y, %H:%M')
		self.days = days
		self.location = location
		self.isMatched = -1
		self.info=info

	def display(self):
		print(self.semester)
		print(self.title)
		print(self.categ)
		print(self.section)
		print(self.sdate)
		print(self.edate)
		print(self.days)
		print(self.location)
		print(self.info)
		print("_________________________")

# a function to get the scraped data
def getdata(tup1):
	result = []
	data = download(tup1[0])# returned resultset
	for y in range(0,len(data)):
		st = data[y].text.encode("utf-8")
		sts = st.split("\n".encode())
		result.append((sts,tup1[1]))
	# in case server refused connection, sleep 
	# sleep(random.random()*3)
	return result




# we search use exact course title or course title, semester, lecture/workshop.. to
# get the course we want, then store each session in a list and return the list
def look(*params):	
	# if three input, flag = 0
	flag = 0
	if len(params)==1:# one input flag = 1
		flag = 1

	# need to change space in course title to +
	# then change special characters in course title to corresponding char
	title = params[0]
	name = title.replace(" ","+")
	name = name.replace("&","%26")
	name = name.replace(",","%2C")
	name = name.replace(":","%3A")
	name = name.replace("/","%2F")
	year = time.localtime().tm_year
	month = time.localtime().tm_mon

	#trimester 1 2 3 are 4133 4136 4139
	#get the semester number 
	term = 0
	if flag==0:
		semester = params[1]
		sems = {"Semester 1":4110, "Semester 2":4120, "Trimester 1":4133, "Trimester 2":4136, "Trimester 3":4139, "Term 1":4142, "Term 2":4144,"Term 3":4146, "Term 4":4148, "Summer":4105, "Winter":4115,"Melb Teaching Period 1":4171,"Melb Teaching Period 2":4172,"Melb Teaching Period 3":4173,"Online Teaching Period 3":4163,"Online Teaching Period 1":4161,"Online Teaching Period 2":4162,"Online Teaching Period 4":4164,"Online Teaching Period 5":4165,"Online Teaching Period 6":4166,"ELC Term 1":4103,"ELC Term 2":4113,"ELC Term 3":4123}
		term = sems[semester]
	

	# this is the middle step page
	value = "https://access.adelaide.edu.au/courses/search.asp?year="+str(year)+"&m=r&title="+name+"&subject=&catalogue=&action=Search&term=&career=&campus=&class=&sort="
	try:
		requests.adapters.DEFAULT_RETRIES = 15
		s = requests.session()
		s.keep_alive = False
		
		html = requests.get(value).text

		key = re.findall('"odd"><a href="details.asp?(.*?)</a>',html,re.S)
		keys = re.findall('"even"><a href="details.asp?(.*?)</a>',html,re.S)
		# urlset has all the course detail page urls after search
		urlset = []

		for x in key:
			us = x.split("\">")
			us[1] = us[1].replace("&amp;","&")
			if us[1] == params[0]:
				urlset.append(us[0])

		for ea in keys:
			us = ea.split("\">")
			us[1] = us[1].replace("&amp;","&")
			if us[1] == params[0]:
				urlset.append(us[0])


		ses = []
		urlsss = []
		for x in urlset:
			s = x.split("+")
			temp = int(s[-2])# integer of term number like 4110
			termn = {4110:"Semester 1", 4120:"Semester 2", 4133:"Trimester 1", 4136:"Trimester 2", 4139:"Trimester 3", 4142:"Term 1", 4144:"Term 2",4146:"Term 3", 4148:"Term 4", 4105:"Summer", 4115:"Winter", 4171:"Melb Teaching Period 1",4172:"Melb Teaching Period 2",4173:"Melb Teaching Period 3",4163:"Online Teaching Period 3",4162:"Online Teaching Period 2",4161:"Online Teaching Period 1",4164:"Online Teaching Period 4",4165:"Online Teaching Period 5",4166:"Online Teaching Period 6",4103:"ELC Term 1",4113:"ELC Term 1",4123:"ELC Term 1"}
			#get corresponding semester number according to given semester
			if flag==0:#three input params
				if term == temp:
					te = termn[temp]
					ur = x.replace("amp;","")
					url = "https://access.adelaide.edu.au/courses/details.asp"+ur
					urlsss.append((url,te))

			else:
				#only title input
				#figure out which semester it is in each url
				te = termn[temp]
				ur = x.replace("amp;","")
				url = "https://access.adelaide.edu.au/courses/details.asp"+ur
				urlsss.append((url,te))



		# using multi-processing to improve running speed
		bb = 2*os.cpu_count()
		pool = mul.Pool(bb)
		rel = pool.map(getdata,urlsss)
		pool.close()
		pool.join()

		for x in rel:
			for y in x:
				ses.append(y)



		# for each in urlsss:		
		# 	data = scraper.download(each[0])# returned resultset

		# 	for y in range(0,len(data)):
		# 		st = data[y].text.encode("utf-8")
		# 		sts = st.split("\n".encode())

		# 		ses.append((sts,each[1]))#append each line in the course details table in ses list

	

		#each line in details table in ses
		ls = []
		for each in ses:

			if len(each[0])==6 or len(each[0]) == 10 or len(each[0]) == 3 or len(each[0]) == 7 or len(each[0]) == 1:
				if len(each[0]) != 1 and each[0][1].decode() != 'Class Nbr':
					ls.append(each)
				elif len(each[0]) == 1:
					ls.append(each)


		result = []
		categ = ""
		for each in ls:#one line in the table
			
			sec = ""
			if len(each[0]) == 1:# this line shows the session type of following sessions
				c = each[0][0].decode()
				c = c.split(":")
				categ = c[1].replace(" ","")


			elif len(each[0]) == 10: # first line of a session
				sec = each[0][2].decode()
				ll = each[0][5].split("-".encode())#date
				la = each[0][7].split("-".encode())#time
				tt = []

				#changing time format
				day = []
				for x in ll:
					x=x.decode().replace(" ","")
					da = parse(x)
					day.append(da)
				
				start = day[0]
				end = day[1]
				ldat = []
				# every 7 days, there is a shift
				while start <= end:
					mo = start.month
					da = start.day
					ele = str(mo)+"/"+str(da)
					ldat.append(ele)
					start = start + datetime.timedelta(days = 7)

			

				for x in ldat:
					for y in la:
						#datetime format c
						c = y.decode()+" "+x+" "+str(year)
						d = parse(c)
						tt.append(d)
				#each [7] change to stime etime, split first
				for i in range(0,len(tt),2):
					se = Session(each[1],title,categ,sec,tt[i],tt[i+1],each[0][6].decode(),each[0][8].decode(),"")
					result.append(se)

			elif len(each[0]) == 6:# lines after first line of a certain session type
				ll = each[0][1].split(" - ".encode())
				la = each[0][3].split("-".encode())
				tt = []
				sec = result[-1].section

				day = []
				for x in ll:
					x=x.decode().replace(" ","")
					da = parse(x)
					day.append(da)
				
				start = day[0]
				end = day[1]
				ldat = []
				while start <= end:
					mo = start.month
					da = start.day
					ele = str(mo)+"/"+str(da)
					ldat.append(ele)
					start = start + datetime.timedelta(days = 7)

				for x in ldat:
					for y in la:
						c = y.decode()+" "+x+" "+str(year)
						d = parse(c)
						tt.append(d)
				for i in range(0,len(tt),2):
					se = Session(each[1],title,categ,sec,tt[i],tt[i+1],each[0][2].decode(),each[0][4].decode(),"")
					result.append(se)


			elif len(each[0]) == 7:#when there is session number but the schedule is not on the website
				infos = each[0][5]
				infos = infos.decode()
				se = Session(each[1],title,categ,each[0][2].decode(),datetime.datetime.now(),datetime.datetime.now(),"","",infos)
				result.append(se)

			elif len(each[0]) == 3:# when it is not first line of a session, and schedule not online
				#there is note in it
				infos = each[0][1]
				infos = infos.decode()
				if len(result)>1:
					sec = result[-1].section
					se = Session(each[1],title,categ,sec,datetime.datetime.now(),datetime.datetime.now(),"","",infos)
				else:
					se = Session(each[1],title,categ,"",datetime.datetime.now(),datetime.datetime.now(),"","",infos)
				result.append(se)
			
		
		#shrink it to only list of lectures or workshops
		res = []
		if flag==0:
			sestype = params[2]
			for obj in result:
				if sestype == obj.categ:
					res.append(obj)
				
		else:
			for obj in result:
				res.append(obj)



		return res#list of session objects

	except Exception as e:
		raise

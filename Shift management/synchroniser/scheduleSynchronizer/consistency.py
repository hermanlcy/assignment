from datetime import datetime, timedelta

from requests.api import get, request
from scheduleSynchronizer.debug import *
from scheduleSynchronizer.web_scraper1111.search import look
import re
# from scheduleSynchronizer.web_scraper.search import *


def add_key(key, value, dict):
    if key in dict:
        return 'exist'
    else:
        dict[key] = value
        return 'added'

courses_cache = {}

def get_courses_cache():
    return courses_cache

# month = {
#     "Jan": 1,
#     "Feb": 2,
#     "Mar": 3,
#     "Apr": 4,
#     "May": 5,
#     "Jun": 6,
#     "Jul": 7,
#     "Aug": 8,
#     "Sep": 9,
#     "Oct": 10,
#     "Nov": 11,
#     "Dec": 12
# }

group_dict = {
    "PBL": "Puzzle Based Learning",
    "CSNS": "Introduction to Computer Systems, Networks and Security",
    "ITP": "Information Technology Project",
    "PITS": "Introduction to Programming for Information Technology Specialists",
    "OOP": "Object Oriented Programming",
    "GSCS": "Grand Challenges in Computer Science",
    "AI": "Artificial Intelligence",
    "FCS": "Foundations of Computer Science",
    "ADDS": "Algorithm Design & Data Structures",
    "ADSA": "Algorithm & Data Structure Analysis",
    "CS": "Computer Systems",
    "CNA": "Computer Networks & Applications"
}


def parse_abbreviation(abbreviation):
    if abbreviation in group_dict.keys():
        return group_dict[abbreviation]
    else:
        return abbreviation

# input a shift and return whether it's mapped
def match(shift):
    isMatched = 1
    shift['groupName'] = parse_abbreviation(shift['groupName'])
    # print("comparing course name: ", shift['groupName'])
    if shift['groupName'] in courses_cache:
        courses = courses_cache[shift['groupName']]
    else:
        print("looking up from course planner. course name: ",
              shift['groupName'])
        courses = look(shift['groupName'])
        print('searching successful! number of classes found:',len(courses))
        courses_cache[shift['groupName']] = courses
        print(shift['groupName'], 'cached')
    # courses = courses_cache[shift['groupName']]
    for course in courses:
        if(course.title == shift['groupName']
          and course.section == shift['displayName']
          and course.location == shift['notes']
          and course.sdate == shift['startDateTime']
          and course.edate == shift['endDateTime']):
            # matched!
            course.isMatched = 0
            isMatched = 0
            break
        elif (course.sdate == shift['startDateTime']
        and course.edate == shift['endDateTime']):
            # incorrect location!
            course.isMatched = 3
            isMatched = 3
        elif(course.location == shift['notes'] and isMatched != 3):
            # incorrect time!
            course.isMatched = 2
            isMatched = 2                    

    # print('matching result:',isMatched)
    # courses_cache[shift['groupName']] = courses
    return isMatched

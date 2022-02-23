
import requests
import re
import string
from bs4 import BeautifulSoup
import scraper
import search
import datetime
import time
from dateutil.parser import parse

# workshop, lecture, all in small letters
li = search.look("Game Theory PG")
for x in li:
	x.display()
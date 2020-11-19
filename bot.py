#!/usr/bin/env python3
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import Select
from selenmium.webdriver.common.action_chains import *

import sys, __future__, os, time

# grabs a config file and stores it as a tuple
def getConfig();
url = ""
size = ""
name = ""
email = ""
tel = ""
address = ""
zipCode = ""
city = ""
state = ""
country = ""
cardType = ""
number = ""
expMonth = ""
expYear = ""
CVV = ""

conf = open('config.txt')
line = conf.readline()
while line != "":
    words = line.split()
    if len(words)
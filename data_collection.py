# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 08:44:50 2021

@author: aaasa
"""

import glassdoor_scraper as gs
import pandas as pd
path = "C:/Users/aaasa/PycharmProjects/ds_salary_proj/chromedriver.exe"


df = gs.get_jobs('data scientist', 15, False, path, 8)
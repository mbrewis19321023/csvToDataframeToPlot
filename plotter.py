import os
import sys
from numpy import mod
from openpyxl.styles import NamedStyle, Font, Border, Side
import tkinter as tk
from tkinter import Label, filedialog, Text
import tkinter.font as font
from openpyxl.utils.dataframe import dataframe_to_rows
from tkinter.filedialog import asksaveasfile
from openpyxl.styles import Alignment
from openpyxl import Workbook
from openpyxl.styles import PatternFill
from openpyxl.styles import NamedStyle, Font, Border, Side, numbers
import pandas as pd
import pandas as pd
import datetime
from openpyxl import Workbook
from openpyxl.styles import Font
import re
import matplotlib.pyplot as plt

f = open("myfile.csv", "w")
gingers = True
digitReplace = re.compile(r"(\d+)(,)(\d+)")
dateModify = re.compile(r"(\d{2})\-(\d{2})\-\d{2}(\d{2})")
regGroup = re.compile(
    r"\"\",\"(.*?)\",\"(.*?)\",\"(.*?)\",\"(.*?)\",\"(.*?)\",\"(.*?)\",\"(.*?)\",\"(.*?)\",")
monthList = ['Jan', 'Feb', 'Mar', 'Apr', 'May',
             'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

date = []
datetick = 0
load = []
solar = []
test = [1, 2, 3, 4, 5]

df = pd.read_pickle("data.pkl")
df2 = pd.read_pickle("data2.pkl")
dM = df.groupby(['Year', 'Month']).Load.max().reset_index().copy()
dMS = df.groupby(['Year', 'Month']).Solar.sum().reset_index().copy()
for x, row in dM.iterrows():
    date.append(str(dM.iloc[x]['Year']) + '-' + str(dM.iloc[x]['Month']))
    load.append(float(dM.iloc[x]['Load']))
    datetick = x
for x, row in dMS.iterrows():
    solar.append(dMS.iloc[x]['Solar'])

for x, i in enumerate(date):
    a = i.split("-")
    if a[1] == '1.0':
        date[x] = "Jan" + '-' + "20" + str(a[0].split('.')[0])
    if a[1] == '2.0':
        date[x] = "Feb" + '-' + "20" + str(a[0].split('.')[0])
    if a[1] == '3.0':
        date[x] = "Mar" + '-' + "20" + str(a[0].split('.')[0])
    if a[1] == '4.0':
        date[x] = "Apr" + '-' + "20" + str(a[0].split('.')[0])
    if a[1] == '5.0':
        date[x] = "May" + '-' + "20" + str(a[0].split('.')[0])
    if a[1] == '6.0':
        date[x] = "Jun" + '-' + "20" + str(a[0].split('.')[0])
    if a[1] == '7.0':
        date[x] = "Jul" + '-' + "20" + str(a[0].split('.')[0])
    if a[1] == '8.0':
        date[x] = "Aug" + '-' + "20" + str(a[0].split('.')[0])
    if a[1] == '9.0':
        date[x] = "Sep" + '-' + "20" + str(a[0].split('.')[0])
    if a[1] == '10.0':
        date[x] = "Oct" + '-' + "20" + str(a[0].split('.')[0])
    if a[1] == '11.0':
        date[x] = "Nov" + '-' + "20" + str(a[0].split('.')[0])
    if a[1] == '12.0':
        date[x] = "Dec" + '-' + "20" + str(a[0].split('.')[0])

# ax = plt.subplot(111)
# ax.bar(date, load, width=0.2, color='b', align='center')
# ax.bar(date, solar, width=0.2, color='r', align='center')
# plt.xticks(rotation = 'vertical')
# plt.show()

plt.title("Maximum demand per months")
plt.xticks(rotation='vertical')
plt.xlabel("Date")
plt.ylabel("Demand (kVA)")
plt.plot(date, load, 'bo-', label="Demand", )
for i, v in enumerate(load):
    plt.text(i, v + 3, "%d" % v, rotation = 90,ha="center", color = "blue")
plt.ylim(-10, 100)
plt.legend()

plt.show()

print()
# for j, x in enumerate(lines):
#         p1 = x.replace(';', '","')
#         p1 = x.replace('\n', '')
#         r1 = re.findall(dateModify, p1)
#         p1 = p1.split(",")
#         try:
#             infoPoints.loc[j] = [int(r1[0][2])] + [int(r1[0][1])] + [int(r1[0][0])]  + [p1[1]] + [float(p1[2])] + [float(p1[3])]
#         except IndexError:
#             pass

# infoPoints.to_pickle("data.pkl")
# infoPointsSumDayLoads = infoPoints.groupby(["Day"]).Load.sum().reset_index()
# infoPointsSumDaySolar= infoPoints.groupby(["Day"]).Solar.sum().reset_index()
# ax = infoPointsSumDayLoads.plot(x="Day",y=["Load"])
# infoPointsSumMonthLoads = infoPoints.groupby(["Month"]).Load.sum().reset_index()
# infoPointsSumDaySolar.plot(x="Day",y=["Solar"],ax = ax)
# plt.show()

# try:
#     if r1[0][1]:
#         if r1[0][1] == '01':
#             p5 = re.sub(dateModify, r"\1-Jan-\3", p1)
#         if r1[0][1] == '02':
#             p5 = re.sub(dateModify, r"\1-Feb-\3", p1)
#         if r1[0][1] == '03':
#             p5 = re.sub(dateModify, r"\1-Mar-\3", p1)
#         if r1[0][1] == '04':
#             p5 = re.sub(dateModify, r"\1-Apr-\3", p1)
#         if r1[0][1] == '05':
#             p5 = re.sub(dateModify, r"\1-May-\3", p1)
#         if r1[0][1] == '06':
#             p5 = re.sub(dateModify, r"\1-Jun-\3", p1)
#         if r1[0][1] == '07':
#             p5 = re.sub(dateModify, r"\1-Jul-\3", p1)
#         if r1[0][1] == '08':
#             p5 = re.sub(dateModify, r"\1-Aug-\3", p1)
#         if r1[0][1] == '09':
#             p5 = re.sub(dateModify, r"\1-Sep-\3", p1)
#         if r1[0][1] == '10':
#             p5 = re.sub(dateModify, r"\1-Oct-\3", p1)
#         if r1[0][1] == '11':
#             p5 = re.sub(dateModify, r"\1-Nov-\3", p1)
#         if r1[0][1] == '12':
#             p5 = re.sub(dateModify, r"\1-Dec-\3", p1)
#         p6 = p5.replace(" ", '","')
#         supString = '"","'
#         p7 = supString + p6
#         r2 = re.findall(regGroup, p7)
#         temp5 = float(r2[0][2]) * 2
#         p9 = p7[:22] + ',"blank",' + p7[23:]
# except IndexError:
#   print("oops")

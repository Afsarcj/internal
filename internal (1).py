# -*- coding: utf-8 -*-
"""internal.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Crxamcc9Ox_sqAyGQFa_uXcStPe5yw51
"""

print("""I am signing up for Replit's 100 days of python challenge! I will make sure to spend some time every day coding alomg, for a minimum of 10 minutes a day.I"ll be using Replit, an amazing online IDE so i can do this from my phone wherever i happened to be No excuses for not coding from the middle pf a feild!""")
malware={'adware':'track search history','Botnet':'attackers command','spyware':'which spy your device and data','keylogger':'monitor user activity like browsinghistory,email etc'}
print(malware)
print(len(malware))
print(type(malware))
malware['virus']:'that damage the data of system by attacker'
print(malware)
malware.update({'keylogger':'spyware'})
print(malware)
malware.pop('Botnet')
print(malware)
print(malware)

cost=12300
GST=18
netprice=cost+GSTamount
GSTamount=12300*18/100
print("Net price",netprice)
print("GST amount",GSTamount)

import pandas as pd
data=pd.DataFrame(
    {'name':['A','B','C','D','E','F','G','H','I','J'],
      'weight':[60,57,78,45,88,61,76,64,55,48],
      'DOY':[2002,2002,2002,2002,2002,2002,2002,2002,2002,2002],
      'height':[160,150,180,145,160,185,164,141,153],
      'age':[20]
}
      )
df['BMI']=df['weight']/df['height']*df['height']
df['health_status']=df['BMI'].apply(lambda x:'underweight' if x<60 else 'overweight')
print(df)



def household():
  print("\n House hold electricity bill")
  unit=int(input("units used"))
  if unit<100:
    price=unit*0.50
    print("bill amount : ",price)
  elif unit>101 and unit<200:
    price=unit*0.75
    print("bill amount : ",price)
  elif unit>201 and unit<300:
    price=unit*1.20
    print("bill amount : ",price)
  else:
    price=unit*1.50
    print("bill amount : ",price)
household()
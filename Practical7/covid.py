# import packages
import os
import pandas as pd
#change directoty
os.chdir("/Users/chenxuqi/IBI1_2020-21/Practical7")

#import the data
covid_data = pd.read_csv("full_data.csv")

#try to show something
covid_data.info()

print("the list for Afghanistan")
#to get the location of afghanistan
#covid_data.loc[covid_data['location'] == "Afghanistan"]
#create a Boolean that is True when the “location” is “Afghanistan”
row=[]
for i  in covid_data.iloc[0:,1]:
  if i =="Afghanistan":
    row.append(True)
  else:
    row.append(False)
#get the total cases of Afghanistan
covid_data.loc[row,"total_cases"]

#import the data
covid_data = pd.read_csv("full_data.csv")
row = []
for i in covid_data.iloc[0:, 1]:
  if i == "World":
    row.append(True)
  else:
    row.append(False)
#create a new object for world_new_cases
my_column = [True, False, True, False, False, False]
world_new_cases = covid_data.iloc[row, my_column]
#compute mean and the median
import numpy as np
mean=np.mean(world_new_cases.iloc[0:,1])
median=np.median(world_new_cases.iloc[0:, 1])
#print
print("mean of world new cases: ", mean)
print("median of world new cases:  =", median)

#create a box plots
import matplotlib.pyplot as plt
#create new list for new_cases
#new_cases only data for new cases
new_cases = world_new_cases.iloc[0:, 1]
#make the box plots
plt.boxplot(new_cases,
  vert = True,
  whis = 1.5,
  patch_artist = True,
  showbox = True,
  showcaps =True,
  showfliers = True,
  notch = False,
  meanline = True,
    )
plt.title("A boxplot of new cases worldwide")
plt.show()

#plot the data over time
world_dates = world_new_cases.iloc[0:, 0]
plt.plot(world_dates,new_cases , 'b+')
plt.title("A plot for dates and newcases")
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.show()


#answer question what proportion of cases have died in Germany and UK
#What proportion of cases have died (as of the latest information) in Germany? What
#proportion of cases have died in the UK?
Germany = []
row=[]
for i  in covid_data.iloc[0:,1]:
  if i =="Germany":
    row.append(True)
  else:
    row.append(False)
Germany_total_cases = covid_data.loc[row,"total_cases"]
Germany_total_deaths = covid_data.loc[row,"total_deaths"]
ratio = int(Germany_total_deaths.iloc[-1])/int(Germany_total_cases.iloc[-1])
print('The proportion of cases have died (until 2020-03-31) in Germany is ' + str(ratio*100)+ '%')

UK = []
row=[]
for i  in covid_data.iloc[0:,1]:
  if i =="United Kingdom":
    row.append(True)
  else:
    row.append(False)
United_Kingdom_total_cases = covid_data.loc[row,"total_cases"]
United_Kingdom_total_deaths = covid_data.loc[row,"total_deaths"]
ratio = int(United_Kingdom_total_deaths.iloc[-1])/int(United_Kingdom_total_cases.iloc[-1])
print('The proportion of cases have died (until 2020-03-31) in United Kingdom is ' + str(ratio*100)+ '%')
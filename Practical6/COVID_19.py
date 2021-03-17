#     Make a dictionary for the table
dict = {'USA':29862124, 'India': 11285561, 'Brazil':11205972, 'Russia':4360823, 'UK': 4234924}
#     Make a pie chart for the table
import matplotlib.pyplot as plt 
#     Pie chat, where the slices will be ordered and plotted counter-clockwis
labels = 'USA', 'India', 'Brazil', 'Russia', 'UK'
#     to make the sizes so we need to deal with number
sizes=[float(dict['USA']), float(dict['India']),float(dict['Brazil']),float(dict['Russia']),float(dict['UK'])] 
explode =(0.1,0,0,0,0)
#     to make a color i like
colors =['gold', 'yellow', 'green', 'red', 'blue']
#     specifies the fraction of the radius with which to offset each wedge
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=False, startangle=90)
plt.axis('equal')
#     equal aspect ratio ensures that pie is drawn as a circle
plt.show()

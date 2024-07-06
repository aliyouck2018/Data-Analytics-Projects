import pandas as pd
import random

dates_raw = pd.date_range(start='2019-01-01', end='2023-12-31', freq='B')
dates = []

for i in range(len(dates_raw)-1):
	dates.append(str(dates_raw[i]).split(' ')[0])

quartiers = pd.read_excel('quartiers-douala.xlsx')

data = []
for i in range(len(dates)-1):
	for index,quartier in quartiers.iterrows():
		data.append([dates[i],
					 quartier['Arrondissement'],
					 quartier['Quartier'],
					 quartier['Equipe'],
					 int(10*random.random())
		 ])

tonnage_journalier = pd.DataFrame(data, columns=['Date','Arrondissement','Quartier','Equipe','Tonnage'])
# tonnage_journalier.to_csv('syrapp-data.csv',sep=',',encoding='utf-8',index = None, header=True)

writer = pd.ExcelWriter('ramasage_ordures_stats.xlsx')
tonnage_journalier.to_excel(writer,'sheet1')
writer.save()
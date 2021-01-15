import json

#Look in the CSV file, and find the station code for Seattle. Station code for Seattle GHCND:US1WAKG0038
with open('stations.csv') as file:
    headers = file.readline()
    locations = []
    for line in file:
        Location, State, Station = line.split(',')
        locations.append({'Location': Location, 'State': State, 'Station': Station})
    
    
#print(f'this is the csv data: {locations}')

#• Use this station code to select all the measurements belonging to it from the JSON data
location_data = []


months = [[], [], [], [], [], [], [], [], [], [], [], []]

with open('precipitation.json') as file:
    data = json.load(file)
    for element in data:
        if element['station'] == 'GHCND:US1WAKG0038': #f'{locations['station']}':
            location_data.append(element)


    for element in location_data:
        for month in range(12):
            if f'-{(month + 1):02d}-'in element['date']:
                months[month].append(element['value'])
print(f'Tryout: {locations[1]['station']}')

#Calculate the sum of the precipitation over the whole year
total_prec_per_month = list(map(sum, months))

print(f'This is the total precipitation per month: {total_prec_per_month}')

#Calculate the relative precipitation per month (percentage compared to the precipitation over the whole year)
year_prec = sum(total_prec_per_month)
print(f'This is the total precipitation of the year {year_prec}')

relative_prec_per_month = []
for value in total_prec_per_month:
    relative_prec_per_month.append(value/year_prec)

print(f'This is the relative precipitation per month {relative_prec_per_month}')
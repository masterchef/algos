# Given people birth and death years find a year where there was most people alive

people = [{'birth': 1939, 'death': 2000},
          {'birth': 1940, 'death': 2010},
          {'birth': 1941, 'death': 2001},
          {'birth': 1942, 'death': 2015},
          {'birth': 1943, 'death': 1988},
          {'birth': 1944, 'death': 1987},
          {'birth': 1945, 'death': 2005},
          {'birth': 1986, 'death': 1987}, #max: 8
          {'birth': 1939, 'death': 1939}]

max_year = {'year': 0, 'count': 0}
year_population_index = {}

# Brute force
for person in people:
  for i in range(person['birth'], person['death']+1):
    if i in year_population_index.keys():
      year_population_index[i] += 1
    else:
      year_population_index[i] = 1
    if year_population_index[i] > max_year['count']:
      max_year['year'] = i
      max_year['count'] = year_population_index[i]

#print year_population_index
print max_year

# Optimal solution
deaths = []
births = []

for person in people:
  births.append(person['birth'])
  deaths.append(person['death'])

births = sorted(births)
deaths = sorted(deaths)

max_pop_year = 0
max_pop_count = 0

birth_index = 0
death_index = 0
current_population = 0
while birth_index < len(births):
  # if next birth is before next death increment count
  if births[birth_index] < deaths[death_index]:
    current_population += 1
    if current_population > max_pop_count:
      max_pop_year = births[birth_index]
      max_pop_count = current_population
    birth_index += 1
  elif births[birth_index] > deaths[death_index]:
    current_population -= 1
    death_index += 1
  # Given same birth and death year the population count does not change
  else:
    death_index += 1
    birth_index += 1

print max_pop_year, max_pop_count









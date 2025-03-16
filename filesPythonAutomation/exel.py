import openpyxl, pprint

wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
countryData = {}

for row in range(2, sheet.max_row + 1):
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value
    
    # print('B' + str(row))
    # print(sheet['B' + str(row)])
    # print(sheet['B' + str(row)].value)
    
    
    countryData.setdefault(state, {})
    countryData[state].setdefault(county, {'tracts':0, 'pop': 0})
    countryData[state][county]['tracts'] += 1
    countryData[state][county]['pop'] += int(pop)
resultFile = open('sheet.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countryData))
resultFile.close()
print('Done')
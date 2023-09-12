#! python3

import re

sampleDate = '29/02/1900'

dateRegex = re.compile(r'''
                       (\d{2}){1}
                       (\/){1}
                       (\d{2}){1}
                       (\/){1}
                       (\d{4})
''', re.VERBOSE)

matches = dateRegex.findall(sampleDate)[0]

day = int(matches[0])
month = int(matches[2])
year = int(matches[4])

day30Months = [4, 6, 9, 11]

if year < 1000 or year > 2999:
    print('Invalid Year!')
elif month > 12 or month < 1:
    print('Invalid Month!')
elif day > 31 or day < 1:
    print('Invalid Day!')
elif day == 31 and month in day30Months:
    print('Invalid Date!')
elif day == 29 and month == 2:
    if year in range(1000,3000,100) and not year % 400 == 0:
        print('Invalid Date!')
    elif year % 4 == 0:
        print('Valid Date!')
    else:
        print('Invalid Date!')
elif day not in range(1, 29) and month == 2:
    print('Invalid Date!')
else:
    print('Valid Date!')

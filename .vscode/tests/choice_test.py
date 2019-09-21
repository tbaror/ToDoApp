import datetime

YEAR_CHOICES = []
#datetime.datetime.now().year+1    
    
for r in range(1980, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))


print(YEAR_CHOICES)
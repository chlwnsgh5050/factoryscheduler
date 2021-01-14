import csv
import os

path = os.path.dirname(os.path.realpath(__file__))
cost = 0

for i in range(1,11):
    violation_time = 0
    setup_time = 0

    with open(path+'\\%i.csv'%i, 'r') as file:
        result = csv.reader(file, delimiter = ',')
              
        for r in result:
            if len(r)>1:
                violation_time += int(r[8])
                if r[7] == "O":
                    setup_time += 2

    print(i, "v_t:", violation_time, "s_t:", setup_time, "c:", violation_time+setup_time)
    cost += (violation_time+setup_time)
print(float(cost/10))
    

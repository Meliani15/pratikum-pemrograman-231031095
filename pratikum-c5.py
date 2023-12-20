import os
os.system ('cls')

a = True
limit = 5
i = 0
while a:
    i += 1
    
    print(f'Menjalankan program {limit + 1 - i}')
    if i == limit:
        a = False
        print('Program berhenti disini!')
    else: 
        a = True
    
    
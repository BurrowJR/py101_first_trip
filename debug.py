import pdb

counter = 1

#pdb.set_trace()

while counter <= 5:
    print(counter)
    #pdb.set_trace()  # add breakpoint
    counter += 1

cats = []

for name in ('Powder', 'Sky', 'Cheddar', 'Cocoa'):
    cats.append(name)

print(cats) 

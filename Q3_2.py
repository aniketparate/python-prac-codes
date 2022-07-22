# Calculate and return simple interest

def si(n, p, r):
    sim = float((n*p*r)/100)
    return sim


n = int(input('Enter Time period : '))
p = int(input('Enter principle amount  : '))
r = int(input('Enter Rate of interest : '))
sim = si(n, p, r)

print('Simple Interest : ', sim)
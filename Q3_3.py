# Calculate and display gross salary of two categories of employees, permanent and temporary.
# For permanent - gross salary = net salary + Bonus of 15% of net salary, no bonus for temporary employee.

def gross_p(ns):
    gs = ns + ns * 0.15
    return gs


ch = 0
while ch != 3:
    ch = int(input('1.Temporary Employee \n2.Permanent Employee \n3.Exit\nEnter your input here : '))
    if ch == 1:
        ns = int(input('\nEnter Net salary : '))
        print('Gross Salary : ', ns, "\n")
    elif ch == 2:
        ns = int(input('\nEnter Net salary : '))
        print('Gross Salary : ', gross_p(ns), "\n")
    else:
        exit(0)

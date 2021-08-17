import numpy as np


def sistema(*args):   
    equations = []
    for n in args:
        equations.append(n)
    message = ""
    term_list = []
    member = []
    member_list = []
    for j in range(len(equations)):
        terms = []
        buffer = ""
        members = equations[j].split("=")
        if len(members) == 2 and members[1].isnumeric():
            member = int(members[1])
            member_list.append(member)
            for i in range(len(members[0])):
                if i == 0 and members[0][i] == '-':
                    buffer += members[0][i]
                    continue
                if i != 0 and members[0][i] == '+':
                    terms.append(int(buffer))
                    buffer = ""
                    continue
                if i != 0 and members[0][i] == '-':
                    terms.append(int(buffer))
                    buffer = "-"
                    continue
                if members[0][i].isnumeric() and i < len(members[0]) - 1:
                    buffer += members[0][i]
                    continue
                if i == len(members[0]) - 1:
                    if members[0][i].isnumeric():
                        buffer += members[0][i]
                    terms.append(int(buffer))
                    break            
        else:
            message = "Arregla tu ecuación {} prro".format(j+1)
            return message

        term_list.append(terms)



    A = np.array(term_list)
    B = np.array(member_list)
    X = np.linalg.inv(A).dot(B)
    message = "Los valores de las incógnitas son: {}".format(X)


    print(A)
    print(B)
    print(message)
    print(-32 * (-0.2704918) + 15 * (0.25409836) - 3 * (3.1557377))
    print(13 * (-0.2704918) - 25 * (0.25409836) + 12 * (3.1557377))
    print(22 * (-0.2704918) + 11 * (0.25409836) + 1 * (3.1557377))
    

print(sistema("-32x+15y-3z=3", "13x-25y+12z=28", "22x+11y+1z=0"))

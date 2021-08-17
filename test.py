import numpy as np
# function: takes a simple linear equation as a string and returns
#           the literal value
def lineal(equation):
    members = equation.split("=")
    message = ""
    if len(members) == 2 and members[1].isnumeric():
        terms = []
        buffer = ""
        for i in range(len(members[0])):
            if i == 0 and members[0][i] == '-':
                buffer += members[0][i]
                continue
            if i != 0 and members[0][i] == '+' :
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

        A = np.array(terms)
        B = np.array([int(members[1])])
        x = (( A[1] * -1 ) + B[0] )/ A[0]
        message = "El valor de x es: " + str(x)
    else:
        message = "Arregla tu ecuación {} prro".format(equation)
    return message


def sistema(equation1, equation2):   
    equations = [equation1,equation2]
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
    print( -32 * (-0.81818182) + 15 * (-1.54545455))
    print(  13 * (-0.81818182) - 25 * (-1.54545455))
    

print(lineal("-32x+15=3"))
print(sistema("-32x+15y=3", "13x-25y=28"))

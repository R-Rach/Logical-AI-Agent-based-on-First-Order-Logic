"""------------------
    RACHIT RATHORE
    2015HS120600P
------------------"""

from KB import *
from Rule import Rule


def readPredicate(filename):
    predicateDict = []

    f = open(filename, "r")
    for line in f:
        temp=[]
        str = line.split("(",1)
        str1 = str[0]
        temp.append(str1)
        predicateDict.append(temp)
        str2 = str[1]
        str2 = str2.split(")",1)
        str2 = str2[0]

        vars = str2.split(",",1)
        temp.append(vars)
    return predicateDict

def readFacts(line):



    temp=[]
    str = line.split("(",1)
    str1 = str[0]
    temp.append(str1)
    str2 = str[1]
    str2 = str2.split(")",1)
    str2 = str2[0]

    vars = str2.split(",",1)
    temp.append(vars)
    return temp


def populate_FOL_KB(kb, filename):

    f = open(filename, "r")
    kb.kbFactDict = []
    for line in f:
        if str(line)==str("RULES\n"):
            break

        kb.kbFactDict.append(readFacts(line))


    for line in f:
        str3 = line.split("{",1)
        str3 = str3[1]
        str3 = str3.split("}",1)
        str3 = str3[0]
        str3 = str3.split(" => ",1)
        str3[0] = str3[0].split(" & ")
        for i in range(len(str3[0])):
            str3[0][i]=readFacts(str3[0][i])
        tempObj = Rule(str3[0],str3[1])
        kb.kbRule.append(tempObj)
    return kb


def isVariable(var1):
    if type(var1) is str:
        return var1.isupper()

def isConstant(var1):
    if type(var1) is str:
        return var1.islower()

def isCompound(var1):
    if type(var1[0]) is str and type(var1[1]) is list:
        return True
    else:
        return False

def isVarList(var1):
    if type(var1) is list :
        return True
    else:
        return False


def unify_var(var, x, s):
    if var in s:
        return unify(s[var], x, s)
    elif occur_check(var, x):
        return None
    else:
        return extend(s, var, x)

def occur_check(var, x):
    "Return true if var occurs anywhere in x."
    if var == x:
        return True
    elif not isConstant(x) and isVarList(x):
        for xi in x:
            if occur_check(var, xi):
                return True
    return False

def extend(s, var, val):
    s2 = s.copy()
    s2[var] = val
    return s2


def unify_list(p, q, substi):
    if not len(p) == len(q):
        return None
    else:
        for i in range(len(p)):
            substi = unify(p[i],q[i],substi)
        return substi

def unify(p,q,substi):
    if substi is None:
        return None
    elif p == q:
        return substi
    elif isVariable(p):
        return unify_var(p,q,substi)
    elif isVariable(q):
        return unify_var(q,p,substi)
    elif isVarList(p) and isVarList(p):
        return unify_list(p,q,substi)
    elif isCompound(p) and isCompound(q):
        if p[0]!=q[0]:
            return None
        else:

            return unify(p[1:],q[1:],unify(p[0],q[0],substi))
    else:
        return None



# Unify algo
# print("--------Unify algo---------")
#
# print('unifying fact = human(marcus) and query = human(X)')
# unifyResult = unify(['human', ['X']],['human',['marcus']],{})
# print(unifyResult)
#
# print('unifying fact = dead(marcus,79) and query = dead(marcus,Y)')
# unifyResult = unify(['dead', ['marcus', 'Y']],['dead',['marcus','79']],{})
# print(unifyResult)
#
# print('unifying fact = dead(marcus,79) and query = dead(X,Y)')
# unifyResult = unify(['dead', ['X', 'Y']],['dead',['marcus','79']],{})
# print(unifyResult)
#
# print('unifying fact = dead(marcus,79) and query = dead(jane,Y)')
# unifyResult = unify(['dead', ['jane', 'Y']], ['dead', ['marcus', '79']], {})
# print(unifyResult)
# print('-----------------------------------')

# unifyResult = unify(['dead', ['jane', 'Y']], ['dead', ['marcus', '79']], {})
# print(unifyResult)

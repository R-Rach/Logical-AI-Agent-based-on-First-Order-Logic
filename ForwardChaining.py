"""------------------
    RACHIT RATHORE
    2015HS120600P
------------------"""


from KB import *
from Rule import Rule
from UtilFuction import *


def forwardChaining_FOL(kb, query):
    pass
    for xRule in kb.kbRule:
        for xPremise in xRule.premise:
            inferFlag = True
            flag=1
            str1 = xPremise.split("(",1)
            argStr = str1[1].split(")",1)
            argStr = argStr[0].split(",")
            # print(argStr)
            predicateStr = str1[0]

            if not predicateStr in kb.kbFactDict.keys():
                inferFlag = False
                flag=0
                break

            else:
                temp1 ={}
                count = 0
                for y in kb.kbFactDict[predicateStr]:
                    temp1= unify(argStr,y,temp1)
                    # count = count+1
                    if temp1 is None:
                        continue
                    else:
                        print(temp1)
                #         else has cobination of temp and temp1
                # if temp.keys().empty():
                #     inferFlag=False
                #     break
                # else:
                #     pass



# kb = KB({},[],{})
#
# kb = populate_FOL_KB(kb,"testruleFile1.txt")
# kb.kbFactDict = {'human': [['john'],['marcus']]}
# print(kb.kbFactDict)
# for x in kb.kbRule:
#     print(x)
#
#
#
# forwardChaining_FOL(kb,None)
# print(kb.kbFactDict.keys())
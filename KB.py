"""------------------
    RACHIT RATHORE
    2015HS120600P
------------------"""


class KB:

    def __init__(self, kbFactDict, kbRule ,kbSubstDict):
        self.kbFactDict = kbFactDict
        self.kbRule = kbRule
        self.kbSubstDict = kbSubstDict

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __str__(self):
        return "Facts - \n" + str(self.kbFactDict) + " Rules - \n" + str(self.kbRule)
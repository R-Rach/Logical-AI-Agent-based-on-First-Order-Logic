"""------------------
    RACHIT RATHORE
    2015HS120600P
------------------"""


class Rule:

    def __init__(self, premise, conclusion):
        self.premise = premise
        self.conclusion = conclusion

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __str__(self):
        return "Premise - " + str(self.premise) + "     Conclusion - " + str(self.conclusion)
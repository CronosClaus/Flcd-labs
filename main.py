import re
from difflib import SequenceMatcher

'''
FA.in example 
p+ = {'q':'a','r':'b'}
q = {'q':'a','r':'b'}
r* = {}

p+ = {'q':'0','p':'1','r':'1'}
q = {'q':'0','r':'1'}
r* = {'r':'0'}
'''


class FA:
    def __init__(self):
        self.__states = []
        self.__initial_state = ''
        self.__alphabet = set()
        self.__transitions = {}
        self.__finalStates = []

    def readFromFile(self, fileName):
        with open(fileName, "r") as f:
            line = f.readline()
            while line:
                line = line.split()
                if line[0][0] == '*':
                    self.__finalStates.append(line[0][1])
                    self.__states.append(line[0][1])
                else:
                    self.__states.append(line[0][0])

                if line[0][-1] == "+":
                    self.__initial_state = line[0][0]

                d = eval(line[2])

                for i in d:
                    if not isinstance(d[i], list):
                        self.__alphabet.add(d[i])
                    else:
                        for j in d[i]:
                            self.__alphabet.add(j)

                if line[0][0] == '*':
                    self.__transitions[line[0][1]] = d
                else:
                    self.__transitions[line[0][0]] = d

                line = f.readline()

    def display(self):
        print(" s - states\n a - alphabet\n t - transitions\n fs - final states\n all - all elements")
        display = input("What elements of the finite automata you want to see?\n")
        if display == "s":
            print("states : ", end=" ")
            print(self.__states)
        elif display == "a":
            print("alphabet : ", end=" ")
            print(list(self.__alphabet))
        elif display == "t":
            print("transitions : ", end=" ")
            print(self.__transitions)
        elif display == "fs":
            print("finalStates : ", end=" ")
            print(self.__finalStates)
        elif display == "all":
            print("states : ", end=" ")
            print(self.__states)
            print("alphabet : ", end=" ")
            print(list(self.__alphabet))
            print("transitions : ", end=" ")
            print(self.__transitions)

            print("finalStates : ", end=" ")
            print(self.__finalStates)
        elif display == "exit":
            return
        self.display()



if __name__ == '__main__':
    fa = FA()
    fa.readFromFile("FA.in")
    fa.display()

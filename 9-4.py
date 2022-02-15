class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        if len(self.data) == 0:
            return False
        else:
            return self.data.pop(-1)

    def read(self):
        if len(self.data) == 0:
            return False
        else:
            return self.data[-1]

def reverseString(string):
    for i in string:
        alphabet_list.push(i)
    while alphabet_list.read():
        reversed_list.append(alphabet_list.pop())
    return reversed_list

alphabet_list = Stack()
string = input()
reversed_list = []
print(reverseString(string))
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

class Linter:
    def __init__(self):
        self.stack = Stack()

    def chkMatch(self, opening_brace, closing_brace):
        if opening_brace == '(' and closing_brace == ')':
            return True
        elif opening_brace == '{' and closing_brace == '}':
            return True
        elif opening_brace == '[' and closing_brace == ']':
            return True
        else:
            return False

    def lint(self, text):
        for i in text:
            if i == '(' or i == '{' or i == '[': #여는 괄호이면
                self.stack.push(i) #stack에 push한다.
            elif i == ')' or i == '}' or i == ']': #닫는 괄호이면
                popped_opening_brace = self.stack.pop() #stack에 pop한다.
                if not popped_opening_brace: #만약에 pop할 수 있는 괄호가 없으면
                    return i + "doesn't have opening brace" #오류 출력
                elif not self.chkMatch(popped_opening_brace, i): #만약에 pop한 괄호가 매칭되지 않으면
                    return i + "has mismatched opening brace" #오류 출력

        if self.stack.read(): #괄호를 모두 pop했음에도 남아있는 (여는)괄호가 있다면
            return self.stack.read() + "does not have closing brace" #오류 출력
        else:
            return True

linter1 = Linter()
linter2 = Linter()
print(linter1.lint("( var x = { y : [1, 2, 3] } )"))
print(linter2.lint("var x = { y : [1, 2, 3] })"))
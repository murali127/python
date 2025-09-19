class stk:
    def __init__(self):
        self.stk=[]
    def push(self,item):
        self.stk.append(item)
    def pop(self):
        if not self.is_empty():
            return self.stk.pop()
        return "Stack is empty"
    def peek(self):
        if not self.is_empty():
            return self.stk[-1]
        return  "Stack is empty"
    def is_empty(self):
        return len(self.stk)==0
    def size(self):
        return len(self.stk)
ss=stk()
ss.push(10)
ss.push(11)
print(ss.peek())
print(ss.size())
ss.pop()
print(ss.peek())
print(ss.size())

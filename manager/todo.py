class ToDoList:
    def __init__(self,todo,done):
        self.todo=[]
        self.done=[]

    def add(self):
        n=int(input("enter the number of tasks to be added: "))
        for i in range(n):
            t=input("enter the tasks: ")
            self.todo.append(t)

    def Done(self):
        m=input('enter the task to be removed: ')
        self.todo.remove(m)
        self.done.append(m)

    def display(self):
        print(self.todo)
        print(self.done)
Todo=ToDoList([],[])
while True:
    Todo.add()
    Todo.Done()
    Todo.display()

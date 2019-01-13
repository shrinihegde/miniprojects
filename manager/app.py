import main
m=main.ToDoList()
n=eval(input("enter the number of tasks to be added: "))
to_do=[]
for i in range(1,(n+1)):
    a=str(input("enter the task to be added: "))
    z=m.addd(a)
print(to_do)
x=eval(input("enter the task number done: "))
c=m.markdone(z,x)
m.done(c)
m.display(z)

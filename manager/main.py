class ToDoList():
    def addd(self,a):
        self.a=a
        to_do.append(self.a)
        
        return(to_do)

    def markdone(self,z,n):
        self.z=z
        self.n=n
        var=z.pop(self.n)
        return(var)

    def done(self,var):
        self.var=var
        done=[]
        done.append(self.var)
        print(done)

    def display(self,z):
        self.z=z
        print(self.z)



n=eval(input("enter the number of tasks to be added: "))
manage=ToDoList()
to_do=[]
for i in range(1,(n+1)):
    a=str(input("enter the task to be added: "))
    z=manage.addd(a)
print(to_do)
x=eval(input("enter the task number done: "))
c=manage.markdone(z,x)
manage.done(c)
manage.display(z)

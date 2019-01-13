class Meeting:
    def time_view(dic):
        a=dic.values()
        print('\n'.join(a))
    def schedule(s,n):
            sch=dic.get(n)
            print(f"the slot {sch} has been scheduled")
               
dic={1:"1: 9.00-10.00 AM",2:"2: 10.15-11.15am",3:"3: 11.30am-12.30PM",4:"4: 1.00-2.00PM",5:"5: 2.15-3.15"}
s=dic.keys()
leng=len(s)
print(s)
manage=Meeting
manage.time_view(dic)
time=eval(input("enter the slot you want: "))
manage.schedule(s,time)

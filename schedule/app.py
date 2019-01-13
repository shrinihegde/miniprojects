import main
z=main.Meeting
dic={1:"1: 9.00-10.00 AM",2:"2: 10.15-11.15am",3:"3: 11.30am-12.30PM",4:"4: 1.00-2.00PM",5:"5: 2.15-3.15"}
keys=dic.keys()
z.time_view(dic)
time=eval(input("enter the slot you want: "))
z.schedule(dic,keys,time)

class Meeting:
    def time_view(dic):
        a=dic.values()
        print('\n'.join(a))
    def schedule(dic,keys,time):
        sch=dic.get(time)
        print(f"the slot {sch} has been scheduled")
        

import random
class ConsoleGame:
    def create(self):
        self.lst=[]
        for i in range(8):
            self.mat= random.sample(range(100),8)
            self.lst.append(self.mat)
        return self.lst

    def check(self,inp):
        self.flg=0
        self.inp=inp
        for i in range(8):
            for j in range(8):
                if self.inp == self.lst[i][j]:
                    self.flg=1
                    break
        return self.flg

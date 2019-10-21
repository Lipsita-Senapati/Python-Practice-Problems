

##class Books:
##    def book(self,bid,bname,bno):
##        self.bid =bid
##        self.bname = bname
##        self.bno = bno
##    def show(self):
##        print(self.bid,self.bname,self.bno)
##
##l = []
##for i in range(3):
##    i = Books()
##    i.book(int(input("Id")),input("bname"),int(input("bno")))
##    l.append(i)
##for i in range(3):
##    l[i].show()


# instance method
class Test:
    x = 100
    def input(self,x,y):


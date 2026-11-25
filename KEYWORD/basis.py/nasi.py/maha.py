class Demo:
 
 a=30
 b=40
 def __init__(self,c,d):
    self.c=c
    self.d=d
 def display(self):
    print(self.c,self.d)
 def ch_display(self,new):
    self.c=new
 @classmethod
 def dis(cls):
    print(cls.a,cls.b)
 @staticmethod
 def msg():
    print("public Acess specifier")
User = Demo(30,40)
User.display()
User.ch_display(50)
User.display()
# class student:
#     def sayHello(self):
#         print("Hellow "+ self.Fname)

# s1=student()
# s2=student()
# s1.Fname="Redwan"
# s2.Fname="Yosehp"
# # print(id(Abebe))
# # print(id(Redwan))
# # s1.sayHello()
# s2.sayHello()


class student:
    def __init__(self,fn,ln,s):
        self.Fname=fn
        self.Lname=ln
        self.sex=s
        

    def FullnameET(self):
        print("In Ethiopia "+self.Fname+" "+self.Lname)

    def  FullnameWET(self):
        print("In Western "+self.Lname+", "+self.Fname)
    def studentdata(self):
        print(self.Fname+" "+self.Lname)
        
s1=student("Abebe","Kebede","M")
s1.FullnameET()

s2=student("Yoseph","Kassaye","M")
s2.FullnameWET()
class A:
    def displayA(self):
        print("welcome to home")

class B:        
     def displayB(self):
        print("welcome to home")

class C(A,B):
     def displayC(self):
        print("welcome to home")    

obj = C()
obj.displayA()     
obj.displayB()
obj.displayC()        
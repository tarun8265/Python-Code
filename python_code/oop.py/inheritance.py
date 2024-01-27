class A:
    def displayA(self):
        print("welcome to home")

class B:        
     def displayB(self):
        print("welcome to home")

class C(A,B):
     def display(self):
        print("welcome to home")    

obj = B()
obj.displayA()     
obj.displayB()        
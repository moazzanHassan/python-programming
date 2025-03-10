'''Exercise 4: Counter Class
Task: Ek Counter class banao jo:

Ek count variable store kare jo shuru me 0 ho
increment() aur decrement() methods likho
get_count() method likho jo current count return kare'''

class counter:
    def __init__(self):
        self.counter = 0
    def decrement(self,dec):
        self.counter = self.counter-dec
    def increment(self,inc):
        self.counter = self.counter + inc
    def get_count(self):
        return self.counter

# count = counter()
# count.increment(1000)
# print(count.get_count())
# count.decrement(10)
# print(count.get_count())

'''Exercise 5: Student Grade System
Task: Ek Student class banao jo:

name aur marks store kare
add_marks(subject, marks) method likho jo ek subject ke marks store kare
get_average() method likho jo sab subjects ke marks ka average return kare'''

class Student:
    def __init__(self,name,sub_mar):
        self.name = name
        sub_mar ={
            sub: [],
            mark : [] 

        }
    def add_marks(self):
        
        self.sub_mar[self.sub].append(self.sub)
        self.sub_mar[self.semark].append(self.mark)
    def get_average(self):
        pass



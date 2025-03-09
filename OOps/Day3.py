'''Exercise 1: Create a Simple Class
Task: Ek Person class banao jo name aur age ko store kare. Ek method introduce() likho jo print kare:

"Hello, my name is [name] and I am [age] years old."'''

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"My naem is {self.name} and my age is {self.age}")
    
# person1 = Person("Moazzan",123)
# person1.introduce()
class BankAccount:
    def __init__(self):
        pass
    def deposit(amount):
        pass
    def withdraw(amount):
        pass
    def get_balance():
        pass

account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance()) 
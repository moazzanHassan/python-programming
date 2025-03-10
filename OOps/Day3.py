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
'''Exercise 2: Bank Account
Task: Ek BankAccount class banao jo:

balance store kare
deposit(amount) aur withdraw(amount) methods likho
get_balance() method likho jo current balance return kare'''
class BankAccount:
    def __init__(self,balance):
        self.balance = balance
    def deposit(self,dep_amou):
        self.balance = self.balance + dep_amou
        return self.balance
    def withdraw(self,wit_amou):
        self.balance = self.balance - wit_amou
        return f"your current balance is {self.balance} and you withdraw {wit_amou}"
    def get_balance(self):
        return self.balance

# account = BankAccount(1000)
# account.deposit(500)
# account.withdraw(200)
# print(account.get_balance()) 
'''Exercise 3: Car Class
Task: Ek Car class banao jo:

brand aur model store kare
Ek describe() method likho jo car ka brand aur model print kare'''
class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def describe(self):
        return f"This car is a {self.brand} {self.model}"
# car1 = Car("toyta","crolla")    
# print(car1.describe())
        

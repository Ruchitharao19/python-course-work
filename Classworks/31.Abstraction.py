from abc import ABC, abstractmethod
class bankaccount:
    def checkbalance(self,username):
        self.username=username
        print(f"\n\nHI {self.username}!!!\ndisplay the balance")
    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def withdraw(self):
        pass
class currentaccount(bankaccount):
    def deposit(self):
        print("deposit anytime")
    def withdraw(self):
        print("withdraw anytime")
class savingsaccount(bankaccount):
    def deposit(self):
        print("deposit limits")
    def withdraw(self):
        print("withdraw limits")
class salaryaccount(bankaccount):
    def deposit(self):
        print("deposit once a month")
    def withdraw(self):
        print("withdraw anytime")
class jointaccount(bankaccount):
    def deposit(self):
        print("deposit anytime by 2 persons")
    def withdraw(self):
        print("withdraw anytime by 2 persons")
class pensionaccount(bankaccount):
    def deposit(self):
        print("deposit once a month")
    def withdraw(self):
        print("withdraw anytime")
class fdaccount(bankaccount):
    def deposit(self):
        print("deposit only once")
    def withdraw(self):
        print("withdraw only once")

sumanth=currentaccount()
sumanth.checkbalance("sumanth")
sumanth.deposit()
sumanth.withdraw()
ruchitha=savingsaccount()
ruchitha.checkbalance("ruchitha")
ruchitha.deposit()
ruchitha.withdraw()
randheer=salaryaccount()
randheer.checkbalance("randheer")
randheer.deposit()
randheer.withdraw()
varsha=jointaccount()
varsha.checkbalance("varsha")
varsha.deposit()
varsha.withdraw()
preethi=pensionaccount()
preethi.checkbalance("preethi")
preethi.deposit()
preethi.withdraw()
suma=fdaccount()
suma.checkbalance("suma")
suma.deposit()
suma.withdraw()

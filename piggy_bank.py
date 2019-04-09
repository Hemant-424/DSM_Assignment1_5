#!/usr/bin/env python
# coding: utf-8

# In[79]:


class Piggy_bank:
    
    print("-"*50,"start","-"*50)

    def __init__(self):
        self.money = 0
        print("Hello!!!Welcome to Piggy_bank")
        
    def add_money(self):
        addmoney = float(input("Enter amount to be Deposited:"))
        self.money = self.money + addmoney
        print("After adding, The available balance is {} rupees".format(self.money))
    
    def withdrawal_money(self):
        withdrawal = float(input("Enter amount to be Withdrawed:"))
        if (self.money > withdrawal):
            self.money = self.money - withdrawal
            print("After withdrawal,The available balance is {} rupees".format(self.money))
        else:
            print("Insufficient balance")
        
    
    def check_balance(self):
        print("Current balance in your account is {} rupees".format(self.money))
    


# In[80]:


user1 = Piggy_bank()


# In[81]:


user1.check_balance()


# In[83]:


user1.add_money()


# In[86]:


user1.withdrawal_money()


# In[87]:


user1.check_balance()


# In[ ]:





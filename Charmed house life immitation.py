#!/usr/bin/env python
# coding: utf-8

# In[1]:


from random import randint
from termcolor import cprint

class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.happiness = 30
        self.house = None
        self.growth = 0
        
    def __str__(self):
        return f'{self.name}: fullness - {self.fullness}, happiness - {self.happiness}, growth {self.growth}.'
        
    def work(self):
        if self.house.money <=15:
            cprint('The family is running out of money, she should go to work.', color='yellow')
        self.house.money += 40
        self.fullness -= 10
        self.happiness -= 5
        self.growth +=5
        cprint(f'{self.name} goes to work and earns money.', color = 'green')
        
    def eat(self):
        if self.house.food >= 10:
            self.house.food -= 10
            self.fullness += 15
            self.happiness += 5
            print(f'{self.name} eats.')
        else:
            print('There is no food left in the house.')
            
    def shopping(self):
        if self.house.food <= 20 or self.house.cat_food <= 20:
            if self.house.money >= 60:
                self.house.food += 20
                self.house.cat_food += 20
                self.fullness -= 5
                self.house.money -= 60
                self.growth += 2
                print(f'{self.name} bought groceries and catfood, now they have {self.house.food} food and {self.house.money} y.e left.')
            elif 10 <= self.house.money < 60:
                self.house.food += 10
                self.fullness -= 5
                self.house.money -= 10
                self.growth += 1
                print(f'{self.name} bought groceries, now they have {self.house.food} food and {self.house.money} y.e left.')
            else: 
                print('There is no money left.')
        else:
            print('There is enough food for everyone.')
    
    def sleep(self):
        self.happiness += 10
        self.fullness -= 5
        self.growth += 1
        cprint(f'{self.name} sleeps well and feels better.', color='magenta')
        
    def learn(self):
        self.happiness += 10
        self.fullness -= 5
        self.growth += 10
        cprint(f'{self.name} studies and feels better.', color='magenta')
        
    def procrastinate(self):
        self.happiness += 10
        self.house.money -= 5
        self.fullness -= 5
        self.growth -= 5
        cprint(f'{self.name} procrastinates.', color='red')
        
    def cleaning(self):
        self.house.dirt -=30
        self.fullness -=10
        self.house.monet = -5
        
    def move_in_house(self, house):
        self.house = house
        self.food = 30
        self.money = 40
        self.growth += 5
        cprint(f'{self.name} moved in the house.', color = 'green')
          
    def life(self):
        if self.fullness <0:
            cprint(f'{self.name} is dead.', color='red')
            return
        dice = randint(1,6)
        if self.fullness < 20:
            self.eat()
        elif self.house.money <= 30:
            self.work()
        elif self.house.food < 20 or self.house.cat_food <30:
            self.shopping()
        elif self.house.cat_food < 30:
            self.shopping()
        elif self.house.dirt> 100:
            self.cleaning()
        elif dice == 1:
            self.sleep()
        elif dice == 2:
            self.eat()
        elif dice == 3:
            self.learn()
        elif dice == 4:
            self.cleaning()
        elif dice == 5:
            self.work()
        else:
            self.procrastinate() 
            
class House:
    
    def __init__(self):
        self.food = 30
        self.money = 40
        self.cat_food = 0
        self.dirt = 0
        
    def __str__(self):
        return f'Food: {self.food}, catfood: {self.cat_food}, money: {self.money}, dirt: {self.dirt}.'
    
class Cat:
    
    def __init__(self, nickname):
        self.nickname = nickname
        self.fullness = 15
        self.house = None
    
    def __str__(self):
        return f'Cat {self.nickname}: full {self.fullness}.'
    
    def be_found(self, house):
        self.house = house
        self.fullness += 10
        self.house.cat_food -=5
        cprint(f'{self.nickname} is found.', color = 'green')
        
    def cat_eat(self):
        self.fullness += 20
        self.house.cat_food -= 10
        print(f'{self.nickname} eats.')
        
    def cat_sleep(self):
        self.fullness -= 10
        print(f'{self.nickname} sleeps.')
        
    def destroy(self):
        self.fullness -=10
        self.house.dirt +=20
        print(f'{self.nickname} destroys.')
        
    def cat_life(self):
        if self.fullness <0:
            cprint(f'{self.nickname} is dead.', color='red')
            return
        dice = randint(1,6)
        if self.fullness < 20:
            self.cat_eat()
        elif dice == 1:
            self.cat_eat()
        elif dice == 2 or dice == 5:
            self.cat_sleep()
        else: 
            self.destroy()
           
sisters = [
    Man('Piper'), 
    Man('Prue'),
    Man('Phoebe'),
    Man('Page'),
    ]
 
kittens = [
Cat('Black'),
Cat('Ginger')
]

charmed_home = House()
for sister in sisters:
    sister.move_in_house(house = charmed_home)
for kitten in kittens:
    kitten.be_found(house = charmed_home)

for day in range(1, 366):
    print(f'=======Day {day} started======')
    for sister in sisters:
        sister.life()
    for kitten in kittens:
        kitten.cat_life()
    print('---By the end of the day---') 
    for sister in sisters:
        print(sister)
    for kitten in kittens:
        print(kitten)    
    print(charmed_home)


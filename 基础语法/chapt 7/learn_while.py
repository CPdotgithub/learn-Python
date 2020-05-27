# car=input ("What kind of car do you want rent ?")
# print("Let me see if I can find you a "+car+" .")
# number=int(input ("How many people are you togather ?\n"))
# active= True
# while active :
#     if number < 8 :
#         print("OK!")
#     else:
#         print("Sorry ! We don't have enough seats .")
#     active=False
# a=int(input("Please input a integer !\n"))
# if a%10==0:
#     print("这个数字是十的整数倍！")
# else:
#     print("这个数字不是十的整数倍！")
# formula_pizza=[]
# print("Please list the ingredient in pizza !\nEnter quit to end input !")
# active=True
# while active:
#     ingredient=input()
#     if ingredient=='quit':
#         active=False
#     else:
#         formula_pizza.append(ingredient)
#         print("We will add "+ingredient+" in the pizza !")    
# print(formula_pizza)   
# tickets_price={
#     'low':'free',
#     'medium':'$3',
#     'high':'$15'
# }
# age=int(input("How old are you ?\n"))
# if age<3:
#     price=tickets_price['low']
# elif age>=3 and age<12:
#     price=tickets_price['medium']
# elif age >=12:
#     price=tickets_price['high']
# print("You should pay "+price+" for it .")
food_orders=['热干面','牛肉面','拉面','擀面','打卤面','热干面','热干面','牛肉面']
# finished_foods=[]
# for food in food_orders:
#     print("I made your "+food+" .")
#     finished_foods.append(food)
# print(finished_foods)
for food in food_orders:
    while food =='热干面':
        new_food_orders=food_orders.remove('热干面')
print(food_orders,new_food_orders)
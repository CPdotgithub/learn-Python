# # direction_travel=['beijing','shanghai','xian','wuhan','henan']
# # # # print(direction_travel)
# # # sorted(direction_travel)
# # # # print(sorted(direction_travel,reverse=True))
# # # direction_travel.reverse()
# # # direction_travel.append('tianjing')
# # # a=len(direction_travel)
# # # print('There are '+str(a)+' place I want go !' )
# # for direction in direction_travel:
# #     print('\nI want to go '+ direction +' .' )
# # print('\nI love all the places in china !')
# # for value in list(range(1,21)):
# #     print(value)
# # for value in list(range(1,10**6)):
# #         print(value)
# # values=list(range(1,10**6+1))
# # print(max(values),min(values),sum(values))
# values=list(range(1,20))
# print(values)
# for value in range(1,11):
#     print(value**3)
# values=[value**3 for value in range(1,11)]
# print(values[8:-2])
directions=['beijing','shanghai','xian','wuhan','chengdu']
print('The first three cities in the list are')
print(directions[0:3])
print('Three cities in the middle of the list are')
print(directions[1:4])
print('The lasr three cities in the  list are')
print(directions[-3:])
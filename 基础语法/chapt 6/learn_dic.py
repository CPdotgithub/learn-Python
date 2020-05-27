# favorite_languages={
#     'jen':'python',
#     'xiaoming':'c',
#     'sarah':'java',
#     'phill':'c',
# }
# # for v in set(favorite_languages.values()):
# #     print(v+' ')
# CP={
#     'first_name':'cao',
#     'last_name':'pan',
#     'city':'wuhan',
#     'age':'25'
# }
# print('\nfirst_name :'+CP['first_name']+
#       '\nlast_name :'+CP['last_name']+
#       '\ncity :'+CP['city']+
#       '\nage :'+CP['age'])
# favorite_numbers={
#     'cp':5,
#     'libai':9,
#     'maozedong':100,
#     'lidan':0,
#     'sushi':7
# }
# for k,v in favorite_numbers.items():
#     print(k+"'s" +"favorite number is "+str(v)+".")
# investigate_name={
#     'cp': False,
#     'dx': True ,
#     'LBW': True ,
# }
# for k,v in investigate_name.items():
#     if v:
#         print(k.title()+" , Thank you !")
#     else:
#         print(k.lower().title()+", we will have a investigation !")
# name_pets={
#     'huanhaun':{'category':'dog','lord':'CP'},
#     'tudou':{'category':'cat','lord':'libai'},
#     'xigua':{'category':'mouse','lord':'dangdang'}
# }
# list_name=[key for key in name_pets.keys()]
# for name in list_name:
#     print(name+" :\n")
#     detail_inf=name_pets[name]
#     print(name +" is a "+detail_inf['category']+", it belongs to "+detail_inf['lord']+" .")
favorite_places={
    'Jordan':['nanjing','beijing','shanghai'],
    'CP':['wuhan','shashi','henan'],
    'cdx':['jingzhou','beijing','xizhang']
}
for name in favorite_places.keys():
    list_places=favorite_places[name]
    print(name.title()+" favorite places are ")
    for place in list_places:
        print(place+' .')
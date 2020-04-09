import classes
import requests
from classes import *

usr = User()
usr.get_user('butanediol')

# print(usr.id)
# print(usr.url)
# print(usr.username)
# print(usr.nickname)
# print(usr.avatar.large)
# print(usr.avatar.medium)
# print(usr.avatar.small)
# print(usr.sign)
# print(usr.usergroup.type)
# print(usr.usergroup.type_id)

usr.get_user_collection()
print(usr.collections[0].subject.id)
print(usr.collections[1].subject.collection)
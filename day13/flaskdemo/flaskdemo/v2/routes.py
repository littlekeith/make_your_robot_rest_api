# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.pet import Pet
from .api.pet_findByStatus import PetFindbystatus
from .api.pet_findByTags import PetFindbytags
from .api.pet_petId import PetPetid
from .api.pet_petId_uploadImage import PetPetidUploadimage
from .api.store_inventory import StoreInventory
from .api.store_order import StoreOrder
from .api.store_order_orderId import StoreOrderOrderid
from .api.user import User
from .api.user_createWithArray import UserCreatewitharray
from .api.user_createWithList import UserCreatewithlist
from .api.user_login import UserLogin
from .api.user_logout import UserLogout
from .api.user_username import UserUsername


routes = [
    dict(resource=Pet, urls=['/pet'], endpoint='pet'),
    dict(resource=PetFindbystatus, urls=['/pet/findByStatus'], endpoint='pet_findByStatus'),
    dict(resource=PetFindbytags, urls=['/pet/findByTags'], endpoint='pet_findByTags'),
    dict(resource=PetPetid, urls=['/pet/<int:petId>'], endpoint='pet_petId'),
    dict(resource=PetPetidUploadimage, urls=['/pet/<int:petId>/uploadImage'], endpoint='pet_petId_uploadImage'),
    dict(resource=StoreInventory, urls=['/store/inventory'], endpoint='store_inventory'),
    dict(resource=StoreOrder, urls=['/store/order'], endpoint='store_order'),
    dict(resource=StoreOrderOrderid, urls=['/store/order/<int:orderId>'], endpoint='store_order_orderId'),
    dict(resource=User, urls=['/user'], endpoint='user'),
    dict(resource=UserCreatewitharray, urls=['/user/createWithArray'], endpoint='user_createWithArray'),
    dict(resource=UserCreatewithlist, urls=['/user/createWithList'], endpoint='user_createWithList'),
    dict(resource=UserLogin, urls=['/user/login'], endpoint='user_login'),
    dict(resource=UserLogout, urls=['/user/logout'], endpoint='user_logout'),
    dict(resource=UserUsername, urls=['/user/<username>'], endpoint='user_username'),
]
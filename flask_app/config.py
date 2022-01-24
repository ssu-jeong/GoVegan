#### config.py ####

import os

BASE_DIR = os.path.dirname(__file__)


# db = {
#     'user'     : 'root',        
#     'password' : 'dla04tn13',    
#     'host'     : 'localhost',    
#     'port'     : 3306,            
#     'database' : 'Products'        
# }



SQLALCHEMY_DATABASE_URI = "mysql://b766cc9b26da01:0892f678@us-cdbr-east-05.cleardb.net/heroku_3a692aa14e1f492"

# #-- MySQL연동
# SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"


#-- 뭘까...?
SQLALCHEMY_TRACK_MODIFICATIONS = True

#-- Flask-WTF를 사용하기 위해서 SECRET_KEY설정 / '원래는 어렵게 설정해야함'
SECRET_KEY = 'dev'
import pymysql
from Configuration import Configuration

def connect():
    return pymysql.connect(host=Configuration.BD_PASS, user="root", password=Configuration.BD_PASS, database="sys")
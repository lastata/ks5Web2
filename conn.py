import pymysql
import config


class Connection:
    @staticmethod
    def connection():
        try:
            connection = pymysql.connect(database=config.database,host=config.host, port=config.port, user=config.user, password=config.password)
            print("conn success")
            return connection
        except:
            print("eror")

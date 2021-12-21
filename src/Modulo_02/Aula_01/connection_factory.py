import MySQLdb

class ConnectionFactory(object):

    def get_connection(self):
        return MySQLdb.connect(host="localhost", user='root', passwd='', db='alura')
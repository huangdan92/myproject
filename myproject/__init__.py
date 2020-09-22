import pymysql

pymysql.version_info = (2, 0, 1, 'final', 0)  # change mysqlclient version
pymysql.install_as_MySQLdb()

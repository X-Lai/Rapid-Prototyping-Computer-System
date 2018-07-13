import json
import pymysql

class DBmanager:
    def __init__(self, host, user, password, db):
        '''
        set user information
        '''
        self.db = pymysql.connect(host=host, user=user, password=password, db=db)
        self.cursor = self.db.cursor()

    def write_dict(self, dict, table_name):
        '''
        write the data of a python diction to the table named table_name of the setting mysql database
        :param dict: input dict
               table_name: a str
        :return: None
        '''
        self.cursor.execute("create table if not exists %s"
                            "(id VARCHAR(10) Primary key, json LONGBLOB)" % table_name)
        count = 0
        for id in dict.keys():
            json_dumps = json.dumps(dict[id])
            try:
                self.cursor.execute("insert into %s (id, json) values ('%s', '%s') "
                            % (table_name, id, json_dumps))
            except:
                continue
            count += 1
        self.db.commit()
        print("Insert %d items successfully" % count)

    def read_dict(self, table_name):
        '''
        read a dict from the table named table_name of the setting database
        :param table_name: a str
        :return: a python dictionary. If table_name not found, return {}
        '''
        try:
            self.cursor.execute("select * from %s" % table_name)
        except:
            print("Table %s is not found" % table_name)
            return {}
        data = self.cursor.fetchall()
        if data == None:
            return {}
        result = {}
        for pair in data:
            key = pair[0]
            value = json.loads(pair[1])
            result[key] = value
        return result

    def update_dict(self, dict, table_name):
        '''
        update the table named table_name of the setting mysql database
        :param dict: input dictionary
        :param table_name: a str
        :return: None
        '''
        try:
            self.cursor.execute("drop table %s" % table_name)
        except:
            print("Table %s is not found" % table_name)
            return
        self.write_dict(dict, table_name)

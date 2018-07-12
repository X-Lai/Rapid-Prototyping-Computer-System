from helper import *
from database import *
import time

if __name__ == '__main__':
    host = 'localhost'
    user = 'testuser'
    password = '000000'
    db = 'testdb'
    dbmanager = DBmanager(host, user, password, db)

    stu_to_stas, sta_to_stus = indivisual_station_usage('day1.csv')
    stu_to_top3stas = find_top3_stations(stu_to_stas)

    dbmanager.write_dict(dict=stu_to_stas, table_name='stu_to_stas')
    dbmanager.write_dict(dict=sta_to_stus, table_name='sta_to_stus')
    dbmanager.write_dict(dict=stu_to_top3stas, table_name='sta_to_top3stas')
    day_count = 1
    while True:
        stu_to_stas, sta_to_stus = indivisual_station_usage('day'+str(day_count)+'.csv')
        stu_to_top3stas = find_top3_stations(stu_to_stas)
        dbmanager.update_dict(dict=stu_to_stas, table_name='stu_to_stas')
        dbmanager.update_dict(dict=sta_to_stus, table_name='sta_to_stus')
        dbmanager.update_dict(dict=stu_to_top3stas, table_name='sta_to_top3stas')
        time.sleep(24*60*60)
        day_count += 1


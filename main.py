from helper import *
from database import *
import time

if __name__ == '__main__':

    # initially set the database
    host = 'localhost'
    user = 'testuser'
    password = '000000'
    db = 'testdb'
    dbmanager = DBmanager(host, user, password, db)

    # compute some useful information
    stu_to_stas, sta_to_stus = indivisual_station_usage('day1.csv')
    stu_to_totaltime = total_station_time(stu_to_stas)
    stu_to_top3stas = find_top3_stations(stu_to_stas)
    social_network = build_social_network("social_network.csv")

    # write to database for the first time
    dbmanager.write_dict(dict=stu_to_stas, table_name='stu_to_stas')
    dbmanager.write_dict(dict=sta_to_stus, table_name='sta_to_stus')
    dbmanager.write_dict(dict=stu_to_totaltime, table_name='stu_to_totaltime')
    dbmanager.write_dict(dict=stu_to_top3stas, table_name='stu_to_top3stas')
    dbmanager.write_dict(dict=social_network, table_name='social_network')
    day_count = 1

    while True:

        # update the database every day
        time.sleep(24*60*60)
        day_count += 1

        # compute some useful information
        stu_to_stas, sta_to_stus = indivisual_station_usage('day'+str(day_count)+'.csv')
        stu_to_top3stas = find_top3_stations(stu_to_stas)

        # update the database
        dbmanager.update_dict(dict=stu_to_stas, table_name='stu_to_stas')
        dbmanager.update_dict(dict=sta_to_stus, table_name='sta_to_stus')
        dbmanager.update_dict(dict=stu_to_totaltime, table_name='stu_to_totaltime')
        dbmanager.update_dict(dict=stu_to_top3stas, table_name='stu_to_top3stas')
        dbmanager.update_dict(dict=social_network, table_name='social_network')


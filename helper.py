import numpy as np
import datetime
import csv
def indivisual_station_usage(filepath):
    '''

    :param filepath: file path of the csv file
    :return: dict1: stations usage per student; dict2: usage per station.
    '''
    with open(filepath) as file:
        reader = csv.reader(file)
        dict1 = {}
        dict2 = {}
        for item in list(reader):
            student_id, station_id, check_in, check_out = item
            time_format = "%Y-%m-%d %H:%M:%S"
            check_in_time = datetime.datetime.strptime(check_in, time_format)
            check_out_time = datetime.datetime.strptime(check_out, time_format)
            time_stamp = (check_out_time-check_in_time).seconds / 60
            if student_id not in dict1.keys():
                dict1[student_id] = {}
            dict1[student_id][station_id] = time_stamp
            if station_id not in dict2.keys():
                dict2[station_id] = {}
            dict2[station_id][student_id] = time_stamp
    return dict1, dict2

def total_station_time(stu_to_sta):
    '''
    :param filepath: file path of the csv file
    :return dict: total usage of all stations each student.
    '''
    dict = {}
    for stu_id in stu_to_sta:
        total_time = 0
        for station_id in stu_to_sta[stu_id]:
            total_time += stu_to_sta[stu_id][station_id]
        dict[stu_id] = total_time
    return dict

def find_top3_stations(stu_to_sta):
    '''

    :param stu_to_sta: a dictionay that maps every student to another dictionary which maps
                every station to the time stamp spent in the corresponding station.
    :return:stu_to_top3sta: a dictionary that maps every student to a list which sort in order the
                top 3 stations the corresponding student has been to.
                For example: stu_to_top3sta = {'1001': [sta1,sta2,sta3]}, where student 1001 spend
                the most time in sta1 and second most in sta2, and then third most in sta3.
    '''
    stu_to_top3sta = {}
    for stu in stu_to_sta.keys():
        sta_to_timestamp = stu_to_sta[stu]
        stations = list(sta_to_timestamp.keys())
        stu_to_top3sta[stu] = sorted(stations, key=lambda x:sta_to_timestamp[x], reverse=True)[:3]
    return stu_to_top3sta

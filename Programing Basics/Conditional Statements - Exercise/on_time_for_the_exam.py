exam_hour = int(input())
exam_minute = int(input())
arival_hour = int(input())
arival_minute = int(input())

exam_time_min = (exam_hour * 60) + exam_minute
arival_time_min = (arival_hour * 60) + arival_minute
diff = (abs(exam_time_min - arival_time_min))
hour = diff // 60
minutes = diff % 60

if exam_time_min < arival_time_min and diff < 60:
    print(f"Late {diff} minutes after the start")
elif exam_time_min < arival_time_min and diff >= 60:
    print(f"Late {hour}:{minutes:02d} hours after the start")
elif exam_time_min > arival_time_min and diff <= 30:
    if diff >= 30 and diff != 0 or diff < 30:
        print(f"On time {diff} minutes before the start")
    elif diff > 60:
        print(f"On time {hour}:{minutes:02d} hours before the start")
elif diff == 0:
    print("On time")
elif exam_time_min > arival_time_min and diff < 60:
    print(f"Early {minutes:02d} minutes before the start")
else:
    print(f"Early {hour}:{minutes:02d} hours before the start")

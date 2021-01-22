# import time
#
# time_sec = int(input('Please input time in seconds'))
# print(time.strftime("%H:%M:%S", time.gmtime(time_sec)))

time = int(input("Введите время в секундах "))
hh = time // 3600
mm = (time - hh * 3600) // 60
ss = time - (hh * 3600 + mm * 60)
print(f"{hh:0>2d}:{mm:0>2d}:{ss:0>2d}")

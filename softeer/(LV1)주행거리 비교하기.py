# split(:) 을 활용하여 시간과 분을 분리
# 총 시간을 더해서 분으로 환산 후 분과 합


total_hour = 0
total_minute = 0
for _ in range(5):
    startT, endT = input().split()
    startT_hour, startT_minute = startT.split(':')
    endT_hour, endT_minute = endT.split(':')

    total_hour += int(endT_hour)-int(startT_hour)
    total_minute += int(endT_minute)-int(startT_minute)
    
total_minute += total_hour*60

print(total_minute)
#speed of 80/ speed limit of 60 / distance of 100


speed = float(input('Enter your average speed traveled '))
distance = float( input('Enter the distance traveled in miles '))
speedlimit = float( input("Enter the speed limit in miles/hour "))

time= distance / speedlimit

speedtime = distance / speed

print(time, speedtime)

Minutes_in_hours= 60

speedtimemin = speedtime*Minutes_in_hours
timemin = time*Minutes_in_hours

if speed> speedlimit:
        savedtime = timemin - speedtimemin
else:
    print('no time saved')

print(f'time taken at speed limit {timemin:.2f} minutes')
print(f'time taken at your speed {speedtimemin:.2f} minutes')
print(f'time saved in min {savedtime:.2f} minutes')

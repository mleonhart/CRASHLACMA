#This script takes driveSource.html and inserts start and stop points to render a driving map at DriveMap.html

origin = '5905 Wilshire Blvd, Los Angeles, CA 90036'
destination = '3355 Wilshire Blvd Los Angeles, CA 90010'

directionString = 'origin: ' + "'" + origin + "'" + ',\n destination: ' + "'" + destination + "'" + ','

f1 = open('driveSource.html', 'rU')
f2 = open('DriveMap.html', 'wb')
for line in f1:
    f2.write(line.replace('startStop', directionString))
f1.close()
f2.close()

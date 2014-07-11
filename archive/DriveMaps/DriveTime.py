from googlemaps import GoogleMaps

## Don't forget to 'sudo easy_install googlemaps'

APIKey = 'AIzaSyAu6zXCa_r-_exJbw2bZ6cAkaQcEUP_HYE'
gmaps = GoogleMaps(APIKey)
address = '5905 Wilshire Blvd, Los Angeles, CA 90036'
destination = '10526 Venice Blvd, Culver City, CA 90232'

directions = gmaps.directions(address, destination)
DriveTime = int(directions['Directions']['Duration']['seconds']/60)

print 'To drive from LACMA to ', destination, ' will take ', DriveTime, ' minutes'

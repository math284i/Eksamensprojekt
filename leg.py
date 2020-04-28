import android

droid = android.Android()

droid.startLocating()

print("Reading GPS...")

event = droid.eventWaitFor("location", 10000).result
if event['name'] == "location":
    try:
        lat = str(event['data']['gps']['latitude'])
        lng = str(event['data']['gps']['longitude'])
    except KeyError:
        lat = str(event['data']['network']['latitude'])
        lng = str(event['data']['network']['longitude'])
    latlng = 'lat: ' + lat + ' lng: ' + lng

    print(latlng)

droid.stopLocating()
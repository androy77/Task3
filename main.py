import tweepy
import folium
import ssl
from geopy.geocoders import Nominatim

ssl._create_default_https_context = ssl._create_unverified_context


def get_user(username):
    """
    This function return object "myself", which contains all information about user
    """
    auth = tweepy.OAuthHandler('gCO32O2Ds5lUEnBHOtnTKnROh', 'Arzxlg4KloGcwoWTO207sLmMRHlKFsOEkfDRmuc1i2uzUHOsaI')
    auth.set_access_token('1230067977699184641-AOJrUI8jLCclVzdZWr3JJnW4HBZP6G',
                          'e4AKZAxEFzEPTRWGA9aPgBrRBeyeeRrXggJo4qHCoDC5U')

    api = tweepy.API(auth, wait_on_rate_limit=True)
    myself = api.get_user(username)
    return myself


def friend_location(myself):
    """
    This function return dict of locations of friends.
    """
    myself = get_user(myself)
    geolocator = Nominatim(user_agent="specify_your_app_name_here")
    locations = {}
    for person in myself.friends(count='friends_count'):
        try:
            location = geolocator.geocode(person.location)
            # print(loc)
            coords = (location.latitude, location.longitude)
            # print(loc2)
            locations[coords] = locations.get(coords, '') + ' \n ' + person.name
        except:
            pass

    return map_create(locations)


def map_create(locations):
    """
    This function creates map with markers of locations via folium
    """
    layer = folium.FeatureGroup(name="Following")
    start = []
    for place in locations:
        layer.add_child(folium.Marker(location=[place[0], place[1]],
                                      popup=locations[place],
                                      icon=folium.Icon(color='red'
                                                       )))
        start = place
    print(start)
    m = folium.Map(location=[start[0], start[1]], tiles='Stamen Toner', zoom_start=10)
    m.add_child(layer)
    return m._repr_html_()


# map_create(friend_location(get_user('ianinasokolova')))

# if __name__ == "__main__":
#     # print(get_user('androy777'))
#     username = input()
#     print(user_location(get_user(username)))
#     print(friend_location(get_user(username)))

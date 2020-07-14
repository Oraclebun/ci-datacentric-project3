import pymodm
from models import Hiker, Trails, Location, Province, Town, Comment
import datetime


# Start the comments.
# We need to save these objects before referencing them later.
henry_hiker = Hiker('Henry','Hiker', "hhiker1", 'France','henry@hiker.com',10, "https://res.cloudinary.com/c7oud0311/image/upload/v1594609854/project3/profile1_tbjthv.jpg").save()
joe_jogger = Hiker('Joe', 'Jogger', "jjogger1", 'UK', 'joe@jogger.com', 12, "https://res.cloudinary.com/c7oud0311/image/upload/v1594654152/project3/profile2_vcog5c.jpg").save()

location_ids = Location.objects.bulk_create([
    Location('Ireland', province = [Province(state='Leinster', town = Town(town='Wicklow'))]),  #0
    Location('Ireland', province = [Province(state='Munster', town = Town(town='Cork'))]),
    Location('Ireland', province = [Province(state='Munster', town = Town(town='Killarney'))]),
    Location('Ireland', province = [Province(state='Munster', town = Town(town='Limerick'))]),
    Location('Ireland', province = [Province(state='Munster', town = Town(town='Waterford'))]),
    Location('Japan', province = [Province(state='Kansai', town = Town(town='Osaka'))])
       
])

trail1 = Trails(
    trail_name = "The Great Sugar Loaf Trail",
    distance= 2.7,
    elevation= 192,
    route_type= 'Out and Back',
    difficulty= 'Moderate',
    description = 'Lightly trafficked trail located near Wicklow, County Wicklow, Ireland. The trail is primarily used for hiking, walking, and nature trips.',
    centrepoint = {'type': 'Point', 'coordinates': [-6.151483,53.151632]},
    waypoints= {'type': 'LineString', 'coordinates': [[-6.15454,53.14446],[-6.151379,53.151431],[-6.154846,53.158786],[-6.148495,53.163254],[-6.139857,53.157922],[-6.151379,53.151431],[-6.15454,53.14446]]},
    embed_route = '<iframe src="https://www.google.com/maps/embed?pb=!1m26!1m12!1m3!1d15348.448577037858!2d-6.158307142221048!3d53.14965633010118!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m11!3e2!4m3!3m2!1d53.1442182!2d-6.1550139999999995!4m5!1s0x48678fbe8560e371%3A0x94d69fa55d377828!2sSugarloaf%20Hill!3m2!1d53.1591704!2d-6.147398!5e0!3m2!1sen!2ssg!4v1594021731588!5m2!1sen!2ssg" width="400" height="400" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>',
    location= location_ids[0],
    comments= [Comment(author=henry_hiker, date_comment= datetime.datetime.now(), body="Sweet short trail. A bit of a climb", sightings = ['dogs', 'city view', 'rocky', 'scramble'], date_started= datetime.date(2015,7,4), ratings=5, hours_taken = 1, minutes_taken = 15)]
).save()

trail_ids = Trails.objects.bulk_create([
    Trails(
    trail_name = "Powerscourt Waterfall Trail",
    distance= 4.7,
    elevation= 304,
    route_type= 'Point to Point',
    difficulty= 'Moderate',
    description = 'Powerscourt Waterfall, is a 121-metre high waterfall, on the River Dargle near Enniskerry in County Wicklow, Ireland. The waterfall flows continuously all year, falling in a horsetail-fan, and ranks as the highest waterfall in Ireland.',
    centrepoint = {'type': 'Point', 'coordinates': [-6.195256,53.169164]},
    waypoints= {'type': 'LineString', 'coordinates': [[-6.1886633,53.184199],[-6.187616,53.179419],[-6.199492,53.170422],[-6.195413,53.156953],[-6.210428, 53.147733]]},
    embed_route = '<iframe src="https://www.google.com/maps/embed?pb=!1m28!1m12!1m3!1d28807.579764561477!2d-6.2191064671149165!3d53.16373470966585!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e2!4m5!1s0x4867a6fd021be2a7%3A0x3dbbbe4c7f7d85bc!2sPowerscourt%20House%20%26%20Gardens%2C%20Powerscourt%20Demesne%2C%20Enniskerry%2C%20County%20Wicklow%2C%20Ireland!3m2!1d53.184250999999996!2d-6.1866327!4m5!1s0x4867a6a894511803%3A0x2e0fdd07918cfadc!2sPowerscourt%20Waterfall%2C%20Powerscourt%20Estate%2C%20Enniskerry%2C%20Co.%20Wicklow%2C%20A98%20WOD0%2C%20Ireland!3m2!1d53.1460771!2d-6.2112376!5e0!3m2!1sen!2ssg!4v1594021910339!5m2!1sen!2ssg" width="400" height="400" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>',
    location= location_ids[0],
    comments= [Comment(author=joe_jogger, date_comment= datetime.datetime.now(), body="Easy and fun trail. Great hike to the waterfall", sightings = ['waterfall', 'wild flowers', 'forest'], date_started= datetime.date(2014,6,23), ratings=5, hours_taken = 1, minutes_taken = 29)]
),
    Trails(
    trail_name = "Wicklow Train Station to Black Castle Trail",
    distance= 1.9,
    elevation= 0,
    route_type= 'Point to Point',
    difficulty= 'Easy',
    description = 'Short walk that starts from Wicklow Train Station, parallel to River Vartry. This walk ends at Black Castle, a castle ruin that stands on a rocky promontory over the sea.',
    centrepoint = {'type': 'Point', 'coordinates': [-6.046169, 52.984252]},
    waypoints= {'type': 'LineString', 'coordinates': [[-6.052832, 52.988141],[-6.045375, 52.982873],[-6.030821, 52.981144]]},
    embed_route = '<iframe src="https://www.google.com/maps/embed?pb=!1m28!1m12!1m3!1d4941.353019295187!2d-6.04537669635306!3d52.98378576642433!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e2!4m5!1s0x4867b0b773c1c8d1%3A0x6989f10238f885bd!2sWicklow%20Train%20Station%2C%20Wicklow%2C%20Corporation%20Murragh%2C%20Wicklow%2C%20Ireland!3m2!1d52.988146!2d-6.052967199999999!4m5!1s0x4867b0d2ee14706d%3A0xad63b5e2279e75a0!2sBlack%20Castle!3m2!1d52.9811225!2d-6.030844999999999!5e0!3m2!1sen!2ssg!4v1594095314897!5m2!1sen!2ssg" width="400" height="400" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>',
    location= location_ids[0],
    comments= [Comment(author=henry_hiker, date_comment= datetime.datetime.now(), body="Short and relaxing walk from the train station to Black Castle. There's a beautiful sea view at the end.", sightings = ['sea', 'cars', 'coastline'], date_started= datetime.date(2016,3,5), ratings=3, hours_taken = 0, minutes_taken = 50)]
),
    Trails(
    trail_name = "Mullaghcleevaun Trail",
    distance= 12.7,
    elevation= 849,
    route_type= 'Point to Point',
    difficulty= 'Difficult',
    description = 'Mullaghcleevaun is the 2nd highest peak in the Wicklow Mountains, and is situated in the central sector of the whole range. A common route to the summit of Mullaghcleevaun is from the south via an 8.5-kilometre 3-4 hour walk which starts from a small car-park in the forest below Carraigshouk 572 metres (1,877 ft) (the car-park is known locally as "The Oasis") just off the R115 road (also called the Old Military Road).[12] This southerly route ascends to Mullaghcleevaun East Top and then to the summit of Mullaghcleevaun, before retracing to the car-park.',
    centrepoint = {'type': 'Point', 'coordinates': [-6.430467,53.150183]},
    waypoints= {'type': 'LineString', 'coordinates': [[-6.466014, 53.198406],[-6.404544, 53.147942],[-6.406239, 53.102660]]},
    embed_route = '<iframe src="https://www.google.com/maps/embed?pb=!1m28!1m12!1m3!1d83188.00496971133!2d-6.490219343046424!3d53.15361009868608!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e2!4m5!1s0x48679de687206d87%3A0xa00c7a997321320!2sManor%20Kilbride!3m2!1d53.198589999999996!2d-6.46694!4m5!1s0x4867996d339c8729%3A0xdd6c7df09f9f5178!2sMullaghcleevaun%2C%20Ballynultagh%2C%20Co.%20Wicklow%2C%20Ireland!3m2!1d53.103055499999996!2d-6.406666599999999!5e0!3m2!1sen!2ssg!4v1594055206176!5m2!1sen!2ssg" width="400" height="400" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>',
    location= location_ids[0],
    comments= [Comment(author=joe_jogger, date_comment= datetime.datetime.now(), body="Invigorating hike up the mountain. It's tough at some points.", sightings = ['mountain', 'wild flowers', 'birds'], date_started= datetime.date(2016,4,5), ratings=5, hours_taken = 6, minutes_taken = 9)]
),
    Trails(
    trail_name = "Torc Waterfall Trail",
    distance= 4.95,
    elevation= 50,
    route_type= 'Out and Back',
    difficulty= 'Moderate',
    description = 'Torc Waterfall is 4.3 miles (7 kilometres) from Killarney, and 1.6 miles (2.5 kilometres) from the gates of Muckross House, in the Killarney National Park. The cascade is one of the main points on the 200-kilometre (120-mile) Kerry Way walking tour.',
    centrepoint = {'type': 'Point', 'coordinates': [-9.506368, 52.012555]},
    waypoints= {'type': 'LineString', 'coordinates': [[-9.502423,52.019564],[-9.506909,52.016831],[-9.508434,52.008956],[-9.507466,52.006069],[-9.5066471,52.005025]]},
    embed_route = '<iframe src="https://www.google.com/maps/embed?pb=!1m50!1m12!1m3!1d7709.946357182832!2d-9.512744034162264!3d52.01336807732087!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m35!3e2!4m3!3m2!1d52.0190771!2d-9.5019972!4m3!3m2!1d52.0188079!2d-9.5047812!4m3!3m2!1d52.016394299999995!2d-9.5066356!4m3!3m2!1d52.0144478!2d-9.5068536!4m3!3m2!1d52.0123472!2d-9.5082095!4m3!3m2!1d52.009563199999995!2d-9.5078018!4m3!3m2!1d52.008136699999994!2d-9.509513499999999!4m5!1s0x48453dd8e82e7d45%3A0x7c316a7b5eb7f96a!2sTorc%20Waterfall%2C%20Rossnahowgarry%2C%20Killarney%2C%20Co.%20Kerry%2C%20Ireland!3m2!1d52.0057453!2d-9.5068652!5e0!3m2!1sen!2ssg!4v1594022266615!5m2!1sen!2ssg" width="400" height="400" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>',
    location= location_ids[2],
    comments= [Comment(author=joe_jogger, date_comment= datetime.datetime.now(), body="Start early as it can get very crowded. Refreshing hike to the fall.", sightings = ['waterfall', 'wild flowers', 'birds', 'forest'], date_started= datetime.date(2015,4,17), ratings=5, hours_taken = 2, minutes_taken = 1)]
),
    Trails(
    trail_name = "Minoo Park Trail",
    distance= 5.6,
    elevation= 266,
    route_type= 'Out and Back',
    difficulty= 'Moderate',
    description = 'Minoo Park (also spelled Mino or Minoh) is a forested valley on the outskirts of Osaka. During the fall, it is one of the best places in the Kansai Region to see the autumn colors in a natural setting. The colors are usually best in the second half of November.',
    centrepoint = {'type': 'Point', 'coordinates': [135.470908, 34.943951]},
    waypoints= {'type': 'LineString', 'coordinates': [[135.468504,34.834440],[135.470908,34.943951],[135.471938,34.854375]]},
    embed_route = '<iframe src="https://www.google.com/maps/embed?pb=!1m28!1m12!1m3!1d24957.767235972166!2d135.45393280318623!3d34.84731054676561!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e2!4m5!1s0x6000fb09f872d2cb%3A0xd41d4f728ccdb1ae!2sJapan%2C%20%E3%80%92562-0001%20Osaka%2C%20Minoo%2C%207%2C%20Unnamed%20Road%20Ichino%20Bridge!3m2!1d34.8382083!2d135.469807!4m5!1s0x6000f98c6d0ac613%3A0x4cd7b8ae9c8328a0!2sMinoo%20Falls!3m2!1d34.8538281!2d135.4719911!5e0!3m2!1sen!2ssg!4v1594038944710!5m2!1sen!2ssg" width="400" height="400" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>',
    location= location_ids[5]
),
    Trails(
    trail_name = "Mount Ikoma Trail",
    distance= 22.8,
    elevation= 470,
    route_type= 'Out and Back',
    difficulty= 'Difficult',
    description = 'At present, Mt Ikoma attracts many people, offering panoramic views that extend as far as the Akashi Kaikyo Bridge and Kansai International Airport. Spectacular views are commanded from Skyland Ikoma, an amusement park situated on the top of the mountain.',
    centrepoint = {'type': 'Point', 'coordinates': [135.661355, 34.666958]},
    waypoints= {'type': 'LineString', 'coordinates': [[135.655389, 34.685458],[135.673053, 34.676862],[135.669831, 34.670840],[135.662991, 34.651603]]},
    embed_route = '<iframe src="https://www.google.com/maps/embed?pb=!1m32!1m12!1m3!1d21917.177426141392!2d135.6510362583446!3d34.669345083680355!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m17!3e2!4m5!1s0x600121a05f40b89f%3A0x6e5c569680411f18!2sIshikiri%20Station%2C%202%20Chome-1-6%20Kamiishikiricho%2C%20Higashiosaka%2C%20Osaka%20579-8012%2C%20Japan!3m2!1d34.6852754!2d135.6554756!4m5!1s0x600121611111fa1b%3A0xfe4051a1642be914!2zT3Nha2EgaHVtaWMgb2YgZm9yZXN0IE51a2F0YSBvcmNoYXJkc-KApiDlpKfpmKrlupzmsJEg44Gu5qOu44Gs44GL44GfIOWckuWcsOahiOWGheaJgA!3m2!1d34.676911499999996!2d135.6731118!4m3!3m2!1d34.6515572!2d135.6629275!5e0!3m2!1sen!2ssg!4v1594053950812!5m2!1sen!2ssg" width="400" height="400" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>',
    location= location_ids[5]
)
])
import pymodm
from models import Hiker, Trails, Location, Province, Town, Comment
import datetime

# Start the comments.
# We need to save these objects before referencing them later.
henry_hiker = Hiker('Henry', 'Hiker', "hhiker1", 'France', 'henry@hiker.com', 10,
                    "https://res.cloudinary.com/c7oud0311/image/upload/v1594609854/project3/profile1_tbjthv.jpg").save()
joe_jogger = Hiker('Joe', 'Jogger', "jjogger1", 'UK', 'joe@jogger.com', 12,
                   "https://res.cloudinary.com/c7oud0311/image/upload/v1594654152/project3/profile2_vcog5c.jpg").save()

location_ids = Location.objects.bulk_create([
    Location('Ireland', province=[Province(
        state='Leinster', town=Town(town='Carlow'))]),
    Location('Ireland', province=[Province(
        state='Leinster', town=Town(town='Dublin'))]),
    Location('Ireland', province=[Province(
        state='Leinster', town=Town(town='Kilkenny'))]),
    Location('Ireland', province=[Province(
        state='Leinster', town=Town(town='Wicklow'))]),
    Location('Ireland', province=[Province(
        state='Munster', town=Town(town='Cork'))]),
    Location('Ireland', province=[Province(
        state='Munster', town=Town(town='Killarney'))]),  # 5
    Location('Ireland', province=[Province(
        state='Munster', town=Town(town='Limerick'))]),
    Location('Ireland', province=[Province(
        state='Munster', town=Town(town='Waterford'))]),
    Location('Japan', province=[Province(
        state='Okinawa', town=Town(town='Kunigami'))]),
    Location('Japan', province=[Province(
        state='Kansai', town=Town(town='Kyoto'))]),
    Location('Japan', province=[Province(
        state='Kansai', town=Town(town='Osaka'))]),  # 10
    Location('Japan', province=[Province(
        state='Kanto', town=Town(town='Tokyo'))]),
    Location('Japan', province=[Province(
        state='Kanto', town=Town(town='Nikko'))]),
    Location('New Zealand', province=[Province(
        state='North Island', town=Town(town='Auckland'))]),
    Location('New Zealand', province=[Province(
        state='North Island', town=Town(town='Bay of Plenty'))]),
    Location('New Zealand', province=[Province(
        state='North Island', town=Town(town="Hawke's Bay"))]),  # 15
    Location('New Zealand', province=[Province(
        state='North Island', town=Town(town='Gisborne'))]),
    Location('New Zealand', province=[Province(
        state='North Island', town=Town(town='Taranaki'))]),
    Location('New Zealand', province=[Province(
        state='North Island', town=Town(town='Waikato'))]),
    Location('New Zealand', province=[Province(
        state='North Island', town=Town(town='Whanganui-Manawatu'))]),
    Location('New Zealand', province=[Province(
        state='North Island', town=Town(town='Wellington'))]),  # 20
    Location('New Zealand', province=[Province(
        state='South Island', town=Town(town='Canterbury'))]),
    Location('New Zealand', province=[Province(
        state='South Island', town=Town(town='Marlborough'))]),
    Location('New Zealand', province=[Province(
        state='South Island', town=Town(town='Nelson-Tasman'))]),
    Location('New Zealand', province=[Province(
        state='South Island', town=Town(town='Otago'))]),
    Location('New Zealand', province=[Province(
        state='South Island', town=Town(town='Southland'))]),  # 25
    Location('New Zealand', province=[Province(
        state='South Island', town=Town(town='West Coast'))]),
    Location('Singapore', province=[Province(
        state='Central', town=Town(town='Bukit Merah'))]),
    Location('Singapore', province=[Province(
        state='Central', town=Town(town='Kallang'))]),
    Location('Singapore', province=[Province(
        state='East', town=Town(town='Pasir Ris'))]),
    Location('Singapore', province=[Province(
        state='East', town=Town(town='Tampines'))]),  # 30
    Location('Singapore', province=[Province(
        state='North', town=Town(town='Woodlands'))]),
    Location('Singapore', province=[Province(
        state='North', town=Town(town='Yishun'))]),
    Location('Singapore', province=[Province(
        state='North East', town=Town(town='Punggol'))])  # 33
])

trail1 = Trails(
    trail_name="The Great Sugar Loaf Trail",
    distance=2.7,
    elevation=192,
    route_type='Out and Back',
    difficulty='Moderate',
    description='Lightly trafficked trail located near Wicklow, County Wicklow, Ireland. The trail is primarily used for hiking, walking, and nature trips.',
    centrepoint={'type': 'Point', 'coordinates': [-6.151483, 53.151632]},
    waypoints={'type': 'LineString', 'coordinates': [[-6.15454, 53.14446], [-6.151379, 53.151431], [-6.154846,
                                                                                                    53.158786], [-6.148495, 53.163254], [-6.139857, 53.157922], [-6.151379, 53.151431], [-6.15454, 53.14446]]},
    image="https://res.cloudinary.com/c7oud0311/image/upload/v1595132223/project3/loca1_vgo4hp.jpg",
    embed_route='<iframe src="https://www.google.com/maps/embed?pb=!1m22!1m8!1m3!1d19141.489183174475!2d-6.151162!3d53.15172700000001!3m2!1i1024!2i768!4f13.1!4m11!3e2!4m3!3m2!1d53.1441765!2d-6.1550702!4m5!1s0x48678fbe8560e371%3A0x94d69fa55d377828!2sSugarloaf%20Hill%2C%20Glencap%20Commons%20Upper%2C%20Co.%20Wicklow%2C%20Ireland!3m2!1d53.1591704!2d-6.147398!5e0!3m2!1sen!2ssg!4v1596021716272!5m2!1sen!2ssg" width="400" height="400" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>',
    location=location_ids[3],
    comments=[Comment(author=henry_hiker, date_comment=datetime.datetime.now(), body="Sweet short trail. A bit of a climb", sightings=[
                      'dogs', 'city view', 'rocky', 'scramble'], date_started=datetime.date(2015, 7, 4), ratings=5, hours_taken=1, minutes_taken=15)]
).save()

trail_ids = Trails.objects.bulk_create([
    Trails(
        trail_name="Powerscourt Waterfall Trail",
        distance=4.7,
        elevation=304,
        route_type='Point to Point',
        difficulty='Moderate',
        description='Powerscourt Waterfall, is a 121-metre high waterfall, on the River Dargle near Enniskerry in County Wicklow, Ireland. The waterfall flows continuously all year, falling in a horsetail-fan, and ranks as the highest waterfall in Ireland.',
        centrepoint={'type': 'Point', 'coordinates': [-6.195256, 53.169164]},
        waypoints={'type': 'LineString', 'coordinates': [
            [-6.1886633, 53.184199], [-6.187616, 53.179419], [-6.199492, 53.170422], [-6.195413, 53.156953], [-6.210428, 53.147733]]},
        image="https://res.cloudinary.com/c7oud0311/image/upload/v1595133223/project3/loca2_wrwxfe.jpg",
        embed_route='<iframe src="https://www.google.com/maps/embed?pb=!1m24!1m8!1m3!1d76538.48419439924!2d-6.189593!3d53.167132!3m2!1i1024!2i768!4f13.1!4m13!3e2!4m5!1s0x4867a6fd021be2a7%3A0x3dbbbe4c7f7d85bc!2sPowerscourt%20House%20%26%20Gardens%2C%20Powerscourt%20Demesne%2C%20Enniskerry%2C%20Co.%20Wicklow%2C%20Ireland!3m2!1d53.184250999999996!2d-6.1866327!4m5!1s0x4867a6a894511803%3A0x2e0fdd07918cfadc!2sPowerscourt%20Waterfall%2C%20Powerscourt%20Estate%2C%20Enniskerry%2C%20Co.%20Wicklow%2C%20A98%20WOD0%2C%20Ireland!3m2!1d53.1460771!2d-6.2112376!5e0!3m2!1sen!2ssg!4v1596022223940!5m2!1sen!2ssg" width="400" height="400" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>',
        location=location_ids[3],
        comments=[Comment(author=joe_jogger, date_comment=datetime.datetime.now(), body="Easy and fun trail. Great hike to the waterfall", sightings=[
                          'waterfall', 'wild flowers', 'forest'], date_started=datetime.date(2014, 6, 23), ratings=5, hours_taken=1, minutes_taken=29)]
    ),
    Trails(
        trail_name="Wicklow Train Station to Black Castle Trail",
        distance=1.9,
        elevation=0,
        route_type='Point to Point',
        difficulty='Easy',
        description='Short walk that starts from Wicklow Train Station, parallel to River Vartry. This walk ends at Black Castle, a castle ruin that stands on a rocky promontory over the sea.',
        centrepoint={'type': 'Point', 'coordinates': [-6.046169, 52.984252]},
        waypoints={'type': 'LineString', 'coordinates': [
            [-6.052832, 52.988141], [-6.045375, 52.982873], [-6.030821, 52.981144]]},
        image="https://res.cloudinary.com/c7oud0311/image/upload/v1595091811/project3/loca3_gabokq.jpg",
        embed_route='<iframe src="https://www.google.com/maps/embed?pb=!1m24!1m8!1m3!1d19216.117659681302!2d-6.041906!3d52.984137!3m2!1i1024!2i768!4f13.1!4m13!3e2!4m5!1s0x4867b0b773c1c8d1%3A0x6989f10238f885bd!2sWicklow%20Train%20Station%2C%20Wicklow%2C%20Corporation%20Murragh%2C%20Wicklow%2C%20Ireland!3m2!1d52.988146!2d-6.052967199999999!4m5!1s0x4867b0d2ee14706d%3A0xad63b5e2279e75a0!2sBlack%20Castle%2C%20S%20Quay%2C%20Corporation%20Lands%2C%20Co.%20Wicklow%2C%20Ireland!3m2!1d52.9811225!2d-6.030844999999999!5e0!3m2!1sen!2ssg!4v1596025026079!5m2!1sen!2ssg" width="400" height="400" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>',
        location=location_ids[3],
        comments=[Comment(author=henry_hiker, date_comment=datetime.datetime.now(), body="Short and relaxing walk from the train station to Black Castle. There's a beautiful sea view at the end.", sightings=[
                          'sea', 'cars', 'coastline'], date_started=datetime.date(2016, 3, 5), ratings=3, hours_taken=0, minutes_taken=50)]
    ),
    Trails(
        trail_name="Mullaghcleevaun Trail",
        distance=12.7,
        elevation=849,
        route_type='Point to Point',
        difficulty='Difficult',
        description='Mullaghcleevaun is the 2nd highest peak in the Wicklow Mountains, and is situated in the central sector of the whole range. A common route to the summit of Mullaghcleevaun is from the south via an 8.5-kilometre 3-4 hour walk which starts from a small car-park in the forest below Carraigshouk 572 metres (1,877 ft) (the car-park is known locally as "The Oasis") just off the R115 road (also called the Old Military Road).[12] This southerly route ascends to Mullaghcleevaun East Top and then to the summit of Mullaghcleevaun, before retracing to the car-park.',
        centrepoint={'type': 'Point', 'coordinates': [-6.430467, 53.150183]},
        waypoints={'type': 'LineString', 'coordinates': [
            [-6.466014, 53.198406], [-6.404544, 53.147942], [-6.406239, 53.102660]]},
        image="https://res.cloudinary.com/c7oud0311/image/upload/v1595132803/project3/loca4_tdcmt1.jpg",
        embed_route='<iframe src="https://www.google.com/maps/embed?pb=!1m24!1m8!1m3!1d153135.13742207357!2d-6.429815!3d53.150823!3m2!1i1024!2i768!4f13.1!4m13!3e2!4m5!1s0x48679e0a8adcc69f%3A0x139d75c0e86fb2f2!2sKilbride%2C%20Co.%20Wicklow%2C%20Ireland!3m2!1d53.1986734!2d-6.4669351!4m5!1s0x4867996d339c8729%3A0xdd6c7df09f9f5178!2sMullaghcleevaun%2C%20Ballynultagh%2C%20Co.%20Wicklow%2C%20Ireland!3m2!1d53.103055499999996!2d-6.406666599999999!5e0!3m2!1sen!2ssg!4v1596006671079!5m2!1sen!2ssg" width="355" height="355" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>',
        location=location_ids[3],
        comments=[Comment(author=joe_jogger, date_comment=datetime.datetime.now(), body="Invigorating hike up the mountain. It's tough at some points.", sightings=[
                          'mountain', 'wild flowers', 'birds'], date_started=datetime.date(2016, 4, 5), ratings=5, hours_taken=6, minutes_taken=9)]
    ),
    Trails(
        trail_name="Torc Waterfall Trail",
        distance=4.95,
        elevation=50,
        route_type='Out and Back',
        difficulty='Moderate',
        description='Torc Waterfall is 4.3 miles (7 kilometres) from Killarney, and 1.6 miles (2.5 kilometres) from the gates of Muckross House, in the Killarney National Park. The cascade is one of the main points on the 200-kilometre (120-mile) Kerry Way walking tour.',
        centrepoint={'type': 'Point', 'coordinates': [-9.506368, 52.012555]},
        waypoints={'type': 'LineString', 'coordinates': [
            [-9.502423, 52.019564], [-9.506909, 52.016831], [-9.508434, 52.008956], [-9.507466, 52.006069], [-9.5066471, 52.005025]]},
        image="https://res.cloudinary.com/c7oud0311/image/upload/v1595091822/project3/loca5_vxrlse.jpg",
        embed_route='<iframe src="https://www.google.com/maps/embed?pb=!1m38!1m12!1m3!1d8728.78362552171!2d-9.505255674582704!3d52.01059329988654!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m23!3e2!4m3!3m2!1d52.0183922!2d-9.503280499999999!4m3!3m2!1d52.016315299999995!2d-9.5066288!4m3!3m2!1d52.012243899999994!2d-9.5082192!4m3!3m2!1d52.0060412!2d-9.5067449!4m5!1s0x48453dd8e82e7d45%3A0x7c316a7b5eb7f96a!2sTorc%20Waterfall!3m2!1d52.0057453!2d-9.5068652!5e0!3m2!1sen!2ssg!4v1596007109370!5m2!1sen!2ssg" width="355" height="355" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>',
        location=location_ids[5],
        comments=[Comment(author=joe_jogger, date_comment=datetime.datetime.now(), body="Start early as it can get very crowded. Refreshing hike to the fall.", sightings=[
                          'waterfall', 'wild flowers', 'birds', 'forest'], date_started=datetime.date(2015, 4, 17), ratings=5, hours_taken=2, minutes_taken=1)]
    ),
    Trails(
        trail_name="City Centre to Shannon Fields Riverside Walk",
        distance=3.5,
        elevation=13,
        route_type='Point to Point',
        difficulty='Easy',
        description='This scenic 3.2km shared walking and cycling trail which runs through the historic Shannon Fields honours Limerick Olympian and World Cross Country Champion Michael O’Shea. Exercise stations are available along the route.',
        centrepoint={'type': 'Point', 'coordinates': [-8.606354, 52.673000]},
        waypoints={'type': 'LineString', 'coordinates': [
            [-8.618198, 52.666321], [-8.610047, 52.681250], [-9.508434, 52.008956]]},
        image="https://res.cloudinary.com/c7oud0311/image/upload/v1595131277/project3/loca6_ikoxjy.jpg",
        embed_route='<iframe src="https://www.google.com/maps/embed?pb=!1m28!1m8!1m3!1d11045.616102406488!2d-8.6158570843936!3d52.670736867467525!3m2!1i1024!2i768!4f13.1!4m17!3e2!4m5!1s0x485b5c698ef8a7e9%3A0x3bcc87157beb7364!2sLock%20Quay%2C%20Limerick%2C%20Ireland!3m2!1d52.6664106!2d-8.618156899999999!4m3!3m2!1d52.6712761!2d-8.5959839!4m5!1s0x485b5c3713e5c2d1%3A0x168588079edeff87!2sAthlunkard%20Bridge%2C%20Corbally%20Rd%2C%20Limerick%2C%20Ireland!3m2!1d52.6812068!2d-8.610025499999999!5e0!3m2!1sen!2ssg!4v1596006812596!5m2!1sen!2ssg" width="355" height="355" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>',
        location=location_ids[6]
    ),
    Trails(
        trail_name="Minoo Park Trail",
        distance=5.6,
        elevation=266,
        route_type='Out and Back',
        difficulty='Moderate',
        description='Minoo Park (also spelled Mino or Minoh) is a forested valley on the outskirts of Osaka. During the fall, it is one of the best places in the Kansai Region to see the autumn colors in a natural setting. The colors are usually best in the second half of November.',
        centrepoint={'type': 'Point', 'coordinates': [135.470908, 34.943951]},
        waypoints={'type': 'LineString', 'coordinates': [
            [135.468504, 34.834440], [135.470908, 34.943951], [135.471938, 34.854375]]},
        image="https://res.cloudinary.com/c7oud0311/image/upload/v1595134704/project3/loca7_vc9tew.jpg",
        embed_route='<iframe src="https://www.google.com/maps/embed?pb=!1m26!1m12!1m3!1d11889.99610572799!2d135.4660077573426!3d34.83905987419768!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m11!3e2!4m3!3m2!1d34.8350346!2d135.4687925!4m5!1s0x6000f98c6d0ac613%3A0x4cd7b8ae9c8328a0!2sMinoo%20Falls%2C%20%EF%BC%92-2%20Minookoen%2C%20Minoo%2C%20Osaka%20562-0002%2C%20Japan!3m2!1d34.8538281!2d135.4719911!5e0!3m2!1sen!2ssg!4v1596007234330!5m2!1sen!2ssg" width="355" height="355" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>',
        location=location_ids[10]
    ),
    Trails(
        trail_name="Mount Ikoma Trail",
        distance=22.8,
        elevation=470,
        route_type='Out and Back',
        difficulty='Difficult',
        description='At present, Mt Ikoma attracts many people, offering panoramic views that extend as far as the Akashi Kaikyo Bridge and Kansai International Airport. Spectacular views are commanded from Skyland Ikoma, an amusement park situated on the top of the mountain.',
        centrepoint={'type': 'Point', 'coordinates': [135.661355, 34.666958]},
        waypoints={'type': 'LineString', 'coordinates': [[135.655389, 34.685458], [
            135.673053, 34.676862], [135.669831, 34.670840], [135.662991, 34.651603]]},
        image="https://res.cloudinary.com/c7oud0311/image/upload/v1595134703/project3/loca8_twurov.jpg",
        embed_route='<iframe src="https://www.google.com/maps/embed?pb=!1m30!1m8!1m3!1d25190.62721113016!2d135.66203201809793!3d34.66998547494666!3m2!1i1024!2i768!4f13.1!4m19!3e2!4m5!1s0x600121a05f40b89f%3A0x6e5c569680411f18!2sIshikiri%20Station%2C%202%20Chome-1-6%20Kamiishikiricho%2C%20Higashiosaka%2C%20Osaka%20579-8012%2C%20Japan!3m2!1d34.6852754!2d135.6554756!4m5!1s0x600121611111fa1b%3A0xfe4051a1642be914!2sOsaka%20humic%20of%20forest%20Nukata%20orchards%20Information%20Center%2C%202030-6%20Yamatecho%2C%20Higashiosaka%2C%20Osaka%20579-8022%2C%20Japan!3m2!1d34.676911499999996!2d135.6731118!4m5!1s0x600126b34c7e3e09%3A0xb7474fcfd0d60ad0!2s1-ch%C5%8Dme-1668%20Rokumanjich%C5%8D%2C%20Higashiosaka%2C%20Osaka%20579-8061%2C%20Japan!3m2!1d34.6514028!2d135.6630037!5e0!3m2!1sen!2ssg!4v1596007351059!5m2!1sen!2ssg" width="355" height="600" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>',
        location=location_ids[10]
    ),
    Trails(
        trail_name="Shijonowate Suihen-Shizen-en Trail",
        distance=3.6,
        elevation=303,
        route_type='Point to Point',
        difficulty='Moderate',
        description='About 20 minutes from Osaka city, Shijonawate City is rich in nature. It is hard to believe that it is a suburb of Osaka city. However, stepping in nature can be tricky. There are pit vipers, beehives, and poisonous mushrooms, so be careful not to touch them and enjoy your walk!',
        centrepoint={'type': 'Point', 'coordinates': [135.652759, 34.730226]},
        waypoints={'type': 'LineString', 'coordinates': [[135.639560, 34.730457], [
            135.646922, 34.734703], [135.656984, 34.730551], [135.666802, 34.728892]]},
        image="https://res.cloudinary.com/c7oud0311/image/upload/v1595134153/project3/loca9_r96hwi.jpg",
        embed_route='<iframe src="https://www.google.com/maps/embed?pb=!1m24!1m8!1m3!1d26231.728758385954!2d135.653458!3d34.731249!3m2!1i1024!2i768!4f13.1!4m13!3e2!4m5!1s0x60011f0aba313259%3A0xc22e6f7b84ef1c28!2zU2hpam9uYXdhdGUgU3RhdGlvbiwgSmFwYW4sIOOAkjU3NC0wMDAxIE9zYWthLCBEYWl0bywgR2FrdWVuY2hvLCAx4oiSNTAg55Wq5Y-3!3m2!1d34.730503!2d135.6392988!4m5!1s0x60011f59fcca2827%3A0xde159d307f85d43c!2z5qOu44Gu5bel5L2c6aSoLCBKYXBhbiwg44CSNTc1LTAwMTEgT3Nha2EsIFNoaWpvbmF3YXRlLCBPc2FrYSwgNDYx!3m2!1d34.7282996!2d135.6667962!5e0!3m2!1sen!2ssg!4v1596007413392!5m2!1sen!2ssg" width="355" height="355" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>',
        location=location_ids[10]
    ),
    Trails(
        trail_name="Nikko Station to Kanmangafuchi Abyss",
        distance=4.1,
        elevation=650,
        route_type='Point to Point',
        difficulty='Easy',
        description='Kanmangafuchi Abyss, a gorge near central Nikko is a quiet and peaceful walking trail. Halfway through, you will see 70 Jizo statues that lined a part of the trail. The statues are also known as "Bake Jizo" (Ghost Jizo).Besides the trail is the beautiful gorge that was formed by the eruption from the nearby Mount Nantai. The view along the short walking trail is simply amazing.',
        centrepoint={'type': 'Point', 'coordinates': [139.604551, 36.752140]},
        waypoints={'type': 'LineString', 'coordinates': [[139.621977, 36.747450], [139.612354, 36.751948], [
            139.604101, 36.753609], [139.594343, 36.750556], [139.581471, 36.747618]]},
        image="https://res.cloudinary.com/c7oud0311/image/upload/v1595133594/project3/loca10_udgre5.jpg",
        embed_route='<iframe src="https://www.google.com/maps/embed?pb=!1m28!1m12!1m3!1d12787.399353789715!2d139.59687008365776!3d36.75017527241373!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e2!4m5!1s0x601fa0c503bb802d%3A0xc6c6dc50d453cfa9!2sNikk%C5%8D%20Station%2C%20Aioich%C5%8D%2C%20Nikko%2C%20Tochigi%20321-1413%2C%20Japan!3m2!1d36.747448!2d139.62204!4m5!1s0x601fa7574334f215%3A0x861356332fc03131!2sKanmangafuchi%20Abyss%2C%20Nikko%2C%20Tochigi%2C%20Japan!3m2!1d36.748956299999996!2d139.5892097!5e0!3m2!1sen!2ssg!4v1596007514652!5m2!1sen!2ssg" width="355" height="355" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>',
        location=location_ids[12]
    ),
    Trails(
        trail_name="Hiji Falls Trail",
        distance=2.9,
        elevation=139,
        route_type='Out and Back',
        difficulty='Moderate',
        description='Hiji Falls is located in Kunigami Village in northern Okinawa. Admission is 300 yen for children 15 and under and 500 yen for adults and older children. The nature trail is open for hikers 09:00 through 18:00 daily (17:30 November to March) with last entry at 16:00 (15:00 November to March).',
        centrepoint={'type': 'Point', 'coordinates': [128.181536, 26.714190]},
        waypoints={'type': 'LineString', 'coordinates': [[128.177421, 26.720088], [
            128.182525, 26.717853], [128.183317, 26.714794], [128.186713, 26.710001]]},
        image="https://res.cloudinary.com/c7oud0311/image/upload/v1595135183/project3/loca11_u0owwk.jpg",
        embed_route='<iframe src="https://www.google.com/maps/embed?pb=!1m28!1m12!1m3!1d7127.885106356178!2d128.17838687499724!3d26.714282166508504!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e2!4m5!1s0x34e44364a9d6dbeb%3A0x2b3f45b1e94aaa3e!2sHiji%20Falls%20National%20Park!3m2!1d26.7191808!2d128.179033!4m5!1s0x34e44481b80a403b%3A0x7149b317e35049cd!2sHijio%20Falls%2C%20Hama%2C%20Kunigami%2C%20Kunigami%20District%2C%20Okinawa%20905-1415%2C%20Japan!3m2!1d26.7105291!2d128.18661079999998!5e0!3m2!1sen!2ssg!4v1596007598490!5m2!1sen!2ssg" width="355" height="355" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>',
        location=location_ids[8]
    ),
    Trails(
        trail_name="Hooker Valley Track",
        distance=10,
        elevation=199,
        route_type='Out and Back',
        difficulty='Easy',
        description='The track leads up the Hooker Valley and along the Hooker River, ending at the glacier lake, where there are amazing views of Aoraki/Mount Cook on a clear day. Along the way you will cross three swingbridges and encounter icebergs.',
        centrepoint={'type': 'Point', 'coordinates': [170.098615, -43.703879]},
        waypoints={'type': 'LineString', 'coordinates': [[170.093309, -43.718564], [
            170.100145, -43.705616], [170.098250, -43.692727], [170.103642, -43.689006]]},
        image="https://res.cloudinary.com/c7oud0311/image/upload/v1595135564/project3/loca12_virfkn.jpg",
        embed_route='<iframe src="https://www.google.com/maps/embed?pb=!1m22!1m8!1m3!1d35470.463113513826!2d170.09839486692846!3d-43.71216169989442!3m2!1i1024!2i768!4f13.1!4m11!3e2!4m3!3m2!1d-43.689054299999995!2d170.10351559999998!4m5!1s0x6d2a4b341d69d4dd%3A0x63bc845abb08c829!2sHooker%20Valley%20track%2C%20Hooker%20Valley%20Track%2C%20Mt%20Cook%20National%20Park%207999%2C%20New%20Zealand!3m2!1d-43.718125699999995!2d170.0939684!5e0!3m2!1sen!2ssg!4v1596007671559!5m2!1sen!2ssg" width="355" height="355" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>',
        location=location_ids[26]
    ),
    Trails(
        trail_name="Kea Point from Mount Cook Village Track",
        distance=6,
        elevation=898,
        route_type='Out and Back',
        difficulty='Difficult',
        description='This walk winds its way through subalpine grasslands and scrub to the Mueller Glacier moraine wall. The walk ends at a viewing deck that gives stunning views of Mount Sefton, The Footstool, Hooker valley, Mueller Glacier lake and Aoraki/Mount Cook. There is a height gain of 180 m over 3 km.',
        centrepoint={'type': 'Point', 'coordinates': [170.086477, -43.722655]},
        waypoints={'type': 'LineString', 'coordinates': [
            [170.095664, -43.732055], [170.093873, -43.731980], [170.084021, -43.710040]]},
        image="https://res.cloudinary.com/c7oud0311/image/upload/v1595091813/project3/loca13_et8ceq.jpg",
        embed_route='<iframe src="https://www.google.com/maps/embed?pb=!1m24!1m8!1m3!1d46134.4013006819!2d170.093461!3d-43.723015!3m2!1i1024!2i768!4f13.1!4m13!3e2!4m5!1s0x6d2a4b532353e20f%3A0xbfce9e4c2c808051!2sBowen%20Drive%2C%20Canterbury%207999%2C%20New%20Zealand!3m2!1d-43.7345137!2d170.0961125!4m5!1s0x6d2a4b2457f0e759%3A0xe26f562fbb0049ce!2sKea%20Point%2C%20Mount%20Cook%20National%20Park%207999%2C%20New%20Zealand!3m2!1d-43.7101993!2d170.0835514!5e0!3m2!1sen!2ssg!4v1596007721256!5m2!1sen!2ssg" width="355" height="355" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>',
        location=location_ids[26]
    ),
    Trails(
        trail_name="Ōrākei Basin Walk",
        distance=4,
        elevation=24,
        route_type='Loop',
        difficulty='Easy',
        description='This walk takes you around the edge of the basin using the boardwalk and the bridge across the Purewa arm of the basin. It offers the chance to see local plant life, as well as views across the city.',
        centrepoint={'type': 'Point', 'coordinates': [174.813457, -36.866901]},
        waypoints={'type': 'LineString', 'coordinates': [[174.810048, -36.863432], [174.816867, -36.868651], [
            174.817707, -36.869028], [174.818927, -36.866059], [174.810048, -36.863432]]},
        image="https://res.cloudinary.com/c7oud0311/image/upload/v1595141322/project3/loca14_anablh.jpg",
        embed_route='<iframe src="https://www.google.com/maps/embed?pb=!1m30!1m12!1m3!1d4707.035330878474!2d174.81281921656915!3d-36.86833888864656!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m15!3e2!4m5!1s0x6d0d483602249f5d%3A0xab4e5744c97d6f24!2sOrakei!3m2!1d-36.862429899999995!2d174.8095081!4m3!3m2!1d-36.870849899999996!2d174.81794689999998!4m3!3m2!1d-36.866399799999996!2d174.8197538!5e0!3m2!1sen!2ssg!4v1596008059041!5m2!1sen!2ssg" width="355" height="355" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>',
        location=location_ids[13]
    ),
    Trails(
        trail_name="One Tree Hill Walk",
        distance=4,
        elevation=178,
        route_type='Loop',
        difficulty='Easy',
        description="Maungakiekie / One Tree Hill is a 182-metre (597 ft) volcanic peak in Auckland, New Zealand. It is an important memorial place for both Māori and other New Zealanders. The suburb around the base of the hill is also called One Tree Hill. It is surrounded by the suburbs of Royal Oak to the west, and clockwise, Epsom, Greenlane, Oranga, and Onehunga. The summit provides views across the Auckland area, and allows visitors to see both of Auckland's harbours.",
        centrepoint={'type': 'Point', 'coordinates': []},
        waypoints={'type': 'LineString', 'coordinates': [[174.786884, -36.896078], [174.787086, -36.901807], [174.780146, -36.904514], [
            174.783205, -36.899682], [174.778881, -36.900085], [174.781735, -36.897434], [174.786884, -36.896078]]},
        image="https://res.cloudinary.com/c7oud0311/image/upload/v1595141835/project3/loca15_ieytlt.jpg",
        embed_route='<iframe src="https://www.google.com/maps/embed?pb=!1m54!1m8!1m3!1d12762.28983882655!2d174.78300500000003!3d-36.900575!3m2!1i1024!2i768!4f13.1!4m43!3e2!4m5!1s0x6d0d489167c724b5%3A0x7d16ecd5717930e2!2sTwin%20Oaks%20Dr%20Parking%2C%20Twin%20Oaks%20Dr%2C%20Auckland%201051%2C%20New%20Zealand!3m2!1d-36.8977165!2d174.78841219999998!4m5!1s0x6d0d4891a9095937%3A0xf5b492939205dfbd!2sPohutukawa%20Drive%20Car%20Park%2C%20Greenlane%2C%20Auckland%201051%2C%20New%20Zealand!3m2!1d-36.8962292!2d174.78681029999998!4m5!1s0x6d0d4896d1cfa9ff%3A0xcddfcfe4a236f5c0!2sTwin%20Oak%20Drive%2C%20Auckland%201051%2C%20New%20Zealand!3m2!1d-36.8992417!2d174.78734419999998!4m5!1s0x6d0d4899c19a5f3f%3A0x7691b7c455fba828!2sOlive%20Grove%2C%20Auckland%201023%2C%20New%20Zealand!3m2!1d-36.9024919!2d174.7812959!4m5!1s0x6d0d4899c19a5f3f%3A0x7691b7c455fba828!2sOlive%20Grove%2C%20Auckland%201023%2C%20New%20Zealand!3m2!1d-36.9024919!2d174.7812959!4m5!1s0x6d0d4899c19a5f3f%3A0x7691b7c455fba828!2sOlive%20Grove%2C%20Auckland%201023%2C%20New%20Zealand!3m2!1d-36.9024919!2d174.7812959!4m5!1s0x6d0d4891a9095937%3A0xf5b492939205dfbd!2sPohutukawa%20Drive%20Car%20Park%2C%20Greenlane%2C%20Auckland%201051%2C%20New%20Zealand!3m2!1d-36.8962292!2d174.78681029999998!5e0!3m2!1sen!2ssg!4v1596008114765!5m2!1sen!2ssg" width="355" height="355" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>',
        location=location_ids[13]
    ),
    Trails(
        trail_name="Queenstown Gardens Lakefront Walk",
        distance=3.1,
        elevation=30,
        route_type='Point to Point',
        difficulty='Easy',
        description='The Queenstown Gardens, located next to the town of Queenstown, New Zealand is a botanical garden which contains a variety of exotic and native trees and plants as well as a large pond and a range of facilities.',
        centrepoint={'type': 'Point', 'coordinates': [168.661232, -45.036955]},
        waypoints={'type': 'LineString', 'coordinates': [[168.661168, -45.033171], [168.662451, -45.034913], [
            168.657459, -45.039189], [168.661674, -45.038065], [168.674122, -45.035638]]},
        image="https://res.cloudinary.com/c7oud0311/image/upload/v1595141835/project3/loca16_ho5rly.jpg",
        embed_route='<iframe src="https://www.google.com/maps/embed?pb=!1m36!1m8!1m3!1d11277.745482240276!2d168.665552!3d-45.03636600000001!3m2!1i1024!2i768!4f13.1!4m25!3e2!4m5!1s0xa9d51d813a115bcb%3A0x9541d0ad817c1319!2sStatue%20of%20William%20Rees%2C%203%20Marine%20Parade%2C%20Queenstown%209300%2C%20New%20Zealand!3m2!1d-45.0327719!2d168.66021569999998!4m5!1s0xa9d51d9d2b92563f%3A0xe4969cf84bebc43b!2sQueenstown%20New%20Zealand%2C%2046%20Robins%20Road%2C%20Queenstown%209300%2C%20New%20Zealand!3m2!1d-45.026322!2d168.66033199999998!4m5!1s0xa9d51d9d2b92563f%3A0xe4969cf84bebc43b!2sQueenstown%20New%20Zealand%2C%2046%20Robins%20Road%2C%20Queenstown%209300%2C%20New%20Zealand!3m2!1d-45.026322!2d168.66033199999998!4m5!1s0xa9d51d8a5cc39021%3A0xbc8d3162cd9bd6bc!2sQueenstown%20Trail%2C%20Lake%20Wakatipu%20Ride%2C%20Queenstown%209300%2C%20New%20Zealand!3m2!1d-45.0359845!2d168.6741032!5e0!3m2!1sen!2ssg!4v1596008164074!5m2!1sen!2ssg" width="355" height="355" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>',
        location=location_ids[24]
    ),
    Trails(
        trail_name="Queenstown Hill Walking Track",
        distance=1.6,
        elevation=613,
        route_type='Point to Point',
        difficulty='Moderate',
        description='The Queenstown Hill walk is one of the best short hikes around Queenstown. The hike takes you to the top of Queenstown Hill and the views are really too good to miss! ',
        centrepoint={'type': 'Point', 'coordinates': [168.672353, -45.023736]},
        waypoints={'type': 'LineString', 'coordinates': [[168.666625, -45.027502], [168.667612, -45.023824], [
            168.673502, -45.026743], [168.673180, -45.023483], [168.672353, -45.023736]]},
        image="https://res.cloudinary.com/c7oud0311/image/upload/v1595142713/project3/loca17_urteil.jpg",
        embed_route='<iframe src="https://www.google.com/maps/embed?pb=!1m24!1m8!1m3!1d11280.336443251621!2d168.67165200000002!3d-45.023218!3m2!1i1024!2i768!4f13.1!4m13!3e2!4m5!1s0xa9d51d852e976d09%3A0xaf9537bb7c2902b1!2sQueenstown%20Hill%20Walking%20Track%2C%209300%2F58%20Belfast%20Terrace%2C%20Queenstown%209300%2C%20New%20Zealand!3m2!1d-45.027504799999996!2d168.6666607!4m5!1s0xa9d51d96240c8c47%3A0x4b8a480bb5e336db!2sQueenstown%20Hill%20Summit%2C%20Queenstown%20Hill%20Walkway%2C%20Queenstown%20Hill%2C%20Queenstown%209371%2C%20New%20Zealand!3m2!1d-45.0190844!2d168.6766463!5e0!3m2!1sen!2ssg!4v1596008219593!5m2!1sen!2ssg" width="355" height="355" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>',
        location=location_ids[24]
    ),
    Trails(
        trail_name="Coney Island Park Trail",
        distance=5.6,
        elevation=13,
        route_type='Loop',
        difficulty='Moderate',
        description='Coney Island Park houses a wide variety of habitats, including coastal forests, grasslands, mangroves, and casuarina woodlands. It is home to a wide variety of fauna and flora, some of which are critically endangered. Some plants at the park are presumed nationally extinct in the wild.',
        centrepoint={'type': 'Point', 'coordinates': [103.921819, 1.408906]},
        waypoints={'type': 'LineString', 'coordinates': [[103.915651, 1.416899, ], [103.929738, 1.401506], [
            103.928770, 1.405492], [103.923835, 1.410408], [103.921217, 1.412392], [103.915651, 1.416899, ]]},
        image="https://res.cloudinary.com/c7oud0311/image/upload/v1595142713/project3/loca18_iokayj.jpg",
        embed_route='<iframe src="https://www.google.com/maps/embed?pb=!1m40!1m12!1m3!1d7977.224127890612!2d103.9181032242087!3d1.4089378215083024!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m25!3e2!4m5!1s0x31da3e1e179c4d17%3A0x5d15e620a65d4375!2sConey%20Island%20(West%20Entrance)!3m2!1d1.4162359!2d103.915184!4m3!3m2!1d1.4016157999999999!2d103.9296948!4m3!3m2!1d1.4105579!2d103.923861!4m5!1s0x31da3f7d06057693%3A0x11be4420beb547bc!2sBeach%20B%20Coney%20Island!3m2!1d1.412391!2d103.9212002!4m3!3m2!1d1.4162314!2d103.91553449999999!5e0!3m2!1sen!2ssg!4v1596008369267!5m2!1sen!2ssg" width="355" height="355" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>',
        location=location_ids[33]
    )
])

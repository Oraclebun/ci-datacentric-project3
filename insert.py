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
    description='Lightly trafficked trail located near Wicklow, County Wicklow, Ireland. The trail is primarily used for hiking, walking, and nature trips. The summit of the Sugar Loaf is the place to be if you want the best views of Dublin and Wicklow.',
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
        description='Powerscourt Waterfall, is a 121-metre high waterfall, on the River Dargle near Enniskerry in County Wicklow, Ireland. The waterfall flows continuously all year, falling in a horsetail-fan, and ranks as the highest waterfall in Ireland. Powerscourt Waterfall is 6km from the Main Estate and is set in one of Ireland’s most beautiful parklands at the foothills of the Wicklow Mountains. It is open to the public for a visitor fee.',
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
        description='This is a short walk that starts from Wicklow Train Station, parallel to River Vartry. This walk ends at Black Castle, a castle ruin that stands on a rocky promontory over the sea, at the eastern side of the town. There is a fine vantage-point for views over the town and the coast of North Wicklow from the ruins.',
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
        embed_route='<iframe src="https://www.google.com/maps/embed?pb=!1m24!1m8!1m3!1d153134.99120362476!2d-6.429815!3d53.150864!3m2!1i1024!2i768!4f13.1!4m13!3e2!4m5!1s0x48679e0a8adcc69f%3A0x139d75c0e86fb2f2!2sKilbride%2C%20Co.%20Wicklow%2C%20Ireland!3m2!1d53.1986734!2d-6.4669351!4m5!1s0x4867996d339c8729%3A0xdd6c7df09f9f5178!2sMullaghcleevaun%2C%20Ballynultagh%2C%20Co.%20Wicklow%2C%20Ireland!3m2!1d53.103055499999996!2d-6.406666599999999!5e0!3m2!1sen!2ssg!4v1596037745048!5m2!1sen!2ssg" width="400" height="400" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>',
        location=location_ids[3],
        comments=[Comment(author=joe_jogger, date_comment=datetime.datetime.now(), body="Invigorating hike up the mountain. It's tough at some points.", sightings=[
                          'mountain', 'wild flowers', 'birds'], date_started=datetime.date(2016, 4, 5), ratings=5, hours_taken=6, minutes_taken=9)]
    ),
    Trails(
        trail_name="Torc Waterfall Trail",
        distance=4.95,
        elevation=50,
        route_type='Loop',
        difficulty='Moderate',
        description='Torc Waterfall is approximately 7 kilometres from Killarney Town and approx 2.5 kilometres from the motor entrance to Muckross House and is signposted from a carpark off the N71. A short walk of approx 200 metres brings you to the waterfall. From that point steps lead to another viewing point at a higher altitude that provides a view over the Middle Lake. The path is also part of the Kerry Way long distance walking route and a starting point for circular walking routes which are indicated by a map down at the start of the trail beside the car park. The waterfall which is approximately 20 metres high is at its best after heavy rainfall.',
        centrepoint={'type': 'Point', 'coordinates': [-9.506368, 52.012555]},
        waypoints={'type': 'LineString', 'coordinates': [
            [-9.502423, 52.019564], [-9.506909, 52.016831], [-9.508434, 52.008956], [-9.507466, 52.006069], [-9.5066471, 52.005025]]},
        image="https://res.cloudinary.com/c7oud0311/image/upload/v1595091822/project3/loca5_vxrlse.jpg",
        embed_route='<iframe src="https://www.google.com/maps/embed?pb=!1m34!1m12!1m3!1d15092.581563816826!2d-9.516525115440176!3d52.01031290578593!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m19!3e2!4m5!1s0x48453dd37e645743%3A0x97b53fbc1b13e3a7!2sMuckross%20House%2C%20The%20National%20Park%2C%20Dromyrourk%2C%20Killarney%2C%20Co.%20Kerry%2C%20Ireland!3m2!1d52.0180696!2d-9.5041358!4m3!3m2!1d52.014168399999996!2d-9.507214699999999!4m3!3m2!1d52.012243899999994!2d-9.5082192!4m3!3m2!1d52.0058869!2d-9.5066703!5e0!3m2!1sen!2ssg!4v1596037463801!5m2!1sen!2ssg" width="400" height="400" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>',
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
        description='This scenic 3.2km shared walking and cycling trail which runs through the historic Shannon Fields honours Limerick Olympian and World Cross Country Champion Michael O’Shea. Exercise stations are available along the route. The route starts at Lock Quay, Clare Street and ends at Athlunkard Bridge, Corbally.',
        centrepoint={'type': 'Point', 'coordinates': [-8.606354, 52.673000]},
        waypoints={'type': 'LineString', 'coordinates': [
            [-8.618198, 52.666321], [-8.610047, 52.681250], [-9.508434, 52.008956]]},
        image="https://res.cloudinary.com/c7oud0311/image/upload/v1595131277/project3/loca6_ikoxjy.jpg",
        embed_route='<iframe src="https://www.google.com/maps/embed?pb=!1m28!1m8!1m3!1d13878.48225483484!2d-8.619410561178112!3d52.67259467334201!3m2!1i1024!2i768!4f13.1!4m17!3e2!4m5!1s0x485b5c698ef8a7e9%3A0x3bcc87157beb7364!2sLock%20Quay%2C%20Limerick%2C%20Ireland!3m2!1d52.6664106!2d-8.618156899999999!4m3!3m2!1d52.671065399999996!2d-8.596178199999999!4m5!1s0x485b5c3713e5c2d1%3A0x168588079edeff87!2sAthlunkard%20Bridge%2C%20Corbally%20Rd%2C%20Limerick%2C%20Ireland!3m2!1d52.6812068!2d-8.610025499999999!5e0!3m2!1sen!2ssg!4v1596038357596!5m2!1sen!2ssg" width="400" height="400" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>',
        location=location_ids[6]
    ),
    Trails(
        trail_name="Minoo Park Trail",
        distance=5.6,
        elevation=266,
        route_type='Out and Back',
        difficulty='Moderate',
        description='Minoo Park (also spelled Mino or Minoh) is a forested valley on the outskirts of Osaka. During autumn, it is one of the best places in the Kansai Region to see the fall colors in a natural setting and it is usually best viewed in the second half of November. The main attraction of Minoo Park is undoubtedly Minoo Waterfall. At 33 metres high and 5 metres wide, with lush surroundings and cool waters, you can see why it has been used as a meditation site as far back as the Asuka Era (592-710 a.d.).',
        centrepoint={'type': 'Point', 'coordinates': [135.470908, 34.943951]},
        waypoints={'type': 'LineString', 'coordinates': [
            [135.468504, 34.834440], [135.470908, 34.943951], [135.471938, 34.854375]]},
        image="https://res.cloudinary.com/c7oud0311/image/upload/v1595134704/project3/loca7_vc9tew.jpg",
        embed_route='<iframe src="https://www.google.com/maps/embed?pb=!1m26!1m12!1m3!1d13097.899820424458!2d135.4624412329136!3d34.844291396916724!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m11!3e2!4m3!3m2!1d34.834923499999995!2d135.4688031!4m5!1s0x6000f98c6d0ac613%3A0x4cd7b8ae9c8328a0!2sMinoo%20Falls%2C%20%EF%BC%92-2%20Minookoen%2C%20Minoo%2C%20Osaka%20562-0002%2C%20Japan!3m2!1d34.8538281!2d135.4719911!5e0!3m2!1sen!2ssg!4v1596039089035!5m2!1sen!2ssg" width="400" height="400" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>',
        location=location_ids[10]
    ),
    Trails(
        trail_name="Mount Ikoma Trail",
        distance=22.8,
        elevation=470,
        route_type='Out and Back',
        difficulty='Difficult',
        description='At present, Mt Ikoma attracts many people, offering panoramic views that extend as far as the Akashi Kaikyo Bridge and Kansai International Airport. Spectacular views are commanded from Skyland Ikoma, an amusement park situated on the top of the mountain. Ikoma Sanjo Amusement Park is a children’s theme park for people of all ages located at the very top of the mountain. The views from the rides are stunning. The park is closed during the winter months but hikers can still stroll through and admire its vintage charm.',
        centrepoint={'type': 'Point', 'coordinates': [135.661355, 34.666958]},
        waypoints={'type': 'LineString', 'coordinates': [[135.655389, 34.685458], [
            135.673053, 34.676862], [135.669831, 34.670840], [135.662991, 34.651603]]},
        image="https://res.cloudinary.com/c7oud0311/image/upload/v1595134703/project3/loca8_twurov.jpg",
        embed_route='<iframe src="https://www.google.com/maps/embed?pb=!1m30!1m8!1m3!1d3204.5856977096846!2d135.67435923924694!3d34.67828491956814!3m2!1i1024!2i768!4f13.1!4m19!3e2!4m5!1s0x600121a05f40b89f%3A0x6e5c569680411f18!2sIshikiri%20Station%2C%202%20Chome-1-6%20Kamiishikiricho%2C%20Higashiosaka%2C%20Osaka%20579-8012%2C%20Japan!3m2!1d34.6852754!2d135.6554756!4m3!3m2!1d34.6781526!2d135.6730308!4m3!3m2!1d34.6782241!2d135.6752688!4m3!3m2!1d34.6784234!2d135.67529109999998!5e0!3m2!1sen!2ssg!4v1596039842948!5m2!1sen!2ssg" width="400" height="400" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>',
        location=location_ids[10]
    ),
    Trails(
        trail_name="Shijonowate Suihen-Shizen-en Trail",
        distance=3.6,
        elevation=303,
        route_type='Point to Point',
        difficulty='Moderate',
        description='About 20 minutes from Osaka city, Shijonawate City is rich in nature. Part of the trail is family friendly and is barrier-free. There are handrails on slopes and steps to cater to people with disabilities and the elderly, as well as small children in strollers. Another part of the trail, is a course that includes a wet garden where you can see beautiful flowers buds, and an observation deck where you can observe wild birds.  However, stepping in nature can be tricky. There are pit vipers, beehives, and poisonous mushrooms, so be careful not to touch them and enjoy your walk.',
        centrepoint={'type': 'Point', 'coordinates': [135.652759, 34.730226]},
        waypoints={'type': 'LineString', 'coordinates': [[135.639560, 34.730457], [
            135.646922, 34.734703], [135.656984, 34.730551], [135.666802, 34.728892]]},
        image="https://res.cloudinary.com/c7oud0311/image/upload/v1595134153/project3/loca9_r96hwi.jpg",
        embed_route='<iframe src="https://www.google.com/maps/embed?pb=!1m26!1m12!1m3!1d21163.448632431144!2d135.6342393510319!3d34.73387090648186!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m11!3e2!4m3!3m2!1d34.7304686!2d135.63965009999998!4m5!1s0x60011f5704d9c9b9%3A0x95374fee2de63c32!2sSuihen%20Shizen-en%2C%20461%20Osaka%2C%20Shijonawate%2C%20Osaka%20575-0011%2C%20Japan!3m2!1d34.7276096!2d135.6662055!5e0!3m2!1sen!2ssg!4v1596040615168!5m2!1sen!2ssg" width="400" height="400" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>',
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
        embed_route='<iframe src="https://www.google.com/maps/embed?pb=!1m24!1m8!1m3!1d25574.804464789257!2d139.605625!3d36.750158!3m2!1i1024!2i768!4f13.1!4m13!3e2!4m5!1s0x601fa0c503bb802d%3A0xc6c6dc50d453cfa9!2sNikk%C5%8D%20Station%2C%20Aioich%C5%8D%2C%20Nikko%2C%20Tochigi%20321-1413%2C%20Japan!3m2!1d36.747448!2d139.62204!4m5!1s0x601fa7574334f215%3A0x861356332fc03131!2sKanmangafuchi%20Abyss%2C%20Nikko%2C%20Tochigi%20321-1415%2C%20Japan!3m2!1d36.748956299999996!2d139.5892097!5e0!3m2!1sen!2ssg!4v1596040717813!5m2!1sen!2ssg" width="400" height="400" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>',
        location=location_ids[12]
    ),
    Trails(
        trail_name="Hiji Falls Trail",
        distance=2.9,
        elevation=139,
        route_type='Out and Back',
        difficulty='Moderate',
        description='Hiji Falls is located in Kunigami Village in northern Okinawa. Admission is 300 yen for children 15 and under and 500 yen for adults and older children. The nature trail is open for hikers 09:00 through 18:00 daily (17:30 November to March) with last entry at 16:00 (15:00 November to March). One of the highlights of the walk is crossing a suspension bridge that spans a valley 17 meters below. The trail comes to an end at the Hiji Waterfall, which makes an impressive sight. ',
        centrepoint={'type': 'Point', 'coordinates': [128.181536, 26.714190]},
        waypoints={'type': 'LineString', 'coordinates': [[128.177421, 26.720088], [
            128.182525, 26.717853], [128.183317, 26.714794], [128.186713, 26.710001]]},
        image="https://res.cloudinary.com/c7oud0311/image/upload/v1595135183/project3/loca11_u0owwk.jpg",
        embed_route='<iframe src="https://www.google.com/maps/embed?pb=!1m24!1m8!1m3!1d14255.771360507322!2d128.182764!3d26.714273!3m2!1i1024!2i768!4f13.1!4m13!3e2!4m5!1s0x34e44364a9d6dbeb%3A0x2b3f45b1e94aaa3e!2sHiji%20Falls%20National%20Park%2C%20781-1%20Hiji%2C%20Kunigami%2C%20Kunigami%20District%2C%20Okinawa%20905-1413%2C%20Japan!3m2!1d26.7191808!2d128.179033!4m5!1s0x34e44481b80a403b%3A0x7149b317e35049cd!2sHijio%20Falls%2C%20Hama%2C%20Kunigami%2C%20Kunigami%20District%2C%20Okinawa%20905-1415%2C%20Japan!3m2!1d26.7105291!2d128.18661079999998!5e0!3m2!1sen!2ssg!4v1596040815442!5m2!1sen!2ssg" width="400" height="400" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>',
        location=location_ids[8]
    ),
    Trails(
        trail_name="Hooker Valley Track",
        distance=10,
        elevation=199,
        route_type='Out and Back',
        difficulty='Easy',
        description='The track leads up the Hooker Valley and along the Hooker River, ending at the glacier lake, where there are amazing views of Aoraki/Mount Cook on a clear day. Along the way you will cross three swingbridges and encounter picturesque icebergs, glaciers and majestic mountains. The best time to walk this stunning track is at dawn when you can view the first rays of the sun creeping over the Southern Alps, including over New Zealand’s highest peak, Aoraki/Mount Cook.',
        centrepoint={'type': 'Point', 'coordinates': [170.098615, -43.703879]},
        waypoints={'type': 'LineString', 'coordinates': [[170.093309, -43.718564], [
            170.100145, -43.705616], [170.098250, -43.692727], [170.103642, -43.689006]]},
        image="https://res.cloudinary.com/c7oud0311/image/upload/v1595135564/project3/loca12_virfkn.jpg",
        embed_route='<iframe src="https://www.google.com/maps/embed?pb=!1m22!1m8!1m3!1d34979.92237089537!2d170.0908026048037!3d-43.70372302939272!3m2!1i1024!2i768!4f13.1!4m11!3e2!4m3!3m2!1d-43.688972199999995!2d170.103614!4m5!1s0x6d2a4b341d69d4dd%3A0x63bc845abb08c829!2sHooker%20Valley%20track%2C%20Hooker%20Valley%20Track%2C%20Mt%20Cook%20National%20Park%207999%2C%20New%20Zealand!3m2!1d-43.718125699999995!2d170.0939684!5e0!3m2!1sen!2ssg!4v1596041138519!5m2!1sen!2ssg" width="400" height="400" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>',
        location=location_ids[26]
    ),
    Trails(
        trail_name="Kea Point from Mount Cook Village Track",
        distance=6,
        elevation=898,
        route_type='Out and Back',
        difficulty='Difficult',
        description='This walk winds its way through subalpine grasslands and scrub to the Mueller Glacier moraine wall. The track passes through a landscape that was formed in 1913 when a stream cut through from the glacier to the original Hermitage site, damaging the building. The walk ends at a viewing deck that gives stunning views of Mount Sefton, The Footstool, Hooker valley, Mueller Glacier lake and Aoraki/Mount Cook. There is a height gain of 180 m over 3 km.',
        centrepoint={'type': 'Point', 'coordinates': [170.086477, -43.722655]},
        waypoints={'type': 'LineString', 'coordinates': [
            [170.095664, -43.732055], [170.093873, -43.731980], [170.084021, -43.710040]]},
        image="https://res.cloudinary.com/c7oud0311/image/upload/v1595091813/project3/loca13_et8ceq.jpg",
        embed_route='<iframe src="https://www.google.com/maps/embed?pb=!1m24!1m8!1m3!1d46133.59886739935!2d170.093461!3d-43.724057!3m2!1i1024!2i768!4f13.1!4m13!3e2!4m5!1s0x6d2a4b532353e20f%3A0xbfce9e4c2c808051!2sBowen%20Drive%2C%20Canterbury%207999%2C%20New%20Zealand!3m2!1d-43.7345137!2d170.0961125!4m5!1s0x6d2a4b2457f0e759%3A0xe26f562fbb0049ce!2sKea%20Point%2C%20Mount%20Cook%20National%20Park%207999%2C%20New%20Zealand!3m2!1d-43.7101993!2d170.0835514!5e0!3m2!1sen!2ssg!4v1596041813162!5m2!1sen!2ssg" width="400" height="400" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>',
        location=location_ids[26]
    ),
    Trails(
        trail_name="Ōrākei Basin Walk",
        distance=4,
        elevation=24,
        route_type='Loop',
        difficulty='Easy',
        description='This walk takes you around the edge of the basin using the boardwalk and the bridge across the Purewa arm of the basin. It offers the chance to see local plant life, as well as views across the city. Most of the walk is flat. There are some steps and steep areas to be aware of, especially behind the water ski club and as you approach Meadowbank Road. These may be a challenge for less confident walkers. It is possible to navigate a pram through these sections but the path is not accessible for wheelchair users.',
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
        embed_route='<iframe src="https://www.google.com/maps/embed?pb=!1m36!1m12!1m3!1d1263.914024021771!2d174.77685459544125!3d-36.88964100419717!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m21!3e2!4m3!3m2!1d-36.8885941!2d174.7767345!4m3!3m2!1d-36.9022194!2d174.7868197!4m3!3m2!1d-36.904106899999995!2d174.78025359999998!4m3!3m2!1d-36.897166899999995!2d174.786487!4m3!3m2!1d-36.8886326!2d174.77670709999998!5e0!3m2!1sen!2ssg!4v1596042594306!5m2!1sen!2ssg" width="400" height="400" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>',
        location=location_ids[13]
    ),
    Trails(
        trail_name="Queenstown Gardens Lakefront Walk",
        distance=3.1,
        elevation=30,
        route_type='Point to Point',
        difficulty='Easy',
        description='The Queenstown Gardens are just a few minutes walk from central Queenstown and offer a beautiful and tranquil setting away from the hustle and bustle. The landscaped gardens include plenty of places to sit down and admire the beauty of the gardens. Pristine lawns, a large water feature, a wide variety of trees and plants and a rose garden all combine to provide that perfect escape from downtown Queenstown. The gardens also feature a couple of significant memorials. The gardens are a popular place to take a picnic, relax with friends and family and enjoy the views of Lake Wakatipu.',
        centrepoint={'type': 'Point', 'coordinates': [168.661232, -45.036955]},
        waypoints={'type': 'LineString', 'coordinates': [[168.661168, -45.033171], [168.662451, -45.034913], [
            168.657459, -45.039189], [168.661674, -45.038065], [168.674122, -45.035638]]},
        image="https://res.cloudinary.com/c7oud0311/image/upload/v1595141835/project3/loca16_ho5rly.jpg",
        embed_route='<iframe src="https://www.google.com/maps/embed?pb=!1m32!1m12!1m3!1d5487.290010543608!2d168.65936523154878!3d-45.03661657960857!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m17!3e2!4m5!1s0xa9d51d8131f8c0ff%3A0x8919b469823cf933!2sCity%20Center%20Queenstown!3m2!1d-45.0330316!2d168.66057849999999!4m3!3m2!1d-45.0379815!2d168.6573398!4m5!1s0xa9d51d8a5cc39021%3A0xbc8d3162cd9bd6bc!2sQueenstown%20Trail%2C%20Lake%20Wakatipu%20Ride%2C%20Queenstown%209300%2C%20New%20Zealand!3m2!1d-45.0359845!2d168.6741032!5e0!3m2!1sen!2ssg!4v1596042759343!5m2!1sen!2ssg" width="400" height="400" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>',
        location=location_ids[24]
    ),
    Trails(
        trail_name="Queenstown Hill Walking Track",
        distance=1.6,
        elevation=613,
        route_type='Point to Point',
        difficulty='Moderate',
        description='The Queenstown Hill walk is one of the best short hikes around Queenstown. The hike takes you to the top of Queenstown Hill and the views are really too good to miss. The Queenstown Hill Time Walk is a 500-metre climb through pine forest to the summit of Te Tapu-nui (mountain of intense sacredness). As you make your way along the track, you will walk by the popular "Basket of Dreams" sculpture as well as six information plates that explain different epochs of Lake Wakatipu and Queenstown.',
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
        description='Coney Island Park houses a wide variety of habitats, including coastal forests, grasslands, mangroves, and casuarina woodlands. It is home to a wide variety of fauna and flora, some of which are critically endangered. Some plants at the park are presumed nationally extinct in the wild. Start exploring the forest and mangrove habitats on the newly built boardwalk and move on to the beach which can be accessed at five locations. You may also ride through the island along the 2.5 km Coney Island Park Connector, taking in the beautiful promenade view of the Serangoon Reservoir.',
        centrepoint={'type': 'Point', 'coordinates': [103.921819, 1.408906]},
        waypoints={'type': 'LineString', 'coordinates': [[103.915651, 1.416899, ], [103.929738, 1.401506], [
            103.928770, 1.405492], [103.923835, 1.410408], [103.921217, 1.412392], [103.915651, 1.416899, ]]},
        image="https://res.cloudinary.com/c7oud0311/image/upload/v1595142713/project3/loca18_iokayj.jpg",
        embed_route='<iframe src="https://www.google.com/maps/embed?pb=!1m38!1m12!1m3!1d13327.778391966802!2d103.9139814308301!3d1.4104154431933373!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m23!3e2!4m5!1s0x31da3e1e179c4d17%3A0x5d15e620a65d4375!2sConey%20Island%20(West%20Entrance)%2C%20Serangoon%20Island!3m2!1d1.4162359!2d103.915184!4m3!3m2!1d1.4017244!2d103.92964789999999!4m3!3m2!1d1.4105409!2d103.9238043!4m3!3m2!1d1.4123668999999999!2d103.9212683!4m3!3m2!1d1.4162035!2d103.91548709999999!5e0!3m2!1sen!2ssg!4v1596043437825!5m2!1sen!2ssg" width="400" height="400" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>',
        location=location_ids[33]
    )
])

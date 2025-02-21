from property import *
from residentialproperty import *
from commericialproperty import *
from viewing import *
from client import *
from status import *
from purpose import *
from restype import *
from status import *
from datetime import datetime

prop = Property(100, "12 Leafy Meadows, Bishopstown, Cork", "Cork", 350000, 120, Status.FORSALE)
prop.showDetails()

res = ResidentialProperty(200, "51 Wood View, Mallow", "Mallow", 255000, 130, Status.UNDEROFFER, 4, Res_type.SEMIDETACHED)
res.showDetails()

comm = CommericialProperty(300, "46 Main Street, Tramore, Co. Waterford", "Waterford", 300000, 210, Status.SALEAGREED, "Excellent retail property", Purpose.RETAIL, Res_type.APARTMENT, 2)
comm.showDetails()

c1 = client.Client(10, "John Webb", "089838384", "jwebb01@gmail.com")
print(c1.__str__())

vw = Viewing(1000, datetime(2024, 1, 31, 10, 45), prop, c1 ,330000, "Nice place but overpriced.")
print(vw.__str__())

res1 = ResidentialProperty(400, "120 Forest Lawn, Douglas, Cork", "Cork", 320000, 93, Status.FORSALE, 3, Res_type.TERRACED)
res1.showDetails()

c1 = client.Client(20, "Janet O Reilly", "0874562732", "joreilly02@gmail.com")

vw1 = Viewing(1100, datetime(2024, 2, 1, 14, 30), res1, c1, 310000, "Great house in a lovely location")
print(vw1.__str__())

#comm1 = CommericialProperty(420, "1 Infinity Road, Wilton Industrial Park, Cork", "Cork", 500000, 2000, Status.UNDEROFFER, "Modern 3 story office building", Purpose.OFFICE)
#comm1.showDetails()

#c2 = client.Client(25, "Slick Software Systems Ltd.", "021-4611222", "slicksoftware@sssl.com")
#print(c2.__str__())

#vw2 = Viewing(1108, datetime(2024, 2, 6, 9, 0), comm1, c2, 475000, "Client thinks property is over-priced")
#print(vw2.__str__())

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///location.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
########################################################################
class Contact(Base):
   
    __tablename__ = "location"

    id = Column(Integer, primary_key=True)
    latitude = Column(String(10))
    longitude = Column(String(10))

    #----------------------------------------------------------------------
    def __init__(self, latitude, longitude):
        
        self.latitude = latitude
        self.longitude = longitude


with open("coordinates.txt") as f:
    for line in f:
        if "$GPGGA" in line:
             x = line
	     break

obt_latitude = (float)(x.split(',')[2])/100
obt_longitude = (float)(x.split(',')[4])/100

# create tables
Base.metadata.create_all(engine)
ed_user = Contact(latitude=obt_latitude,longitude=obt_longitude)
session.add(ed_user)
session.commit()

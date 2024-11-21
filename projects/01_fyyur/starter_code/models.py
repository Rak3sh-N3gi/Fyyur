# from datetime import datetime
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#
db = SQLAlchemy()

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String(120)))
    website_link = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean)
    seeking_description = db.Column(db.String(120))

    def __repr__(self) -> str:
       return f'<Venue {self.id} {self.city} {self.name}>'
    # TODO: implement any missing fields, as a database migration using Flask-Migrate

    def distictVenue(self):
        return (self.query.distinct(self.state,self.city).all())
    

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String(120)))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website_link = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean)
    seeking_description = db.Column(db.String(120))

    def num_upcoming_shows(self):
        return self.query.join(Show).filter_by(artist_id=self.id).filter(Show.start_time > datetime.now()).count()
   
    def num_past_shows(self):
      return self.query.join(Show).filter_by(artist_id=self.id).filter(Show.start_time < datetime.now()).count()
   
    def past_shows(self):
       return Show.get_past_by_artist(self.id)

    # TODO: implement any missing fields, as a database migration using Flask-Migrate

def getValue(self,id):
   return self.query.get(id)

def delValue(self,id):
    self.query.filter_by(id=id).delete()

def valueSearch(self,queryInput):
       return self.query.filter(self.name.ilike('%{}%'.format(queryInput))).all()

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.
class Show(db.Model):
   __tablename__ = 'Show'

   id = db.Column(db.Integer, primary_key=True)
   artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'), nullable=False)
   venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'), nullable=False)
   start_time = db.Column(db.DateTime)
   
   def get_past_by_venue(cls, venue_id):
    # shows = cls.query.filter_by(venue_id=venue_id).join(Artist,cls.artist_id==Artist.id).filter(cls.start_time < datetime.now()).all()
    shows = db.session.query(cls,Artist).filter_by(venue_id=venue_id).join(cls).filter(cls.start_time < datetime.now()).all()
    print( ' Displaying from get_past_by_venue ')
    pastShowList = []
    pastShowDict = {}
    for show in shows:
        pastShowDict["artist_id"]=show.Show.artist_id
        pastShowDict["artist_name"]=show.Artist.name
        pastShowDict["artist_image_link"] = show.Artist.image_link
        pastShowDict["start_time"] = str(show.Show.start_time)
        pastShowList.append(pastShowDict)
        pastShowDict = {}
    return pastShowList
   
   def get_up_by_venue(cls, venue_id):
    # shows = cls.query.filter_by(venue_id=venue_id).join(Artist,cls.artist_id==Artist.id).filter(cls.start_time < datetime.now()).all()
        shows = db.session.query(cls,Artist).filter_by(venue_id=venue_id).join(cls).filter(cls.start_time > datetime.now()).all()
        print( ' Displaying from get_up_by_venue ')
        upShowList = []
        upShowDict = {}
        for show in shows:
            upShowDict["artist_id"]=show.Show.artist_id
            upShowDict["artist_name"]=show.Artist.name
            upShowDict["artist_image_link"] = show.Artist.image_link
            upShowDict["start_time"] = str(show.Show.start_time)
            upShowList.append(upShowDict)
            upShowDict = {}
        return upShowList
   
   @classmethod
   def get_past_by_artist(cls,artist_id):
    shows = db.session.query(cls,Venue).filter_by(artist_id=artist_id).join(cls).filter(cls.start_time < datetime.now()).all()
    pastShowDict = {}
    pastShowList = []
    for show in shows:
        pastShowDict["venue_id"]=show.Show.venue_id
        pastShowDict["venue_name"]=show.Venue.name
        pastShowDict["venue_image_link"] = show.Venue.image_link
        pastShowDict["start_time"] = str(show.Show.start_time)
        pastShowList.append(pastShowDict)
        pastShowDict = {}
    print(' Displaying from Artist ')
    print(pastShowList)
    return pastShowList
   
   @classmethod
   def get_up_by_artist(cls, artist_id):
    shows = db.session.query(cls,Venue).filter_by(artist_id=artist_id).join(cls).filter(cls.start_time > datetime.now()).all()
    upShowDict = {}
    upShowList = []
    for show in shows:
        upShowDict["venue_id"]=show.Show.venue_id
        upShowDict["venue_name"]=show.Venue.name
        upShowDict["venue_image_link"] = show.Venue.image_link
        upShowDict["start_time"] = str(show.Show.start_time)
        upShowList.append(upShowDict)
        upShowDict = {}
    return upShowList

#----------------------------------------------------------------------------#
# Filters.
#----------------------------------------------------------------------------#
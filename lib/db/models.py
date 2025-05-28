from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()

class Artist(Base):
    __tablename__ = 'artists'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    genre = Column(String)

    albums = relationship('Album', back_populates='artist')

class Album(Base):
    __tablename__ = 'albums'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    artist_id = Column(Integer, ForeignKey('artists.id'))

    artist = relationship('Artist', back_populates='albums')
    tracks = relationship('Track', back_populates='album')

class Track(Base):
    __tablename__ = 'tracks'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    album_id = Column(Integer, ForeignKey('albums.id'))
    duration = Column(Integer) 

    album = relationship('Album', back_populates='tracks')

# DB setup
engine = create_engine('sqlite:///lib/db/my_music.db')
Session = sessionmaker(bind=engine)
session = Session()


if __name__ == "__main__":
    print("Creating tables...")
    Base.metadata.create_all(engine)
    print("Tables created successfully!")

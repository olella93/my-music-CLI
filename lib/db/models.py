from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()

# Association table for many-to-many relationship between Playlist and Track
playlist_track_association = Table(
    'playlist_tracks',
    Base.metadata,
    Column('playlist_id', Integer, ForeignKey('playlists.id'), primary_key=True),
    Column('track_id', Integer, ForeignKey('tracks.id'), primary_key=True)
)

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
    playlists = relationship('Playlist', secondary=playlist_track_association, back_populates='tracks')

class Playlist(Base):
    __tablename__ = 'playlists'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    tracks = relationship('Track', secondary=playlist_track_association, back_populates='playlists')

# DB setup
engine = create_engine('sqlite:///lib/db/my_music.db')
Session = sessionmaker(bind=engine)
session = Session()

if __name__ == "__main__":
    print("Creating tables...")
    Base.metadata.create_all(engine)
    print("Tables created successfully!")
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Setup the engine and session
engine = create_engine('sqlite:///lib/db/my_music.db')
Session = sessionmaker(bind=engine)
session = Session()

# Association table for many-to-many Playlist <-> Track
playlist_tracks = Table(
    'playlist_tracks', Base.metadata,
    Column('playlist_id', ForeignKey('playlists.id'), primary_key=True),
    Column('track_id', ForeignKey('tracks.id'), primary_key=True)
)

class Artist(Base):
    __tablename__ = 'artists'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    genre = Column(String, default='Unknown')

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
    duration = Column(Integer)
    album_id = Column(Integer, ForeignKey('albums.id'))

    album = relationship('Album', back_populates='tracks')
    playlists = relationship('Playlist', secondary=playlist_tracks, back_populates='tracks')

class Playlist(Base):
    __tablename__ = 'playlists'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    tracks = relationship('Track', secondary=playlist_tracks, back_populates='playlists')

# CLI Functions
def create_playlist():
    name = input("Enter playlist name: ")
    playlist = Playlist(name=name)
    session.add(playlist)
    session.commit()
    print(f"Playlist '{name}' created.")

def add_track_to_playlist():
    playlist_id = int(input("Enter playlist ID: "))
    track_id = int(input("Enter track ID to add: "))
    playlist = session.get(Playlist, playlist_id)
    track = session.get(Track, track_id)
    if playlist and track:
        playlist.tracks.append(track)
        session.commit()
        print(f"Added '{track.title}' to '{playlist.name}'")
    else:
        print("Invalid playlist or track ID.")

def view_playlist():
    playlist_id = int(input("Enter playlist ID: "))
    playlist = session.get(Playlist, playlist_id)
    if playlist:
        print(f"Playlist: {playlist.name}")
        for track in playlist.tracks:
            print(f"- {track.title} ({track.duration})")
    else:
        print("Playlist not found.")

# Main CLI Loop
def main():
    while True:
        print("\nMusic CLI")
        print("1. Create Playlist")
        print("2. Add Track to Playlist")
        print("3. View Playlist")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_playlist()
        elif choice == "2":
            add_track_to_playlist()
        elif choice == "3":
            view_playlist()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
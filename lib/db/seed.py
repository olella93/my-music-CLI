from .models import Base, engine, session, Artist, Album, Track, Playlist

def seed_data():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    # Seed artists, albums, and tracks
    artist = Artist(name="SZA", genre="R&B")
    album = Album(title="Ctrl", artist=artist)
    track1 = Track(title="Love Galore", duration=260, album=album)
    track2 = Track(title="The Weekend", duration=220, album=album)

    # Create playlists
    playlist1 = Playlist(name="Chill Vibes")
    playlist2 = Playlist(name="Workout Hits")

    # Create additional tracks
    track3 = Track(title="Smooth Ride", duration=225)
    track4 = Track(title="Pump It Up", duration=245)

    # Add tracks to playlists
    playlist1.tracks.append(track3)
    playlist2.tracks.append(track4)
    playlist2.tracks.append(track3) 

    # Add all data to the session
    session.add_all([artist, album, track1, track2, playlist1, playlist2, track3, track4])
    session.commit()
    print("✅ Seeded database!")

if __name__ == "__main__":
    seed_data()
from .models import Base, engine, session, Artist, Album, Track

def seed_data():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    artist = Artist(name="SZA", genre="R&B")
    album = Album(title="Ctrl", artist=artist)
    track1 = Track(title="Love Galore", duration=260, album=album)
    track2 = Track(title="The Weekend", duration=220, album=album)

    session.add_all([artist, album, track1, track2])
    session.commit()
    print("✅ Seeded database!")

if __name__ == "__main__":
    seed_data()

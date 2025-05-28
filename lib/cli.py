import click
from lib.db.models import session, Artist, Album, Track
from lib.helpers import print_album

@click.group()
def cli():
    """🎶 MyMusic CLI — Manage your personal music catalog."""
    pass

@cli.command()
@click.argument('name')
@click.option('--genre', default='Unknown')
def add_artist(name, genre):
    artist = Artist(name=name, genre=genre)
    session.add(artist)
    session.commit()
    click.echo(f"✅ Added artist: {name} ({genre})")

@cli.command()
@click.argument('artist_name')
@click.argument('album_title')
def add_album(artist_name, album_title):
    artist = session.query(Artist).filter_by(name=artist_name).first()
    if not artist:
        click.echo("❌ Artist not found.")
        return
    album = Album(title=album_title, artist=artist)
    session.add(album)
    session.commit()
    click.echo(f"✅ Added album '{album_title}' to artist '{artist_name}'")

@cli.command()
@click.argument('album_title')
@click.argument('track_title')
@click.argument('duration', type=int)
def add_track(album_title, track_title, duration):
    album = session.query(Album).filter_by(title=album_title).first()
    if not album:
        click.echo("❌ Album not found.")
        return
    track = Track(title=track_title, duration=duration, album=album)
    session.add(track)
    session.commit()
    click.echo(f"✅ Added track '{track_title}' to album '{album_title}'")

@cli.command()
def list_artists():
    artists = session.query(Artist).all()
    for artist in artists:
        click.echo(f"- {artist.name} ({artist.genre})")

@cli.command()
@click.argument('artist_name')
def show_albums(artist_name):
    artist = session.query(Artist).filter_by(name=artist_name).first()
    if not artist:
        click.echo("❌ Artist not found.")
        return
    for album in artist.albums:
        print_album(album)

if __name__ == '__main__':
    cli()

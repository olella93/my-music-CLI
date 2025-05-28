### My Music CLI

Welcome to the My Music CLI, a command-line application designed to help you manage your music library efficiently. This project demonstrates key skills from Phase 3, including database management, object-relational mapping (ORM), and CLI development.

## Features
1. Create Playlists
Easily create new playlists to organize your favorite tracks.

2. Add Tracks to Playlists
Add tracks to existing playlists, allowing you to customize your music collections.

3. View Playlists
View the contents of a playlist, including track titles and durations.

4. List All Playlists
Display all playlists in your library.

5. List All Tracks
Display all tracks in your library, including their titles and durations.

6. Exit
Safely exit the application.

## Technologies Used

- Python: Core programming language for the CLI.
- SQLAlchemy: ORM for managing the database and relationships.
- SQLite: Lightweight database for storing music data.
- Virtual Environment: .venv for dependency management.

## Database Structure

The application uses a relational database with the following tables:

1. ## Artists:

id: Unique identifier.
name: Name of the artist.
genre: Genre of the artist.

2. ## Albums:

id: Unique identifier.
title: Title of the album.
artist_id: Foreign key linking to the artists table.

3. ## Tracks:

id: Unique identifier.
title: Title of the track.
duration: Duration of the track (in seconds).
album_id: Foreign key linking to the albums table.

4. ## Playlists:

id: Unique identifier.
name: Name of the playlist.

5. ## Playlist Tracks:

Association table for the many-to-many relationship between Playlists and Tracks.

## How to Run

1. ## Set Up Virtual Environment:

- Activate the virtual environment:
  
  source .venv/bin/activate

2. ## Run the CLI:

- Start the application:

  python lib/cli.py

3. ## Follow the Prompts:

Use the menu options to create playlists, add tracks, view playlists, and more.

## Example Usage

## Create a Playlist

Music CLI
1. Create Playlist
2. Add Track to Playlist
3. View Playlist
4. List Playlists
5. List Tracks
6. Exit
Enter your choice: 1
Enter playlist name: Chill Vibes
Playlist 'Chill Vibes' created.

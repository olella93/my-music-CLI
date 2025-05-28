def format_duration(seconds):
    minutes = seconds // 60
    return f"{minutes}:{str(seconds % 60).zfill(2)}"

def print_album(album):
    print(f"\n🎵 Album: {album.title}")
    for track in album.tracks:
        print(f"  - {track.title} ({format_duration(track.duration)})")

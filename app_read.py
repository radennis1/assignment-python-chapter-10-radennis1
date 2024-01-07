import sqlite3
# Ryan Dennis

# Open connection with SQL database chinook.db
with sqlite3.connect("chinook.db") as conn:
    command = """
                SELECT Name, Composer, UnitPrice 
                FROM tracks 
                INNER JOIN playlist_track 
                ON tracks.TrackId = playlist_track.TrackId 
                WHERE playlist_track.PlaylistId = 12
            """

    # Create cursor variable to read through table rows
    cursor = conn.execute(command)

    # For loop to read and print each row
    for row in cursor:
        title = row[0]
        composer = row[1]
        unit_price = row[2]
        print(
            f"Title: {title}. Composer: {composer}. Unit Price: {unit_price}")

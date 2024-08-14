import requests
import time

# Variables for easy modification
minyear = 2008
maxyear = 2020
songtitle = 'i\'m a sucker'

def search_song(song_title, min_year, max_year):
    base_url = "https://musicbrainz.org/ws/2/recording"
    offset = 0
    seen_artists = set()  # Track artists to prevent duplicates
    html_output = []  # Collect HTML lines for output

    html_output.append("<html><head><title>Music Search Results</title></head><body>")
    html_output.append(f"<h1>Search Results for Songs Titled '{song_title}' from {min_year} to {max_year} and Unknown Dates</h1>")
    html_output.append("<ul>")

    while True:
        params = {
            "fmt": "json",
            "query": f'title:"{song_title}" AND type:album',  # Use the title as is, without quoting
            "limit": 100,  # Max limit per page
            "offset": offset
        }

        response = requests.get(base_url, params=params)
        results = response.json()
        recordings = results.get('recordings', [])
        
        if not recordings:
            break  # Stop if no more recordings are found

        for recording in recordings:
            if recording['title'].lower() == song_title.lower():  # Ensuring exact title match
                artist_name = recording['artist-credit'][0]['name']
                
                if artist_name in seen_artists:
                    continue
                seen_artists.add(artist_name)

                release_year = "Unknown"
                if 'releases' in recording and recording['releases']:
                    release_date = recording['releases'][0].get('date', 'Unknown')
                    release_year = release_date[:4] if release_date != 'Unknown' else 'Unknown'
                
                # Check if release year is within the specified range or unknown
                if release_year == "Unknown" or (release_year.isdigit() and int(release_year) >= min_year and int(release_year) <= max_year):
                    youtube_url = f"https://www.youtube.com/results?search_query={artist_name}+{recording['title']}".replace(" ", "+")
                    html_output.append(f"<li>Title: {recording['title']} - Artist: {artist_name} - Release Year: {release_year} - <a href='{youtube_url}'>YouTube Search</a></li>")
        
        offset += 100  # Move to the next page of results
        time.sleep(1)  # Sleep for 1 second to avoid rate limiting

    html_output.append("</ul>")
    html_output.append("</body></html>")

    filename = "mbz_" + songtitle.replace('.', '').replace(' ', '') + ".html"  # Remove dots for filename
    print(filename)
    with open(filename, "w") as file:
        file.write("\n".join(html_output))

# Calling the search function with the defined variables
search_song(songtitle, minyear, maxyear)

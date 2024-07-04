import json
import requests

def download_reviews(game_id, file_name):
    # URL to get Steam reviews
    url = f"https://store.steampowered.com/appreviews/{game_id}?json=1"

    # Get the response from the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        reviews_data = response.json()

        # Save the reviews to a file
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(reviews_data, file, ensure_ascii=False, indent=4)

        print(f"Reviews downloaded and saved to {file_name}")
    else:
        print(f"Failed to download reviews. Status code: {response.status_code}")

# Parameters
game_id = 2778580
file_name = "steam_reviews_2778580.json"

# Download the reviews
download_reviews(game_id, file_name)

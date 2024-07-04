import json

# File name
file_name = "steam_reviews_2778580.json"

# Load the JSON data
with open(file_name, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Dictionary to store counts of positive and negative reviews per language
review_counts = {}

# Initialize counts for each language
for review_id, review_data in data.items():
    if isinstance(review_data, dict):  # Check if review_data is a dictionary
        language = review_data.get("language", "")
        if language not in review_counts:
            review_counts[language] = {
                "positive": 0,
                "negative": 0
            }

# Process each review
for review_id, review_data in data.items():
    if isinstance(review_data, dict):  # Check if review_data is a dictionary
        language = review_data.get("language", "")
        voted_up = review_data.get("voted_up", None)

        if voted_up is not None:
            if voted_up:
                review_counts[language]["positive"] += 1
            else:
                review_counts[language]["negative"] += 1

# Output the results
for language, counts in review_counts.items():
    total_reviews = counts["positive"] + counts["negative"]
    print(f"Language: {language}")
    print(f"  Positive Reviews: {counts['positive']}")
    print(f"  Negative Reviews: {counts['negative']}")
    print(f"  Total Reviews: {total_reviews}")
    if total_reviews > 0:
        percentage_positive = (counts["positive"] / total_reviews) * 100
        percentage_negative = (counts["negative"] / total_reviews) * 100
        print(f"  Percentage Positive Reviews: {percentage_positive:.2f}%")
        print(f"  Percentage Negative Reviews: {percentage_negative:.2f}%")
    print()

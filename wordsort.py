import json
import re
from collections import Counter
from nltk.corpus import stopwords

# Initialize the stop words list
stop_words = set(stopwords.words('english'))

# Function to analyze downloaded reviews
def analyze_reviews(file_path):
    # Load the reviews from the generated JSON file
    with open(file_path, 'r', encoding='utf-8') as file:
        reviews = json.load(file)

    # Initialize a Counter for word frequencies
    word_counter = Counter()

    # Iterate over the reviews
    for review in reviews.values():
        # Check if the review is in English and is a negative review
        if review.get('language') == 'english' and not review.get('voted_up'):
            # Extract review text
            review_text = review.get('review', '').lower()

            # Remove punctuation and non-alphanumeric characters
            review_text = re.sub(r'[^\w\s]', '', review_text)

            # Tokenize by splitting on whitespace
            words = review_text.split()

            # Filter out stop words and update the word counter
            filtered_words = [word for word in words if word not in stop_words]
            word_counter.update(filtered_words)

    # Get the most common words
    most_common_words = word_counter.most_common(50)

    # Save the results to a file
    output_file_path = 'most_common_words.txt'
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write("Top 50 Most Used Words in Negative Reviews:\n")
        for word, count in most_common_words:
            output_file.write(f"{word}: {count}\n")

    print(f"Output saved to {output_file_path}")

# Path to the JSON file with the reviews
file_path = 'steam_reviews_2778580.json'

# Check if the file exists and analyze the reviews
if file_path:
    analyze_reviews(file_path)
else:
    print("No review file found to analyze.")

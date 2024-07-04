import json

# Keywords to check in the review field
difficulty_keywords = ["difficult", "difficulty", "hard", "unfair"]
performance_keywords = ["performance", "fps", "lag", "stutter", "frame rate", "crash", "freeze", "optimization"]

# File name
file_name = "steam_reviews_2778580.json"

# Load the JSON data
with open(file_name, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Variables to store counts
total_negative_reviews = 0
difficulty_issues = 0
performance_issues = 0
both_issues = 0

# Process each review
for review_id, review_data in data.items():
    if isinstance(review_data, dict):  # Check if review_data is a dictionary
        if review_data.get("voted_up") == False and review_data.get("language", "") == "english":
            total_negative_reviews += 1
            review_text = review_data.get("review", "").lower()

            has_difficulty_issue = any(keyword in review_text for keyword in difficulty_keywords)
            has_performance_issue = any(keyword in review_text for keyword in performance_keywords)

            if has_difficulty_issue and has_performance_issue:
                both_issues += 1
            elif has_difficulty_issue:
                difficulty_issues += 1
            elif has_performance_issue:
                performance_issues += 1

# Calculate percentages
percentage_difficulty_issues = (difficulty_issues / total_negative_reviews) * 100 if total_negative_reviews > 0 else 0
percentage_performance_issues = (performance_issues / total_negative_reviews) * 100 if total_negative_reviews > 0 else 0
percentage_both_issues = (both_issues / total_negative_reviews) * 100 if total_negative_reviews > 0 else 0

# Output the results
print(f'Total Negative Reviews in English: {total_negative_reviews}')
print(f'Negative Reviews in English mentioning only Difficulty Issues: {difficulty_issues}')
print(f'Negative Reviews in English mentioning only Performance Issues: {performance_issues}')
print(f'Negative Reviews in English mentioning both Difficulty and Performance Issues: {both_issues}')
print(f'Percentage of Negative Reviews in English with only Difficulty Issues: {percentage_difficulty_issues:.2f}%')
print(f'Percentage of Negative Reviews in English with only Performance Issues: {percentage_performance_issues:.2f}%')
print(f'Percentage of Negative Reviews in English with both Difficulty and Performance Issues: {percentage_both_issues:.2f}%')

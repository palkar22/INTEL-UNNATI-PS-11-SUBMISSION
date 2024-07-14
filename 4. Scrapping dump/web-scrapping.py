import praw
import csv
import re
from datetime import datetime, timedelta

# Define your Reddit API credentials
#client_id = 
#client_secret = 
#user_agent = 

# Initialize PRAW with credentials
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent
)

# Calculate the timestamp for two years ago
two_years_ago = datetime.now() - timedelta(days=2*365)
two_years_ago_timestamp = int(two_years_ago.timestamp())

# Define known Intel products for extraction
intel_products = ['i3', 'i5', 'i7', 'i9', 'Xeon', 'Pentium', 'Celeron']

# Function to extract Intel product name from the text
def extract_product_name(text):
    for product in intel_products:
        if re.search(r'\b' + product + r'\b', text, re.IGNORECASE):
            return product
    return 'Unknown'

# Function to scrape posts and save to CSV
def scrape_and_save_reviews(subreddit_name, keyword, min_reviews=1000, csv_filename='intel_reviews.csv'):
    reviews = []
    subreddit = reddit.subreddit(subreddit_name)

    for submission in subreddit.search(keyword, sort='new', time_filter='all'):
        # Check the post date
        if submission.created_utc < two_years_ago_timestamp:
            continue

        # Check for non-null reviews
        if submission.selftext:
            product_name = extract_product_name(submission.title + ' ' + submission.selftext)
            reviews.append({
                'review': submission.selftext.replace('\n', ' '),  # Ensure single-line review text
                'product': keyword,
                'product_id': submission.id,
                'product_name': product_name
            })

        # Stop if we have collected the required number of reviews
        if len(reviews) >= min_reviews:
            break

    # Save to CSV
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['review', 'product', 'product_id', 'product_name'])
        writer.writeheader()
        for review in reviews:
            writer.writerow(review)

# List of subreddits to scrape for Intel reviews
subreddits = ['hardware', 'buildapc', 'technology']

# Collect and save reviews from each subreddit
for subreddit in subreddits:
    scrape_and_save_reviews(subreddit, 'Intel', min_reviews=1000, csv_filename=f'intel_reviews_{subreddit}.csv')

print("Reviews have been saved to CSV files for each subreddit.")


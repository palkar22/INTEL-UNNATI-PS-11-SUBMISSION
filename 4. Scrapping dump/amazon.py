import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Function to get the HTML of a page
def get_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return None

# Function to extract reviews from a page
def extract_reviews(soup):
    reviews = []
    review_blocks = soup.find_all("div", {"data-hook": "review"})
    for block in review_blocks:
        review = {}
        review['title'] = block.find("a", {"data-hook": "review-title"}).text.strip()
        review['rating'] = block.find("i", {"data-hook": "review-star-rating"}).text.strip()
        review['text'] = block.find("span", {"data-hook": "review-body"}).text.strip()
        review['date'] = block.find("span", {"data-hook": "review-date"}).text.strip()
        reviews.append(review)
    return reviews

# Function to get all reviews from multiple pages
def get_all_reviews(product_url, num_pages=5):
    all_reviews = []
    for page in range(1, num_pages + 1):
        url = f"{product_url}/ref=cm_cr_arp_d_paging_btm_next_{page}?pageNumber={page}"
        html = get_html(url)
        if html:
            soup = BeautifulSoup(html, 'html.parser')
            reviews = extract_reviews(soup)
            all_reviews.extend(reviews)
        time.sleep(2)  # Be respectful and don't overload the server
    return all_reviews

# URL of the product review page (example)
product_url = "https://www.amazon.com/product-reviews/B08P2D1JZZ"  # Replace with the actual product URL

# Get reviews
reviews = get_all_reviews(product_url, num_pages=5)

# Save reviews to a DataFrame
df = pd.DataFrame(reviews)
df.to_csv("amazon_intel_reviews.csv", index=False)

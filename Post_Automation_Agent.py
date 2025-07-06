
import tweepy
import os
from dotenv import load_dotenv
import schedule
import time

# Load environment variables
load_dotenv()

# X API credentials
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

# Debug: Print credentials
print("Script started...")

# Check credentials
if not all([API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET]):
    print("Error: Missing credentials in credentials.env")
    exit()

# Authenticate with X API v2
try:
    client = tweepy.Client(
        consumer_key=API_KEY,
        consumer_secret=API_SECRET,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET
    )
    print("Authentication successful")
except Exception as e:
    print(f"Authentication error: {e}")
    exit()

# List of 10 quotes to avoid duplicates
quotes = [
    "Keep pushing forward, no matter the obstacles! #Motivation",
    "Every day is a new opportunity to shine. #Inspiration",
    "Success is the sum of small efforts, repeated daily. #Growth",
    "Stay focused and never give up on your dreams! #Mindset",
    "You are stronger than you think. Keep going! #Resilience",
    "Believe in yourself and all that you are. #Confidence",
    "The only limit is the one you set for yourself. #Potential",
    "Small steps lead to big victories. Keep moving! #Progress",
    "Your dreams are worth fighting for. #Determination",
    "Embrace challenges as opportunities to grow. #Mindset"
]

# Track current quote index and post history
current_quote_index = 0
post_history = []

# Function to generate a post (cycle through quotes)
def generate_post():
    global current_quote_index
    post_content = quotes[current_quote_index]
    current_quote_index = (current_quote_index + 1) % len(quotes)  # Move to next quote
    return post_content

# Function to post to X
def post_to_x():
    post_content = generate_post()
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    try:
        response = client.create_tweet(text=post_content)
        tweet_id = response.data['id']
        print(f"Posted to X: {post_content} (Tweet ID: {tweet_id}) at {current_time}")
        post_history.append((post_content, current_time, tweet_id))
    except Exception as e:
        print(f"Failed to post: {e}")

# Function to print post history
def print_post_history():
    print("\nPost History:")
    if not post_history:
        print("No posts yet.")
    else:
        for i, (content, timestamp, tweet_id) in enumerate(post_history, 1):
            print(f"{i}. {content} at {timestamp} (Tweet ID: {tweet_id})")
    print()

# Post immediately
post_to_x()
print_post_history()

# Schedule posts every 4 hours
schedule.every(4).hours.do(post_to_x)
schedule.every(4).hours.do(print_post_history)

# Main loop
while True:
    try:
        next_post_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time() + 4*3600))
        print(f"Next post at {next_post_time}")
        schedule.run_pending()
        time.sleep(60)
    except KeyboardInterrupt:
        print("Script stopped by user")
        print_post_history()
        break
    except Exception as e:
        print(f"Error in scheduler: {e}")
        time.sleep(60)

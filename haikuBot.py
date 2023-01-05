import openai
import tweepy
import time
import pickle

# Authenticate with Twitter API
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Set up ChatGPT
openai.api_key = "YOUR_API_KEY"
model_engine = "text-davinci-002"


def generate_haiku(tweet_text=None):
    # Generate a haiku using ChatGPT
    if tweet_text:
        prompt = f"generate a haiku about this tweet: {tweet_text}"
    else:
        prompt = "generate a haiku"
    completions = openai.Completion.create(
        engine=model_engine, prompt=prompt, max_tokens=1024, n=1, stop=None, temperature=0.7)
    haiku = completions.choices[0].text
    return haiku


def post_haiku():
    # Load the list of haikus that have been posted from the pickle file
    with open("haikus_posted.pkl", "rb") as f:
        haikus_posted = pickle.load(f)

    while True:
        haiku = generate_haiku()
        if haiku not in haikus_posted:
            break
    haikus_posted.append(haiku)
    # Save the updated list of haikus that have been posted to the pickle file
    with open("haikus_posted.pkl", "wb") as f:
        pickle.dump(haikus_posted, f)
    # Post the haiku to the account's timeline
    tweet = api.update_status(haiku)
    # Track the engagement of the tweet
    likes = tweet.favorite_count
    retweets = tweet.retweet_count
    return likes, retweets


def send_haikus_to_followers():
    # Get a list of the account's followers
    followers = api.followers()
    for follower in followers:
        # Check if the follower is a new follower
        if follower.following:
            continue
        user_id = follower.id
        # Send a haiku to the follower in a direct message
        send_haiku_to_follower(user_id)


def send_haiku_to_follower(user_id):
    # Get the user's most recent text-based tweet
    tweets = api.user_timeline(user_id)
    for tweet in tweets:
        if tweet.in_reply_to_status_id is None and tweet.in_reply_to_user_id is None:
            most_recent_tweet = tweet
            break
    else:
        return  # No text-based tweets found

    # Generate a haiku about the tweet
    haiku = generate_haiku(tweet_text=most_recent_tweet.text)

 # Send the haiku to the user in a direct message along with a custom message
    message = f"Thanks for the follow, I created a custom poem about one of your most recent tweets: {haiku}"
    api.send_direct_message(user_id, message)

# Autofollow anyone that follows the account
@api.on_event(tweepy.StreamingEvent.FOLLOW)
def autofollow(event):
    api.create_friendship(event.source.id)

while True:
    # Post a haiku every 30 minutes
    for i in range(50):
        post_haiku()
        time.sleep(30 * 60)

    # Send haikus to any new followers at 9:00am every day
    while True:
        current_time = time.localtime()
        if current_time.tm_hour == 9:
            send_haikus_to_followers()
            break
        time.sleep(60)
  

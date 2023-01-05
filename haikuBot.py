import openai
import tweepy
import random
import time

# Authenticate with Twitter API
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
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
  completions = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024, n=1, stop=None, temperature=0.7)
  haiku = completions.choices[0].text
  return haiku

def post_haiku():
  haiku = generate_haiku()
  # Post the haiku to the account's timeline
  tweet = api.update_status(haiku)
  # Track the engagement of the tweet
  likes = tweet.favorite_count
  retweets = tweet.retweet_count
  return likes, retweets

def send_haiku_to_follower(user_id):
  # Get the user's most recent text-based tweet
  tweets = api.user_timeline(user_id)
  for tweet in tweets:
    if tweet.in_reply_to_status_id is None and tweet.in_reply_to_user_id is None:
      most_recent_tweet = tweet
      break
  else:
    return # No text-based tweets found

  # Generate a haiku about the tweet
  haiku = generate_haiku(tweet_text=most_recent_tweet.text)

  # Send the haiku to the user in a direct message along with a custom message
  message = f"Thanks for the follow, I created a custom poem about your most recent tweet: {haiku}"
  api.send_direct_message(user_id, message)

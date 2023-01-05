# haikuBot

# Daily Haiku Twitter Bot

This is a simple bot that tweets a daily haiku on Twitter. The haiku is randomly selected from a pre-defined list of haiku poems.

## How to use

1.  Clone this repository to your local machine.

Copy code

`git clone https://github.com/<your-username>/daily-haiku-bot.git`

1.  Navigate to the project directory and install the dependencies.

Copy code

`cd daily-haiku-bot
pip install -r requirements.txt`

1.  Create a new Twitter account and obtain the necessary API keys and access tokens to access the Twitter API.

2.  Create a file called `secrets.py` in the project directory and add the following lines, replacing the placeholder text with your own API keys and access tokens:

Copy code

`api_key = "YOUR_API_KEY"
api_secret_key = "YOUR_API_SECRET_KEY"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"`

1.  Run the script to tweet a daily haiku. You can use a service like [cron](https://en.wikipedia.org/wiki/Cron) to schedule the script to run at a specific time each day.

Copy code

`python tweet.py`

## Customization

You can customize the list of haiku poems by modifying the `haiku_list` variable in the `tweet.py` script. Each haiku should be added as a separate string in the list.

## Disclaimer

This project is for educational purposes only and is not affiliated with Twitter in any way. Please make sure to follow the [Twitter Rules](https://twitter.com/en/rules) when using the Twitter API.

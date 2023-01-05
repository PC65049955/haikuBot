# Daily Haiku Twitter Bot

Welcome to the Daily Haiku Twitter Bot! This bot was designed to tweet a daily haiku to your Twitter account. A haiku is a traditional Japanese form of poetry consisting of three lines, with the first and third lines having five syllables, and the second line having seven syllables.

## How to use

### Prerequisites

Before you get started, you'll need the following:

- A Twitter account. If you don't have one already, you can sign up for free at [twitter.com](https://twitter.com/).
- Python 3.6 or higher. You can download Python from the [official website](https://www.python.org/downloads/).

### Setting up the bot

1.  First, you'll need to clone this repository to your local machine. Open a terminal window and enter the following command:

`git clone https://github.com/<your-username>/daily-haiku-bot.git`

1.  Next, navigate to the project directory and install the dependencies:

`cd daily-haiku-bot
pip install -r requirements.txt`

1.  Now you'll need to create a new Twitter app and obtain the necessary API keys and access tokens. Follow these steps:

- Go to the [Twitter Developer Portal](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api).
- If you don't already have a developer account, click the "Apply" button and follow the prompts to create one.
- Once you've created a developer account, click the "Apps" tab in the top menu and then click the "Create App" button.
- Follow the prompts to create a new app. You'll need to provide a name and a brief description of your app, as well as a URL (you can use a placeholder URL if you don't have a website).
- Once your app is created, click the "Keys and Tokens" tab and make note of your API key and API secret key. You'll also need to generate an access token and access token secret.
- Create a file called `secrets.py` in the project directory and add the following lines, replacing the placeholder text with your own API keys and access tokens:

`api_key = "YOUR_API_KEY"
api_secret_key = "YOUR_API_SECRET_KEY"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"`

1.  The bot is now set up and ready to tweet! To tweet a daily haiku, simply run the `tweet.py` script:

`python tweet.py`

The bot will select a random haiku from the pre-defined list of haiku poems and tweet it to your account.

### Scheduling the bot

To have the bot tweet a haiku on a daily basis, you can use a scheduling tool such as [cron](https://en.wikipedia.org/wiki/Cron) to run the `tweet.py` script at a specific time each day.

## Customization

You can customize the list of haiku poems by modifying the `haiku_list` variable in the `tweet.py` script. Simply add or remove strings from the

list to include or exclude haiku poems from being tweeted.

## Disclaimer

This project is for educational purposes only and is not affiliated with Twitter in any way. Please make sure to follow the [Twitter Rules](https://twitter.com/en/rules) when using the Twitter API. Additionally, use of this bot is at your own risk. The author of this project is not responsible for any issues that may arise from using the bot.

## Contributions

If you'd like to contribute to this project, please feel free to create a pull request. All contributions are welcome and appreciated!

## License

This project is licensed under the MIT License - see the [LICENSE](https://chat.openai.com/chat/LICENSE) file for details.

![Twitter Follow](https://img.shields.io/twitter/follow/PC65049955?style=social)

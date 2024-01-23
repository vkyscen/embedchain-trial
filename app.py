import os
from dotenv import load_dotenv
from embedchain import Pipeline as App

# Load environment variables from .env file
load_dotenv()

# Create a bot instance
token = os.getenv("HUGGINGFACE_ACCESS_TOKEN")
print('token',token)

# elon_bot = App.from_config("mistral.yaml")
alex_bot = App.from_config("mistral.yaml")
# Embed online resources
# elon_bot.add("https://en.wikipedia.org/wiki/Elon_Musk")
# elon_bot.add("https://www.forbes.com/profile/elon-musk")


alex_bot.add("@AlexHormozi", data_type="youtube_channel")

# Query the bot
# answer = elon_bot.query("How many companies does Elon Musk run and name those?")
answer2 = alex_bot.query("What was the billion dollar decision that alex has to face?")
# Answer: Elon Musk currently runs several companies. As of my knowledge, he is the CEO and lead designer of SpaceX, the CEO and product architect of Tesla, Inc., the CEO and founder of Neuralink, and the CEO and founder of The Boring Company. However, please note that this information may change over time, so it's always good to verify the latest updates.
# print(answer)  # Output: Elon Musk runs Tesla, Neuralink
print(answer2)  
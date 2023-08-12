# relationship-conflict-solver - NOTE: scraper probably deprecated 
I upset my girlfriend on a solemn Sunday during the first 2020 lockdown. Being halfway around the world from her, I needed an innovative way to cheer her up. My solution was to create a bot which scraped pictures of dogs from Twitter and send her one every hour.

Seeing as this is a very informal use case, please forgive the lack of modularity. To learn how to code this step-by-step, see my [Medium Article](https://medium.com/@twobithack/fixing-relationship-problems-with-python-twilio-and-a-metric-shit-ton-of-dogs-6cd6716dc41a).

NOTE: To use this bot, you will need a Twitter Developer account and a Twilio account. 

## Setup

Create and activate a virtual environment using 

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Set environment variables in a .env file and run `source .env`

Create your little message in main.py.

## Running the project
In a terminal:

```
python get_content.py
python main.py
```

An extra tip, if you're using a mac, open a separate terminal and use the command `caffeinate` to prevent it from going into restmode and stopping the project running

Name

Psychotweet

Description

The goal of this project is to analyze the social and psychological profile of a Twitter user by examining both the tweets posted by the user and those posted about the user.

App Visual

Add a photo of the app.

Installation

To run our program:

Clone the repository.
Edit the credentials.py file by adding your Twitter developer credentials.
Install the following packages:
pip install stop_words wordcloud pandas textblob json dash plotly express graph objects
Navigate to the root of the repository and run the following command:
python -m display.app
Usage

This app performs a psychological analysis of a Twitter user. It can also help detect whether the Twitter environment around the user is toxic or supportive, and identify whether the user speaks in a more positive or negative tone.

Support

samuel.moyal@student-cs.fr

Roadmap

Provide assistance and suggestions for improving the user's Twitter environment. For example, suggest a playlist based on the user's tastes. Warn the user about tweets with overly aggressive language.

Contributing

Specify if you are open to contributions and the requirements for accepting them.

For those wanting to make changes to the project, providing documentation on getting started can be helpful. This might include scripts to run or environment variables to set. Make these steps explicit for clarity. Such instructions can also benefit your future self.

You may also include instructions for linting the code or running tests to maintain high code quality and minimize the chance of accidental errors. Instructions for running tests are particularly useful if additional setup, like starting a Selenium server for browser testing, is required.

Authors and Acknowledgment

Thanks to the entire Mercure team for two fantastic weeks of coding!

Project Status

Our initial idea was to suggest music that could be beneficial for the user's mental health based on their positive preferences.

User Psychological Profile

Social profile (information gathered from tweets mentioning the user)
Psychological profile (information gathered from statuses posted by the user)
"collect" Package Modules

Collect statuses where the user is mentioned without being the author (social)
Collect statuses published by the user (psychological)
Identify the user's most popular tweet (based on RTs and likes) (psychological)
Retrieve the user’s bio (psychological)
Convert and save gathered tweets in .json format
"analysis" Package Modules (using transformers)

Generate a word cloud of relevant keywords used by the user (filter to be determined; social & psychological)
Determine how controversial the user is (social) (sentiment diversity? Virality?)
Classify the sentiments that best describe how the user expresses themselves (psychological) (friendly/hostile -> pie chart)
Classify the sentiments that best describe how the user is portrayed (social) (friendly/hostile -> pie chart)
Generate a word cloud of relevant keywords used when talking about the user (filtered by grammatical category? nouns/adjectives?)
Generate a sentiment cloud reflecting the most common sentiments in the user’s tweets
Generate a sentiment cloud reflecting the most common sentiments in tweets where the user is tagged
"display" Package Modules

Pie chart for psychological sentiment classification
Pie chart for social sentiment classification + final behavior analysis
Controversy gauge
Social keywords word cloud
Psychological keywords word cloud
Public opinion trend over a week

Dash:

Change the language throughout
Fix the padding issue
Add the bio
Add the new features
Samuel-Moyal-Coding-Weeks

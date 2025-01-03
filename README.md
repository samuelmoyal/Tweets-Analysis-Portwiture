# Psychotweet

## Description

Psychotweet is a project designed to analyze the social and psychological profile of a Twitter user. By examining both the tweets posted by the user and those posted about them, the app provides insights into their online persona and environment.

---

## Installation

To set up and run the project, follow these steps:

1. **Clone the Repository**  
   Clone this repository to your local machine using Git or download the zip file.

2. **Set Up Credentials**  
   Edit the `credentials.py` file to include your Twitter developer credentials.

3. **Install Required Packages**  
   Install the necessary dependencies using the following command:  
   ```bash
   pip install stop_words wordcloud pandas textblob json dash plotly
   ```

4. **Run the Application**  
   Navigate to the root directory of the repository and execute the following command:  
   ```bash
   python -m display.app
   ```

---

## Usage

Psychotweet provides tools to analyze a Twitter user's activity and environment. Its main features include:

- **Psychological Analysis:** Examines the sentiments and tone of tweets posted by the user.  
- **Toxicity Detection:** Evaluates whether the user's Twitter environment is toxic or supportive.  
- **Tone Analysis:** Determines if the user’s tone is generally positive or negative.  

---

## Roadmap

### Planned Features

1. **Suggestions for Improvement:**  
   - Provide recommendations for improving the user's Twitter environment.  
   - Suggest playlists tailored to the user's preferences.  
   - Alert users about tweets containing aggressive or negative language.

2. **User Profiles:**  
   - Social profile: Insights from tweets mentioning the user.  
   - Psychological profile: Insights from tweets authored by the user.  

---

## Features and Packages

### `collect` Package Modules

- **Social Profile:**  
  - Collect tweets mentioning the user where they are not the author.  

- **Psychological Profile:**  
  - Collect tweets authored by the user.  
  - Identify the user's most popular tweet (based on retweets and likes).  
  - Retrieve the user’s bio.  
  - Save collected tweets in `.json` format.  

---

### `analysis` Package Modules (Using Transformers)

- Generate a **word cloud** of relevant keywords:  
  - Used by the user (psychological analysis).  
  - Used about the user (social analysis).  
- Determine the user's **controversy level:**  
  - Based on sentiment diversity or virality.  
- **Sentiment Classification:**  
  - Psychological: Friendly/hostile sentiments in the user's tweets.  
  - Social: Friendly/hostile sentiments in tweets mentioning the user.  
- Generate a **sentiment cloud** for:  
  - The user's tweets.  
  - Tweets mentioning the user.  

---

### `display` Package Modules

- **Charts:**  
  - Pie charts for psychological and social sentiment classification.  
  - A controversy gauge for the user's activity.  

- **Word Clouds:**  
  - Social profile keywords.  
  - Psychological profile keywords.  

- **Trend Analysis:**  
  - Public opinion trends over a week.

---

## Contributions

Contributions are welcome! If you have ideas for new features, feel free to open a pull request or create an issue.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.



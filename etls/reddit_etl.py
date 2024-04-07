import sys
import pandas as pd
import praw
import nltk
from nrclex import NRCLex
from nltk.sentiment.vader import SentimentIntensityAnalyzer


# Constants used in the script
from utils.constants import POST_FIELDS


def connect_reddit(client_id: str, client_secret: str,
                   user_agent: str) -> praw.Reddit:
    """
    Connect to Reddit using credentials and return a Reddit instance.

    Parameters:
    - client_id (str): The client ID for Reddit API.
    - client_secret (str): The client secret for Reddit API.
    - user_agent (str): The user agent description.

    Returns:
    - praw.Reddit: An instance of the Reddit client.
    """
    try:
        reddit = praw.Reddit(client_id=client_id,
                             client_secret=client_secret,
                             user_agent=user_agent)
        print("Connected to Reddit!")
        return reddit
    except Exception as e:
        print(e)
        sys.exit(1)  # Exit the script if connection fails


def extract_posts(reddit_instance: praw.Reddit,
                  subreddit: str, time_filter: str,
                  limit: int = None) -> list:
    """
    Extract posts from a specified subreddit using Reddit instance.

    Parameters:
    - reddit_instance (praw.Reddit): The Reddit instance for API access.
    - subreddit (str): The name of the subreddit to extract posts from.
    - time_filter (str): The time filter (e.g., "day", "week", "month") to apply.
    - limit (int, optional): The maximum number of posts to retrieve.

    Returns:
    - list: A list of dictionaries, each containing post data.
    """
    subreddit = reddit_instance.subreddit(subreddit)
    posts = subreddit.top(time_filter=time_filter, limit=limit)
    post_lists = []

    for post in posts:
        post_dict = vars(post)
        post_filtered = {key: post_dict[key] for key in POST_FIELDS}
        post_lists.append(post_filtered)

    return post_lists


def sentiment_analysis(dict_list: list):
    nltk.download('vader_lexicon')
    analyzer = SentimentIntensityAnalyzer()

    for post_dict in dict_list:
        selftext = post_dict['selftext']
        polarity_scores = analyzer.polarity_scores(selftext)
        compound_score = polarity_scores['compound']
        post_dict['sentiment_score'] = compound_score
        affect_freq = NRCLex(selftext).affect_frequencies
        post_dict.update(affect_freq)

    return dict_list


def transform_data(post_df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply transformations to the post DataFrame for data consistency.

    Parameters:
    - post_df (pd.DataFrame): The DataFrame containing post data.

    Returns:
    - pd.DataFrame: The transformed DataFrame.
    """
    # Convert the 'created_utc' column to datetime format
    post_df['created_utc'] = pd.to_datetime(post_df['created_utc'], unit='s')
    # Ensure data types are consistent for analysis
    post_df['author'] = post_df['author'].astype(str)
    post_df['num_comments'] = post_df['num_comments'].astype(int)
    post_df['score'] = post_df['score'].astype(int)
    post_df['title'] = post_df['title'].astype(str)

    return post_df


def load_data_to_csv(data: pd.DataFrame, path: str) -> None:
    data.to_csv(path, index=False)

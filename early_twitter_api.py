import requests
import os
import json
import threading
import tweepy
import early_warning_system
from early_warning_system import send_message

# interval function
def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'

# SINGE REQUEST

def auth():
    return ("AAAAAAAAAAAAAAAAAAAAABbcIgEAAAAATWcuOsi5%2B3lACmzy4%2Fsqa9z6p%2Bc%3DlATquZYJ9P7Pf16JRTVzRJAEy9zamhFShlY5ImgRVEHDcspdKY")

def create_url():
    # Seach for specific hashtag == "#thehashtag" IMPORTANT use %23 instead of "#"
    query = "%23red_cross_warning_system -is:retweet"

    tweet_fields = "tweet.fields=attachments,author_id,created_at"
    url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}".format(query, tweet_fields)
    return url


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def connect_to_endpoint(url, headers):
    response = requests.request("GET", url, headers=headers)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

previous_results = 0
# main function
def main():
    global previous_results
    bearer_token = auth()
    url = create_url()
    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint(url, headers)
    # gets the "result_count" value from the json file in a variable

    current_results = json_response["meta"]["result_count"]

    if current_results > previous_results:
        print("Ny tweet har upptäckts")
        previous_results = current_results
        send_message()
        # print(json.dumps(json_response, indent=4, sort_keys=True))
    else:
        print("\nInga nya tweets")

if __name__ == "__main__":
    # runs function in intervalls (function to run, time between function)
    timer = set_interval(main, 10)

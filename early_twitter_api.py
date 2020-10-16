from early_warning_system import send_message
import requests
import os
import json
import threading


# interval function
def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t


def auth():
    # authenticate access to Twitter API with "BEARER_TOKEN"
    # note: change to your Twitter API Bearer Token 
    # could be expanded upon for security reasons
    return ("BEARER_TOKEN")


def create_url():
    # search for specific hashtag => "#thehashtag" IMPORTANT use %23 instead of "#"
    # "-is:retweet => if the tweet is a retweet it will not "
    query = "%23thehashtag"

    # variable with values for the recent search function
    # "tweet.fields" is what function it will send
    # "=attatchments" is what attatchments it will bring 
    # "author_id" will look for the user's id who sent the Tweet and print it out
    # "created_at"" will look for the time the tweet was sent and print it out
    tweet_fields = "tweet.fields=attachments,author_id,created_at"

    # "url" takes two arguments and sends them to the Twitter API search quary and
    # looks for the decided arguments in "quary" and "tweet_fields"
    url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}".format(query, tweet_fields)
    return url


def create_headers(bearer_token):
    # creates the header with our bearer token
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def connect_to_endpoint(url, headers):
    response = requests.request("GET", url, headers=headers)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


# -- bad solution -- 
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

    # if the "current_results" is higher than "previous_results", which it 
    # always will be if it spots a tweet.
    if current_results > previous_results:
        print("Ny tweet har upptäckts")
        # sets the two variables to the same value so that we will only 
        # send an email if it spots another tweet.
        previous_results = current_results
        send_message()

        # use to see exactly what the twitter api prints out
        # "print(json.dumps(json_response, indent=4, sort_keys=True))"

    else:
        print("\nInga nya tweets")

if __name__ == "__main__":
    # runs function in intervalls, right now every 10 seconds
    # (function to run, time between function)
    timer = set_interval(main, 10)
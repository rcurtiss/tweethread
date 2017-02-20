# Tweethread

Console tool that parses text into tweet-sized chunks, and publishes threaded tweets (a tweetstorm) of them in order.

## Installation

Download this repository and run `python setup.py install`

## How to Tweethread

1. Register a Twitter application. A good guide can be found [here](https://github.com/sferik/t/blob/master/README.md/#configuration)

2. Set the following *environment variables* with the values from your application:
    * TWITTER_CONSUMER_KEY
    * TWITTER_CONSUMER_SECRET
    * TWITTER_ACCESS_TOKEN
    * TWITTER_ACCESS_TOKEN_SECRET

3. Now, you can use it like this:
    * `tweethread filename` to tweet the contents of a file called `filename`. If it doesn't find `filename` then it will do it like this:
    * `tweethread 'Can I haz cheezburger? Yes you can cutie patootie.'` where it will tweet the value of the command line argument.


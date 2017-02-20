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

3. Now, you can use it in a few different ways:

Tweethread has 2 modes; "tweet", and "parse". 

First is it's main purpose, which is to create a tweetstorm out of a large block of text.

   * `tweethread tweet filename.txt` 
      will tweet the contents of a file called 'filename.txt'.
      
   * `tweethread tweet 'Can I haz cheezburger? Yes you can cutie patootie.'`
       will tweet, or parse the value of the command line argument.

However, before you run tweethread in "tweet" mode, you may want to preview your work in "parse" mode.

   * `tweethread parse filename.txt >> tweets.txt`
   parses the textfile 'textfile.txt', and saves the output to a file called 'tweets.txt'.
   
   * `tweethread parse filename.txt`
   parses the textfile 'textfile.txt', and displays the output in the console.
         

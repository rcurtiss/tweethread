'''Tweethread core module'''


from os import getenv
import sys
import tweepy
import nltk
import math

def get_environment_variable(environment_variable_name):
    ''' Returns an environment variable's value or raises an error'''
    key = getenv(environment_variable_name)
    if not key:
        raise LookupError('Please set the {} environment variable'
                          .format(environment_variable_name))
    return key


def get_tweepy_api():
    '''Returns a tweepy api object with the authentication set by environment variables'''
    consumer_key = get_environment_variable('TWITTER_CONSUMER_KEY')
    consumer_secret = get_environment_variable('TWITTER_CONSUMER_SECRET')
    access_token = get_environment_variable('TWITTER_ACCESS_TOKEN')
    access_token_secret = get_environment_variable('TWITTER_ACCESS_TOKEN_SECRET')

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    print(api.me().name)
    return tweepy.API(auth)


def split_seq(seq, size):
        newseq = []
        splitsize = 1.0/size*len(seq)
        for i in range(size):
                newseq.append(seq[int(round(i*splitsize)):int(round((i+1)*splitsize))])
        return newseq


def get_number_of_chunks(i, f):
	x=math.ceil(len(i)/float(f))
	return int(x)

def get_sentences(p):
	if not p:
		raise ValueError("Parameter `p` is empty")
	try:
		nltk.data.find('tokenizers/punkt/english.pickle')
	except LookupError:
		nltk.download('punkt')
	sentences = nltk.tokenize.sent_tokenize(p)
	sentencearray=[]
	while len(sentences) != 0:
		x=sentences.pop(0)
		if len(x) > 136:
			sentencearray.append(x)
		elif len(sentences) > 1:
			if len(x + sentences[0] + ' ') > 136:
				sentencearray.append(x)			
			else:
				if sentences == '.':
					sentences[0]=x + sentences[0]
				else:
					sentences[0]=x + ' ' + sentences[0]
		else:
			sentencearray.append(x) 
	return sentencearray

def break_into_tweets(i):
	tweets=[]
	x=get_sentences(i)
	index=1
	for each in x:
		if len(each) > 136:
			sentence=each.split(" ")
			y=split_seq(sentence,get_number_of_chunks(each,136))
			for every in y:
				tweets.append(' '.join(every))
				index = index + 1
		else:
			tweets.append(each)
			index = index + 1

	return tweets


def main():
    '''tweetstorm's main function, to be run in the command line'''
    numbering_scheme='default'
    mode = sys.argv[1]
    if sys.argv[2] == 'nonum':
        print "Tweet numbering is turned off"
        numbering_scheme='none'
        filename = sys.argv[3]
    else: 
        if len(sys.argv) > 3:
           print "Tweethread has no [[" + sys.argv[2] + ']] option. Using default numbering method.'
           filename = sys.argv[3]
        else:
           filename = sys.argv[2] 
    try:
        with open(filename) as file:
            text = file.read()
    except FileNotFoundError:
        text = filename
    tweets = break_into_tweets(text)
    index = 1
    numbered_tweets=[]
    if numbering_scheme == 'default':
        for tweet in tweets:
            numbered_tweets.append(str(index) + '/ ' + tweet)
            index = index + 1 
        tweets=numbered_tweets
    api = get_tweepy_api()
    index=1
    tweetid=0
    for tweet in tweets:
        if mode == 'tweet':
	    if index != 1:
               api.update_status(tweet,str(tweetid))
               index=index + 1
            else:
               tweet=api.update_status(tweet)
               tweetid=tweet.id_str
               index=index + 1
        elif mode == 'parse':
            print tweet
        else:
            if index == 1:
              print "Tweethread doesn't recognize a [[" + mode + "]] mode...please choose either 'tweet' or 'parse'"
              index = index + 1
            else:
              pass

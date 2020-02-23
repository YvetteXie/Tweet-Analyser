"""Assignment 1.
"""

import math

# Maximum number of characters in a valid tweet.
MAX_TWEET_LENGTH = 50

# The first character in a hashtag.
HASHTAG_SYMBOL = '#'

# The first character in a mention.
MENTION_SYMBOL = '@'

# Underscore is the only non-alphanumeric character that can be part
# of a word (or username) in a tweet.
UNDERSCORE = '_'

SPACE = ' '


def is_valid_tweet(text: str) -> bool:
    """Return True if and only if text contains between 1 and
    MAX_TWEET_LENGTH characters (inclusive).

    >>> is_valid_tweet('Hello Twitter!')
    True
    >>> is_valid_tweet('')
    False
    >>> is_valid_tweet(2 * 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    False

    """

    return 1 <= len(text) <= MAX_TWEET_LENGTH
      

def compare_tweet_lengths(tweet1: str, tweet2: str) -> int:
    '''Return 1 if tweet1 is longer than tweet2, return -1 if tweet2 is longer
    than tweet1, return 0 if tweet1 has the same length as tweet2
    
    Pre-condition: tweet1 and tweet2 are valid
    
    >>> compare_tweet_lengths('hello', 'hi')
    1
    >>> compare_tweet_lengths('lol', 'hahaha')
    -1
    
    '''
    
    if len(tweet1) > len(tweet2):
        return 1
    elif len(tweet1) < len(tweet2):
        return -1
    else:
        return 0


def add_hashtag(original_tweet: str, tag: str) -> str:
    '''Return potential tweet with a space, a hash symbol, and tag appended to
    the end if the potential tweet is valid , otherwise only return 
    original_tweet.
    
    >>> add_hashtag('The winner is', 'Raptors')
    'The winner is #Raptors'
    >>> add_hashtag('I like', 'UofT')
    'I like #UofT'
    
    '''
    
    potential_tweet = original_tweet + SPACE + HASHTAG_SYMBOL + tag
    if is_valid_tweet(potential_tweet):
        return potential_tweet
    else:
        return original_tweet
    

def contains_hashtag(tweet: str, tag_word: str) -> bool:
    '''Return True if and only if tweet contains a hashtag made up of a hashtag
    symbol and tag_word.
    
    >>> contains_hashtag('I went to #orientation2019', 'orientation2019')
    True
    >>> contains_hashtag('Did you watch #NBAfinals?', 'NBA')
    False
    
    '''
    return hashtag_or_mentioned(tweet, tag_word, HASHTAG_SYMBOL)


def is_mentioned(tweet: str, user: str) -> bool:
    '''Return True if and only if tweet contains a mention made up of the 
    mention symbol and user.
    
    >>> is_mentioned("It's nice to meet @taylorswift13", 'taylorswift13')
    True
    >>> is_mentioned('Good job today @Raptors!', 'R')
    False
    
    '''
   
    return hashtag_or_mentioned(tweet, user, MENTION_SYMBOL)                 
     
    
def add_mention_exclusive(original_tweet: str, user: str) -> str:
    '''Return the valid potential tweet by appending a space, a mention symbol,
    and user to the end of original_tweet. Return original_tweet if user is 
    already mentioned, potential tweet is not valid, or original_tweet does not
    contain user.
    
    >>> add_mention_exclusive('I like UofTCompSci', 'UofTCompSci')
    'I like UofTCompsci @UofTCompSci'
    >>> add_mention_exclusive('Excited to be a part of @UofTArtSci', 'UofTArtSci')
    'Excited to be a part of @UofTArtSci'
    
    '''
   
    potential_tweet = original_tweet + SPACE + MENTION_SYMBOL + user
    if ((is_valid_tweet(potential_tweet)) and 
            (is_mentioned(original_tweet, user) is False)
            and (user in original_tweet)):
        return potential_tweet
    else:
        return original_tweet
    
    
def num_tweets_required(message: str) -> int:
    '''Return the minimum number of tweets that would be required to communicate
    the entire message.
    
    >>> num_tweets_required(2* 'abcdefghijklmnopqrstuvwxyz')
    2
    >>> num_tweets_required('Hello')
    1
    
    '''
    
    return math.ceil(len(message) / MAX_TWEET_LENGTH)


def get_nth_tweet(message: str, n: int) -> str:
    '''Return the the nth valid tweet in the sequence of tweets in which message
    is split into. Return an empty string if n is larger than the number of 
    tweets in the sequence
    
    Precondition: n >= 0 
    
    >>> get_nth_tweet(52 * 'a', 2)
    'aa'
    >>> get_nth_tweet('aaaaaaa', 3)
    ' '
    
    '''
    
    num_tweets = num_tweets_required(message)
    if n == num_tweets-1:
        return message[n*MAX_TWEET_LENGTH:]
    elif n < num_tweets-1:
        return message[n*MAX_TWEET_LENGTH:(n+1)*MAX_TWEET_LENGTH]
    else:
        return ""
    



# A helper function.  Do not modify this function, but you are welcome
# to call it.

def clean(text: str) -> str:
    """Return text with every non-alphanumeric character, except for
    HASHTAG_SYMBOL, MENTION_SYMBOL, and UNDERSCORE, replaced with a
    SPACE, and each HASHTAG_SYMBOL replaced with a SPACE followed by
    the HASHTAG_SYMBOL, and each MENTION_SYMBOL replaced with a SPACE
    followed by a MENTION_SYMBOL.

    >>> clean('A! lot,of punctuation?!!')
    'A  lot of punctuation   '
    >>> clean('With#hash#tags? and@mentions?in#twe_et #end')
    'With #hash #tags  and @mentions in #twe_et  #end'
    """

    clean_str = ''
    for char in text:
        if char.isalnum() or char == UNDERSCORE:
            clean_str = clean_str + char
        elif char == HASHTAG_SYMBOL or char == MENTION_SYMBOL:
            clean_str = clean_str + SPACE + char
        else:
            clean_str = clean_str + SPACE
    return clean_str


#Another helper function that avoids writing the same code twice for 
#is_mentioned and contains_hashtag.

def hashtag_or_mentioned(tweet: str, keyword: str, symbol: str) -> bool: 
    '''Return true if there is a hashtag or a user is mentioned
    in the tweet by checking if the order of space, symbol, and keyword is
    correct depending on where might the hashtag or mention be.
    
    >>>hashtag_or_mentioned('I go to #UofT, 'of')
    False
    >>>hashtag_or_mentioned('I am from @RichmondHill, 'RichmondHill')
    True
    
    '''

    tweet = clean(tweet)
    beginning = tweet.startswith(symbol + keyword + SPACE) 
    end = tweet.endswith(SPACE + symbol + keyword)
    middle = (SPACE + symbol + keyword + SPACE) in tweet
    return beginning or end or middle
    
        

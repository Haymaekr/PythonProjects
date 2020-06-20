import tweepy
import time

auth = tweepy.OAuthHandler('y1pGVGk0JMdgBYFBE6LSN2Gnp', 'dxlvHPQIhx2Au5n5gD3SLIOpOkX9R1DgWtKHTYwvPU7wfiKf0o')
auth.set_access_token("1271802693028245505-O3LjsTu8xDFTzUx40E5CXkDIhyk1V5", 'YF6pFQ9ADKR66ak8wE7H2rj6qts2JJFze9D0Dmhx8ZMXn')

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)
user = api.me()
print(user.name)

def limit_handler( curssor):
	try:
		while True:
			try:
				yield curssor.next()
			except StopIteration:
				break
	except tweepy.RateLimitError :
		time.sleep(1000)
	

search_string = "Machine Learning"
number = 1
	

for tweet in limit_handler(tweepy.Cursor(api.search,search_string).items(number)):
	try:
		tweet.favorite()
		print("Done")

	except StopIteration:
		break

	except tweepy.TweepError as er:
		print(er.reason)
	
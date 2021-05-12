# based on ur sentence or mood
# output : Please Rate Our Services >>: i am very sad
# Negative


from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# nltk.download('vader_lexicon')
user_input = input("Please Rate Our Services >>: ")
sid = SentimentIntensityAnalyzer()
score = sid.polarity_scores(user_input)

if score["neg"] != 0:
    print("Negative")
else:
    print("Positive")

tweet = input("Input: ")
for letter in "aeiouAEIOU":
    tweet=tweet.replace(letter,"")
print(tweet)
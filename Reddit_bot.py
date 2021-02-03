# import the modules after we pip installed the package
import praw 

# initialize what we want for the bot
client_id = "" 
client_secret = "" 
username = "" 
password = "" 
user_agent = "" 
  
# We must go to reddit, go to dev tab and get the information thats needed bellow
reddit = praw.Reddit(client_id = client_id,  
                     client_secret = client_secret,  
                     username = username,  
                     password = password, 
                     user_agent = user_agent)

# Now we will demonstrate popular actions the bot can take and we can remove from comment the one we want
'''
# Access a Subreddit:

subreddit = reddit.subreddit('wallstreetbets') 
for submission in subreddit.top(limit = 1): 
    # displays the submission title 
    print(submission.title)   
    # displays the net upvotes of the submission 
    print(submission.score)   
    # displays the submission's ID 
    print(submission.id)    
    # displays the url of the submission 
    print(submission.url)  
''' 

'''

#Comments:

subreddit = reddit.get_subreddit('wallstreetbets')
subreddit_comments = subreddit.get_comments()
for comment in subreddit_comments:
    print(comment.id)
    print(comment.body)
'''


'''
#Upvoting and Downvoting:

# the ID of the comment 
comment_id = "id_here"
# instantiating the Comment class 
comment = reddit.comment(comment_id) 
print("Score before downvoting : " + str(comment.score)) 
# downvoting the comment 
comment.downvote() 
print("Score after downvoting : " + str(comment.score))
'''
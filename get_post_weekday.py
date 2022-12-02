from read_data import fromJson
def get_post_weekday(data:dict)->dict:
    """
    Return the number of posts for each weekday
    args:
        data: a dictionary of posts
    returns: a dictionary with the number of posts for each weekday
    """
    return


# Example
data = fromJson('posts.json')
print(get_post_weekday(data))
# output =  {
#     'Monday': 5, 
#     'Tuesday': 3,
#     'Wednesday': 10, 
#     'Thursday': 0,
#     'Friday': 0, 
#     'Saturday': 1,
#     'Sunday': 7
# }
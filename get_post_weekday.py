import datetime
from read_data import fromJson
def get_post_weekday(data:dict)->dict:
    """
    Return the number of posts for each weekday
    args:
        data: a dictionary of posts
    returns: a dictionary with the number of posts for each weekday
    """
    weekdays = {
        "Monday": 0,
        "Tuesday": 0,
        "Wednesday": 0,
        "Thursday": 0,
        "Friday": 0,
        "Saturday": 0,
        "Sunday": 0
    }
    messages = data['messages']
    for message in messages:
        date = message['date']
        weekday = datetime.datetime.strptime(date,'%Y-%m-%dT%H:%M:%S').strftime('%A')
        # Increment the weekday
        weekdays[weekday] += 1
        
       
        

    return weekdays


# Example
data = fromJson('data/result.json')
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

from read_data import fromJson
# Define a function get post for given month
def get_post_month(data:dict,month:int)->int:
    """
    Return the number of posts for a given month

    args:
        data: a dictionary of posts
        month: the month to check

    returns: the number of posts for the given month
    """
    # Initialize a counter
    count = 0
    messages = data['messages']
    # Loop through the dictionary
    for msg in messages:
        
        if msg['type']=='message':
            date=msg['date']
            # Get month from date
            
            if int(date[5:7])==month:
                count+=1
    
 
    return count

# Path of the file to read
file_path = "data/result.json"
# Read the data
data = fromJson(file_path)
# Get the number of posts for the month of September
count = get_post_month(data,10)
print(count)
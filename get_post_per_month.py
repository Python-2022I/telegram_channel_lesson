from read_data import fromJson
def get_post_per_month(data:dict)->dict:
    count = {
        12:0,
        7:0,
        8:0,
        9:0,
        10:0,
        11:0,
        6:0,
    }
    messages = data['messages']
    for msg in messages:
        if msg['type']=='message':
            date=msg['date']
            # Get month from date
            
            count[int(date[5:7])]+=1
                
    
    return count


# Path of the file to read
file_path = "data/result.json"
# Read the data
data = fromJson(file_path)
# Get the number of posts for the month of September
count = get_post_per_month(data)
print(count)
def hello(event, context):
  print (event)
  if isinstance(event['data'], dict) and 'num_image' in event['data']:
    print ("inside the if condition")
  return "successful return"
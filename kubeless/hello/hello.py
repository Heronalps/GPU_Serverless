def hello(event, context):
  print (event)
  if isinstance(event['data'], dict) and 'num_image' in event['data']:
    print (event['data'])
    print (type(event['data']))
    print("==================")
  return "successful return"
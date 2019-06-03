def hello(event, context):
  print (event)
  if 'data' in event and isinstance(event['data'], dict) and 'num_image' in event['data']:
    print (event['data'])
    print (type(event['data']))
    print("==================")
  return "successful return"

if __name__ == "__main__":
    hello({}, {})
import json

with open("followers.json") as json_file:
  data = json.load(json_file)

follower_lists = data['data']['user']['edge_followed_by']['edges']

flw = []

for i, item in enumerate(follower_lists):

    flw.append(item['node']['username'])

print(len(flw))

import json

following_doc = ""
follower_doc = ""

with open('name_of_files.txt', 'r') as fp:
    for i, ln in enumerate(fp):
        if i == 1:
            following_doc = ln[0:len(ln) - 1]
        elif i == 5:
            follower_doc = ln[0:len(ln) - 1]

# print(follower_doc)
# print(following_doc)


accts_i_follow = set()

with open(following_doc) as f:
    data = json.load(f)

for item in data['relationships_following']:
    string_list_data = item.get('string_list_data', [])
    for string_item in string_list_data:
        value = string_item.get('value')
        if value:
            accts_i_follow.add(value)


accts_follow_me = set()

with open(follower_doc) as f:
    data = json.load(f)

for item in data:
    string_list_data = item.get('string_list_data', [])
    for string_item in string_list_data:
        value = string_item.get('value')
        if value:
            accts_follow_me.add(value)


print("\nACCOUNTS TO UNFOLLOW ˙◠˙")

accounts_that_dont_follow_back = []
for x in accts_i_follow:
    if x not in accts_follow_me:
        accounts_that_dont_follow_back.append(x)

list.sort(accounts_that_dont_follow_back)
for x in accounts_that_dont_follow_back:
    print(x)

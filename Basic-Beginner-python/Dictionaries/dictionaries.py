#dictionary = A changeable, unordered collection of unique key:value pairs
#Fast because they use hashing, allow us to access a value quickly

capitals = {'USA': 'Washington DC',
'India':'New Dehli',
'China':'Beijing',
'Russia':'Moscow'}

capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'Las Vegas'})
capitals.pop('China')
capitals.clear()



#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())

for key,Value in capitals.items():
    print(key,Value)



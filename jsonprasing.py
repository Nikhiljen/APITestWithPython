import json

# json file
course = '{"name": "Nikhil", "language" : ["Java", "python"]}'

# .loads method to load json contain and convert it into dict
dict_courses = json.loads(course)

print(type(dict_courses))
print(dict_courses)

# to get first language
list_lang = dict_courses["language"]

print(list_lang[0])

print(dict_courses["language"][1])

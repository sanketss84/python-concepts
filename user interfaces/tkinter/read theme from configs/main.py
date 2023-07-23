from configparser import ConfigParser

config_object = ConfigParser()

# config_object["APP.STYLE"] = {
#     "theme": "forest-dark"
# }

# with open('./config.ini', 'w') as conf:
#     config_object.write(conf)

config_object.read('./config.ini')
print(config_object.sections()) # reads all config sections

print(config_object.get('APP.STYLE','theme'))

# read all values manually
# print(config_object.get('DEFAULT','name'))
# print(config_object.get('DEFAULT','version'))
# print(config_object.get('DEFAULT','theme'))

# read all values automatically
for key in config_object['DEFAULT']:
    print(key)
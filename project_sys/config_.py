import configparser as cp 

# Initialize ConfigParser
conf = cp.ConfigParser()

# Set default values for all sections
conf['DEFAULT'] = {
    'lending_period': '0',  # Default lending period
    'max_value': '0'         # Default maximum value
}

# Custom settings for Fred and Anne
conf['Fred'] = {
    'max_value': '200'  # Fred's maximum value
}

conf['Anne'] = {
    'lending_period': '30'  # Anne's lending period
}

# Write configuration to file
with open('toolhire.ini', 'w') as toolhire:
    conf.write(toolhire)

print("Configuration file 'toolhire.ini' has been successfully created.")

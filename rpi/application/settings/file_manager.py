import json

# Function reads settings file and parses data.
# Returns dict containing parsed data.
def load_settings():
    settings = {}
    print "\n                  Loading Config"
    print "######################################################### \n"
    for line in open('/home/pi/iot-devices/devices/sparc_htm/rpi/application/settings/settings', 'r'):
        line.strip()
        key, value = line.split(':')
        value = value.strip(' \n\t\r')
        print key + ": " + value
        settings[key] = value
    print "\n######################################################### \n"
    return settings


# Function takes dict with values to update.
# Loads the previous settings from the file.
# Updates the current values with the new.
# Save settings to file.
def save_settings(update):
    settings = load_settings()
    for key in update:
        settings[key] = update[key]
    with open('/home/pi/iot-devices/devices/sparc_htm/rpi/application/settings/settings', 'w') as file:
        for key in settings:
            print "Save " +settings[key]
            file.write(key + ': ' + settings[key] + '\n')


# Function sets settings to default values.
def reset_to_default():
    settings = "Name: none\nType: none\nLocation: none"
    with open('/home/pi/iot-devices/devices/sparc_htm/rpi/application/settings/settings', 'w') as file:
        file.write(settings)

# Function reads factory_settings file and parses data.
# Returns dict containing parsed data.
def load_factory_settings():
    settings = {}
    print "\n                  Loading UUID"
    print "######################################################### \n"
    for line in open('/home/pi/iot-devices/devices/sparc_htm/rpi/application/settings/factory_settings', 'r'):
        line.strip()
        key, value = line.split(':')
        value = value.strip(' \n\t\r')
        settings[key] = value
        print key + ": " + value
    print "\n######################################################### \n"
    return settings

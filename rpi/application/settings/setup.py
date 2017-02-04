import uuid

# Python scrips to generate a nodes unique id
# Writes it to the afctory_settings file.

def generate_uuid():
    UUID = uuid.uuid4()
    with open('factory_settings', 'w') as file:
            print "Save " + str(UUID)
            file.write("serial_number" + ': ' + str(UUID) + '\n')

# Run
generate_uuid()

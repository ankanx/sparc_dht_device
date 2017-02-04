Note: First check if you have git etc

1. sudo apt-get update

2. sudo apt-get install git-core
Note: If you get an error installing Git, run sudo apt-get update and try it again.

##############################################################################
To install the Adafruit DHT11 library:

1. Enter this at the command prompt to download the library:

   sudo  git clone https://github.com/adafruit/Adafruit_Python_DHT.git

2. Change directories with:

     cd Adafruit_Python_DHT

3. Enter this:

     sudo apt-get install build-essential python-dev

4. Install the library with:

     sudo python setup.py install


##############################################################################
To install the python mqtt package


1. Install the paho-mqtt package

    sudo pip install paho-mqtt
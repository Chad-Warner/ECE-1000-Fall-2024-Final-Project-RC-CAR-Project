Low Energy Bluetooth RC Car

        In this project, we use a rasberry Pi Pico WH to emit a bluetooth signal.
        To emit these signals we will use micropython and some bluetooth libraries.
        We then connect to this low energy Bluetooth signal using specialty apps for low voltage
            In this code we use https://play.google.com/store/apps/details?id=de.kai_morich.serial_bluetooth_terminal&hl=en_US

        Once connected to the bluetooth RC car you can use the bluetooth terminal to send messages directly to the pi.
        We use micro python to read these codes and then turn on a motor and a servo to move and turn the car.
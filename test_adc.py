import numpy as np 
import time
import datetime
import os
import sys

import smtplib, ssl
from email.message import EmailMessage

import pyvisa

import board
import busio
import digitalio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn


print("Hello blinka!")

# Try to great a Digital input
pin = digitalio.DigitalInOut(board.D4)
print("Digital IO ok!")

# Try to create an I2C device
i2c = busio.I2C(board.SCL, board.SDA)
print("I2C ok!")

# Try to create an SPI device
spi = busio.SPI(board.SCLK, board.MOSI, board.MISO)
print("SPI ok!")

print("done!")

def GPM_measure(resistor_load=100):
    '''
        INPUTS
            resistor_load - [float] - load resistor ohm value. by default should be 100 ohms.
        OUTPUTS
            gpm - [float] -  gallons per minute readout value from the sensor. converted from ADC measurement
    '''
    # Create the I2C bus
    i2c = busio.I2C(board.SCL, board.SDA)

    # Create the ADC object using the I2C bus
    ads = ADS.ADS1115(i2c)

    # Create single-ended input on channel 0
    chan = AnalogIn(ads, ADS.P0, ADS.P1)

    print("{:>5}\t{:>5}".format('raw', 'v'))  # print headers for table of measurements
    
    ''' perform measurement using ADC and gpib '''
    # use try-except to allow pi to continue working even if error is raised
    try:
        raw_data = chan.value
        voltage = chan.voltage
    except:
        pass
        
    # take measurement and print
    print("{:>5}\t{:>5.3f}".format(raw_data, voltage))

    ''' convert measurement '''
    # convert mA measurement to flowrate
    ### range of device is from 4mA to 20mA
    ### gpm is from ASP to AEP, by default 0.00 to 5.28 gpm

    
    #changed SSP and SEP to be function parameters
    #SSP = 4     # signal start point [mV]
    #SEP = 20    # signal end point [mV]
    ASP = 0.00   # analog start point [gpm]
    AEP = 5.28   # analog end point [gpm]

    # shift data down by 4mV (SSP), then 
    # divide by 16mV (SEP-SSP) to get percentage. 
    # then convert to gpm using the meter's analog range
    #percentage = (data-SSP)/(SEP-SSP)
    #gpm = percentage*(AEP-ASP)
    
    return 

while True:
    time.sleep(2)
    GPM_measure()
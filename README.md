# tsl2561-webthing

WebThing switch for TSL2561 lux sensor

Porting from here https://github.com/mozilla-iot/yeelight-adapter

With tips from this blog https://hacks.mozilla.org/2018/05/creating-web-things-with-python-node-js-and-java/

# Ideally want:

## types

## tests

## setup the pi automation

sudo apt-get install python3-smbus
sudo apt-get install i2c-tools

Go to the Interfacing Options, then P5 I2C, then select yes.

Ok your way out and select reboot.

to confirm the TSL2561's i2c address is 039 run the command

i2cdetect -y 1

Sample source for CoreBlutooth via PyObjC(Python)
====

#Overview

## Description

 This sample source code is writing in how to implementation BLE application using python on OSX.
 It is using CoreBluetooth Library via [PyObjC](https://pythonhosted.org/pyobjc/).
 Target BLE device is [2JCIE-BL01 OMRON Enviroment sensor](http://www.omron.co.jp/ecb/products/sensor/special/environmentsensor/).
 The sensor provid some sensor data throw BLE interface.(see below table)

|Sensor name|unit|
|:----|:----|
|Templature|Celusiuse|
|Humidity|%|
|Air Pressure|hPa|
|lumix|lux|
|UV indicate|?|
|Noise Level|dB|

## License

[MIT LICENCE](https://github.com/masato-ka/geo-hash-potate/blob/master/LICENSE.txt)



# Build

##Install PyObjC

Type below command on OSX

~~~~
$pip install pyobjc
~~~~

When you encount error about libffi, try below it.
~~~
$brew install pkg-config libffi
$export PKG_CONFIG_PATH=/usr/local/Cellar/libffi/3.0.13/lib/pkgconfig/
~~~

I recommend try in new enviroment what create using virtualenv. 


##Run script

~~~
$git clone 
$

# Author

[masato-ka](https://twitter.com/masato_ka)

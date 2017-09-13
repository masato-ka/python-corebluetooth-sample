#!/usr/bin/env python
# encoding: utf-8

import struct

from Foundation import *
from PyObjCTools import AppHelper


wx2_service = CBUUID.UUIDWithString_(u'0C4C3000-7700-46F4-AA96-D5E974E32A54')
wx2_characteristic_data = CBUUID.UUIDWithString_(u'0C4C3001-7700-46F4-AA96-D5E974E32A54')

class BleClass(object):

    def centralManagerDidUpdateState_(self, manager):
        self.manager = manager
        manager.scanForPeripheralsWithServices_options_(None,None)

    def centralManager_didDiscoverPeripheral_advertisementData_RSSI_(self, manager, peripheral, data, rssi):
        self.peripheral = peripheral
        if '8A783AEE-4277-4C3F-8382-ABFA4F6DB8B6' in repr(peripheral.UUID):
            print 'DeviceName' + peripheral.name()
            manager.connectPeripheral_options_(peripheral, None)
            manager.stopScan()


    def centralManager_didConnectPeripheral_(self, manager, peripheral):
        print repr(peripheral.UUID())
        peripheral.setDelegate_(self)
        self.peripheral.discoverServices_([wx2_service])
        
    def peripheral_didDiscoverServices_(self, peripheral, services):
        self.service = self.peripheral.services()[0]
        self.peripheral.discoverCharacteristics_forService_([wx2_characteristic_data], self.service)

    def peripheral_didDiscoverCharacteristicsForService_error_(self, peripheral, service, error):

        for characteristic in self.service.characteristics():
#            print wx2_characteristic_data.UUIDString()
#            print characteristic.UUID().UUIDString()
            if characteristic.properties() == 18:
                peripheral.readValueForCharacteristic_(characteristic)
                break

    def peripheral_didWriteValueForCharacteristic_error_(self, peripheral, characteristic, error):
        print 'In error handler'
        print 'ERROR:' + repr(error)

    def peripheral_didUpdateNotificationStateForCharacteristic_error_(self, peripheral, characteristic, error):
        print "Notification handler"

    def peripheral_didUpdateValueForCharacteristic_error_(self, peripheral, characteristic, error):
        print repr(characteristic.value().bytes().tobytes())
        value = characteristic.value().bytes().tobytes()

        temp = decode_value(value[1:3],0.01)
        print 'temprature:' + str(temp)

        humid = decode_value(value[3:5],0.01)
        print 'humidity:' + str(humid)

        lum = decode_value(value[5:7])
        print 'lumix:' + str(lum)

        uvi = decode_value(value[9:7], 0.01)
        print 'UV index:' + str(uvi)

        atom = decode_value(value[9:11], 0.1)
        print 'Atom:' + str(atom)

        noise = decode_value(value[11:13], 0.01)
        print 'Noise:' + str(noise)

        disco = decode_value(value[13:15], 0.01)
        print 'Disco:' + str(disco)

        heat = decode_value(value[15:17], 0.01)
        print 'Heat:' + str(heat)
        
        batt = decode_value(value[17:19],0.001)
        print 'Battery:' + str(batt)


#Decoding sensor value from Wx2Beancon Data format.
def decode_value(value, multi=1.0):
    if(len(value) != 2):
        return None
    lsb,msb = struct.unpack('BB',value)
    result = ((msb << 8) + lsb) * multi
    return result

if "__main__" == __name__:
    central_manager = CBCentralManager.alloc()
    central_manager.initWithDelegate_queue_options_(BleClass(), None, None)
#    AppHelper.callLater(0.1, comms.loop)
    AppHelper.runConsoleEventLoop()

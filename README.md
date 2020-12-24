# CANClientLib

## Overview

CAN Client library for Python.  
**NOTE:** this library requires `python-can`.

## Usage

### Install

You can install this library using `pip`. To install:

    pip install git+https://github.com/Enchan1207/CANClient

### Import to your application

To import it into your python script, insert `import CANClientLib.canClient`.  
And `client = canClient.Client()` to create instance.  
If no arguments was passed to `canClient.Client`, Client configure virtual CAN and provide it.

(This virtual CAN is provided by `python-can`, **not `SocketCAN`.**  
If you need virtual CAN by `SocketCAN`, use `client = canClient.Client("vcan1", "socketcan_native")`.)

## Library Dependencies

This library requires some modules shown below:  

 - [pyhton-can](https://github.com/hardbyte/python-can)

And if you use it on Raspberry Pi, you also need:

 - RPi.GPIO (but almost Raspbian OS includes it)

## Licence

All files in this repository is published under the MIT Licence.  
In details, see `LICENCE`.

def getInfo():
    import os
    deviceName = os.popen('adb shell getprop ro.product.model').read().strip()
    print(deviceName)
    platformVersion = os.popen('adb shell getprop ro.build.version.release').read().strip()
    print(platformVersion)
    return deviceName,platformVersion

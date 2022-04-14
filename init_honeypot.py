import ConfigParser

class HoneyPotClass:
  def __init__(self, listenAddress='0.0.0.0', listenPort=445, configFile=None):
    if configFile == None:
      print "[*] Config File Required"
      sys.exit(0)
    self.__smbConfig = configFile
    self.__server = SMBSERVER((listenAddress, listenPort), config_parser=self.__smbConfig)
    self.__server.processConfigFile()

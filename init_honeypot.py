import sys
import ConfigParser

class HoneyPotClass:
  def __init__(self, listenAddress='0.0.0.0', listenPort=445, configFile=None):
    if configFile is None:
      print ("[*] Config File Required")
      sys.exit(0)
    print ("[*] Honeypot test fire")

def main():
  honeypot = HoneyPotClass()

if __name__ is "__main__":
  main()
# Import system modules
import sys, string, os, smtplib
import datetime
import xml.etree.ElementTree as ET



import datetime
startTime = datetime.datetime.now()
print "START process Get GDB config:", startTime.strftime("%b %d %Y %H:%M:%S")

# Load and parse the configuration file
tree = ET.parse('C:\Users\saraeh\MyPython\gdbConfig.xml')
#tree.getroot()

root = tree.getroot()

def getActiveChildGDB(serverName):
    for server in root.getiterator():
        if server.tag == "server":
            if server.attrib["name"] == serverName:
                items = server.findall("activeGDB")
                for item in items:
                    activeChildGDB = item.attrib["name"]
                    print serverName + ": " + activeChildGDB          
    return (activeChildGDB)

def getReplicaInfo(serverName):
    for server in root.getiterator():
        if server.tag == "server":
            if server.attrib["name"] == serverName:
                items = server.findall("replica")
                for item in items:
                    repRelease = item.attrib["release"]
                    repPrefix = item.attrib["prefix"]
                    print serverName + ": " + repRelease
                    print serverName + ": " + repPrefix
    return(repRelease, repPrefix)

endTime = datetime.datetime.now()
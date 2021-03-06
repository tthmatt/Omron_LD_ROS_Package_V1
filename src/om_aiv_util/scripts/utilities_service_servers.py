#!/usr/bin/env python
from om_aiv_util.srv import OmAivService, OmAivServiceResponse
import rospy
from om_aiv_util.socketconnection_class import ConnectSocket, connecttcp
s = connecttcp.sock
import socket
import time
import re
import sys
import rospy
from std_msgs.msg import String
BUFFER_SIZE = 1024
ip_address = rospy.get_param("ip_address")
port = rospy.get_param("port")
# ip_address = "172.21.5.122"
# port = 7171
connecttcp.connect(str(ip_address), port)

def handle_applicationFaultClear(req):
    name = req.a[0]
    rcv = applicationFaultClear(name)
    return rcv
def handle_applicationFaultSet(req):
    name = req.a[0]
    short_description = req.a[1]
    long_description = req.a[2]
    bool_driving = req.a[3]
    bool_critical = req.a[4]
    rcv = applicationFaultSet(name, short_description, long_description, bool_driving, bool_critical)
    return rcv
def handle_arclSendText(req):
    string = req.a[0]
    rcv = arclSendText(string)
    return rcv
def handle_configAdd(req):
    configuration_section = req.a[0]
    value = req.a[1]
    rcv = configAdd(configuration_section, value)
    return rcv
def handle_configParse(req):
    rcv = configParse()
    return rcv
def handle_createInfo(req):
    info_name = req.a[0]
    max_len = req.a[1]
    info_value = req.a[2]
    rcv = createInfo(info_name, max_len, info_value)
    return rcv
def handle_echo(req):
    state = req.a[0]
    rcv = echo(state)
    return rcv
def handle_getDataStoreFieldInfo(req):
    field = req.a[0]
    rcv = getDataStoreFieldInfo(field)
    return rcv
def handle_getDataStoreFieldList(req):
    rcv = getDataStoreFieldList()
    return rcv
def handle_getDataStoreFieldValues(req):
    field = req.a[0]
    rcv = getDataStoreFieldValues(field)
    return rcv
def handle_getDataStoreGroupInfo(req):
    group = req.a[0]
    rcv = getDataStoreGroupInfo(group)
    return rcv
def handle_getDataStoreGroupList(req):
    rcv = getDataStoreGroupList()
    return rcv
def handle_getDataStoreGroupValues(req):
    group = req.a[0]
    rcv = getDataStoreGroupValues(group)
    return rcv
def handle_getDataStoreTripGroupList(req):
    rcv = getDataStoreTripGroupList()
    return rcv
def handle_getGoals(req):
    rcv = getGoals()
    return rcv
def handle_getInfoList(req):
    rcv = getInfoList()
    return rcv
def handle_getMacros(req):
    rcv = getMacros()
    return rcv
def handle_getRoutes(req):
    rcv = getRoutes()
    return rcv
def handle_help(req):
    rcv = help()
    return rcv
def handle_log(req):
    message = req.a[0]
    level = req.a[1]
    rcv = log(message, level)
    return rcv
def handle_mapObjectInfo(req):
    name = req.a[0]
    rcv = mapObjectInfo(name)
    return rcv
def handle_mapObjectList(req):
    type = req.a[0]
    rcv = mapObjectList(type)
    return rcv
def handle_mapObjectTypeInfo(req):
    type = req.a[0]
    rcv = mapObjectTypeInfo(type)
    return rcv
def handle_mapObjectTypeList(req):
    rcv = mapObjectTypeList()
    return rcv
def handle_newConfigParam(req):
    section = req.a[0]
    name = req.a[1]
    description = req.a[2]
    priority_level = req.a[3]
    type = req.a[4]
    default_value = req.a[5]
    min = req.a[6]
    max = req.a[7]
    display_hint = req.a[8]
    rcv = newConfigParam(section, name, description, priority_level,
    type, default_value, min, max, display_hint)
    return rcv
def handle_newConfigSectionComment(req):
    section = req.a[0]
    comment = req.a[1]
    rcv = newConfigSectionComment(section, comment)
    return rcv
def handle_popupSimple(req):
    title = req.a[0]
    message = req.a[1]
    button_label = req.a[2]
    timeout = req.a[3]
    rcv = popupSimple(title, message, button_label, timeout)
    return rcv
def handle_quit(req):
    rcv = quit()
    return rcv
def handle_say(req):
    text_str = req.a[0]
    rcv = say(text_str)
    return rcv
def handle_shutdown(req):
    rcv = shutdown()
    return rcv
def handle_tripReset(req):
    rcv = tripReset()
    return rcv
def handle_updateInfo(req):
    info_name = req.a[0]
    info_value = req.a[1]
    rcv = updateInfo(info_name, info_value)
    return rcv
def handle_waitTaskCancel(req):
    rcv = waitTaskCancel()
    return rcv

def utilities_servers(op):
    if op == "applicationFaultClear":
        rospy.loginfo("running applicationFaultClear")
        s1 = rospy.Service('applicationFaultClear', OmAivService, handle_applicationFaultClear)
    elif op == "applicationFaultSet":
        rospy.loginfo("running applicationFaultSet")
        s2 = rospy.Service('applicationFaultSet', OmAivService, handle_applicationFaultSet)
    elif op == "arclSendText":
        rospy.loginfo("running arclSendText")
        s3 = rospy.Service('arclSendText', OmAivService, handle_arclSendText)
    elif op == "configAdd":
        rospy.loginfo("running configAdd")
        s4 = rospy.Service('configAdd', OmAivService, handle_configAdd)
    elif op == "configParse":
        rospy.loginfo("running configParse")
        s5 = rospy.Service('configParse', OmAivService, handle_configParse)
    elif op == "createInfo":
        rospy.loginfo("running createInfo")
        s6 = rospy.Service('createInfo', OmAivService, handle_createInfo)
    elif op == "echo":
        rospy.loginfo("running echo")
        s7 = rospy.Service('echo', OmAivService, handle_echo)
    elif op == "getDataStoreFieldInfo":
        rospy.loginfo("running getDataStoreFieldInfo")
        s8 = rospy.Service('getDataStoreFieldInfo', OmAivService, handle_getDataStoreFieldInfo)
    elif op == "getDataStoreFieldList":
        rospy.loginfo("running getDataStoreFieldList")
        s9 = rospy.Service('getDataStoreFieldList', OmAivService, handle_getDataStoreFieldList)
    elif op == "getDataStoreFieldValues":
        rospy.loginfo("running getDataStoreFieldvalues")
        s10 = rospy.Service('getDataStoreFieldValues', OmAivService, handle_getDataStoreFieldValues)
    elif op == "getDataStoreGroupInfo":
        rospy.loginfo("running getDataStoreGroupInfo")
        s11 = rospy.Service('getDataStoreGroupInfo', OmAivService, handle_getDataStoreGroupInfo)
    elif op == "getDataStoreGroupList":
        rospy.loginfo("running getDataStoreGroupList")
        s12 = rospy.Service('getDataStoreGroupList', OmAivService, handle_getDataStoreGroupList)
    elif op == "getDataStoreGroupValues":
        rospy.loginfo("running getDataStoreGroupValues")
        s13 = rospy.Service('getDataStoreGroupValues', OmAivService, handle_getDataStoreGroupValues)
    elif op == "getDataStoreTripGroupList":
        rospy.loginfo("running getDataStoreTripGroupList")
        s14 = rospy.Service('getDataStoreTripGroupList', OmAivService, handle_getDataStoreTripGroupList)
    elif op == "getInfoList":
        rospy.loginfo("running getInfoList")
        s15 = rospy.Service('getInfoList', OmAivService, handle_getInfoList)
    elif op == "help":
        rospy.loginfo("running help")
        s15 = rospy.Service('help', OmAivService, handle_help)
    elif op == "log":
        rospy.loginfo("running log")
        s16 = rospy.Service('log', OmAivService, handle_log)
    elif op == "mapObjectInfo":
        rospy.loginfo("running mapObjectInfo")
        s17 = rospy.Service('mapObjectInfo', OmAivService, handle_mapObjectInfo)
    elif op == "mapObjectList":
        rospy.loginfo("running mapObjectList")
        s18 = rospy.Service('mapObjectList', OmAivService, handle_mapObjectList)
    elif op == "mapObjectTypeInfo":
        rospy.loginfo("running mapObjectTypeInfo")
        s19 = rospy.Service('mapObjectTypeInfo', OmAivService, handle_mapObjectTypeInfo)
    elif op == "mapObjectTypeList":
        rospy.loginfo("running mapObjectTypeList")
        s20 = rospy.Service('mapObjectTypeList', OmAivService, handle_mapObjectTypeList)
    elif op == "newConfigParam":
        rospy.loginfo("running newConfigParam")
        s21 = rospy.Service('newConfigParam', OmAivService, handle_newConfigParam)
    elif op == "newConfigSectionComment":
        rospy.loginfo("running newConfigSectionComment")
        s22 = rospy.Service('newConfigSectionComment', OmAivService, handle_newConfigSectionComment)
    elif op == "popupSimple":
        rospy.loginfo("running popupSimple")
        s23 = rospy.Service('popupSimple', OmAivService, handle_popupSimple)
    elif op == "quit":
        rospy.loginfo("running quit")
        s24 = rospy.Service('quit', OmAivService, handle_quit)
    elif op == "say":
        rospy.loginfo("running say")
        s25 = rospy.Service('say', OmAivService, handle_say)
    elif op == "shutdown":
        rospy.loginfo("running shutdown")
        s26 = rospy.Service('shutdown', OmAivService, handle_shutdown)
    elif op == "tripReset":
        rospy.loginfo("running tripReset")
        s27 = rospy.Service('tripReset', OmAivService, handle_tripReset)
    elif op == "updateInfo":
        rospy.loginfo("running updateInfo")
        s28 = rospy.Service('updateInfo', OmAivService, handle_updateInfo)
    elif op == "waitTaskCancel":
        rospy.loginfo("running waitTaskCancel")
        s29 = rospy.Service('waitTaskCancel', OmAivService, handle_waitTaskCancel)
    elif op == "getGoals":
        rospy.loginfo("running getGoals")
        s30 = rospy.Service('getGoals', OmAivService, handle_getGoals)
    elif op == "getMacros":
        rospy.loginfo("running getMacros")
        s31 = rospy.Service('getMacros', OmAivService, handle_getMacros)
    elif op == "getRoutes":
        rospy.loginfo("running getRoutes")
        s32 = rospy.Service('getRoutes', OmAivService, handle_getRoutes)

def applicationFaultClear(name):
    command = "applicationFaultClear {}".format(name)
    print "Running command: ", command
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "ApplicationFaultClear cleared" in rcv:
                print rcv
                return rcv
                break
            if "CommandErrorDescription" in rcv:
                print rcv
                return rcv
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e

def applicationFaultSet(name, short_description, long_description, bool_driving, bool_critical):
    command = "applicationFaultSet {}".format(name + " " + short_description
    + " " + long_description + " " + bool_driving + " " + bool_critical)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "Fault:" in rcv:
                print rcv
                return rcv
                break
            if "CommandErrorDescription" in rcv:
                print rcv
                return rcv
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as errormsg:
        print("Connection  failed")
        return errormsg

def arclSendText(string):
    command = "arclSendText {}".format(string)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if string in rcv:
                print rcv
                return rcv
                break
            if "CommandErrorDescription" in rcv:
                print rcv
                return rcv
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e

def configAdd(configuration_section, value):
    command = "configAdd {}".format(configuration_section + " " + value)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "Added" in rcv:
                print rcv
                return rcv
                break
            if "CommandErrorDescription" in rcv:
                print rcv
                return rcv
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as errormsg:
        print("Connection  failed")
        return errormsg

def configParse():
    command = "configParse"
    print "Running command: ", command
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "Config parsed fine" in rcv:
                print rcv
                return rcv
                break
            if "CommandErrorDescription" in rcv:
                print rcv
                return rcv
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e

def createInfo(info_name, max_len, info_value):
    command = "createInfo {}".format(info_name + " " + max_len + " " + info_value)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "Created info" in rcv:
                print rcv
                return rcv
            if "CommandErrorDescription" in rcv:
                print rcv
                return rcv
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as errormsg:
        print("Connection  failed")
        return errormsg

def echo(state):
    command = "echo {}".format(state)
    print "Running command: ", command
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "Echo is" in rcv:
                print rcv
                return rcv
            if "Echo turned" in rcv:
                print rcv
                return rcv
            if "usage" in rcv:
                print rcv
                return rcv
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e

def getDataStoreFieldInfo(field):
    command = "getDataStoreFieldInfo {}".format(field)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "EndOfGetDataStoreFieldInfo" in rcv:
                print rcv
                return rcv
            if "CommandErrorDescription" in rcv:
                print rcv
                return rcv
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e

def getDataStoreFieldList():
    command = "getDataStoreFieldList"
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "EndOfGetDataStoreFieldList" in rcv:
                print rcv
                return rcv
            if "CommandErrorDescription" in rcv:
                print rcv
                return rcv
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e

def getDataStoreFieldValues(field):
    command = "getDataStoreFieldValues {}".format(field)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "EndOfGetDataStoreFieldValues" in rcv:
                print rcv
                return rcv
            if "CommandErrorDescription" in rcv:
                print rcv
                return rcv
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e

def getDataStoreGroupInfo(group):
    command = "getDataStoreGroupInfo {}".format(group)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "EndOfGetDataStoreGroupInfo" in rcv:
                print rcv
                return rcv
            if "CommandErrorDescription" in rcv:
                print rcv
                return rcv
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e

def getDataStoreGroupList():
    command = "getDataStoreGroupList"
    print "Running command: ", command
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "EndOfGetDataStoreGroupList" in rcv:
                print rcv
                return rcv
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e

def getDataStoreGroupValues(group):
    command = "getDataStoreGroupValues {}".format(group)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "EndOfGetDataStoreGroupValues" in rcv:
                print rcv
                return rcv
            if "CommandErrorDescription" in rcv:
                print rcv
                return rcv
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e

def getDataStoreTripGroupList():
    command = "getDataStoreTripGroupList"
    print "Running command: ", command
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "EndOfGetDataStoreTripGroupList" in rcv:
                print rcv
                return rcv
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e

def getGoals():
    command = "getGoals"
    print "Running command: ", command
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "End of goals" in rcv:
                print rcv
                return rcv
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')
    except socket.error as e:
        print("Connection  failed")
        return e

def getInfoList():
    command = "getInfoList"
    print "Running command: ", command
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "End of info list" in rcv:
                print rcv
                return rcv
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e

def getMacros():
    command = "getMacros"
    print "Running command: ", command
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "End of macros" in rcv:
                print rcv
                return rcv
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')
    except socket.error as e:
        print("Connection  failed")
        return e

def getRoutes():
    command = "getRoutes"
    print "Running command: ", command
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "End of routes" in rcv:
                print rcv
                return rcv
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')
    except socket.error as e:
        print("Connection  failed")
        return e


def help():
    command = "help"
    print "Running command: ", command
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "End of commands" in rcv:
                print rcv
                return rcv
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e

def log(message, level):
    command = "log {}".format(message + " " + level)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "Logging" in rcv:
                print rcv
                return rcv
            if "CommandErrorDescription" in rcv:
                print rcv
                return rcv
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as errormsg:
        print("Connection  failed")
        return errormsg

def mapObjectInfo(name):
    command = "mapObjectInfo {}".format(name)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "End of MapObjectInfo" in rcv:
                print rcv
                return rcv
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e

def mapObjectList(type):
    command = "mapObjectList {}".format(type)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "End of MapObjectList" in rcv:
                print rcv
                return rcv
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e

def mapObjectTypeInfo(type):
    command = "mapObjectTypeInfo {}".format(type)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "End of MapObjectTypeInfo" in rcv:
                print rcv
                return rcv
            if "CommandErrorDescription" in rcv:
                print rcv
                return rcv
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e

def mapObjectTypeList():
    command = "mapObjectTypeList"
    print "Running command: ", command
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "End of MapObjectTypeList" in rcv:
                print rcv
                return rcv
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e

def newConfigParam(section, name, description, priority_level, type, default_value, min, max, display_hint):
    command = "newConfigParam {}".format(section + " " + name + " \"" + description + "\" " + priority_level
     + " " + type + " \"" + default_value + "\" " + min + " " + max + " \"" + display_hint + "\"")
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "Will add new param" in rcv:
                print rcv
                return rcv
            if "CommandErrorDescription" in rcv:
                print rcv
                return rcv
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as errormsg:
        print("Connection  failed")
        return errormsg

def newConfigSectionComment(section, comment):
    command = "newConfigSectionComment {}".format(section + " " + comment)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "Will add config comment" in rcv:
                print rcv
                return rcv
            if "CommandErrorDescription" in rcv:
                print rcv
                return rcv
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as errormsg:
        print("Connection  failed")
        return errormsg

def popupSimple(title, message, button_label, timeout):
    command = "popupSimple {}".format(" \"" + title + "\" " +" \"" + message
    +"\" "+ " \"" + button_label + "\" " + timeout)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "Creating simple popup" in rcv:
                print rcv
                return rcv
            if "CommandErrorDescription" in rcv:
                print rcv
                return rcv
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as errormsg:
        print("Connection  failed")
        return errormsg

def quit():
    command = "quit"
    print "Running command: ", command
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "Closing connection" in rcv:
                print rcv
                return rcv
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e

def say(text_str):
    command = "say {}".format(text_str)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "Saying" in rcv:
                print rcv
                return rcv
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e

def shutdown():
    command = "shutdown"
    print "Running command: ", command
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "Shutting down" in rcv:
                print rcv
                return rcv
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e

def tripReset():
    command = "tripReset"
    print "Running command: ", command
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "EndOfTripReset" in rcv:
                print rcv
                return rcv
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e

def updateInfo(info_name, info_value):
    command = "updateInfo {}".format(info_name + " " + info_value)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "Updated info" in rcv:
                print rcv
                return rcv
            if "CommandErrorDescription" in rcv:
                print rcv
                return rcv
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as errormsg:
        print("Connection  failed")
        return errormsg

def waitTaskCancel():
    command = "waitTaskCancel"
    print "Running command: ", command
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "WaitState" in rcv:
                print rcv
                return rcv
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e

if __name__ == "__main__":
    rospy.init_node('utilities_service_servers')
    utilities_servers("applicationFaultClear")
    utilities_servers("applicationFaultSet")
    utilities_servers("arclSendText")
    utilities_servers("configAdd")
    utilities_servers("configParse")
    utilities_servers("createInfo")
    utilities_servers("echo")
    utilities_servers("getDataStoreFieldInfo")
    utilities_servers("getDataStoreFieldList")
    utilities_servers("getDataStoreFieldValues")
    utilities_servers("getDataStoreGroupInfo")
    utilities_servers("getDataStoreGroupList")
    utilities_servers("getDataStoreGroupValues")
    utilities_servers("getDataStoreTripGroupList")
    utilities_servers("getGoals")
    utilities_servers("getInfoList")
    utilities_servers("getMacros")
    utilities_servers("getRoutes")
    utilities_servers("help")
    utilities_servers("log")
    utilities_servers("mapObjectInfo")
    utilities_servers("mapObjectList")
    utilities_servers("mapObjectTypeInfo")
    utilities_servers("mapObjectTypeList")
    utilities_servers("newConfigParam")
    utilities_servers("newConfigSectionComment")
    utilities_servers("popupSimple")
    utilities_servers("quit")
    utilities_servers("say")
    utilities_servers("shutdown")
    utilities_servers("tripReset")
    utilities_servers("updateInfo")
    utilities_servers("waitTaskCancel")
    rospy.spin()

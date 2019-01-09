#!/usr/bin/env python

import urllib.request as ur
import sys
import json
import codecs
import platform

if platform.system() == 'Linux':
  file=open('/etc/zabbix/papercut.conf','r')
elif platform.system() == 'Windows':
  file=open('C:/zabbix/binz/papercut.conf','r')

for line in file.readlines():
    (key, sep, value) = line.partition('=')
    if key == 'papercut_ip':
        serverip = value[1:-2]
    if key == 'papercut_auth':
        serverauth = value[1:-2]

url='http://{0}/api/health?{1}'.format(serverip,serverauth)
url2='http://{0}/api/stats/held-jobs-count?minutes=10&{1}'.format(serverip,serverauth)
url3='http://{0}/api/stats/recent-pages-count?minutes=60&{1}'.format(serverip,serverauth)

#response = ur.urlopen(url)
reader = codecs.getreader("utf-8")
#json_input = json.load(reader(response))


response = ur.urlopen(url)
data = json.load(reader(response))

response2 = ur.urlopen(url2)
data2 = json.load(reader(response2))

response3 = ur.urlopen(url3)
data3 = json.load(reader(response3))

def main():
  if len(sys.argv)<2:
    print("Run as:\n{0} [version | diskSpaceFreeMB | jvmMemoryUsedPercentage | uptimeHours]".format(sys.argv[0]))

  elif sys.argv[1]=='version':
    version = data['applicationServer']['systemInfo']['version']
    print(version)

  elif sys.argv[1]=='diskSpaceFreeMB':
    diskSpaceFreeMB = data['applicationServer']['systemMetrics']['diskSpaceFreeMB']
    print(diskSpaceFreeMB)
  
  elif sys.argv[1]=='diskSpaceTotalMB':
    diskSpaceTotalMB = data['applicationServer']['systemMetrics']['diskSpaceTotalMB']
    print(diskSpaceTotalMB)

  elif sys.argv[1]=='diskSpaceUsedPercentage':
    diskSpaceUsedPercentage = data['applicationServer']['systemMetrics']['diskSpaceUsedPercentage']
    print(diskSpaceUsedPercentage)

  elif sys.argv[1]=='jvmMemoryUsedPercentage':
    jvmMemoryUsedPercentage = data['applicationServer']['systemMetrics']['jvmMemoryUsedPercentage']
    print(jvmMemoryUsedPercentage)

  elif sys.argv[1]=='jvmMemoryMaxMB':
    jvmMemoryMaxMB = data['applicationServer']['systemMetrics']['jvmMemoryMaxMB']
    print(jvmMemoryMaxMB)

  elif sys.argv[1]=='jvmMemoryTotalMB':
    jvmMemoryTotalMB = data['applicationServer']['systemMetrics']['jvmMemoryTotalMB']
    print(jvmMemoryTotalMB)

  elif sys.argv[1]=='jvmMemoryUsedMB':
    jvmMemoryUsedMB = data['applicationServer']['systemMetrics']['jvmMemoryUsedMB']
    print(jvmMemoryUsedMB)

  elif sys.argv[1]=='uptimeHours':
    uptimeHours = data['applicationServer']['systemMetrics']['uptimeHours']
    print(uptimeHours)

  elif sys.argv[1]=='validlicense':
    validlicense = data['license']['valid']
    print(validlicense)

  elif sys.argv[1]=='licenseRemaining':
    licenseRemaining = data['license']['upgradeAssuranceRemainingDays']
    print(licenseRemaining)

  elif sys.argv[1]=='licenseUsersUsed':
    licenseUsersUsed = data['license']['users']['used']
    print(licenseUsersUsed)
  
  elif sys.argv[1]=='licenseUsersLicensed':
    licenseUsersLicensed = data['license']['users']['licensed']
    print(licenseUsersLicensed)

  elif sys.argv[1]=='licenseUsersRemaining':
    licenseUsersRemaining = data['license']['users']['remaining']
    print(licenseUsersRemaining)

  elif sys.argv[1]=='licenseSiteServersUsed':
    licenseSiteServersUsed = data['license']['siteServers']['used']
    print(licenseSiteServersUsed)
  
  elif sys.argv[1]=='licenseSiteServersLicensed':
    licenseSiteServersLicensed = data['license']['siteServers']['licensed']
    print(licenseSiteServersLicensed)

  elif sys.argv[1]=='licenseSiteServersRemaining':
    licenseSiteServersRemaining = data['license']['siteServers']['remaining']
    print(licenseSiteServersRemaining)

  elif sys.argv[1]=='licenseAdvancedClientsUsed':
    licenseAdvancedClientsUsed = data['license']['advancedClients']['used']
    print(licenseAdvancedClientsUsed)
  
  elif sys.argv[1]=='licenseAdvancedClientsLicensed':
    licenseAdvancedClientsLicensed = data['license']['advancedClients']['licensed']
    print(licenseAdvancedClientsLicensed)

  elif sys.argv[1]=='licenseAdvancedClientsRemaining':
    licenseAdvancedClientsRemaining = data['license']['advancedClients']['remaining']
    print(licenseAdvancedClientsRemaining)

  elif sys.argv[1]=='databaseStatus':
    databaseStatus = data['database']['status']
    print(databaseStatus)

  elif sys.argv[1]=='activeConnections':
    activeConnections = data['database']['activeConnections']
    print(activeConnections)

  elif sys.argv[1]=='maxConnections':
    maxConnections = data['database']['maxConnections']
    print(maxConnections)

  elif sys.argv[1]=='totalConnections':
    totalConnections = data['database']['totalConnections']
    print(totalConnections)
  
  elif sys.argv[1]=='timeToConnectMilliseconds':
    timeToConnectMilliseconds = data['database']['timeToConnectMilliseconds']
    print(timeToConnectMilliseconds)

  elif sys.argv[1]=='timeToQueryMilliseconds':
    timeToQueryMilliseconds = data['database']['timeToQueryMilliseconds']
    print(timeToQueryMilliseconds)

  elif sys.argv[1]=='heldJobsCount':
    heldJobsCount = data2['heldJobsCount']
    print(heldJobsCount)

  elif sys.argv[1]=='recentPagesCount':
    recentPagesCount = data3['recentPagesCount']
    print(recentPagesCount)

  elif sys.argv[1]=='processCpuLoadPercentage':
    processCpuLoadPercentage = data['applicationServer']['systemMetrics']['processCpuLoadPercentage']
    print(processCpuLoadPercentage)

  elif sys.argv[1]=='systemCpuLoadPercentage':
    systemCpuLoadPercentage = data['applicationServer']['systemMetrics']['systemCpuLoadPercentage']
    print(systemCpuLoadPercentage)

  elif sys.argv[1]=='gcTimeMilliseconds':
    gcTimeMilliseconds = data['applicationServer']['systemMetrics']['gcTimeMilliseconds']
    print(gcTimeMilliseconds)

  elif sys.argv[1]=='gcExecutions':
    gcExecutions = data['applicationServer']['systemMetrics']['gcExecutions']
    print(gcExecutions)

  elif sys.argv[1]=='siteserverCount':
    siteserverCount = data['siteServers']['count']
    print(siteserverCount)

  elif sys.argv[1]=='siteserverOfflineCount':
    siteserverOfflineCount = data['siteServers']['offlineCount']
    print(siteserverOfflineCount)

  elif sys.argv[1]=='siteserverOfflinePercentage':
    siteserverOfflinePercentage = data['siteServers']['offlinePercentage']
    print(siteserverOfflinePercentage)

if __name__ == '__main__':
    main()
#!/usr/bin/env python

import urllib.request as ur
import sys, json, codecs, ssl

sys.tracebacklimit=0 # Make the errors a bit clearer for those that don't Python
ssl._create_default_https_context = ssl._create_unverified_context # Ignore Cert errors

file = open('/etc/zabbix/papercut.conf', 'r')

protocol = 'https' # Set default protocol to HTTPS

for line in file.readlines():
    (key, sep, value) = line.partition('=')
    if key == 'papercut_ip':
        serverip = value[1:-2]
    if key == 'papercut_auth':
        serverauth = value[1:-2]
    if key == 'https':
        useHTTPS = value[0:]

if useHTTPS != 'true':
  print ( 'using http')
  protocol = 'http'


r = { "data": [] }
domains = []

url='{0}://{1}/api/health/devices?{2}'.format(protocol,serverip,serverauth)
print ( url )
response = ur.urlopen(url)
reader = codecs.getreader("utf-8")
json_input = json.load(reader(response))


def main():
  if len(sys.argv)<2:
    print ("Run as:\n{0} [devicename]".format(sys.argv[0]))

  else:
    devicename = sys.argv[1]

    try:
        var = [ i["state"]["status"] for i in json_input['devices'] if i["name"] == devicename ]
        if var == [u'OK']:
          print(1)
        else:
          print(0)

    except (ValueError, KeyError, TypeError):
        print("JSON format error")
        print(json.dumps(r, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()

import M2Crypto
import sys, ssl, datetime

def printlog(host, message):
  now = datetime.datetime.now()
  datestr = now.strftime("%Y-%m-%d %H:%M:%S")
  print '%s|server=\'%s\'|ssl_expires=\'%s\'' % (datestr, host, message)

if len(sys.argv) != 3:
  printlog('', 'no host or port specified.')
  sys.exit(1)
else:
  srvr = sys.argv[1]
  port = sys.argv[2]

host = srvr+':'+str(port)
try:
  cert = ssl.get_server_certificate((srvr, int(port)))
  x509 = M2Crypto.X509.load_cert_string(cert)
  printlog(host, str(x509.get_not_after()))
except Exception as e:
  printlog(host, str(e))

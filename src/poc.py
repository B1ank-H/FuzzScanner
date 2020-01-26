dna = '''
360 | headers | wangzhan
360 | url | / wzws - waf - cgi / | 360wzws
Airlock | headers | \AAL[_-]?(SESS|LB)=
Anquanbao | headers | MISS
Anquanbao | url | / aqb_cc / error / 
Armor | url | This request has been blocked by website protection from Armor
Aws | headers | \bAWS
Baidu | headers | fhl
BaiduYunjiasu | headers | yunjiasu - nginx
Barracuda | headers | \Abarra_counter_session=
Barracuda | headers | (\A|\b)barracuda_
BigIP | headers | BIGipServer
BigIP | headers | BigIP | BIGipServer
BinarySEC | headers | fill | miss
BinarySEC | headers | binarysec
BlockDoS | headers | BlockDos\.net
CloudFlare | headers | cloudflare - nginx
Cloudfront | headers | cloudfront
Ciscoacexml | headers | ACE XML Gateway
Comodo | headers | Protected by COMODO
IBM - DataPower | headers |\A(OK | FAIL)
DenyAll | headers | \Asessioncookie =
Incapsula | headers | Incapsula
Jiasule | headers | jsluid =
Edgecast | headers | \AECDF
Expressionengine | url | Invalid GET Data
Fortiweb | headers | \AFORTIWAFSID=
KSYUN | headers | KSYUN ELB
KONA | headers | AkamaiGHost
Hyperguard | headers | \AODSESSION=
ModSecurity | headers | Mod_Security | NOYB
NetContinuum | headers |\Aclose
NetContinuum | headers |\Aclose
NetContinuum | headers | citrix_ns_id
Newdefend | headers | newdefend
NSFOCUS | headers | NSFocus
Safe3 | headers | Safe3WAF
Safe3 | headers | Safe3 Web Firewall
secureiis | url | SecureIIS[^<]+Web Server Protection
secureiis | url | \?subject=[^>]*SecureIIS Error
secureiis | url | http://www.eeye.com/SecureIIS/
Sophos | url | Powered by UTM Web Protection
Safedog | headers | WAF / 2\.0
Safedog | headers | Safedog
Safedog | headers | safedog
Senginx  | url | SENGINX-ROBOT-MITIGATION
Sitelock | url | SiteLock Incident ID
SonicWALL | headers | SonicWALL
SonicWALL | url | This request is blocked by the SonicWALL
SonicWALL | url | Web Site Blocked.+\bnsa_banner
Stingray | headers |\AX - Mapping -
Sucuri | headers | Sucuri / Cloudproxy
Usp - Sec | headers | Secure Entry Server
Varnish | headers | varnish
Wallarm | headers | nginx - wallarm
WebKnight | headers | WebKnight
Yundun | headers | YUNDUN
Yundun | headers | YUNDUN
Yunsuo | headers | yunsuo
Urlscan | headers | Rejected-By-UrlScan
Trafficshield | headers | F5-TrafficShield
Trafficshield | headers | \AASINFO=
Teros | headers | \Ast8(id|_wat|_wlf)
Tencent | url | waf.tencent-cloud.com
Sucuri | url | Sucuri WebSite Firewall - CloudProxy - Access Denied
Requestvalidationmode | url | ASP.NET has detected data in the request that is potentially dangerous
Requestvalidationmode | url | Request Validation has detected a potentially dangerous client input valu
Radware | url | Unauthorized Activity Has Been Detected.+Case Number:
Profense | headers | \APLBSID=
Profense | headers | Profense
Incapsula | headers | incap_ses|visid_incap
Incapsula | headers | Incapsula
Incapsula | url | Incapsula incident ID
Isaserver | url | The server denied the specified Uniform Resource Locator (URL). Contact the server administrator.
Isaserver | url | The ISA Server denied the specified Uniform Resource Locator (URL)
'''
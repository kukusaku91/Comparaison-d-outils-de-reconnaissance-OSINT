import time
from OSINT_tools.whois_lookup import get_whois_info
from OSINT_tools.dns_resolver import resolve_dns
from OSINT_tools.email_hunter import find_emails

def compare_osint_tools(domain, api_key):
    start_time = time.time()
    whois_info = get_whois_info(domain)
    whois_time = time.time() - start_time
    
    start_time = time.time()
    dns_info = resolve_dns(domain)
    dns_time = time.time() - start_time
    
    start_time = time.time()
    emails = find_emails(domain, api_key)
    email_time = time.time() - start_time
    
    return {
        "domain": domain,
        "whois_info": whois_info,
        "dns_info": dns_info,
        "emails": emails,
        "whois_time": whois_time,
        "dns_time": dns_time,
        "email_time": email_time
    }




if __name__ == "__main__":
    api_key = "4877081247da0f62e5019f9fb24fa64ac82b0c99"
    domain = "wordpress.org"
    results = compare_osint_tools(domain, api_key)
    print(results)
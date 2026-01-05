import dns.resolver
def resolve_dns(domain):
    records = {}
    for qtype in ['A', 'MX', 'NS', 'TXT']:
        try:
            answers = dns.resolver.resolve(domain, qtype)
            records[qtype] = [str(rdata) for rdata in answers]
        except:
            records[qtype] = []
    return records

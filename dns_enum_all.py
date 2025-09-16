import dns.resolver
import dns.query
import dns.zone
import dns.reversename

def dns_lookup(domain):
    try:
        answers = dns.resolver.resolve(domain, 'A')
        for rdata in answers:
            print(f"A record: {domain} -> {rdata.address}")
    except Exception as e:
        print(f"A record lookup error: {e}")

def get_ns_record(domain):
    try:
        answers = dns.resolver.resolve(domain, 'NS')
        ns_list = []
        for rdata in answers:
            ns = rdata.target.to_text()
            ns_list.append(ns)
            print(f"NS record: {ns}")
        return ns_list
    except Exception as e:
        print(f"NS record lookup error: {e}")
        return []

def get_mx_record(domain):
    try:
        answers = dns.resolver.resolve(domain, 'MX')
        for rdata in answers:
            print(f"MX record: preference={rdata.preference}, exchanger={rdata.exchange}")
    except Exception as e:
        print(f"MX record lookup error: {e}")

def get_txt_record(domain):
    try:
        answers = dns.resolver.resolve(domain, 'TXT')
        for rdata in answers:
            for txt_string in rdata.strings:
                print(f"TXT record: {txt_string.decode()}")
    except Exception as e:
        print(f"TXT record lookup error: {e}")

def get_spf_record(domain):
    try:
        answers = dns.resolver.resolve(domain, 'TXT')
        for rdata in answers:
            for txt_string in rdata.strings:
                txt_decoded = txt_string.decode()
                if txt_decoded.startswith('v=spf1'):
                    print(f"SPF record: {txt_decoded}")
    except Exception as e:
        print(f"SPF record lookup error: {e}")

def zone_transfer(domain, ns):
    try:
        print(f"Trying zone transfer on {ns} for domain {domain}")
        zone = dns.zone.from_xfr(dns.query.xfr(ns, domain))
        if zone is None:
            print("Zone transfer failed or no data.")
            return
        for name, node in zone.nodes.items():
            print(name.to_text())
    except Exception as e:
        print(f"Zone transfer failed: {e}")

def subdomain_enum(domain, wordlist):
    resolver = dns.resolver.Resolver()
    print("Starting subdomain enumeration...")
    with open(wordlist, 'r') as f:
        for sub in f:
            sub = sub.strip()
            try:
                full_domain = f"{sub}.{domain}"
                answers = resolver.resolve(full_domain, 'A')
                for rdata in answers:
                    print(f"Subdomain found: {full_domain} -> {rdata.address}")
            except:
                pass

if __name__ == "__main__":
    domain = input("Enter domain: ")
    wordlist = input("Enter subdomain wordlist file path: ")

    dns_lookup(domain)
    ns_list = get_ns_record(domain)
    get_mx_record(domain)
    get_txt_record(domain)
    get_spf_record(domain)

    for ns in ns_list:
        zone_transfer(domain, ns)

    subdomain_enum(domain, wordlist)

import dns.resolver

def dns_lookup(domain):
    try:
        answers = dns.resolver.resolve(domain, 'A')
        for rdata in answers:
            print(f"{domain} has address {rdata.address}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    domain = input("Enter domain: ")
    dns_lookup(domain)

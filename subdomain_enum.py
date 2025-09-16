import dns.resolver

def subdomain_enum(domain, wordlist):
    resolver = dns.resolver.Resolver()
    with open(wordlist, 'r') as f:
        for sub in f:
            sub = sub.strip()
            try:
                full_domain = f"{sub}.{domain}"
                answers = resolver.resolve(full_domain, 'A')
                for rdata in answers:
                    print(f"{full_domain} -> {rdata.address}")
            except:
                pass

if __name__ == "__main__":
    domain = input("Enter domain: ")
    wordlist = input("Enter wordlist file path: ")
    subdomain_enum(domain, wordlist)

import dns.resolver

def dns_bruteforce(domain, wordlist):
    resolver = dns.resolver.Resolver()
    with open(wordlist, 'r') as f:
        for sub in f:
            sub = sub.strip()
            try:
                full_domain = f"{sub}.{domain}"
                answers = resolver.resolve(full_domain, 'A')
                for rdata in answers:
                    print(f"{full_domain} -> {rdata.address}")
            except dns.resolver.NXDOMAIN:
                pass
            except dns.resolver.NoAnswer:
                pass
            except Exception as e:
                print(f"Error resolving {full_domain}: {e}")

if __name__ == "__main__":
    domain = input("Enter domain: ")
    wordlist = input("Enter wordlist file path: ")
    dns_bruteforce(domain, wordlist)

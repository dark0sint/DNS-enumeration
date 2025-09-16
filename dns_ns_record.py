import dns.resolver

def get_ns_record(domain):
    try:
        answers = dns.resolver.resolve(domain, 'NS')
        for rdata in answers:
            print(f"Name server: {rdata.target}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    domain = input("Enter domain: ")
    get_ns_record(domain)

import dns.resolver

def get_mx_record(domain):
    try:
        answers = dns.resolver.resolve(domain, 'MX')
        for rdata in answers:
            print(f"MX preference = {rdata.preference}, mail exchanger = {rdata.exchange}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    domain = input("Enter domain: ")
    get_mx_record(domain)

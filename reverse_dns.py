import dns.reversename
import dns.resolver

def reverse_dns(ip):
    try:
        rev_name = dns.reversename.from_address(ip)
        answers = dns.resolver.resolve(rev_name, "PTR")
        for rdata in answers:
            print(f"{ip} resolves to {rdata.target}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    ip = input("Enter IP address: ")
    reverse_dns(ip)

import dns.query
import dns.zone

def zone_transfer(domain, ns):
    try:
        zone = dns.zone.from_xfr(dns.query.xfr(ns, domain))
        if zone is None:
            print("Zone transfer failed or no data.")
            return
        for name, node in zone.nodes.items():
            print(name.to_text())
    except Exception as e:
        print(f"Zone transfer failed: {e}")

if __name__ == "__main__":
    domain = input("Enter domain: ")
    ns = input("Enter nameserver IP: ")
    zone_transfer(domain, ns)

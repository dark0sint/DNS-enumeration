import dns.resolver

def get_spf_record(domain):
    try:
        answers = dns.resolver.resolve(domain, 'TXT')
        for rdata in answers:
            for txt_string in rdata.strings:
                txt_decoded = txt_string.decode()
                if txt_decoded.startswith('v=spf1'):
                    print(f"SPF record for {domain}: {txt_decoded}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    domain = input("Enter domain: ")
    get_spf_record(domain)

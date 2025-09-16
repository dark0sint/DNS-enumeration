import dns.resolver

def get_txt_record(domain):
    try:
        answers = dns.resolver.resolve(domain, 'TXT')
        for rdata in answers:
            for txt_string in rdata.strings:
                print(f"TXT record: {txt_string.decode()}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    domain = input("Enter domain: ")
    get_txt_record(domain)

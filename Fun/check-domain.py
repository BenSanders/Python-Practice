import subprocess


def check_domain_ownership(domain):
    tlds = [".com", ".net", ".tv", ".info"]  # Add more TLDs as needed
    for tld in tlds:
        full_domain = domain + tld
        whois_command = f"whois {full_domain}"
        try:
            output = subprocess.check_output(whois_command, shell=True, encoding="utf-8")
        except subprocess.CalledProcessError:
            return tld[1:]  # TLD is available

        if "No match" in output:
            return tld[1:]  # TLD is available

    return None  # No available TLD found


# Specify the domain to check
domain = "jastas"

# Check domain ownership
available_tld = check_domain_ownership(domain)

if available_tld:
    print(f"The domain {domain}.{available_tld} is available.")
else:
    print(f"No available TLD found for the domain {domain}.")

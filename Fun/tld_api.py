import requests
from bs4 import BeautifulSoup

def get_available_tlds():
    url = "https://www.iana.org/domains/root/db"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    tld_table = soup.find("table", class_="table table-bordered")
    tld_rows = tld_table.find_all("tr")

    available_tlds = []
    for row in tld_rows[1:]:
        tld_data = row.find_all("td")
        tld = tld_data[0].text.strip()
        status = tld_data[3].text.strip()
        if status == "Delegated":
            available_tlds.append(tld)

    return available_tlds

# Example usage
available_tlds = get_available_tlds()
print(available_tlds)

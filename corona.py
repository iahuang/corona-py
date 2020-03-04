import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass


def extract_text(td):
    return td.get_text().strip()


def extract_country(td):
    return td.get_text().strip().lower().replace('.', '').replace(' ', '_').replace(':', '')


def extract_int(td):
    text = td.get_text().strip().replace(',', '')
    return int(text) if text else 0


@dataclass
class RecentCountryData:
    deaths: int
    infected: int


@dataclass
class CountryData:
    country: str
    total_cases: int
    infected: int
    deaths: int
    recovered: int
    critical_cases: int
    recent: RecentCountryData


class CountryNotFoundException(Exception):
    pass


class DiseaseData:
    def __init__(self):
        self.data = {}

    def get_country(self, cname):
        data = self.data.get(cname)
        if not data:
            raise CountryNotFoundException()
        return data

    @property
    def infected_countries(self):
        return list(self.data.keys())


def fetch_global_data():
    disease_data = DiseaseData()
    r = requests.get("https://www.worldometers.info/coronavirus/#countries")
    soup = BeautifulSoup(r.text, "html.parser")
    table_rows = soup.find_all("tr")
    for row in table_rows:
        cols = list(row.find_all("td"))
        if not cols:
            continue

        country = extract_country(cols[0])
        disease_data.data[country] = CountryData(
            country,
            extract_int(cols[1]),
            extract_int(cols[5]),
            extract_int(cols[3]),
            extract_int(cols[6]),
            extract_int(cols[7]),
            RecentCountryData(
                extract_int(cols[2]),
                extract_int(cols[4])
            )
        )

    world = DiseaseData.get_country(disease_data, "total")
    world.country = "world"

    disease_data.world = world
    return disease_data


if __name__ == "__main__":
    for c in fetch_global_data().infected_countries:
        print(c)
    print(fetch_global_data().world.infected,
          "people around the world are currently infected with COVID-19")

import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass
from termcolor import colored


def extract_text(td):
    return td.get_text().strip()


def extract_country(td):
    return td.get_text().strip().lower().replace('.', '').replace(' ', '_').replace(':', '')


def extract_int(td):
    text = td.get_text().strip().replace(',', '')
    return int(text) if text else 0


def extract_flt(td):
    text = td.get_text().strip().replace(',', '')
    return float(text) if text else 0.0


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
    per_mil: int
    recent: RecentCountryData

    def death_rate(self):
        return self.deaths/self.total_cases

    def recovery_rate(self):
        return self.recovered/self.total_cases

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
    table_rows = soup.find(id='nav-today').find_all("tr")
    for row in table_rows:
        cols = list(row.find_all("td"))
        if not cols:
            continue

        country = extract_country(cols[0])
        disease_data.data[country] = CountryData(
            country=country,
            total_cases=extract_int(cols[1]),
            infected=extract_int(cols[6]),
            deaths=extract_int(cols[3]),
            recovered=extract_int(cols[5]),
            critical_cases=extract_int(cols[7]),
            per_mil=extract_flt(cols[8]),
            recent=RecentCountryData(
                deaths=extract_int(cols[2]),
                infected=extract_int(cols[4])
            )
        )

    world = DiseaseData.get_country(disease_data, "total")
    world.country = "world"

    disease_data.world = world
    return disease_data


if __name__ == "__main__":
    data = fetch_global_data()
    print(colored(data.world.infected, 'yellow'),
          "people around the world are currently infected with COVID-19")
    print("\tand")
    print(colored(data.world.deaths, 'red'),
          "have died")
    print(colored(data.get_country('usa').death_rate()*100, 'cyan'),
          "percent that have contracted the disease in the US have died")
    print(colored(data.get_country('usa').recovery_rate()*100, 'cyan'),
          "percent that have contracted the disease in the US have recovered")

# corona.py

> Wow I really want to write a Python script that tells me how many people have died of COVID-19

- nobody ever

## How to Use

Throw the file into your project directory and install the dependencies. I'm not putting this up on PiPy because I'm lazy.

### Dependencies

This project requires BeautifulSoup 4 (an HTML parsing library) and `requests`. You can install both using the commands below

```bash
$ pip install beautifulsoup4
$ pip install requests
```

### Quick example

```python
import corona # ...into your country

world_data = corona.fetch_world_data()
ded = world_data.get_country('usa').deaths
print("oh no", ded, "people have died in the us. tragic")
```

## Documentation

### `corona.fetch_world_data()`

Returns a `DiseaseData` object

### `DiseaseData`

Properties:

- `infected_countries`: a list of infected countries by country code

Methods:

- `get_country(country_code: str)`

Returns a `CountryData` object.
For a list of country codes, refer to `DiseaseData.infected_countries`

### `CountryData`

Properties:

- `country`
- `total_cases`
- `infected`
- `deaths`
- `recovered`
- `critical_cases`
- `recent`
  - `.infected`
  - `.deaths`

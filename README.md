# corona.py

> Wow I really want to write a Python script that tells me how many people have died of COVID-19

*– nobody ever*

## How to Use

Throw the file into your project directory and install the dependencies. I'm not putting this up on PiPy because I'm lazy.

### Dependencies

This project requires BeautifulSoup 4 (an HTML parsing library) and `requests`. You can install both using the commands below

```bash
$ pip install beautifulsoup4
$ pip install requests
```

### Examples

```python
import corona # ...into your country

world_data = corona.fetch_world_data()
ded = world_data.get_country('usa').deaths
print("oh no", ded, "people have died in the US very sad")
```

```python
import corona
print(corona.fetch_global_data().world.infected, "people around the world are currently infected with COVID-19")
```

## Documentation

### `corona.fetch_world_data()`

Returns a `DiseaseData` object

### `DiseaseData`

Properties:

- `infected_countries`: a list of infected countries by country code
- `world`: a `CountryData` object that represents the world cumulatively

Methods:

- `get_country(country_code: str)`

Returns a `CountryData` object.

The country code is usually just the name of the country, but lowercase and underscored. For a list of country codes refer to the list below:

```python
china # mainland
s_korea
italy
iran
diamond_princess # A British cruise ship that contracted the virus
japan
france
germany
spain
usa
singapore
hong_kong
switzerland
kuwait
uk
bahrain
thailand
australia
taiwan
malaysia
canada
norway
iraq
sweden
uae # United Arab Emirates
austria
netherlands
india
vietnam
belgium
israel
iceland
lebanon
oman
san_marino
macao
denmark
croatia
algeria
qatar
ecuador
finland
greece
mexico
czechia
pakistan
belarus
portugal
romania
philippines
azerbaijan
georgia
russia
brazil
egypt
estonia
indonesia
ireland
new_zealand
senegal
afghanistan
andorra
armenia
cambodia
dominican_republic
jordan
latvia
lithuania
luxembourg
north_macedonia
monaco
morocco
nepal
nigeria
saudi_arabia
sri_lanka
tunisia
ukraine
argentina
chile
liechtenstein
```

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

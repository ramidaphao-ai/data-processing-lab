import csv
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        r['latitude'] = float(r['latitude'])
        r['longitude'] = float(r['longitude'])
        r['temperature'] = float(r['temperature'])
        cities.append(dict(r))
        
def filter_items(condition, dict_list):
    """
    Return a new list containing only the dictionaries that satisfy
    the given condition function.

    Args:
        condition: A function that takes a dictionary and returns True or False.
        dict_list: A list of dictionaries.

    Returns:
        A list of dictionaries for which condition(item) is True.
    """
    return [item for item in dict_list if condition(item)]


def aggregate(aggregation_key, aggregation_function, dict_list):
    """
    Aggregate values associated with aggregation_key using the
    provided aggregation function.

    Args:
        aggregation_key: The dictionary key whose values should be aggregated.
        aggregation_function: A function such as sum, max, min, etc.

    Returns:
        The aggregated result.
    """
    values = [item[aggregation_key] for item in dict_list]
    return aggregation_function(values)


# Print the average temperature of all the cities
print(
    aggregate(
        "temperature",
        lambda temperatures: sum(temperatures) / len(temperatures),
        cities
    )
)


# Print all cities in Germany
print(
    filter_items(
        lambda item: item["country"] == "Germany",
        cities
    )
)


# Print all cities in Spain with a temperature above 12°C
print(
    filter_items(
        lambda item: item["country"] == "Spain" and item["temperature"] > 12,
        cities
    )
)


# Count the number of unique countries
print(
    len(set(item["country"] for item in cities))
)


# Print the average temperature for all the cities in Germany
germany_cities = filter_items(
    lambda item: item["country"] == "Germany",
    cities
)

print(
    aggregate(
        "temperature",
        lambda temperatures: sum(temperatures) / len(temperatures),
        germany_cities
    )
)


# Print the max temperature for all the cities in Italy
italy_cities = filter_items(
    lambda item: item["country"] == "Italy",
    cities
)

print(
    aggregate(
        "temperature",
        max,
        italy_cities
    )
)

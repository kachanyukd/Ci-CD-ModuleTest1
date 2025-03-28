def read_and_sort_population_data(file_name):
    countries = []

    with open(file_name, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 3:
                name = parts[0].strip()
                area = float(parts[1].strip())
                population = int(parts[2].strip())
                countries.append((name, area, population))

    # Sorting by area
    sorted_by_area = sorted(countries, key=lambda x: x[1])

    # Sorting by population
    sorted_by_population = sorted(countries, key=lambda x: x[2])

    return sorted_by_area, sorted_by_population

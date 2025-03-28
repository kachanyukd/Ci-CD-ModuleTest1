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

    return countries
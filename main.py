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

    sorted_by_area = sorted(countries, key=lambda x: x[1])

    sorted_by_population = sorted(countries, key=lambda x: x[2])

    return sorted_by_area, sorted_by_population

def print_sorted_data(sorted_by_area, sorted_by_population):
    print("Сортування за площею:")
    for country in sorted_by_area:
        print(f"{country[0]}: Площа = {country[1]} кв. км, Населення = {country[2]} осіб")

    print("\nСортування за населенням:")
    for country in sorted_by_population:
        print(f"{country[0]}: Площа = {country[1]} кв. км, Населення = {country[2]} осіб")

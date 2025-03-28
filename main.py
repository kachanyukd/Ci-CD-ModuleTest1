import unittest

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
    data = []
    data.append("Сортування за площею:")
    for country in sorted_by_area:
        data.append(f"{country[0]}: Площа = {int(country[1])} кв. км, Населення = {country[2]} осіб")
    
    data.append("\nСортування за населенням:")
    for country in sorted_by_population:
        data.append(f"{country[0]}: Площа = {int(country[1])} кв. км, Населення = {country[2]} осіб")
    
    return "\n".join(data)



class TestPopulationData(unittest.TestCase):

    def test_read_and_sort_population_data(self):
        test_data = "Ukraine, 603628, 41052600\nUSA, 9833517, 331000000\nChina, 9596961, 1402112000"
        
        with open('test_population.txt', 'w') as f:
            f.write(test_data)
        
        sorted_by_area, sorted_by_population = read_and_sort_population_data('test_population.txt')
        
        self.assertEqual(sorted_by_area[0][0], 'Ukraine')
        self.assertEqual(sorted_by_area[-1][0], 'USA')
        
        self.assertEqual(sorted_by_population[0][0], 'Ukraine')
        self.assertEqual(sorted_by_population[-1][0], 'China')

    def test_print_sorted_data(self):
        sorted_by_area = [("Ukraine", 603628, 41052600), ("USA", 9833517, 331000000)]
        sorted_by_population = [("China", 9596961, 1402112000), ("USA", 9833517, 331000000)]
        
        expected_output = """Сортування за площею:
Ukraine: Площа = 603628.0 кв. км, Населення = 41052600 осіб
USA: Площа = 9833517.0 кв. км, Населення = 331000000 осіб

Сортування за населенням:
USA: Площа = 9833517.0 кв. км, Населення = 331000000 осіб
China: Площа = 9596961.0 кв. км, Населення = 1402112000 осіб"""

        
        self.assertEqual(print_sorted_data(sorted_by_area, sorted_by_population), expected_output)

if __name__ == '__main__':
    unittest.main()
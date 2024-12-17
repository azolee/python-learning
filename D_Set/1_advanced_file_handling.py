from Helpers.data_handling import print_list_of_persons, generate_fake_persons_data, calculate_statistics
from Helpers.Writer.writer import Writer
from Helpers.Writer.json_writer_strategy import JSONWriterStrategy
from Helpers.Writer.csv_writer_strategy import CSVWriterStrategy
import os
import rich

os.makedirs('./data', exist_ok=True)

while True:
    try:
        writer = Writer(JSONWriterStrategy())
        default_value = 10000000
        user_input = input(f"Enter the number of persons (default is {default_value}) or 'exit': ") or default_value

        if user_input.lower() == "exit":
            break

        number = int(user_input)
        persons = list(generate_fake_persons_data(number))
        statistics = calculate_statistics(persons)

        writer.write(f'./data/statistics.json', [statistics])
        writer.write(f'./data/persons.json', persons)
        writer.set_strategy(CSVWriterStrategy())
        writer.write(f'./data/persons.csv', persons)

        print(f"Printed {number} persons to JSON and CSV.")

        print_list_of_persons(
            persons=list(persons),
            name_of_list=f"The list of persons ({number})"
        )

        print(f"Printed {number} persons. Here are some statistics:")
        rich.print(statistics)

    except ValueError:
        print("Invalid input. Please enter a number.")
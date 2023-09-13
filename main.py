# from faker import Faker
import faker_module
import json

# initialize faker generator
# fake = Faker()

table_name = input("Enter the table name: ")
table_range = input("Enter the table range: ")

func = getattr(faker_module, table_name)
get_data = func(int(table_range))

with open("data.json", "w") as outfile:
    json.dump(get_data, outfile)


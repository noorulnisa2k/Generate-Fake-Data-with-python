import faker_module
import json
import os

# access all function that are created to generate data
print("Available tables to generate data:")
func_list=['DynamicProvider','Faker','fake','lyftrondata_provider']
attributes = [attr for attr in dir(faker_module) 
              if not attr.startswith('__') and attr not in func_list]
for attribute in attributes:
    print(attribute)

#######################################################################

table_name = input("Enter table name: ")

if table_name in attributes:
    table_range = input("Enter Number of Records: ")

    # Fetching table
    func = getattr(faker_module, table_name)
    get_data = func(int(table_range))

    # Data will be added in a json file
    with open("data.json", "w") as outfile:
        json.dump({f"{table_name}":get_data}, outfile)
else:
    os.remove("data.json")
    print("Table you entered does not exist")

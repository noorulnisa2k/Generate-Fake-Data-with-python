from faker import Faker
import json

# initialize faker generator
fake = Faker()

dict={
    "customer":[],
    "product":[],
    "employee":[]
}
table_name = input("Enter the table name: ")
table_range = input("Enter the table range: ")

for x in range(int(table_range)):
    customer={
    "name":fake.name(),
    "country":fake.country()
    }
    product={
        "product_code":fake.random_number(),
        "p_name":fake.name()
    }
    employee={
        'id':fake.random_number(),
        'name':fake.name()
    }
    dict['customer'].append(customer)
    dict['product'].append(product)
    dict['employee'].append(employee)

# with open("data.json", "w") as outfile:
#     json.dump(dict, outfile)

# with open('data.json','r') as json_File :
#     data=json.load(json_File)

# print(data)
for i in dict[table_name]:
    print(i)
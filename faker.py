from faker import Faker
import json

# initialize faker generator
fake = Faker()

# initialize with localization (multible localization allowed)
# fake = Faker(['en_IN','jp_JP'])

for _ in range(10):
    # print(fake.name())
    print(fake.bothify(text='##_Lyftrondata_?????', letters='ABCDXYZ'))


# Generate-Fake-Data-with-python

install library
```bash
  pip install Faker
```

initialize faker generator
```bash
  fake = Faker()
```

initialize with localization (multiple localization allowed) 
```bash
  fake = Faker(['en_IN','jp_JP'])
```
To Print all available faker modules
```bash
  faker_dir = dir(fake)

  with open('all_faker_modules.json','w') as json_File :
	  json.dump(faker_dir, json_File)
```

Faker module Example:
```bash
  for _ in range(10):
    print(fake.name())
    print(fake.bothify(text='##_Lyftrondata_?????', letters='ABCDXYZ'))
```

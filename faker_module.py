from faker import Faker
from faker.providers import DynamicProvider

# Custom list for products
lyftrondata_provider = DynamicProvider(
    provider_name="product_names",
    elements=['Shirts','Jeans', 'Top','Cap','Formal Dress','Casual dress']
)

# initialize Faker generator
fake = Faker(["en_US"])
# add custom provider to in faker generator
fake.add_provider(lyftrondata_provider)

# Function that will generate specific fake data
def customer(number):
    fetchedData = {
        "customer": []
    }
    for x in range(number):
        customer = {
            "id": fake.unique.random_int(),
            "customer_name": fake.name(),
            "new_customer":fake.boolean(),
            "phone_number": fake.phone_number(),
            "country": fake.country(),
            "customer_feedback":fake.sentence()
        }
        fetchedData['customer'].append(customer)
    return fetchedData["customer"]


def product(number):
    fetchedData = {
        "product": []
    }
    for x in range(number):
        product = {
            "id": fake.unique.random_int(),
            "product_code": fake.bothify(text='###_Lyftrondata_?????', letters='ABCDXYZ'),
            "product_name": fake.product_names(),
            "product_color": fake.color_name(),
            "in_stock":fake.boolean(),
            "no_of_products":fake.random_digit_above_two(),
            "image_url":fake.image_url()
        }
        fetchedData['product'].append(product)
    return fetchedData["product"]


def cart(number):
    fetchedData = {
        "cart": []
    }
    for x in range(number):
        cart = {
            "product_id": fake.unique.random_int(),
            "product_name": fake.product_names(),
            "country": fake.country(),
            "address": fake.address(),
            "order_data": fake.date(),
            "credit_card_number": fake.credit_card_number(),
            "total_amount":f"{fake.random_int()}{fake.currency_symbol()}"

        }
        fetchedData['cart'].append(cart)
    return fetchedData["cart"]


def transaction(number):
    fetchedData = {
        "transaction": []
    }
    for x in range(number):
        transaction = {
            "id": fake.unique.random_int(),
            "aba_transit": fake.aba(),
            "iban":fake.iban(),
            "bank_country": fake.bank_country(),
        }
        fetchedData['transaction'].append(transaction)
    return fetchedData["transaction"]

def credit_card(number):
    fetchedData = {
        "credit_card": []
    }
    for x in range(number):
        credit_card = {
            "id": fake.unique.random_int(),
            "credit_card_full_detial": fake.credit_card_full(),
            "credit_card_provider": fake.credit_card_provider(),
            "credit_card_number": fake.credit_card_number(card_type='maestro'),
            "credit_card_cvc": fake.credit_card_security_code(),
            "credit_card_expiry_date":fake.credit_card_expire(),
        }
        fetchedData['credit_card'].append(credit_card)
    return fetchedData["credit_card"]

def user(number):
    fetchedData = {
        "user": []
    }
    for x in range(number):
        user = {
            "id": fake.unique.random_int(),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "phone_number": fake.phone_number(),
            "country": fake.country(),
            "company": fake.company(),
            "company_email": fake.company_email(),
            "joinded_at": fake.date()
        }
        fetchedData['user'].append(user)
    return fetchedData["user"]


def account(number):
    fetchedData = {
        "account": []
    }
    for x in range(number):
        account = {
            "name": fake.name(),
            "country": fake.country()
        }
        fetchedData['account'].append(account)
    return fetchedData["account"]


def setting(number):
    fetchedData = {
        "setting": []
    }
    for x in range(number):
        setting = {
            "name": fake.name(),
            "country": fake.country()
        }
        fetchedData['setting'].append(setting)
    return fetchedData["setting"]


def module(number):
    fetchedData = {
        "module": []
    }
    for x in range(number):
        module = {
            "uuid": fake.uuid4(),
            "country": fake.country()
        }
        fetchedData['module'].append(module)
    return fetchedData["module"]


def organization(number):
    fetchedData = {
        "organization": []
    }
    for x in range(number):
        organization = {
            "name": fake.name(),
            "country": fake.country()
        }
        fetchedData['organization'].append(organization)
    return fetchedData["organization"]


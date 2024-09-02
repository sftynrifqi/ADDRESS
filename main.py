
import pandas as pd
from faker import Faker

# Initialize the Faker library
fake = Faker()

# Number of random addresses to generate
num_addresses = 20000

# Generate random addresses
addresses = []
for _ in range(num_addresses):
    address = {
        'Street Address': fake.street_address(),
        'City': fake.city(),
        'State': fake.state(),
        'Zip Code': fake.zipcode(),
        'Country': 'USA'
    }
    addresses.append(address)

# Create a DataFrame
df = pd.DataFrame(addresses)

# Save to an Excel file
df.to_excel('random_addresses.xlsx', index=False)

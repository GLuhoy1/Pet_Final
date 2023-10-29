import faker


def generate_random_user():
    fake = faker.Faker()
    fake_user_data = {
        'First Name': fake.first_name(),
        'Last Name': fake.last_name(),
        'E-Mail': fake.email(),
        'Telephone': fake.phone_number(),
        'Password': fake.password()
    }

    return fake_user_data


def random_product(test_pattern: str):
    fake = faker.Faker()

    product_name = 'AaA' + test_pattern + fake.text(max_nb_chars=10)
    meta_title = fake.sentence(nb_words=4)
    model = fake.bothify(text="??#??#")

    product_data_dict = {
        'product_name': product_name,
        'meta_title': meta_title,
        'model': model
    }

    return product_data_dict


if __name__ == "__main__":
    user_data = generate_random_user()
    product_data = random_product()

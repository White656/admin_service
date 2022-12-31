import random

from core.config import config

import uuid
from datetime import datetime
from faker import Faker

from example_usage.query.helper import get_query_from_file, variants
from example_usage.utils.uploader.postgres_upload import PostgresUploader


def generate_data_from_person_table(now) -> tuple:
    persons_id = [str(uuid.uuid4()) for _ in range(PERSONS_COUNT)]
    return [(pk, fake.last_name(), now, now) for pk in persons_id], persons_id


def generate_date_from_person_film_fork(now):
    cursor = uploader.get_cursor
    query = get_query_from_file(variant=variants.get_all_film_work)
    cursor.execute(query)
    roles = ['actor', 'producer', 'director']
    person_film_work_data = []
    film_works_ids = [database_date[0] for database_date in cursor.fetchall()]

    for film_work_id in film_works_ids:
        for person_id in random.sample(persons_ids, 5):
            role = random.choice(roles)
            person_film_work_data.append((str(uuid.uuid4()), film_work_id,
                                          person_id, role, now))
    return person_film_work_data


fake = Faker()

database_dns = config.database.json()

PERSONS_COUNT = config.persons_count
PAGE_SIZE = config.page_size
uploader = PostgresUploader(dns=config.database)
conn = uploader.get_connection
now = datetime.utcnow()

generated_date, persons_ids = generate_data_from_person_table(now)

query = get_query_from_file(variant=variants.into_person)
uploader.upload(query, generated_date, PAGE_SIZE)

person_film_work_data = generate_date_from_person_film_fork(now)
query = get_query_from_file(variant=variants.into_person_film_work)
uploader.upload(query, person_film_work_data, PAGE_SIZE)

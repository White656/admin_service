"""This file shows the usual use of the overload function."""
import random
import uuid
from datetime import datetime

from core.config import config
from faker import Faker

from upload_db.query.helper import get_query_from_file, variants
from upload_db.utils.uploader.postgres_upload import PostgresUploader


def generate_data_from_person_table() -> tuple[list[tuple], list]:
    """
    The function generates data for the table.

    :return: tuple[list[tuple[uuid, last_name, datetime, datetime]], list].
    """
    persons_id = [str(uuid.uuid4()) for _ in range(PERSONS_COUNT)]
    return [(pk, fake.last_name(), datetime.utcnow(), datetime.utcnow()) for pk in persons_id], persons_id


def generate_date_from_person_film_fork_table() -> list[tuple]:
    """
    The function generated data from database table personfilm work.

    :return: list[tuple]. Date from upload in database table or insert into sql query.
    """
    data_from_upload = []
    cursor = uploader.get_cursor
    query = get_query_from_file(variant=variants.get_all_film_work)
    cursor.execute(query)
    roles = ['actor', 'producer', 'director']
    film_works_ids = [database_date[0] for database_date in cursor.fetchall()]
    for film_work_id in film_works_ids:
        for person_id in random.sample(persons_ids, 5):
            role = random.choice(roles)
            data_from_upload.append((str(uuid.uuid4()), film_work_id, person_id, role, datetime.utcnow()))
    return data_from_upload


fake = Faker()

database_dns = config.database.json()

PERSONS_COUNT = config.persons_count
PAGE_SIZE = config.page_size

uploader = PostgresUploader(dns=config.database)
conn = uploader.get_connection

generated_date, persons_ids = generate_data_from_person_table()

query = get_query_from_file(variant=variants.into_person)
uploader.upload(query, generated_date, PAGE_SIZE)

person_film_work_data = generate_date_from_person_film_fork_table()

query = get_query_from_file(variant=variants.into_person_film_work)
uploader.upload(query, person_film_work_data, PAGE_SIZE)

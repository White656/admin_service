CREATE SCHEMA IF NOT EXISTS content;

CREATE TABLE IF NOT EXISTS content.film_work (
    id uuid PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    creation_date DATE,
    rating FLOAT NOT NULL,
    type TEXT not null,
    created timestamp with time zone,
    modified timestamp with time zone
);

CREATE TABLE IF NOT EXISTS content.genre (
    id uuid PRIMARY KEY,
    name varchar(128) NOT NULL,
    description TEXT,
    created timestamp with time zone,
    modified timestamp with time zone

);

CREATE TABLE IF NOT EXISTS content.person (
    id uuid PRIMARY KEY,
    full_name varchar(127) NOT NULL,
    created timestamp with time zone,
    modified timestamp with time zone
);

CREATE TABLE IF NOT EXISTS content.person_film_work (
    id uuid PRIMARY KEY,
    film_work_id uuid NOT NULL,
    person_id uuid NOT NULL,
    role varchar(127) NOT NULL,
    created timestamp with time zone
);

CREATE TABLE IF NOT EXISTS content.genre_film_work (
id uuid PRIMARY KEY,
genre_id uuid NOT NULL,
film_work_id uuid NOT NULL,
created timestamp with time zone
);



ALTER ROLE ALL SET search_path TO content,public;

CREATE INDEX IF NOT EXISTS film_work_index_id ON content.film_work(id);
CREATE UNIQUE INDEX film_work_person_idx ON content.person_film_work (film_work_id, person_id);

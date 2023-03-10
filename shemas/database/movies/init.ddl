CREATE SCHEMA IF NOT EXISTS content;

CREATE TABLE IF NOT EXISTS content.film_work (
    id uuid not null
		primary key,
	created_at timestamp with time zone not null,
	updated_at timestamp with time zone not null,
	title text not null,
	description text not null,
	creation_date timestamp with time zone not null,
	type varchar(300) not null,
	rating double precision not null,
	file_path varchar(256)
);

CREATE TABLE IF NOT EXISTS content.genre (
    id uuid PRIMARY KEY,
    name varchar(128) NOT NULL,
    description TEXT,
    created_at timestamp with time zone,
    updated_at timestamp with time zone

);

CREATE TABLE IF NOT EXISTS content.person (
    id uuid PRIMARY KEY,
    full_name varchar(127) NOT NULL,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
);

CREATE TABLE IF NOT EXISTS content.person_film_work (
    id uuid PRIMARY KEY,
    film_work_id uuid NOT NULL,
    person_id uuid NOT NULL,
    role varchar(127) NOT NULL,
    created_at timestamp with time zone
);

CREATE TABLE IF NOT EXISTS content.genre_film_work (
id uuid PRIMARY KEY,
genre_id uuid NOT NULL,
film_work_id uuid NOT NULL,
created_at timestamp with time zone
);



ALTER ROLE ALL SET search_path TO content,public;
--
-- CREATE INDEX IF NOT EXISTS film_work_index_id ON content.film_work(id);
-- CREATE UNIQUE INDEX film_work_person_idx ON content.person_film_work (film_work_id, person_id);

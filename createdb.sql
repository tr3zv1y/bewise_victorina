create table questions(
    sort_id serial unique not null,
    id int primary key,
    question text not null,
    answer varchar not null,
    created timestamp not null);
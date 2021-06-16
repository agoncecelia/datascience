create table users (
	user_id serial PRIMARY KEY,
	firstname varchar(50) not null,
	lastname varchar(50) not null,
	average decimal not null,
	created_at timestamp with time zone default current_timestamp
);

insert into users (firstname, lastname, average) values ('Agon', 'Cecelia
', 7.89);

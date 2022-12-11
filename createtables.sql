create database Harshal;
use harshal;

drop table ord;
drop table ownr;
drop table inventory;
drop table login;

create table login 
(
user_id char(5) not null, 
pwd char(10) not null, 
primary key (user_id)
);

create table inventory
(
rc char(20) not null, 
make varchar(20) not null,
model varchar(20) not null,
yr int(5) not null,
run int(10) not null,
colour varchar(25) not null,
fuel varchar(20) not null,
selling_price int(10) not null,
stat boolean,
primary key (rc)
);

create table ord
(
trno int (5) not null auto_increment,
rc char(20) not null,
amt_paid int (10) not null,
amt_pending int (10),
primary key (trno),
foreign key (rc) references inventory(rc)
);

create table ownr
(
contact_no char (20) not null,
rc char(20) not null,
owner_name varchar(25) not null,
owner_price int (10) not null,
primary key (contact_no),
foreign key (rc) references inventory(rc)
);

#delete from ord;
#delete from ownr;
#delete from inventory;
#delete from login;
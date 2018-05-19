drop database if exists contact_person;
create database contact_person default charset utf8;
use contact_person;
drop table if exists cp;
create table cp
(
pid int not null auto_increment, -- 联系人编号
pname varchar(10) not null, -- 名字
tel char(11) not null,  -- 电话
qq varchar(20) not null, -- qq
email varchar(20) not null, -- email
primary key (pid)
);

-- 录入联系人信息
insert into cp (pname, tel, qq, email) values
('王大锤', 13823456123, 2374511, '2374511@qq.com'),
('货松', 13823456124, 2374522, '2374522@qq.com'),
('陈晨', 13823456125, 2374533, '2374533@qq.com'),
('小强', 13823456126, 2374544, '2374544@qq.com'),
('大强', 13823456127, 2374555, '2374555@qq.com');
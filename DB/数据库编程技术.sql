CREATE TABLE table1 (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  birthday DATE,
  gender VARCHAR(10)
);

INSERT INTO table1 (id, name, birthday, gender) VALUES
(1, 'John', '1990-05-15', 'Male'),
(2, 'Jane', '1992-08-21', 'Female'),
(3, 'Bob', '1985-12-03', 'Male'),
(4, 'Alice', '1993-07-10', 'Female'),
(5, 'Mike', '1988-09-27', 'Male'),
(6, 'Sarah', '1991-04-08', 'Female');

-- 数据库编程技术
-- 1.1:变量 用户变量,系统变量，局部变量（作用范围 begin...end语句块中）
-- 只能定义在存储过程，存储函数，触发器中
set @deptno='hello mysql';
select @deptno;
declare sum int default 0;
-- 变量赋值
select id,name into @sid,@sname from tablename;

-- 1.2 系统内置函数和，其他函数
-- if(5>0,'是'，'否')返回结果 是;
-- ifnull(5,2)返回结果 5；

-- 1.3流程控制语句
-- 1.3.1
begin
   select * from tablename where id=1;
   select @sno='Mysql';
end;
-- 1.3.2修改Mysql结束标志 作用：连续执行多条sql语句
delimiter ##
-- 1.3.3分支语句
delimiter ##
begin
    declare sum int default 0;
    if sum<4 then
    select '1';
    else
    select 'over';
    end if;
end;
delimiter ;
-- 2
delimiter ##
begin
    declare sum varchar(10) default 'a';
    declare name varchar(10) default 'zs';
    case sum
        where 'a' then set name='hello'
        where 'b' then set name='over'
    end case;
end ##
delimiter ;
-- 1.3.4 循环语句
delimiter ##
begin
    declare n int default 0;
    declare sum int default 0;
    where n<=100 do
        set sum=n+sum;
        set n=n+1;
    end where;
end ##
delimiter ;
-- 2 repeat （先执行后判断）
delimiter ##
begin
    declare n int default 0;
    declare sum int default 0;
    repeat
        set sum=sum+n;
        set n=n+2;
    untll n>100
    end repeat;
  end ##
delimiter ;
-- 3 loop,执行语句退出循环,语句标号用户自定义
delimiter ##
   begin
   declare n,f int default 1;
   labell:loop
       set f=f*n;
       set n=n+1;
       if n>5 then
       leave labell;
       end if;
    end loop labell;
    end ##
delimiter ;
-- 1.3.5存储过程：数据库定义sql语句的集合
-- 参数：in输入参数,out输出参数,inout输入输出参数，输出参数：存储过程执行后将形参的结果传递给实参
delimiter ##
create procedure f_data(in sname char(50))
begin
select name, year(now())-year(birthday) as '年龄' from table1 where name=sname;
end ##
delimiter ;
-- 调用存储工程
call f_data('Bob');
select * from table1;











    






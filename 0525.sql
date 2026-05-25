SELECT
o.id as 'ID',
u.name as '購買人姓名'
p.name as '商品名稱'
o.quantity as '購買數量'
from orders as o
join users as u on o.user_id = u.id
join products as p on o.product_id = p.id


SELECT
p.name
from products as p a
left join orders as o on o.product_id = p.id and o.status not in ('CANCELLED')


SELECT
p.name, ifnull(sum(o.quantity),0) as `總銷售量`
from products as p
left join orders as o on o.product_id = p.id and o.status not in ('CANCELLED')
group by p.id, p.name
having 


select 
o.user_id,
sum(o.price_at_purchase) as '總金額' 
from order as o
where o.status in ('PAID','SHIPPED')
group by user_id
HAVING sum(o.price_at_purchase) > 50000
order by `總金額` desc

create view view_over_50000_spent_total
as
select 
o.user_id,
sum(o.price_at_purchase) as '總金額' 
from order as o
where o.status in ('PAID','SHIPPED')
group by user_id
HAVING sum(o.price_at_purchase) > 50000
order by `總金額` desc

select *,t2.name from  view_over_50000_spent_total as t1
join users as t2 on t1.user_id = t2.id


--錯誤示範
--會因為清單中提供了null，所以是空資料集回傳
select * from users id
where id not in (1, 3, null)


select * from user
where id not EXISTS(
    select 1 from vip_list as v where v.user_id = `users`.id
) 

select * from users
where id not in (
    select user_id from vip_list where user_id 
)


create darabase ADD
use XXXX
show DATABASE
show TABLESPACE

select * from table limit 5
select * from table limit 5 offset 10
group by 欄位





查資料過濾條件 用 WHERE

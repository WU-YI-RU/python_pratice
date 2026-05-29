use 0525_new

select * from employees


--1. 將員工工作年資分類成「新進」（< 2年）、「資深」（2-4年）與「專家」（>= 5年）

select *,
    CASE
        WHEN years_of_service <= 2 THEN '新進'
        WHEN years_of_service <= 4 THEN '資深'
        ELSE  '專家'
    END as '年資'
FROM employees

--2. 統計各部門的薪資等級分布（高薪 >= 60000，中薪 40000-59999，低薪 < 40000）

SELECT
department,
sum(case when '年資' == '資深')


--3. 寫一個 UPDATE 語句，將所有「新進」員工的薪水增加 8%

--改成CTE版本
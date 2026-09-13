# Write your MySQL query statement below
-- select student_id , student_name , subject_name , count()
select s.student_id,s.student_name,a.subject_name ,count(e.subject_name) as attended_exams 
from Students s 
cross join subjects a
left join Examinations e
on s.student_id = e.student_id and a.subject_name = e.subject_name
group by s.student_id,s.student_name,a.subject_name 
order by s.student_id , a.subject_name;


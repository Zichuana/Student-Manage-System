select 
app_stuinfo.id,
stuname, 
app_course.cno,
cname,
ccredit,
grade,
stumajor
from app_sc,app_stuinfo,
app_course where app_sc.scno_id=app_course.cno and
app_stuinfo.id=app_sc.sid_id


select * from app_sc

select 
app_stuinfo.id,
stuname, 
app_course.cno,
cname,
ccredit,
grade,
stumajor
from app_sc,app_stuinfo,app_course 
where app_sc.scno_id=app_course.cno and app_stuinfo.id=app_sc.sid_id and
 app_stuinfo.id='0002'


 select app_stuinfo.id, stuname,app_course.cno, cname,ccredit, grade
 from app_sc,app_stuinfo,app_course 
where app_sc.scno_id=app_course.cno and app_stuinfo.id=app_sc.sid_id and stumajor='ҽѧ��Ϣ����'


select * from app_stuinfo

select app_stuinfo.id, stuname,count(*) as �޿�����, sum(case when grade>=60 then 1 else 0 end) as ͨ������,
Convert(decimal(5,2), sum((case when grade>=60 then grade-50 else 0 end)*ccredit)*1.0/sum(ccredit)*0.1) as point 
from app_sc,app_stuinfo,app_course 
where app_sc.scno_id=app_course.cno and app_stuinfo.id=app_sc.sid_id and
 stumajor='ҽѧ��Ϣ����' 
 group by app_stuinfo.id, stuname order by Convert(decimal(5,2), sum((case when grade>=60 then grade-50 else 0 end)*ccredit)*1.0/sum(ccredit)*0.1) desc


select app_stuinfo.id, stuname, stucollege, stumajor, grade
from app_sc,app_stuinfo,app_course 
where app_sc.scno_id=app_course.cno and app_stuinfo.id=app_sc.sid_id and cname='���������' order by stucollege desc, stumajor  desc, grade desc



select top 1 percent app_stuinfo.id, stuname, grade
from app_sc,app_stuinfo,app_course 
where app_sc.scno_id=app_course.cno and app_stuinfo.id=app_sc.sid_id and cname='���������' and stumajor='ҽѧ��Ϣ����'
order by grade desc


select app_stuinfo.id, stuname,stumajor, stucollege,cname, grade
from app_sc,app_stuinfo,app_course 
where app_sc.scno_id=app_course.cno and app_stuinfo.id=app_sc.sid_id and grade<60
and cname='���������' 
and stumajor='ҽѧ��Ϣ����' 
and app_stuinfo.id = '0003'
and stucollege = '�Ź�Ժ'
order by 
stucollege, stumajor, app_course.cno,app_stuinfo.id, grade desc


select * from app_course
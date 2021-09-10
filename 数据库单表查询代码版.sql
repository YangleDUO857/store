SELECT *FROM t_dept WHERE deptno = '30';
SELECT ename ,empno,deptno FROM t_employees WHERE job = '经理';
SELECT *FROM t_employees WHERE 'comn'>'sal';
SELECT *FROM t_employees WHERE comm>(sal*0.6);
SELECT *FROM t_employees WHERE (deptno = 10 AND job = '经理') OR (deptno = 20 AND job = '分析员');
SELECT *FROM t_employees WHERE (deptno = 10 AND job = '经理') OR (deptno = 20 AND job = '分析员')   OR(job NOT IN('经理','武装上将') AND sal >= 3000);
SELECT DISTINCT job FROM t_employees WHERE comm IS NULL OR comm < 1000;
SELECT * FROM t_employees WHERE ename LIKE '___';
SELECT * FROM t_employees WHERE hiredate LIKE '2000%';
SELECT * FROM t_employees ORDER BY empno ASC;
SELECT * FROM t_employees ORDER BY sal DESC,hiredate ASC;

SELECT AVG(sal) FROM t_employees WHERE deptno = 10;
SELECT AVG(sal) FROM t_employees WHERE deptno = 20;
SELECT AVG(sal) FROM t_employees WHERE deptno = 30;
SELECT AVG(sal) FROM t_employees WHERE deptno = 40;

SELECT deptno,COUNT(1)FROM t_dept GROUP BY deptno;
SELECT job,MAX(sal),MIN(sal),COUNT(1)FROM t_employees GROUP BY job;
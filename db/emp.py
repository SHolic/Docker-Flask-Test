from db.mysql import Session
from sqlalchemy import text


def search_emp_list():
    session = Session()
    sql = '''
    SELECT e.empno, e.ename, e.job, d.dname
    FROM t_emp e JOIN t_dept d ON e.deptno=d.deptno
    '''
    cursor = session.execute(text(sql))
    result = cursor.fetchall()
    session.close()
    return result

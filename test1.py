import pymysql


class Contacts(object):

    def __init__(self, pid=None, pname=None, tel=None, qq=None, email=None, **kwargs):
        self._pid = pid
        self._pname = pname
        self._tel = tel
        self._qq = qq
        self._email = email

    @property
    def pid(self):
        return self._pid

    @property
    def pname(self):
        return self._pname

    @property
    def tel(self):
        return self._tel

    @property
    def qq(self):
        return self._qq

    @property
    def email(self):
        return self._email


def main():
    conn = pymysql.connect(host='localhost', user='root', passwd='123456',
                           db='contact_person', charset='utf8',
                           cursorclass=pymysql.cursors.DictCursor)
    try:
        with conn.cursor() as cursor:
            run = ['增', '删', '改', '查', '终止']
            abc = True
            while abc:
                fig = True
                operation = input('请输入操作:')
                if operation not in run:
                    print('请重新输入')
                    fig = False
                while fig:
                    if operation == run[0]:
                        pname = input('请输入名字:')
                        tel = input('输入电话:')
                        qq = input('输入qq号:')
                        email = input('输入邮箱:')
                        cursor.execute('insert into cp (pname, tel, qq, email) values (%s, %s, %s, %s)',
                                       (pname, tel, qq, email))
                        fig = False
                    elif operation == run[1]:
                        pid = int(input('请输入编号:'))
                        result = cursor.execute('delete from cp where pid=%s', (pid, ))
                        print('删除成功' if result == 1 else '删除失败')
                        fig = False
                    elif operation == run[2]:
                        tel = input('请输入电话:')
                        cursor.execute('update cp set tel=%s where pname="大强"', (tel, ))
                        fig = False
                    elif operation == run[3]:
                        cursor.execute('select * from cp where pname like "%王%"')
                        result = cursor.fetchone()
                        while result:
                            contact = Contacts(**result)
                            print(contact.pid, contact.pname, contact.tel, contact.qq, contact.email)
                            result = cursor.fetchone()
                        fig = False
                    else:
                        abc = False
                    conn.commit()

    except ValueError:
        conn.rollback()
    finally:
        conn.close()


if __name__ == '__main__':
    main()

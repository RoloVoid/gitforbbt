from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
import config
from extends import error

try:
    engine = create_engine('mysql+pymysql://%s:%s%s/%s?charset=utf8' % (
        config.mysql.get('user'), config.mysql.get('password'), config.mysql.get('ip+port'), config.mysql.get('database'))
                       , encoding='UTF-8', echo=True)
except Exception:
    raise error.error500

# mysql数据库：mysql+数据库驱动：//用户名：密码@localhost:端口号/数据库
# 连接服务器mysql数据库,这个是将数据库方法解释为python的类方法的核心接口

Session = sessionmaker(bind=engine)
# 会话，与数据库建立连接，绑定数据库的session对象
# 有意思的是，这个Session是一个类，和下面的Base性质一样
# 看起来都是sqlalchemy的底层设计，确实很精妙(发出无用的感慨)

Base = declarative_base()  # 生成ORM基类，用于描述表和将表映射为python的类


# 继承declarative生成的类至少需要一个__tablename__和一个主键

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=False, autoincrement=True, unique=True)
    username = Column(String(100), primary_key=True, unique=True)
    gender = Column(String(10), default="保密")
    age = Column(Integer, default=18)
    nickname = Column(String(100), unique=True)

    # 保留用户信息的表

    def __repr__(self):
        return '<id: %s username: %s gender: %s age: %s nickname: %s>' % (
            self.id, self.username, self.gender, self.age, self.nickname)


class Privacy(Base):
    __tablename__ = 'privacy'
    id = Column(Integer, primary_key=False, autoincrement=True, unique=True)
    username = Column(String(100), primary_key=True, unique=True)
    password = Column(String(100))

    # 保存用户名和密码的表

    def __repr__(self):
        return '<id: %s username: %s password: %s>' % (self.id, self.username, self.password)


class Boards(Base):
    __tablename__ = 'boards'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nickname = Column(String(100))
    username = Column(String(100))
    text = Column(String(100))
    ptime = Column(String(100))
    ltime = Column(String(100))

    # 储存留言板的表

    def __repr__(self):
        return '<id: %s username: %s text: %s, ptime: %s, ltime: %s>' % (
            self.id, self.username, self.text, self.ptime, self.ltime)


Base.metadata.create_all(engine)  # 应该是生成Base基类下所有的表

session = Session()
# 构造Session类的一个实例,用于实际与数据库进行数据交互
# 之后所有的接口调用的都是这个对象或者说实例，换言之不需要重复建立连接

# ed_user = Test(name='ed', password='123456')
# sessiontest.add(ed_user)
# 可以认为现在这一行数据还没有被写入数据库，直到flush进程被调用(这跟实际数据库的读写一致)
# sessiontest.commit() 实际将数据写入数据库

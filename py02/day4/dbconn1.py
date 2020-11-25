from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#创建连接数据库的引擎
engine = create_engine(
    'mysql+pymysql://root:tedu.cn@127.0.0.1/tedu2006?charset=utf8',
    encoding = 'utf8',
    echo = True
)

Base = declarative_base()
Session = sessionmaker(bind=engine)

class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer,primary_key=True)
    dep_name = Column(String(20),unique=True)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
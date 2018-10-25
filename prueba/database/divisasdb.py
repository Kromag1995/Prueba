from sqlalchemy import Column, Integer, Float, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

Base = declarative_base()

engine = create_engine("sqlite:///divisas.db", echo=False)

db = scoped_session(sessionmaker(bind=engine))

class Divisasdb(Base):
    __tablename__='divisas'
    id=Column(Integer, primary_key=True)
    DESCRIPCION = Column(String(100))
    ULTIMO = Column(String(100))
    ANTERIOR = Column(String(100))
    VARIACION = Column(String(100))
    FECHA = Column(String(100))

    def __init__(self, id=None, divisa=None, ultimo=None, anterior=None, variacion=None, fecha=None):
        self.id = id
        self.DESCRIPCION = divisa
        self.ULTIMO = ultimo
        self.ANTERIOR = anterior
        self.VARIACION = variacion
        self.FECHA = fecha

    def __repr__(self):
        return "<Divisas(DESCRIPCION='%s', ULTIMO='%s', ULTIMO='%s', ULTIMO='%s', ULTIMO='%s')>" %(self.DESCRIPCION, self.ULTIMO, self.ANTERIOR, self.VARIACION, self.FECHA)
    

    

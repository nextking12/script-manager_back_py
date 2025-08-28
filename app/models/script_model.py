from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Script(Base):
    __tablename__ = 'scripts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    language = Column(String, nullable=False)
    script_content = Column(Text, nullable=False)

    def __init__(self, name=None, language=None, script_content=None):
        self.name = name
        self.language = language
        self.script_content = script_content

    def __repr__(self):
        return f"Script(id={self.id}, name='{self.name}', language='{self.language}', script_content='{self.script_content}')"

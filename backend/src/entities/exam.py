# coding=utf-8
# marshmallow to handle serialization and deserialization of JSON object
from marshmallow import Schema, fields
from sqlalchemy import Column, String

from .entity import Entity, Base


class Exam(Entity, Base):
    __tablename__ = 'exams'

    title = Column(String)
    description = Column(String)

    def __init__(self, title, description, created_by):
        Entity.__init__(self, created_by)
        self.title = title
        self.description = description

# Using the Schema class of marshmallow to define a new class called ExamSchema. Use this class to transform instances of Exam into JSON objects.
class ExamSchema(Schema):
    id = fields.Number()
    title = fields.Str()
    description = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()
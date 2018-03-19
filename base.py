try:
    import ujson as json
except ImportError:
    import json

from abc import ABCMeta

class UnknownTypeError(Exception):
    pass
class BOJObject(object):
    __metaclass__ = ABCMeta
    _id_attrs = ()

    def __str__(self):
        return str(self.to_dict())

    def __getitem__(self, item):
        return self.__getattribute__[item]

    @classmethod
    def de_json(cls, data):
        if not data:
            return None
        data = data.copy()
        return data
    @classmethod
    def to_sql(cls):
        import types
        query = "create table if not exists _{0}".format(cls.__name__)
        inner = []
        for slot in cls.__slots__:
            t = None
            if cls.__types__[slot] == int:
                t = "int"
            elif cls.__types__[slot] == str:
                t = "text"
            else:
                raise UnknownTypeError("Failed to create SQL Table : type of {0} = {1}".format(slot, cls.__types__[slot]))
            inner.append("{0} {1} not null".format(slot, t))
        query += "("
        query += ", ".join(inner)
        query += ", primary key({0})".format(cls.__slots__[0])
        query += ")"
        return query
    def to_sql2(self):
        import types
        query = "insert or replace into _{0}".format(self.__class__.__name__)
        query += "({0})".format(", ".join(self.__slots__))
        query += " values ("
        query += ", ".join(['?' for x in self.__slots__])
        query += ")"
        return query
    def to_json(self):
        return json.dumps(self.to_dict())
    def to_dict(self):
        data = dict()
        for idx, key in enumerate(self.__slots__):
            value = self.__getattribute__(key)
            if value is not None:
                if hasattr(value, 'to_dict'):
                    data[key] = value.to_dict()
                else:
                    data[key] = value
        return data

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._id_attrs == other._id_attrs
        return super(BOJObject, self).__eq__(other)  # pylint: disable=no-member

    def __hash__(self):
        if self._id_attrs:
            return hash((self.__class__, self._id_attrs))  # pylint: disable=no-member
        return super(BOJObject, self).__hash__()

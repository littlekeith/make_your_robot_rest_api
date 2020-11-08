# -*- coding: utf-8 -*-

import six
from jsonschema import RefResolver
# TODO: datetime support

class RefNode(object):

    def __init__(self, data, ref):
        self.ref = ref
        self._data = data

    def __getitem__(self, key):
        return self._data.__getitem__(key)

    def __setitem__(self, key, value):
        return self._data.__setitem__(key, value)

    def __getattr__(self, key):
        return self._data.__getattribute__(key)

    def __iter__(self):
        return self._data.__iter__()

    def __repr__(self):
        return repr({'$ref': self.ref})

    def __eq__(self, other):
        if isinstance(other, RefNode):
            return self._data == other._data and self.ref == other.ref
        elif six.PY2:
            return object.__eq__(other)
        elif six.PY3:
            return object.__eq__(self, other)
        else:
            return False

    def __deepcopy__(self, memo):
        return RefNode(copy.deepcopy(self._data), self.ref)

    def copy(self):
        return RefNode(self._data, self.ref)

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###

base_path = '/v2'

definitions = {'definitions': {'Order': {'type': 'object', 'properties': {'id': {'type': 'integer', 'format': 'int64'}, 'petId': {'type': 'integer', 'format': 'int64'}, 'quantity': {'type': 'integer', 'format': 'int32'}, 'shipDate': {'type': 'string', 'format': 'date-time'}, 'status': {'type': 'string', 'description': 'Order Status', 'enum': ['placed', 'approved', 'delivered']}, 'complete': {'type': 'boolean', 'default': False}}, 'xml': {'name': 'Order'}}, 'Category': {'type': 'object', 'properties': {'id': {'type': 'integer', 'format': 'int64'}, 'name': {'type': 'string'}}, 'xml': {'name': 'Category'}}, 'User': {'type': 'object', 'properties': {'id': {'type': 'integer', 'format': 'int64'}, 'username': {'type': 'string'}, 'firstName': {'type': 'string'}, 'lastName': {'type': 'string'}, 'email': {'type': 'string'}, 'password': {'type': 'string'}, 'phone': {'type': 'string'}, 'userStatus': {'type': 'integer', 'format': 'int32', 'description': 'User Status'}}, 'xml': {'name': 'User'}}, 'Tag': {'type': 'object', 'properties': {'id': {'type': 'integer', 'format': 'int64'}, 'name': {'type': 'string'}}, 'xml': {'name': 'Tag'}}, 'Pet': {'type': 'object', 'required': ['name', 'photoUrls'], 'properties': {'id': {'type': 'integer', 'format': 'int64'}, 'category': {'$ref': '#/definitions/Category'}, 'name': {'type': 'string', 'example': 'doggie'}, 'photoUrls': {'type': 'array', 'xml': {'name': 'photoUrl', 'wrapped': True}, 'items': {'type': 'string'}}, 'tags': {'type': 'array', 'xml': {'name': 'tag', 'wrapped': True}, 'items': {'$ref': '#/definitions/Tag'}}, 'status': {'type': 'string', 'description': 'pet status in the store', 'enum': ['available', 'pending', 'sold']}}, 'xml': {'name': 'Pet'}}, 'ApiResponse': {'type': 'object', 'properties': {'code': {'type': 'integer', 'format': 'int32'}, 'type': {'type': 'string'}, 'message': {'type': 'string'}}}}, 'parameters': {}}

validators = {
    ('pet', 'POST'): {'json': {'$ref': '#/definitions/Pet'}},
    ('pet', 'PUT'): {'json': {'$ref': '#/definitions/Pet'}},
    ('pet_findByStatus', 'GET'): {'args': {'required': ['status'], 'properties': {'status': {'description': 'Status values that need to be considered for filter', 'type': 'array', 'items': {'type': 'string', 'enum': ['available', 'pending', 'sold'], 'default': 'available'}, 'collectionFormat': 'multi'}}}},
    ('pet_findByTags', 'GET'): {'args': {'required': ['tags'], 'properties': {'tags': {'description': 'Tags to filter by', 'type': 'array', 'items': {'type': 'string'}, 'collectionFormat': 'multi'}}}},
    ('pet_petId', 'POST'): {'form': {'required': [], 'properties': {'name': {'description': 'Updated name of the pet', 'required': False, 'type': 'string'}, 'status': {'description': 'Updated status of the pet', 'required': False, 'type': 'string'}}}},
    ('pet_petId', 'DELETE'): {'headers': {'required': [], 'properties': {'api_key': {'required': False, 'type': 'string'}}}},
    ('pet_petId_uploadImage', 'POST'): {'form': {'required': [], 'properties': {'additionalMetadata': {'description': 'Additional data to pass to server', 'required': False, 'type': 'string'}, 'file': {'description': 'file to upload', 'required': False, 'type': 'file'}}}},
    ('store_order', 'POST'): {'json': {'$ref': '#/definitions/Order'}},
    ('user', 'POST'): {'json': {'$ref': '#/definitions/User'}},
    ('user_createWithArray', 'POST'): {'json': {'type': 'array', 'items': {'$ref': '#/definitions/User'}}},
    ('user_createWithList', 'POST'): {'json': {'type': 'array', 'items': {'$ref': '#/definitions/User'}}},
    ('user_login', 'GET'): {'args': {'required': ['username', 'password'], 'properties': {'username': {'description': 'The user name for login', 'type': 'string'}, 'password': {'description': 'The password for login in clear text', 'type': 'string'}}}},
    ('user_username', 'PUT'): {'json': {'$ref': '#/definitions/User'}},
}

filters = {
    ('pet', 'POST'): {405: {'headers': None, 'schema': None}},
    ('pet', 'PUT'): {400: {'headers': None, 'schema': None}, 404: {'headers': None, 'schema': None}, 405: {'headers': None, 'schema': None}},
    ('pet_findByStatus', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': {'$ref': '#/definitions/Pet'}}}, 400: {'headers': None, 'schema': None}},
    ('pet_findByTags', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': {'$ref': '#/definitions/Pet'}}}, 400: {'headers': None, 'schema': None}},
    ('pet_petId', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/Pet'}}, 400: {'headers': None, 'schema': None}, 404: {'headers': None, 'schema': None}},
    ('pet_petId', 'POST'): {405: {'headers': None, 'schema': None}},
    ('pet_petId', 'DELETE'): {400: {'headers': None, 'schema': None}, 404: {'headers': None, 'schema': None}},
    ('pet_petId_uploadImage', 'POST'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/ApiResponse'}}},
    ('store_inventory', 'GET'): {200: {'headers': None, 'schema': {'type': 'object', 'additionalProperties': {'type': 'integer', 'format': 'int32'}}}},
    ('store_order', 'POST'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/Order'}}, 400: {'headers': None, 'schema': None}},
    ('store_order_orderId', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/Order'}}, 400: {'headers': None, 'schema': None}, 404: {'headers': None, 'schema': None}},
    ('store_order_orderId', 'DELETE'): {400: {'headers': None, 'schema': None}, 404: {'headers': None, 'schema': None}},
    ('user', 'POST'): {},
    ('user_createWithArray', 'POST'): {},
    ('user_createWithList', 'POST'): {},
    ('user_login', 'GET'): {200: {'headers': {'X-Rate-Limit': {'type': 'integer', 'format': 'int32', 'description': 'calls per hour allowed by the user'}, 'X-Expires-After': {'type': 'string', 'format': 'date-time', 'description': 'date in UTC when token expires'}}, 'schema': {'type': 'string'}}, 400: {'headers': None, 'schema': None}},
    ('user_logout', 'GET'): {},
    ('user_username', 'GET'): {200: {'headers': None, 'schema': {'$ref': '#/definitions/User'}}, 400: {'headers': None, 'schema': None}, 404: {'headers': None, 'schema': None}},
    ('user_username', 'PUT'): {400: {'headers': None, 'schema': None}, 404: {'headers': None, 'schema': None}},
    ('user_username', 'DELETE'): {400: {'headers': None, 'schema': None}, 404: {'headers': None, 'schema': None}},
}

scopes = {
    ('pet', 'POST'): ['write:pets', 'read:pets'],
    ('pet', 'PUT'): ['write:pets', 'read:pets'],
    ('pet_findByStatus', 'GET'): ['write:pets', 'read:pets'],
    ('pet_findByTags', 'GET'): ['write:pets', 'read:pets'],
    ('pet_petId', 'GET'): [],
    ('pet_petId', 'POST'): ['write:pets', 'read:pets'],
    ('pet_petId', 'DELETE'): ['write:pets', 'read:pets'],
    ('pet_petId_uploadImage', 'POST'): ['write:pets', 'read:pets'],
    ('store_inventory', 'GET'): [],
}

resolver = RefResolver.from_schema(definitions)

class Security(object):

    def __init__(self):
        super(Security, self).__init__()
        self._loader = lambda: []

    @property
    def scopes(self):
        return self._loader()

    def scopes_loader(self, func):
        self._loader = func
        return func

security = Security()


def merge_default(schema, value, get_first=True, resolver=None):
    # TODO: more types support
    type_defaults = {
        'integer': 9573,
        'string': 'something',
        'object': {},
        'array': [],
        'boolean': False
    }

    results = normalize(schema, value, type_defaults, resolver=resolver)
    if get_first:
        return results[0]
    return results


def normalize(schema, data, required_defaults=None, resolver=None):
    if required_defaults is None:
        required_defaults = {}
    errors = []

    class DataWrapper(object):

        def __init__(self, data):
            super(DataWrapper, self).__init__()
            self.data = data

        def get(self, key, default=None):
            if isinstance(self.data, dict):
                return self.data.get(key, default)
            return getattr(self.data, key, default)

        def has(self, key):
            if isinstance(self.data, dict):
                return key in self.data
            return hasattr(self.data, key)

        def keys(self):
            if isinstance(self.data, dict):
                return list(self.data.keys())
            return list(getattr(self.data, '__dict__', {}).keys())

        def get_check(self, key, default=None):
            if isinstance(self.data, dict):
                value = self.data.get(key, default)
                has_key = key in self.data
            else:
                try:
                    value = getattr(self.data, key)
                except AttributeError:
                    value = default
                    has_key = False
                else:
                    has_key = True
            return value, has_key

    def _merge_dict(src, dst):
        for k, v in six.iteritems(dst):
            if isinstance(src, dict):
                if isinstance(v, dict):
                    r = _merge_dict(src.get(k, {}), v)
                    src[k] = r
                else:
                    src[k] = v
            else:
                src = {k: v}
        return src

    def _normalize_dict(schema, data):
        result = {}
        if not isinstance(data, DataWrapper):
            data = DataWrapper(data)

        for _schema in schema.get('allOf', []):
            rs_component = _normalize(_schema, data)
            _merge_dict(result, rs_component)

        for key, _schema in six.iteritems(schema.get('properties', {})):
            # set default
            type_ = _schema.get('type', 'object')

            # get value
            value, has_key = data.get_check(key)
            if has_key or '$ref' in _schema:
                result[key] = _normalize(_schema, value)
            elif 'default' in _schema:
                result[key] = _schema['default']
            elif key in schema.get('required', []):
                if type_ in required_defaults:
                    result[key] = required_defaults[type_]
                else:
                    errors.append(dict(name='property_missing',
                                       message='`%s` is required' % key))

        additional_properties_schema = schema.get('additionalProperties', False)
        if additional_properties_schema is not False:
            aproperties_set = set(data.keys()) - set(result.keys())
            for pro in aproperties_set:
                result[pro] = _normalize(additional_properties_schema, data.get(pro))

        return result

    def _normalize_list(schema, data):
        result = []
        if hasattr(data, '__iter__') and not isinstance(data, (dict, RefNode)):
            for item in data:
                result.append(_normalize(schema.get('items'), item))
        elif 'default' in schema:
            result = schema['default']
        return result

    def _normalize_default(schema, data):
        if data is None:
            return schema.get('default')
        else:
            return data

    def _normalize_ref(schema, data):
        if resolver == None:
            raise TypeError("resolver must be provided")
        ref = schema.get(u"$ref")
        scope, resolved = resolver.resolve(ref)
        if resolved.get('nullable', False) and not data:
            return {}
        return _normalize(resolved, data)

    def _normalize(schema, data):
        if schema is True or schema == {}:
            return data
        if not schema:
            return None
        funcs = {
            'object': _normalize_dict,
            'array': _normalize_list,
            'default': _normalize_default,
            'ref': _normalize_ref
        }
        type_ = schema.get('type', 'object')
        if type_ not in funcs:
            type_ = 'default'
        if schema.get(u'$ref', None):
            type_ = 'ref'

        return funcs[type_](schema, data)

    return _normalize(schema, data), errors

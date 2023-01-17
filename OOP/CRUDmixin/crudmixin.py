from search import search_object

class CRUDMixin:
    def _get_or_set_object_and_id(self):
        try:
            if (self.objects or not self.objects) and (self.id or not self.id):
                pass
        except (NameError, AttributeError):
            self.objects = []
            self.id = 0

    def __init__(self) -> None:
        self._get_or_set_object_and_id()

    def create(self, **kwargs):
        self.id += 1
        object_ = dict(id=self.id, **kwargs)
        self.objects.append(object_)
        return {'status': 201, 'msg': object_}
    def list(self):
        res = []
        for obj in self.objects:
            res.append({'id': obj['id'], 'title': obj['title'], 'price': obj['price']})
        return{'status': 200, 'msg': res}
    
    @search_object
    def detail(self, id, **kwargs):
        obj = kwargs['object_']
        if obj:
            return{'status': 200, 'msg': obj}
        return{'status': 404, 'msg': 'Not Found'}

    @search_object
    def update(self, id, **kwargs):
        obj = kwargs.pop('object_')
        if obj:
            obj.update(**kwargs)
            return{'status': 206, 'msg': obj}
        return {'status': 404, 'msg': 'Not Found'}
    
    @search_object
    def delete(self, id, **kwargs):
        obj = kwargs.get('object_')
        if obj:
            self.objects.remove(obj)
            return{'status': 204, 'msg': 'deleted'}
        return {'status': 404, 'msg': 'Not Found'}

    def save(self):
        import json
        with open('data.json', 'w') as file:
            json.dump(self.objects, file)
        return 'Saved!'



smartphones = CRUDMixin()
print(smartphones.create(title='Redmi Note 10', descriprions='The bestphone for own price', gty=10, price=200))
print(smartphones.create(title='Redmi Note 20', descriprions='The Flagman of redmi phones', gty=5, price=500))
print(smartphones.create(title='IPhone 14 Pro max', descriprions='New phone cool and best', gty=15, price=1300))
print()
print(smartphones.detail(6))
print(smartphones.detail(3))
print()
print(smartphones.update(3, title='IPhone 14'))
print(smartphones.update(10, title='IPhone 13 Pro'))
print(smartphones.list())
print()
print(smartphones.delete(1))
print()
print(smartphones.list())
print(smartphones.create(title='SUmsung s22 Ultra', descriprions='The best phone for android lovers price', gty=8, price=1000))
print(smartphones.create(title='Poco Phone 19', descriprions='Flagman of Pococ Phones', gty=5, price=400))
print(smartphones.save())
print(smartphones.list())

#==========================================================================================================================================
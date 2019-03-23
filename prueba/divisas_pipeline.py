from .database.divisasdb import db, Divisasdb
class AddTablePipeline(object):
    def process_item(self, item, spider):
        record = Divisasdb(divisa= item['descripcion'], ultimo=item['ultimo'], anterior=item['anterior'], variacion=item['variacion'], fecha=item['fecha'])
        db.add(record)
        db.commit()
        return item
from .database.divisasdb import db, Divisasdb
class AddTablePipeline(object):
    def process_item(self, item, spider):
        record = Divisasdb(divisa= item['DESCRIPCION'], ultimo=item['ULTIMO'], anterior=item['ANTERIOR'], variacion=item['VARIACION'], fecha=item['FECHA'])
        db.add(record)
        db.commit()
        return item
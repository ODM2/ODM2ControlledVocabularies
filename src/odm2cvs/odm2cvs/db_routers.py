class ControlVocabularyRouter(object):
    def db_for_read(self, model, **hints):
        "Point all operations on chinook models to 'chinookdb'"
        if model._meta.app_label == 'cvservices':
            return 'control_vocabularies'
        return 'default'

    def db_for_write(self, model, **hints):
        "Point all operations on chinook models to 'chinookdb'"
        if model._meta.app_label == 'cvservices':
            return 'control_vocabularies'
        return 'default'

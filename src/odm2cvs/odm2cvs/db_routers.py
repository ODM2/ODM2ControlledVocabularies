class ControlledVocabularyRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'cvservices':
            return 'vocabularies'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'cvservices':
            return 'vocabularies'
        return 'default'



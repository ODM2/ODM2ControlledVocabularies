class ControlledVocabularyRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'cvservices':
            return 'vocabularies'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'cvservices':
            return 'vocabularies'
        return 'default'

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if 'target_db' in hints:
            return db == hints['target_db']
        return True



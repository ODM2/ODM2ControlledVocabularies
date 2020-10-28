class ControlledVocabularyRouter:
    """
    A router to control all database operations on models and web services.
    """
    route_app_labels = {'cvservices', 'rdfserializer'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'vocabularies'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'vocabularies'
        return 'default'

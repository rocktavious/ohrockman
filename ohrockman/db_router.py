
class PhotologueRouter(object):
    """
    A router to control all database operations on models in the
    photologue application.
    """
    apps = ["photologue"]
    using = "photos"
    
    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.apps:
            return self.using
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.apps:
            return self.using
        return None
    
    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the app is involved.
        """
        if obj1._meta.app_label in self.apps or obj2._meta.app_label in self.apps:
            return True
        return None
    
    def allow_migrate(self, db, model):
        """Make sure the apps we care about appear in the db"""
        if db == self.using:
            return model._meta.app_label in self.apps
        elif model._meta.app_label in self.apps:
            return False
        return None

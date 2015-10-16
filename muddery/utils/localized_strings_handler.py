"""
This model translates default strings into localized strings.
"""

from django.conf import settings
from django.db.models.loading import get_model
from evennia.utils import logger


class LocalizedStringsHandler(object):
    """
    This model translates default strings into localized strings.
    """
    def __init__(self):
        """
        Initialize handler
        """
        self.clear()


    def clear(self):
        """
        Clear data.
        """
        self.dict = {}


    def reload(self):
        """
        Reload local string data.
        """
        self.clear()

        # Get db model
        try:
            model_obj = get_model(settings.WORLD_DATA_APP, settings.LOCALIZED_STRINGS_MODEL)
            for record in model_obj.objects.all():
                # Add db fields to dict.
                self.dict[record.origin] = record.local
        except Exception, e:
            print "Can not load server local string: %s" % e
            pass


    def translate(self, origin):
        """
        Translate origin string to local string.
        """
        try:
            # Get local string.
            local = self.dict[origin]
            if local:
                return local
        except:
            pass

        # Else return origin string.
        return origin


# main dialoguehandler
LOCALIZED_STRINGS_HANDLER = LocalizedStringsHandler()


# translater
def LS(origin):
    """
    This function returns the localized string.
    """
    return LOCALIZED_STRINGS_HANDLER.translate(origin)

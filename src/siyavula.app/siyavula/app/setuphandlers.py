from Products.CMFCore.utils import getToolByName
from Products.ATContentTypes.permission import ModifyConstrainTypes
from Products.ATContentTypes.lib.constraintypes import ENABLED
from Products.CMFDynamicViewFTI.permissions import ModifyViewTemplate

def setupVarious(context):
    """ Run setuphandlers
    """
    if context.readDataFile("siyavula.app_marker.txt") is None:
        return

    # Create a few top-level folders for the content.
    portal = context.getSite()
    if not portal.hasObject('books'):
        portal.invokeFactory(type_name='Folder', id='books',
            title='Books') 
        books = portal._getOb('books')
        books.setConstrainTypesMode(ENABLED)
        books.setLocallyAllowedTypes(['siyavula.app.book'])
        books.setImmediatelyAddableTypes(['siyavula.app.book'])
        # The next line enables a different view.
        # books.setLayout('statusandnews_listing')
        # stop anyone from changing the display of this folder
        books.manage_permission(ModifyViewTemplate, roles=[])
        # stop people from change the allowed types
        books.manage_permission(ModifyConstrainTypes, roles=[])

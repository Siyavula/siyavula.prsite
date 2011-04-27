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
        portal.invokeFactory(type_name='siyavula.app.section', id='books',
            title='WebBooks') 
        section = portal._getOb('books')

        wf = getToolByName(portal, 'portal_workflow')
        wf.doActionFor(section,'publish')
        section.reindexObject()

        # The next line enables a different view.
        section.setLayout('booksview')
        # stop anyone from changing the display of this folder
        section.manage_permission(ModifyViewTemplate, roles=[])
        # stop people from change the allowed types
        section.manage_permission(ModifyConstrainTypes, roles=[])

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

    sections = [
        {'id': 'books',
        'title': 'WebBooks',
        'view': 'booksview'},
        {'id': 'other',
        'title': 'Other Products',
        'view': 'view'},
        {'id': 'volunteers',
        'title': 'Volunteers',
        'view': 'volunteersview'},
        {'id': 'courses',
        'title': 'Courses',
        'view': 'coursesview'},
        {'id': 'blog',
        'title': 'Blog',
        'view': 'blogview'},
        {'id': 'about',
        'title': 'About',
        'view': 'view'},
        {'id': 'contact',
        'title': 'Contact',
        'view': 'view'},
    ]

    for section_dict in sections:
        if not portal.hasObject(section_dict['id']):
            portal.invokeFactory(type_name='siyavula.app.section', id=section_dict['id'],
                title=section_dict['title']) 
            section = portal._getOb(section_dict['id'])

            wf = getToolByName(portal, 'portal_workflow')
            wf.doActionFor(section,'publish')
            section.reindexObject()

        else:
            section = portal._getOb(section_dict['id'])

        # Set the default view.
        section.setLayout(section_dict['view'])
        # Stop anyone from changing the display of this folder
        section.manage_permission(ModifyViewTemplate, roles=[])
        # Stop people from changing the allowed types
        section.manage_permission(ModifyConstrainTypes, roles=[])

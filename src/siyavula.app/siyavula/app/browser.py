from five import grok
from Acquisition import aq_inner

from plone.memoize import view
from Products.CMFCore.utils import getToolByName
from Products.CMFCore.interfaces import IContentish

class MainTemplateHelpers(grok.View):
    """Get some dynamic things we need in the main template.
    """
    
    grok.context(IContentish)
    grok.require('zope2.View')
    grok.name('main-template-helpers')
    
    def render(self):
        """No-op to keep grok.View happy
        """
        return ''

    @view.memoize
    def sections(self):
        context = aq_inner(self.context)
        portal = context.portal_url.getPortalObject()
        sections = portal.getFolderContents()
        return [i.getObject() for i in sections]
        
    @view.memoize
    def books(self):
        """Get the message representation of the context
        """
        context = aq_inner(self.context)
        portal = context.portal_url.getPortalObject()
        pc = getToolByName(context, 'portal_catalog')
        query = {'portal_type' : 'siyavula.app.book',
                 'review_state' : 'published',
                 'sort_on' : 'getObjPositionInParent',
                }
        brains = pc(query)
        return [brain.getObject() for brain in brains]

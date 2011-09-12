from five import grok
from plone.app.layout.viewlets.interfaces import IPortalFooter
from zope.interface import Interface

grok.templatedir('browser_templates')

class ThemeViewlet(grok.Viewlet):
    grok.context(Interface)
    grok.viewletmanager(IPortalFooter)

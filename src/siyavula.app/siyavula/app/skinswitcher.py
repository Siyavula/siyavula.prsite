def setSkin(self, event):
    request = event.request
    po = self.portal_url.getPortalObject()
    skinner = po.portal_skins.getSkinSelections()
    if request.get('URL').startswith('http://admin'):
        if 'Sunburst Theme' in skinner:
            po.changeSkin('Sunburst Theme', request)
        else:
            po.changeSkin('Plone Default', request)
    else:
        po.changeSkin('Siyavula', request)

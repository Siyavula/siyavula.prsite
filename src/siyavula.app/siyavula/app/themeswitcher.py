def switch_theme(obj, event):
    """ Suppress the Diazo theme if the url starts with admin."""
    if event.request.get('ACTUAL_URL', '').startswith('http://admin'):
        event.request.response.setHeader('X-Theme-Disabled', 'True')

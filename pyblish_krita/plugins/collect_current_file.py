import pyblish.api


class CollectKritaCurrentFile(pyblish.api.ContextPlugin):
    """Inject the current working file into context"""

    order = pyblish.api.CollectorOrder - 0.5
    label = "Krita Current File"

    hosts = ['krita']
    version = (0, 1, 0)

    def process(self, context):
        import os
        import krita
        krita_instance = krita.Krita.instance()
        document = krita_instance.activeDocument()
        if not document:
            return
        current_file = document.fileName()

        """Inject the current working file"""
        normalised = os.path.normpath(current_file)

        context.set_data('currentFile', value=normalised)
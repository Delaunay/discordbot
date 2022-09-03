from vlcbot.core.conf import discover_plugins
import vlcbot.plugins.sources

sources =  []

def refresh_sources():
    global sources
    sources = discover_plugins(vlcbot.plugins.sources)

refresh_sources()



class SourceNotFound(Exception):
    pass


def get_source(name):
    module = sources.get(name)

    if module is None:
        raise SourceNotFound(name)

    return module.source



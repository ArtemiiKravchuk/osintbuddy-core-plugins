from urllib.parse import urlparse
from osintbuddy.elements import Title, CopyText
import osintbuddy as ob


class GoogleCacheResult(ob.Plugin):
    label = "Cache Result"
    show_label = False
    color = "#145070"
    node = [
        Title(label="result", title="Some title"),
        [
            CopyText(label="URL"),
        ],
    ]

    author = 'the OSINTBuddy team'

    @ob.transform(label="To website", icon="world-www")
    async def transform_to_website(self, node, use):
        WebsitePlugin = await ob.Registry.get_plugin('website')
        return WebsitePlugin.blueprint(domain=urlparse(node.url).netloc)

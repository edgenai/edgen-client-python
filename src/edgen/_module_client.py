

from typing_extensions import override

from . import resources, _load_client
from ._utils import LazyProxy


class ChatProxy(LazyProxy[resources.Chat]):
    @override
    def __load__(self) -> resources.Chat:
        return _load_client().chat


class AudioProxy(LazyProxy[resources.Audio]):
    @override
    def __load__(self) -> resources.Audio:
        return _load_client().audio

class MiscProxy(LazyProxy[resources.Misc]):
    @override
    def __load__(self) -> resources.Misc:
        return _load_client().misc

chat: resources.Chat = ChatProxy().__as_proxied__()
audio: resources.Audio = AudioProxy().__as_proxied__()
misc: resources.Misc = MiscProxy().__as_proxied__()

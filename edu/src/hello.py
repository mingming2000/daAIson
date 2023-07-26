from typing import Any


class Hello(object):
    def __call__(self, *args: Any, **kwds: Any) -> int:
        return 1
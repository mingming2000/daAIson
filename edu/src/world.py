from typing import Any

from .hello import Hello


class World(object):
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        _hello = Hello()
        return _hello()


if __name__ == '__main__':
    world = World()
    print(world())


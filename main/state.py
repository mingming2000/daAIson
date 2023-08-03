import logging
from text_color import TextColor


class State(object):
    _state: str = "READY"

    def __repr__(self) -> str:
        return self._state

    @property
    def cur_state(self):
        return self._state

    @property
    def ready(self):
        self._state = "READY"
        _txt = f"S:{self._state}"
        _txt = TextColor.yellow_bright(_txt)
        logging.info(_txt)

    @property
    def wait(self):
        self._state = "WAIT"
        _txt = f"S:{self._state}"
        _txt = TextColor.yellow_bright(_txt)
        logging.info(_txt)

    @property
    def detecting(self):
        self._state = "DETECTING"
        _txt = f"S:{self._state}"
        _txt = TextColor.yellow_bright(_txt)
        logging.info(_txt)

    @property
    def saving(self):
        self._state = "SAVING"
        _txt = f"S:{self._state}"
        _txt = TextColor.yellow_bright(_txt)
        logging.info(_txt)

    @property
    def is_ready(self):
        return self._state == "READY"

    @property
    def is_wait(self):
        return self._state == "WAIT"

    @property
    def is_detecting(self):
        return self._state == "DETECTING"

    @property
    def is_saving(self):
        return self._state == "SAVING"
class TextColor:
    _origin_color = "\033[0m"
    _red_bright = "\033[91m"
    _green_bright = "\033[92m"
    _yellow_bright = "\033[93m"
    _blue_bright = "\033[94m"

    @classmethod
    def _cvt2string(cls, msg: str) -> str:
        if not isinstance(msg, str):
            msg = str(msg)
        return msg

    @classmethod
    def red_bright(cls, msg: str):
        _tc = TextColor()
        _msg = _tc._red_bright
        _msg += _tc._cvt2string(msg)
        _msg += _tc._origin_color
        return _msg

    @classmethod
    def green_bright(cls, msg: str):
        _tc = TextColor()
        _msg = _tc._green_bright
        _msg += _tc._cvt2string(msg)
        _msg += _tc._origin_color
        return _msg

    @classmethod
    def yellow_bright(cls, msg: str):
        _tc = TextColor()
        _msg = _tc._yellow_bright
        _msg += _tc._cvt2string(msg)
        _msg += _tc._origin_color
        return _msg

    @classmethod
    def blue_bright(cls, msg: str):
        _tc = TextColor()
        _msg = _tc._blue_bright
        _msg += _tc._cvt2string(msg)
        _msg += _tc._origin_color
        return _msg

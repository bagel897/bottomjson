from json import JSONDecoder, JSONEncoder

from bottom import decode, encode


class BottomDecoder(JSONDecoder):
    def decode(self, s, w=None):
        return super().decode(decode(s))


class BottomEncoder(JSONEncoder):
    def encode(self, o):
        return encode(super().encode(o))

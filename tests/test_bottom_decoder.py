import uuid
from json import JSONDecoder, JSONEncoder

import pytest

from bottomjson import BottomDecoder, BottomEncoder


@pytest.mark.parametrize(
    "encoder, decoder",
    [(JSONEncoder(), JSONDecoder()), (BottomEncoder(), BottomDecoder())],
)
class TestSimple:
    @staticmethod
    def test_simple(encoder: JSONEncoder, decoder: JSONDecoder):
        data = {"hello": "world"}
        assert decoder.decode(encoder.encode(data)) == data

    @staticmethod
    def test_benchmarrk(encoder: JSONEncoder, decoder: JSONDecoder):
        for _ in range(100):
            data = {str(uuid.uuid4()): str(uuid.uuid4()) for _ in range(1000)}
            assert decoder.decode(encoder.encode(data)) == data

from validator.rules import Integer
from validator import validate


def test_integer_01():
    assert Integer().check("23")

    assert Integer().check("0")

    assert Integer().check("99999")

    assert Integer().check("85189125")

    assert Integer().check("-1")

    assert Integer().check("-10000")

    assert Integer().check("-161651651")


def test_integer_02():
    assert Integer().check(23)

    assert Integer().check(0)

    assert Integer().check(99999)

    assert Integer().check(85189125)

    assert Integer().check(-1)

    assert Integer().check(-10000)

    assert Integer().check(-161651651)


def test_integer_03():
    assert not Integer().check("-")

    assert not Integer().check("9.1")

    assert not Integer().check("-0.0")

    assert not Integer().check("0.0")

    assert not Integer().check("10.0")

    assert not Integer().check("-10000.213")

    assert not Integer().check("-161651651.12312312312")


def test_integer_04():
    assert not Integer().check(9.1)

    assert not Integer().check(-0.0)

    assert not Integer().check(0.0)

    assert not Integer().check(10.0)

    assert not Integer().check(-10000.213)

    assert not Integer().check(-161651651.12312312312)


def test_integer_05():
    assert not Integer().check([])

    assert not Integer().check([0, 1, 2])

    assert not Integer().check("string")

    assert not Integer().check(None)

    assert not Integer().check({"a": 2})

    assert not Integer().check(__file__)


def test_integer_06_string():
    assert validate({"val": -63}, {"val": "integer"})

    assert validate({"val": 0}, {"val": "integer"})

    assert validate({"val": 5}, {"val": "integer"})

    assert validate({"val": "42"}, {"val": "integer"})

    assert not validate({"val": {}}, {"val": "integer"})

    assert not validate({"val": [123, 5]}, {"val": "integer"})

    assert not validate({"val": 2.3}, {"val": "integer"})

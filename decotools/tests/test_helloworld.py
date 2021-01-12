from decotools import byfunc, byattr


def test_helloworld():
    @byfunc('upper')
    def greet():
        return 'hello world'

    assert greet() == 'HELLO WORLD'

    @byattr('__class__')
    def greet():
        return 'hello world'

    assert greet() == 'hello world'.__class__

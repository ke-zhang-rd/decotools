from decotools import byfunc, byattr


def test_helloworld():
    @byfunc('upper')
    def greet():
        return 'hello world'

    assert greet.__name__ == 'greet'

    @byattr('__class__')
    def greet():
        return 'hello world'

    assert greet.__name__ == 'greet'

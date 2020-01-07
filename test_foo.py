from core.foo import foo
def test_foo():
  a = [1, 2, 3]
  b = [2, 1, 4]
  assert len(foo(a, b)) == 3
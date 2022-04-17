def data_types():
    a = 5
    b = "hello"
    c = 5.2
    d = True
    e = ['1', '2']
    f = {}
    g = ()
    h = set()
    print('[%s, %s, %s, %s, %s, %s, %s, %s]'
          % (
              type(a).__name__, type(b).__name__ ,
              type(c).__name__, type(d).__name__,
              type(e).__name__, type(f).__name__ ,
              type(g).__name__, type(h).__name__
            )
          )

if __name__ == '__main__':
  data_types()
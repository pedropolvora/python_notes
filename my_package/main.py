import reader

r = reader.Reader('test.gz')
print(r.read())
r.close()
r = reader.Reader('test.bz2')
print(r.read())
r.close()
r = reader.Reader('reader/__init__.py')
print(r.read())
r.close()


# using __all__
from reader.compressed import *

print(bz2_opener)
print(gzip_opener)

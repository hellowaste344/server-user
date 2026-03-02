import os
import tempfile

tmp = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)

print(tmp.name)
print(tmp)

os.unlink(tmp)

print(tmp.name)

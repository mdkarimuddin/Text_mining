import importlib
reqs = ["numpy","sklearn","nltk","spacy","requests"]
for r in reqs:
    try:
        importlib.import_module(r)
        print(f"OK: {r}")
    except Exception as e:
        print(f"MISSING: {r} -> {e}")

import os
print("abstracts folder present:", os.path.exists('abstracts'))

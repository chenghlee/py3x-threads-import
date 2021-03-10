This repository demonstrates a behavior change (and possible bug) in Python 3.9
that causes delayed relative imports (e.g., one performed inside a function) to
sometimes fail in multi-threaded scenarios.  This was originally discovered
while working on [conda#10490](https://github.com/conda/conda/issues/10490).

This behavior can be observed by installing a Python 3.9 interpreter, and
running `python3 demo.py`; the failure mode produces output similar to:

```
Thread-1: performing relative import
Thread-2: performing relative import
Exception in thread Thread-2:
Traceback (most recent call last):
  File "${PYTHON_PREFIX}/lib/python3.9/threading.py", line 954, in _bootstrap_inner
    self.run()
  File "${PYTHON_PREFIX}/lib/python3.9/threading.py", line 892, in run
    self._target(*self._args, **self._kwargs)
  File "${THIS_REPO}/mypkg/a.py", line 16, in relative
    from .b import fn
ImportError: cannot import name 'fn' from partially initialized module 'mypkg.b' (most likely due to a circular import) (${THIS_REPO}/mypkg/b.py)
Thread-1: running fn()

Python executable: ${PYTHON_PREFIX}/bin/python3
Python version:
3.9.2 (default, Mar  3 2021, 11:58:52)
[Clang 10.0.0 ]
```

This `ImportError` behavior has been observed with the following builds of the
CPython 3.9 interpreter:

    - Anaconda (defaults) Python 3.9.2, Linux (Ubuntu 18.04)
    - Anaconda (defaults) Python 3.9.1, Linux (Ubuntu 18.04)
    - Anaconda (defaults) Python 3.9.0, Linux (Ubuntu 18.04)
    - Anaconda (defaults) Python 3.9.2, macOS 10.15
    - Anaconda (defaults) Python 3.9.1, macOS 10.15
    - Anaconda (defaults) Python 3.9.0, macOS 10.15
    - Anaconda (defaults) Python 3.9.2, Windows 10
    - Anaconda (defaults) Python 3.9.1, Windows 10
    - Anaconda (defaults) Python 3.9.0, Windows 10
    - conda-forge Python 3.9.2, Linux (Ubuntu 18.04)
    - conda-forge Python 3.9.2, macOS 10.15
    - conda-forge Python 3.9.2, Windows 10
    - Homebrew Python 3.9.2, macOS 10.15
    - `deadsnakes` PPA Python 3.9.2, Ubuntu 18.04

It has _not_ been been observed with Python 3.7 and 3.8, nor with delayed
absolute imports (e.g., `python demo.py absolute`).

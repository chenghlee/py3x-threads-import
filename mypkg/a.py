from threading import current_thread


def absolute():
    thread = current_thread()
    print(f"{thread.name}: performing absolute import")

    from mypkg.b import fn
    fn()


def relative():
    thread = current_thread()
    print(f"{thread.name}: performing relative import")

    from .b import fn
    fn()

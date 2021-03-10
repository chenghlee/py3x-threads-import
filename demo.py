import sys
from threading import Thread

from mypkg.a import absolute, relative

if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("method", choices=["absolute", "relative"],
                        help="Import type for mypkg.b")
    parser.add_argument("--threads", "-t", type=int, default=2,
                        help="Number of threads to run")
    args = parser.parse_args()

    sys.setswitchinterval(0.005)

    numThreads = args.threads
    threads = [None] * numThreads

    for i in range(numThreads):
        threads[i] = Thread(target=globals()[args.method])

    for i in range(numThreads):
        threads[i].start()

    for i in range(numThreads):
        threads[i].join()

    # Done here to avoid possible interference with timing-sensitive code above
    print(f"\nPython executable: {sys.executable}",
          f"\nPython version:\n{sys.version}\n",
          sep="")

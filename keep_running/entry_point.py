import argparse
from keep_running.run_process import RunProcess


def entry_point():

    parser = argparse.ArgumentParser(
        description='Keep Running Process'
    )

    parser.add_argument(
        'process',
        action='store',
        type=str,
        help='Process to run.'
    )

    args = parser.parse_args()

    keep = RunProcess.create(args.process)
    keep.run()


if __name__ == '__main__':
    entry_point()

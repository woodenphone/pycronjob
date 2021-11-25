#!python3
## helloworld.oy
## Pretend to do something useful.
import logging
import argparse


def helloworld(low, high):
    """Our super important task"""
    logging.info(f'Hello world from logging! {low!r}-{high!r}')
    print(f'Hello world from print! {low!r}-{high!r}')
    return


def dynamic_get_range():
    """Use the smart automated way to decide what to do"""
    return (1, 1000) # This is just pretend for the example


def main():
    """Run with user-selected parameters"""
    logging.basicConfig(level=logging.DEBUG)
    logging.debug('Logging started')

    parser = argparse.ArgumentParser()
    parser.add_argument( '-l', '--low',
        dest='low', help='Start of range' )
    parser.add_argument( '-h', '--high',
        dest='high', help='End of range' )
    args = parser.parse_args()
    logging.debug(f'args={0!r}')

    helloworld(args.low, args.high )
    return


if __name__ == '__main__':
    main()
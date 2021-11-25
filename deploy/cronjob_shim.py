#!python3
## cronjob_shim.py
## Shim to handle running from cron.
import logging

import helloworld


def main():
    """Run with automatically selected parameters
    suitable for the cronjob"""
    logging.basicConfig(level=logging.DEBUG)
    logging.debug('Logging started')
    low, high = helloworld.dynamic_get_range()
    helloworld.helloworld(low, high)
    return


if __name__ == '__main__':
    main()
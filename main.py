from lib.bybit import Bybit
from config import BYBIT_API_KEY, BYBIT_API_SECRET


def main():

    """
    Entry point.
    """

    bb = Bybit(BYBIT_API_KEY, BYBIT_API_SECRET)
    bb.withdraw("TDur1oVF8JzGwpdfnrNUQmQivjNuuvqR8E", "2")

if __name__ == "__main__":

    main()
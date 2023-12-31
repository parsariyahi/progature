import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from progature.utils import create_all_games


if __name__ == "__main__":
    create_all_games()
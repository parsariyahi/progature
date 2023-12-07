import os
import sys
from pathlib import Path

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from progature.utils.init import create_all_games


if __name__ == "__main__":
    create_all_games()
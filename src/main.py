import argparse
from .worldgen import generate_map


def parse_args(args=None):
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Game entry point")
    parser.add_argument(
        "--seed", type=int, default=None, help="World generation seed"
    )
    return parser.parse_args(args)


def main(args=None):
    """Generate a map using the provided command line arguments."""
    opts = parse_args(args)
    game_map = generate_map(10, 10, seed=opts.seed)
    for row in game_map:
        print(" ".join(row))


if __name__ == "__main__":
    main()

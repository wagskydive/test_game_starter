import argparse
from .worldgen import generate_map


def parse_args(args=None):
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Game entry point")
    parser.add_argument(
        "--seed", type=int, default=None, help="World generation seed"
    )
    parser.add_argument(
        "--width", type=int, default=10, help="Map width"
    )
    parser.add_argument(
        "--height", type=int, default=10, help="Map height"
    )
    return parser.parse_args(args)


def main(args=None):
    """Generate a map using the provided command line arguments."""
    opts = parse_args(args)
    game_map = generate_map(opts.width, opts.height, seed=opts.seed)
    for row in game_map:
        print(" ".join(row))


if __name__ == "__main__":
    main()

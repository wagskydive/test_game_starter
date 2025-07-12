from src.asset_manager import ensure_assets, DEFAULT_ASSETS


def main() -> None:
    """Download and index the default asset packs."""
    ensure_assets(DEFAULT_ASSETS)


if __name__ == "__main__":
    main()

"""
Quality@1 (FQS) calculator.

Formula:
    Quality@1(t) = Pass@1(t) × (1 - min(1, β × SQALE_Index(t) / NCLOC(t)))

Usage:
    python compute_fqs.py <pass_at_1> <sqale_index> <ncloc> [--beta BETA]
"""

import argparse
from typing import Optional

BETA = 0.1


def compute_fqs(
    pass_at_1: float,
    sqale_index: float,
    ncloc: float,
    beta: float = BETA,
) -> Optional[float]:
    """Return Quality@1 for a single task, or None when inputs are invalid."""
    if pass_at_1 == 0.0:
        return 0.0
    if ncloc == 0:
        return None
    penalty = min(1.0, beta * sqale_index / ncloc)
    return pass_at_1 * (1.0 - penalty)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Compute Quality@1 (FQS) for a single task."
    )
    parser.add_argument("pass_at_1",   type=float, help="Pass@1 value (0 or 1)")
    parser.add_argument("sqale_index", type=float, help="SQALE index (minutes of technical debt)")
    parser.add_argument("ncloc",       type=float, help="Non-commented lines of code")
    parser.add_argument("--beta",      type=float, default=BETA, help=f"Penalty weight (default: {BETA})")
    args = parser.parse_args()

    result = compute_fqs(args.pass_at_1, args.sqale_index, args.ncloc, args.beta)
    if result is None:
        print("None  # undefined: pass=1 but ncloc=0")
    else:
        print(f"{result:.6f}")


if __name__ == "__main__":
    main()

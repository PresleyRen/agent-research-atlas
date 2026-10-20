#!/usr/bin/env python3
"""Synthetic routing fixture for testing record plumbing, not research evidence."""

import argparse
import json
import random
import sys
import time


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=7)
    parser.add_argument("--mode", choices=("success", "fail", "timeout"), default="success")
    args = parser.parse_args()
    if args.mode == "fail":
        print("SYNTHETIC intentional failed experiment", flush=True)
        print("SYNTHETIC fixture failure; preserve this stderr", file=sys.stderr, flush=True)
        return 7
    if args.mode == "timeout":
        print("SYNTHETIC waiting to exercise timeout preservation", flush=True)
        time.sleep(5)
        return 0
    rng = random.Random(args.seed)
    labels = [rng.choice(("cancel", "status", "refund")) for _ in range(60)]
    # This synthetic dataset and these rules were authored together. The result
    # only tests the recording workflow; it cannot support a real agent claim.
    baseline = sum(label == "status" for label in labels) / len(labels)
    result = {
        "schema_version": 1,
        "synthetic": True,
        "status": "succeeded",
        "metrics": {"accuracy": 1.0, "constant_baseline_accuracy": baseline},
        "elapsed_seconds": 0.0,
        "notes": "SYNTHETIC hand-authored routing fixture. No model, real users, benchmark, or scientific finding.",
    }
    print(json.dumps(result, sort_keys=True, allow_nan=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

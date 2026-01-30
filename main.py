#!/usr/bin/env python3
"""
Deploy MonkeyApe (MAPE) token contract using Python and web3.py.

Prerequisites:
  - Compile first: npx hardhat compile
  - Set RPC URL and deployer private key (optional for local chain):

    export RPC_URL=http://127.0.0.1:8545
    export DEPLOYER_PRIVATE_KEY=0x...

  For local Hardhat node, you can use the default test key:
    export DEPLOYER_PRIVATE_KEY=0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80
"""

import json
import os
import subprocess
import sys
from pathlib import Path

try:
    from web3 import Web3
except ImportError:
    print("Install dependencies: pip install -r requirements.txt")
    sys.exit(1)

# Paths relative to project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent
ARTIFACT_PATH = PROJECT_ROOT / "artifacts" / "contracts" / "MonkeyApe.sol" / "MonkeyApe.json"


def compile_contract():
    """Run Hardhat compile so artifact exists."""
    if ARTIFACT_PATH.exists():
        return True
    print("Compiling contracts (npx hardhat compile)...")
    result = subprocess.run(
        ["npx", "hardhat", "compile"],
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(result.stderr or result.stdout)
        return False
    return ARTIFACT_PATH.exists()


def load_artifact():
    with open(ARTIFACT_PATH, encoding="utf-8") as f:
        return json.load(f)


def main():
    rpc_url = os.environ.get("RPC_URL", "http://127.0.0.1:8545")
    pk = os.environ.get("DEPLOYER_PRIVATE_KEY")

    w3 = Web3(Web3.HTTPProvider(rpc_url))
    if not w3.is_connected():
        print(f"Cannot connect to RPC: {rpc_url}")
        sys.exit(1)
    print(f"Connected to {rpc_url} (chain_id={w3.eth.chain_id})")

    if not pk:
        print("Set DEPLOYER_PRIVATE_KEY in the environment to deploy.")
        sys.exit(1)

    if not compile_contract():
        print("Compilation failed.")

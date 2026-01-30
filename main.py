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

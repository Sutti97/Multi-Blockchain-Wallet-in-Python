# Import dependencies
import subprocess
import json
from dotenv import load_dotenv
from eth_account import Account
import os 

# Load and set environment variables
load_dotenv()
mnemonic = Account.from_key(os.getenv("mnemonic"))
# mnemonic=.getenv("mnemonic")
cmd = 'php derive -g --mnemonic='+mnemonic+' --cols=path,address,privkey,pubkey --format=json'

# Import constants.py and necessary functions from bit and web3
from constants import *
 
 
# Create a function called `derive_wallets`
def derive_wallets(cmd1):
    command = cmd1
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()
    return json.loads(output)

# Create a dictionary object called coins to store the output from `derive_wallets`.
coins = derive_wallets(cmd)

# Create a function called `priv_key_to_account` that converts privkey strings to account objects.
def priv_key_to_account(# YOUR CODE HERE):
    # YOUR CODE HERE

# Create a function called `create_tx` that creates an unsigned transaction appropriate metadata.
def create_tx(# YOUR CODE HERE):
    # YOUR CODE HERE

# Create a function called `send_tx` that calls `create_tx`, signs and sends the transaction.
def send_tx(# YOUR CODE HERE):
    # YOUR CODE HERE


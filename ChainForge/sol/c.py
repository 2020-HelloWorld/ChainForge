from web3 import Account
from web3 import Web3
from web3.contract import Contract

# from web3.auto import w3
from web3.exceptions import BadFunctionCallOutput
from flask import Flask
import web3

# Connect to an Ethereum node
w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
assert True is w3.is_connected()
# Load the contract bytecode and ABI from files
with open("cbi.bin", "r") as f:
    bytecode = f.read()
with open("contract.abi", "r") as f:
    abi = f.read()

# Create a new account
# account = Account.create()

# Print the account address and private key
# print("Account address:", account.address)
# print("Account private key:", account._private_key.hex())

# Create a contract instance
contract_mi = w3.eth.contract(
    abi=abi, bytecode=bytecode, address="0x5540a95552a9bB12a50F364a11EEC196dD7be756"
)

app = Flask(__name__)

private_key = "0xb837b04cfcddac059f8bef88d87f83b9069b3e2acd466685420a5137e3d6c6bb"

# Create an account object from the private key
account = Account.from_key(private_key)

# Get the latest nonce value
nonce = w3.eth.get_transaction_count(account.address)
# print(nonce)


# # Encode function call data
# reg = contract_mi.functions.register("Urmin").build_transaction(
#     {"from": account.address, "gas": 3000000, "gasPrice": 853803135, "nonce": nonce}
# )
# # .buildTransaction(
# #     {"from": account.address, "gas": 3000000, "gasPrice": 552132826, "nonce": nonce}
# # )


# signed_txn = account.sign_transaction(reg)
# tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
# receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

# # Print the transaction receipt
# print(receipt)


# Create a transaction object for the contract function call
transaction = contract_mi.functions.createProject(
    "Reshma", "Paddy", 2
).build_transaction(
    {"from": account.address, "gas": 3000000, "gasPrice": 574826203, "nonce": nonce}
)
signed_txn = account.sign_transaction(transaction)

# Send the signed transaction to the network
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

# Wait for the transaction to be mined
receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

# Print the transaction receipt
print(receipt)

# # Instantiate a new contract object using the loaded ABI and contract address


# # @app.route("/")
# # def index():
# #     # Call a contract function and return the result to the view
# #     # result = contract.functions.createProject('Reshma', 'Paddy', 2).call()
# #     print("result")
# #     # reg = contract.functions.register("Urmil").call()
# #     # create_prod = contract.functions.createProject("Reshma", "Paddy", 2).call()
# #     # result = contract.functions.returnProj(1).call()
# #     # return str(result)


# # if __name__ == "__main__":
# #     app.run()

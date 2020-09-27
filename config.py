import json

API_ENDPOINT = "http://localhost:2222"
private_key = "0x9aede013637152836b14b423dabef30c9b880ea550dbec132183ace7ca6177ed"
source_addr = "0x53781e106a2e3378083bdcede1874e5c2a7225f8"

withdraw_contract_abi = json.loads(
    '[{"constant":false,"inputs":[{"name":"_addr","type":"string"},{"name":"_amount","type":"uint256"},{"name":"_fee","type":"uint256"}],"name":"receivePayload","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_addr","type":"string"},{"indexed":false,"name":"_amount","type":"uint256"},{"indexed":false,"name":"_crosschainamount","type":"uint256"},{"indexed":true,"name":"_sender","type":"address"}],"name":"PayloadReceived","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_sender","type":"address"},{"indexed":false,"name":"_amount","type":"uint256"},{"indexed":true,"name":"_black","type":"address"}],"name":"EtherDeposited","type":"event"}]')
withdraw_contract_address_test = "0x491bC043672B9286fA02FA7e0d6A3E5A0384A31A"
withdraw_contract_address_mainnet = "0xC445f9487bF570fF508eA9Ac320b59730e81e503"
withdraw_fee = 100000000000000
withdraw_gas = 3000000
gas_price = 0.00002

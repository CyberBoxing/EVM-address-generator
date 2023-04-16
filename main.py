from eth_account import Account

# Enabling the use of functions to work with Mnemonic
Account.enable_unaudited_hdwallet_features()


count = int(input('Enter the required number of addresses: '))

for i in range(0, count + 1):
    acc, seed_phrase = Account.create_with_mnemonic()

    with open('addresses.txt', 'a') as file:
        file.write(f'{i}\nAddress: {acc.address}\nSeed phrase: {seed_phrase}\nPrivate key: {acc.key.hex()}\n\n')


print(f'created {count} addresses')

# How Bitcoin-Blockchain Works - Notes

- [How Bitcoin-Blockchain Works - Notes](#how-bitcoin-blockchain-works---notes)
  - [Helpful Resources](#helpful-resources)
  - [Bitcoin](#bitcoin)
    - [Unspent Transaction Output (UTXO)](#unspent-transaction-output-utxo)
  - [Blockchain](#blockchain)
    - [What does each block have](#what-does-each-block-have)
    - [What is a permissionless blockchain?](#what-is-a-permissionless-blockchain)
      - [Consensus Algorithm](#consensus-algorithm)
    - [What is a permissioned blockchain?](#what-is-a-permissioned-blockchain)

## Helpful Resources

IBM Lecture: https://mediacenter.ibm.com/media/Blockchain%20Explained/1_e34h0ey8

The Bitcoin Protocol Explained: How it Actually Works: https://komodoplatform.com/en/academy/bitcoin-protocol/

## Bitcoin

### Unspent Transaction Output (UTXO)

See: https://komodoplatform.com/en/academy/bitcoin-protocol/

## Blockchain

### What does each block have

- A hash
- A list of transactions that have occurred on that block
- Previous block's hash

### What is a permissionless blockchain?

These are what is used by cryptocurrencies. Everyone can see all transactions that have ever taken place. You will see the transactions by each person's address. Any time it gets updated and new transactions are made you get a new block.

#### Consensus Algorithm

You have all these transactions coming in how do you decide which transactions will make up the next block. 

1. A client will first submit a transaction and that transaction will join a list of other transactions that have been made on the network.
2. A node will start picking up the transactions, look through all the previous transactions on the blockchain and know those are valid. It will kind of emulate a block and then start a proof of work algorithm.
   1. The proof of work algorithm is a complex crypto-hash algorithm everyone works together to solve. Once one node resolves it, it will broadcast the position of that next block to all the other nodes in the network.

### What is a permissioned blockchain?

There is an idea called pluggable consensus algorithms. You can use this when the nodes in the blockchain are trusted. In addition, the nodes may not be just users but entire organizations. Privacy here is important.

Scenario: You have a retailer who buys 100 pounds of something at $1000. Then you have a shipper who wants $100 for shipping. The shipper should know when the order was placed, for what, and how much they charged, but they wouldn't know how much the total original cost was.

Smart contracts: This allows you to do something like make sure the warehouse has enough goods at the manufacturer, the retailer has enough money to pay the shipper, and you can take automated action (like refunding money when goods aren't available) based on this information.
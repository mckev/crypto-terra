# terra

My learning on internal working of terra (luna) coin

- Generate 24 "mnemonic" words to construct an arbitrary 256-bit number + 8-bit checksum. Each word corresponds to a
  11-bit number.
- These mnemonic words are converted into a 512-bit number called "seed".
- From the seed, we can generate chains of public key and private key pairs deterministically. Terra is using a specific
  path: m/44'/330'/0'/0/0.
- From the 256-bit public key, we can generate the wallet address by hashing it twice: ripemd160(sha256(public_key)).
  This is the same as Bitcoin.
- Lastly for Terra, this wallet address is encoded with a base32 variant encoding with checksum, called Bech32. This is
  the wallet address which you can give to anyone.

Using the above, I can generate wallet addresses which have my name as prefix :).

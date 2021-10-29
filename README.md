# ckb-address-demo

CKB address format demo code.

Based on original Bech32 demo code form: https://github.com/sipa/bech32/tree/master/ref/python

```yml
== default short address (code_hash_index = 0x00) test ==
args to encode:          b39bbc0b3673c7d36450bc14cfcdad2d559c6c64
mainnet address:	 ckb1qyqt8xaupvm8837nv3gtc9x0ekkj64vud3jqfwyw5v
testnet address:	 ckt1qyqt8xaupvm8837nv3gtc9x0ekkj64vud3jq5t63cs
>> decode address:
 - format type:          short
 - code_hash_index:      0
 - args:                 b39bbc0b3673c7d36450bc14cfcdad2d559c6c64

== multisign short address (code_hash_index = 0x01) test ==
multi sign script:	 00010203bd07d9f32bce34d27152a6a0391d324f79aab854094ee28566dff02a012a66505822a2fd67d668fb4643c241e59e81b7876527ebff23dfb24cf16482
args to encode:		 4fb2be2e5d0c1a3b8694f832350a33c1685d477a
mainnet address:	 ckb1qyq5lv479ewscx3ms620sv34pgeuz6zagaaqklhtgg
testnet address:	 ckt1qyq5lv479ewscx3ms620sv34pgeuz6zagaaqt6f5y5
>> decode address:
  - format type:         short
  - code_hash_index:	 1
  - args:		 4fb2be2e5d0c1a3b8694f832350a33c1685d477a

== acp short address (code_hash_index = 0x02) test ==
args to encode:          bd07d9f32bce34d27152a6a0391d324f79aab854
mainnet address:	 ckb1qypt6p7e7v4uudxjw9f2dgper5ey77d2hp2qxz4u4u
testnet address:	 ckt1qypt6p7e7v4uudxjw9f2dgper5ey77d2hp2qm8treq
>> decode address:
 - format type:          short
 - code_hash_index:      2
 - args:                 bd07d9f32bce34d27152a6a0391d324f79aab854

== full address test (hash_type = 0x00) test ==
code_hash to encode:	 9bd7e06f3ecf4be0f2fcd2188b23f1b9fcc88e5d4b65a8637b17723bbda3cce8
with args to encode:	 b39bbc0b3673c7d36450bc14cfcdad2d559c6c64
mainnet address:	 ckb1qzda0cr08m85hc8jlnfp3zer7xulejywt49kt2rr0vthywaa50xwsq9nnw7qkdnnclfkg59uzn8umtfd2kwxceqvguktl
testnet address:	 ckt1qzda0cr08m85hc8jlnfp3zer7xulejywt49kt2rr0vthywaa50xwsq9nnw7qkdnnclfkg59uzn8umtfd2kwxceqz6hep8
>> decode address:
  - format type:	 full
  - code hash:		 9bd7e06f3ecf4be0f2fcd2188b23f1b9fcc88e5d4b65a8637b17723bbda3cce8
  - hash type:		 00
  - args:		 b39bbc0b3673c7d36450bc14cfcdad2d559c6c64

== full address test (hash_type = 0x01) ==
code_hash to encode:     9bd7e06f3ecf4be0f2fcd2188b23f1b9fcc88e5d4b65a8637b17723bbda3cce8
with args to encode:     b39bbc0b3673c7d36450bc14cfcdad2d559c6c64
mainnet address:	 ckb1qzda0cr08m85hc8jlnfp3zer7xulejywt49kt2rr0vthywaa50xwsqdnnw7qkdnnclfkg59uzn8umtfd2kwxceqxwquc4
testnet address:	 ckt1qzda0cr08m85hc8jlnfp3zer7xulejywt49kt2rr0vthywaa50xwsqdnnw7qkdnnclfkg59uzn8umtfd2kwxceqgutnjd
>> decode address:
 - format type:          full
 - code hash:            9bd7e06f3ecf4be0f2fcd2188b23f1b9fcc88e5d4b65a8637b17723bbda3cce8
 - hash type:            01
 - args:                 b39bbc0b3673c7d36450bc14cfcdad2d559c6c64

 == full address test (hash_type = 0x02) ==
code_hash to encode:     9bd7e06f3ecf4be0f2fcd2188b23f1b9fcc88e5d4b65a8637b17723bbda3cce8
with args to encode:     b39bbc0b3673c7d36450bc14cfcdad2d559c6c64
mainnet address:	 ckb1qzda0cr08m85hc8jlnfp3zer7xulejywt49kt2rr0vthywaa50xwsq4nnw7qkdnnclfkg59uzn8umtfd2kwxceqcydzyt
testnet address:	 ckt1qzda0cr08m85hc8jlnfp3zer7xulejywt49kt2rr0vthywaa50xwsq4nnw7qkdnnclfkg59uzn8umtfd2kwxceqkkxdwn
>> decode address:
 - format type:          full
 - code hash:            9bd7e06f3ecf4be0f2fcd2188b23f1b9fcc88e5d4b65a8637b17723bbda3cce8
 - hash type:            02
 - args:                 b39bbc0b3673c7d36450bc14cfcdad2d559c6c64

== deprecated full address (code_type = Data) test ==
code_hash to encode:	 9bd7e06f3ecf4be0f2fcd2188b23f1b9fcc88e5d4b65a8637b17723bbda3cce8
with args to encode:	 b39bbc0b3673c7d36450bc14cfcdad2d559c6c64
mainnet address:	 ckb1q2da0cr08m85hc8jlnfp3zer7xulejywt49kt2rr0vthywaa50xw3vumhs9nvu786dj9p0q5elx66t24n3kxgdwd2q8
testnet address:	 ckt1q2da0cr08m85hc8jlnfp3zer7xulejywt49kt2rr0vthywaa50xw3vumhs9nvu786dj9p0q5elx66t24n3kxgqd588c
>> decode address:
  - format type:         deprecated full
  - code type:		 Data
  - code hash:		 9bd7e06f3ecf4be0f2fcd2188b23f1b9fcc88e5d4b65a8637b17723bbda3cce8
  - args:		 b39bbc0b3673c7d36450bc14cfcdad2d559c6c64

== deprecated full address (code_type = Type) test ==
code_hash to encode:	 9bd7e06f3ecf4be0f2fcd2188b23f1b9fcc88e5d4b65a8637b17723bbda3cce8
with args to encode:	 b39bbc0b3673c7d36450bc14cfcdad2d559c6c64
mainnet address:         ckb1qjda0cr08m85hc8jlnfp3zer7xulejywt49kt2rr0vthywaa50xw3vumhs9nvu786dj9p0q5elx66t24n3kxgj53qks
testnet address:         ckt1qjda0cr08m85hc8jlnfp3zer7xulejywt49kt2rr0vthywaa50xw3vumhs9nvu786dj9p0q5elx66t24n3kxglhgd30
>> decode address:
  - format type:         deprecated full
  - code type:		 Type
  - code hash:		 9bd7e06f3ecf4be0f2fcd2188b23f1b9fcc88e5d4b65a8637b17723bbda3cce8
  - args:		 b39bbc0b3673c7d36450bc14cfcdad2d559c6c64
```

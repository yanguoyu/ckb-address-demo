#!/usr/bin/python3

# CKB Address test code
# cipher@nervos.org


import segwit_addr as sa
import hashlib
import unittest

def ckbhash():
    return hashlib.blake2b(digest_size=32, person=b'ckb-default-hash')

# ref: https://github.com/nervosnetwork/rfcs/blob/master/rfcs/0021-ckb-address-format/0021-ckb-address-format.md
FORMAT_TYPE_FULL      = 0x00
FORMAT_TYPE_SHORT     = 0x01
FORMAT_TYPE_FULL_DATA = 0x02
FORMAT_TYPE_FULL_TYPE = 0x04

CODE_INDEX_SECP256K1_SINGLE = 0x00
CODE_INDEX_SECP256K1_MULTI  = 0x01
CODE_INDEX_ACP              = 0x02

BECH32_CONST = 1
BECH32M_CONST = 0x2bc830a3

# ref: https://github.com/nervosnetwork/rfcs/blob/master/rfcs/0024-ckb-system-script-list/0024-ckb-system-script-list.md
SCRIPT_CONST_MAINNET = {
    CODE_INDEX_SECP256K1_SINGLE : {
        "code_hash" : "0x9bd7e06f3ecf4be0f2fcd2188b23f1b9fcc88e5d4b65a8637b17723bbda3cce8",
        "hash_type" : "type",
        "tx_hash"   : "0x71a7ba8fc96349fea0ed3a5c47992e3b4084b031a42264a018e0072e8172e46c",
        "index"     : "0",
        "dep_type"  : "dep_group"
    },
    CODE_INDEX_SECP256K1_MULTI : {
        "code_hash" : "0x5c5069eb0857efc65e1bca0c07df34c31663b3622fd3876c876320fc9634e2a8",
        "hash_type" : "type",
        "tx_hash"   : "0x71a7ba8fc96349fea0ed3a5c47992e3b4084b031a42264a018e0072e8172e46c",
        "index"     : "1",
        "dep_type"  : "dep_group"
    },
    CODE_INDEX_ACP : {
        "code_hash" : "0xd369597ff47f29fbc0d47d2e3775370d1250b85140c670e4718af712983a2354",
        "hash_type" : "type",
        "tx_hash"   : "0x4153a2014952d7cac45f285ce9a7c5c0c0e1b21f2d378b82ac1433cb11c25c4d",
        "index"     : "0",
        "dep_type"  : "dep_group"
    }
}

SCRIPT_CONST_TESTNET = {
    CODE_INDEX_SECP256K1_SINGLE : {
        "code_hash" : "0x9bd7e06f3ecf4be0f2fcd2188b23f1b9fcc88e5d4b65a8637b17723bbda3cce8",
        "hash_type" : "type",
        "tx_hash"   : "0xf8de3bb47d055cdf460d93a2a6e1b05f7432f9777c8c474abf4eec1d4aee5d37",
        "index"     : "0",
        "dep_type"  : "dep_group"
    },
    CODE_INDEX_SECP256K1_MULTI : {
        "code_hash" : "0x5c5069eb0857efc65e1bca0c07df34c31663b3622fd3876c876320fc9634e2a8",
        "hash_type" : "type",
        "tx_hash"   : "0xf8de3bb47d055cdf460d93a2a6e1b05f7432f9777c8c474abf4eec1d4aee5d37",
        "index"     : "1",
        "dep_type"  : "dep_group"
    },
    CODE_INDEX_ACP : {
        "code_hash" : "0x3419a1c09eb2567f6552ee7a8ecffd64155cffe0f1796e6e61ec088d740c1356",
        "hash_type" : "type",
        "tx_hash"   : "0xec26b0f85ed839ece5f11c4c4e837ec359f5adc4420410f6453b1f6b60fb96a6",
        "index"     : "0",
        "dep_type"  : "dep_group"
    }
}

def generateShortAddress(code_index, args, network = "mainnet"):
    """ generate a short ckb address """
    hrp = {"mainnet": "ckb", "testnet": "ckt"}[network]
    hrpexp =  sa.bech32_hrp_expand(hrp)
    format_type  = FORMAT_TYPE_SHORT
    payload = bytes([format_type, code_index]) + bytes.fromhex(args)
    data_part = sa.convertbits(payload, 8, 5)
    values = hrpexp + data_part
    polymod = sa.bech32_polymod(values + [0, 0, 0, 0, 0, 0]) ^ BECH32_CONST
    checksum = [(polymod >> 5 * (5 - i)) & 31 for i in range(6)]
    combined = data_part + checksum
    addr = hrp + '1' + ''.join([sa.CHARSET[d] for d in combined])
    return addr

def generateFullAddress(code_hash, hash_type, args, network = "mainnet"):
    hrp = {"mainnet": "ckb", "testnet": "ckt"}[network]
    hrpexp =  sa.bech32_hrp_expand(hrp)
    format_type  = FORMAT_TYPE_FULL
    payload = bytes([format_type]) + bytes.fromhex(code_hash)
    payload += bytes([hash_type]) + bytes.fromhex(args)
    data_part = sa.convertbits(payload, 8, 5)
    values = hrpexp + data_part
    polymod = sa.bech32_polymod(values + [0, 0, 0, 0, 0, 0]) ^ BECH32M_CONST
    checksum = [(polymod >> 5 * (5 - i)) & 31 for i in range(6)]
    combined = data_part + checksum
    addr = hrp + '1' + ''.join([sa.CHARSET[d] for d in combined])
    return addr

def generateDeprecatedFullAddress(hash_type, code_hash, args, network = "mainnet"):
    format_type = {"Data" : bytes([FORMAT_TYPE_FULL_DATA]),
                 "Type" : bytes([FORMAT_TYPE_FULL_TYPE])}[hash_type]
    hrp = {"mainnet": "ckb", "testnet": "ckt"}[network]
    hrpexp =  sa.bech32_hrp_expand(hrp)
    payload = bytes(format_type) + bytes.fromhex(code_hash)
    payload += bytes.fromhex(args)
    data_part = sa.convertbits(payload, 8, 5)
    values = hrpexp + data_part
    polymod = sa.bech32_polymod(values + [0, 0, 0, 0, 0, 0]) ^ BECH32_CONST
    checksum = [(polymod >> 5 * (5 - i)) & 31 for i in range(6)]
    combined = data_part + checksum
    addr = hrp + '1' + ''.join([sa.CHARSET[d] for d in combined])
    return addr

def decodeAddress(addr, network = "mainnet"):
    hrp = {"mainnet": "ckb", "testnet": "ckt"}[network]
    hrpgot, data, spec = sa.bech32_decode(addr)
    if hrpgot != hrp or data == None:
        return False
    print(" - addr:\t\t", addr)
    print(" - bech32_decode data:\t\t", data)
    decoded = sa.convertbits(data, 5, 8, False)
    if decoded == None:
        return False
    payload = bytes(decoded)
    format_type = payload[0]
    if format_type == FORMAT_TYPE_FULL:
        ptr = 1
        code_hash = payload[ptr : ptr+32].hex()
        ptr += 32
        hash_type = payload[ptr : ptr+1].hex()
        ptr += 1
        args = payload[ptr :].hex()
        return ("full", code_hash, hash_type, args)
    elif format_type == FORMAT_TYPE_SHORT:
        code_index = payload[1]
        pk = payload[2:].hex()
        return ("short", code_index, pk)
    elif format_type == FORMAT_TYPE_FULL_DATA or format_type == FORMAT_TYPE_FULL_TYPE:
        full_type = {FORMAT_TYPE_FULL_DATA:"Data", FORMAT_TYPE_FULL_TYPE:"Type"}[format_type]
        ptr = 1
        code_hash = payload[ptr : ptr+32].hex()
        ptr += 32
        args = payload[ptr :].hex()
        return ("deprecated full", full_type, code_hash, args)

def expandShortAddress(address):
    network = address[:3]
    content = decodeAddress(address, "mainnet" if network=="ckb" else "testnet")
    if content == False or content[0] == "full":
        return False
    script_dict = SCRIPT_CONST_MAINNET if network == "ckb" else SCRIPT_CONST_TESTNET
    code_index = content[1]
    code_setup = script_dict[code_index]
    lock_script = {
        "Code Hash" : code_setup["code_hash"],
        "Hash Type" : code_setup["hash_type"],
        "args"      : content[2]
    }
    return lock_script

if __name__ == "__main__":
    # setup network
    mainnet = "mainnet"
    testnet = "testnet"

    # test constant parameters
    SECP256K1_CODE_HASH = "9bd7e06f3ecf4be0f2fcd2188b23f1b9fcc88e5d4b65a8637b17723bbda3cce8"
    SECP256K1_MULTISIGN_CODE_HASH = "5c5069eb0857efc65e1bca0c07df34c31663b3622fd3876c876320fc9634e2a8"
    PKBLAKE160 = "b39bbc0b3673c7d36450bc14cfcdad2d559c6c64"
    PKBLAKE_Alice = "3403fcbbd9e20fa31e722eb9981b2203ad475904" ## ckt1qyqrgqluh0v7yrarreezawvcrv3q8t28tyzqveg4zl
    PKBLAKE_Bob = "c75e25d1a08c03617fd7211607a0a7479ad2ec31" ## ckt1qyqvwh396xsgcqmp0ltjz9s85zn50xkjascsz88vrw
    PKBLAKE_Cipher = "cdef55dcb787257236bbe8d8c338951b4290ca69" ## ckt1qyqvmm64mjmcwftjx6a73kxr8z23ks5sef5sv2702w
    MULTI_SISG_PREFIX = b'\x00\x01\x02\x03'

    # # test short address (code_hash_index = 0x00) functions
    # print("== default short address (code_hash_index = 0x00) test ==")
    # args = PKBLAKE160
    # print("args to encode:\t\t", args)
    # mainnet_addr_short = generateShortAddress(CODE_INDEX_SECP256K1_SINGLE, args, mainnet)
    # testnet_addr_short = generateShortAddress(CODE_INDEX_SECP256K1_SINGLE, args, testnet)
    # print("mainnet address:\t", mainnet_addr_short)
    # print("testnet address:\t", testnet_addr_short)
    # decoded = decodeAddress(mainnet_addr_short, mainnet)
    # print(">> decode address:")
    # print(" - format type:\t\t", decoded[0])
    # print(" - code_hash_index:\t", decoded[1])
    # print(" - args:\t\t", decoded[2])
    # print(">> expand to script")
    # print(expandShortAddress(mainnet_addr_short))

    # # test short address (code_hash_index = 0x01) functions
    # print("\n== multisign short address (code_hash_index = 0x01) test ==")
    # multi_sign_script = MULTI_SISG_PREFIX \
    #     + bytes.fromhex(PKBLAKE_Cipher) \
    #     + bytes.fromhex(PKBLAKE_Alice) \
    #     + bytes.fromhex(PKBLAKE_Bob)
    # hasher = ckbhash()
    # hasher.update(multi_sign_script)
    # multi_sign_script_hash = hasher.hexdigest()
    # args = multi_sign_script_hash[:40]
    # print("multi sign script:\t", multi_sign_script.hex())
    # print("args to encode:\t\t", args)
    # mainnet_addr_short = generateShortAddress(CODE_INDEX_SECP256K1_MULTI, args, mainnet)
    # testnet_addr_short = generateShortAddress(CODE_INDEX_SECP256K1_MULTI, args, testnet)
    # print("mainnet address:\t", mainnet_addr_short)
    # print("testnet address:\t", testnet_addr_short)
    # decoded = decodeAddress(mainnet_addr_short, mainnet)
    # print(">> decode address:")
    # print(" - format type:\t\t", decoded[0])
    # print(" - code_hash_index:\t", decoded[1])
    # print(" - args:\t\t", decoded[2])
    # print(">> expand to script")
    # print(expandShortAddress(mainnet_addr_short))

    # # test short address (code_hash_index = 0x02) functions
    # print("\n== acp short address (code_hash_index = 0x02) test ==")
    # args = PKBLAKE_Cipher
    # print("args to encode:\t\t", args)
    # mainnet_addr_short = generateShortAddress(CODE_INDEX_ACP, args, mainnet)
    # testnet_addr_short = generateShortAddress(CODE_INDEX_ACP, args, testnet)
    # print("mainnet address:\t", mainnet_addr_short)
    # print("testnet address:\t", testnet_addr_short)
    # decoded = decodeAddress(mainnet_addr_short, mainnet)
    # print(">> decode address:")
    # print(" - format type:\t\t", decoded[0])
    # print(" - code_hash_index:\t", decoded[1])
    # print(" - args:\t\t", decoded[2])
    # print(">> expand to script")
    # print(expandShortAddress(mainnet_addr_short))

    # # test full address (hash_type = 0x00) functions
    # print("\n== full address (hash_type = 0x00) test ==")
    # code_hash = SECP256K1_CODE_HASH
    # hash_type = 0x00
    # args = PKBLAKE160
    # print("code_hash to encode:\t", code_hash)
    # print("with args to encode:\t", args)
    # mainnet_addr_full = generateFullAddress(code_hash, hash_type, args, mainnet)
    # testnet_addr_full = generateFullAddress(code_hash, hash_type, args, testnet)
    # print("mainnet address:\t", mainnet_addr_full)
    # print("testnet address:\t", testnet_addr_full)
    # decoded = decodeAddress(mainnet_addr_full, mainnet)
    # print(">> decode address:")
    # print(" - format type:\t\t", decoded[0])
    # print(" - code hash:\t\t", decoded[1])
    # print(" - hash type:\t\t", decoded[2])
    # print(" - args:\t\t", decoded[3])

    # # test full address (hash_type = 0x01) functions
    # print("\n== full address (hash_type = 0x01) test ==")
    # code_hash = SECP256K1_CODE_HASH
    # hash_type = 0x01
    # args = PKBLAKE160
    # print("code_hash to encode:\t", code_hash)
    # print("with args to encode:\t", args)
    # mainnet_addr_full = generateFullAddress(code_hash, hash_type, args, mainnet)
    # testnet_addr_full = generateFullAddress(code_hash, hash_type, args, testnet)
    # print("mainnet address:\t", mainnet_addr_full)
    # print("testnet address:\t", testnet_addr_full)
    # decoded = decodeAddress(mainnet_addr_full, mainnet)
    # print(">> decode address:")
    # print(" - format type:\t\t", decoded[0])
    # print(" - code hash:\t\t", decoded[1])
    # print(" - hash type:\t\t", decoded[2])
    # print(" - args:\t\t", decoded[3])

    # # test full address (hash_type = 0x02) functions
    # print("\n== full address (hash_type = 0x02) test ==")
    # code_hash = SECP256K1_CODE_HASH
    # hash_type = 0x02
    # args = PKBLAKE160
    # print("code_hash to encode:\t", code_hash)
    # print("with args to encode:\t", args)
    # mainnet_addr_full = generateFullAddress(code_hash, hash_type, args, mainnet)
    # testnet_addr_full = generateFullAddress(code_hash, hash_type, args, testnet)
    # print("mainnet address:\t", mainnet_addr_full)
    # print("testnet address:\t", testnet_addr_full)
    # decoded = decodeAddress(mainnet_addr_full, mainnet)
    # print(">> decode address:")
    # print(" - format type:\t\t", decoded[0])
    # print(" - code hash:\t\t", decoded[1])
    # print(" - hash type:\t\t", decoded[2])
    # print(" - args:\t\t", decoded[3])

    # # test deprecated full address (code_type = Data) functions
    # print("\n== deprecated full address (code_type = Data) test ==")
    # code_hash = SECP256K1_CODE_HASH
    # args = PKBLAKE160
    # print("code_hash to encode:\t", code_hash)
    # print("with args to encode:\t", args)
    # mainnet_addr_full = generateDeprecatedFullAddress("Data", code_hash, args, mainnet)
    # testnet_addr_full = generateDeprecatedFullAddress("Data", code_hash, args, testnet)
    # print("mainnet address:\t", mainnet_addr_full)
    # print("testnet address:\t", testnet_addr_full)
    # decoded = decodeAddress(mainnet_addr_full, mainnet)
    # print(">> decode address:")
    # print(" - format type:\t\t", decoded[0])
    # print(" - code type:\t\t", decoded[1])
    # print(" - code hash:\t\t", decoded[2])
    # print(" - args:\t\t", decoded[3])

    # # test deprecated full address (code_type = Type) functions
    # print("\n== deprecated full address (code_type = Type) test ==")
    # code_hash = SECP256K1_CODE_HASH
    # args = PKBLAKE160
    # print("code_hash to encode:\t", code_hash)
    # print("with args to encode:\t", args)   
    # mainnet_addr_full = generateDeprecatedFullAddress("Type", code_hash, args, mainnet)
    # testnet_addr_full = generateDeprecatedFullAddress("Type", code_hash, args, testnet)
    # print("mainnet address:\t", mainnet_addr_full)
    # print("testnet address:\t", testnet_addr_full)
    # decoded = decodeAddress(mainnet_addr_full, mainnet)
    # print(">> decode address:")
    # print(" - format type:\t\t", decoded[0])
    # print(" - code type:\t\t", decoded[1])
    # print(" - code hash:\t\t", decoded[2])
    # print(" - args:\t\t", decoded[3])

    # test multisign full address (hash_type = 0x00) functions
    print("\n== full multisign address (hash_type = 0x00) test ==")
    code_hash = SECP256K1_MULTISIGN_CODE_HASH
    hash_type = 0x02
    print('bytes.fromhex(PKBLAKE_Cipher): \t', bytes.fromhex(PKBLAKE_Cipher))
    multi_sign_script = MULTI_SISG_PREFIX \
        + bytes.fromhex(PKBLAKE_Cipher) \
        + bytes.fromhex(PKBLAKE_Alice) \
        + bytes.fromhex(PKBLAKE_Bob)
    hasher = ckbhash()
    hasher.update(multi_sign_script)
    multi_sign_script_hash = hasher.hexdigest()
    args = multi_sign_script_hash[:40]
    print("multi sign script:\t", multi_sign_script.hex())
    print("code_hash to encode:\t", code_hash)
    print("with args to encode:\t", args)
    mainnet_addr_full = generateFullAddress(code_hash, hash_type, args, mainnet)
    testnet_addr_full = generateFullAddress(code_hash, hash_type, args, testnet)
    print("mainnet address:\t", mainnet_addr_full)
    print("testnet address:\t", testnet_addr_full)
    decoded = decodeAddress(mainnet_addr_full, mainnet)
    print(">> decode address:")
    print(" - format type:\t\t", decoded[0])
    print(" - code hash:\t\t", decoded[1])
    print(" - hash type:\t\t", decoded[2])
    print(" - args:\t\t", decoded[3])
    ## 下面是 sdk 生成的地址
    decoded1 = decodeAddress('ckt1qpw9q60tppt7l3j7r09qcp7lxnp3vcanvgha8pmvsa3jplykxn32sq2q2xyzry2ms80qv9xcc3wmaam32x3z45gut5d40', testnet)
    print(">> decoded1 address:")
    print(" - format type:\t\t", decoded1[0])
    print(" - code hash:\t\t", decoded1[1])
    print(" - hash type:\t\t", decoded1[2])
    print(" - args:\t\t", decoded1[3])
# Dynamic Radix Encryption (DRE)



## Quickstart
1. Go to `DRE.py` and see the code usage in `demo()`.<br>
2. Go to `challenge.py` to get started on cracking my cipher.

<hr>

## Table of Contents

* Scroll to **"What is dre-basic?"** for a rationale of this project.
* Scroll to **"Demo: how to use dre-basic"** for a code demo.
* Scroll to **"Files"** for a brief description of the files in this repo.

<hr>

## What is dre-basic?

This project is meant to be a basic demo of how **dynamic radix encryption (DRE)** can be implemented, as well as a challenge for the public. DRE is essentially base conversion, except the input and output symbol sets are unknown.

Usually when we do base conversion, we use standard symbol sets like binary (`01`), decimal (`0123456789`), or hex (`0123456789ABCDEF`). Since we all know about these symbol sets, we can easily convert bases in a standard way, like so:

| binary &rarr; decimal     | decimal &rarr; hex         | hex &rarr; binary                  |
|:--------------------------|:---------------------------|:-----------------------------------|
| `110100100` &rarr; `420`  | `11408351` &rarr; `AE13DF` | `10F2C` &rarr; `10000111100101100` |

But what if we didn't know the symbol sets? For example, if I was converting from hex to decimal using some arbitrary symbols other than `0123456789ABCDEF` and `0123456789`, we could get something like

| hex &rarr; decimal        |
|:--------------------------|
| `$*%%#@` &rarr; `m0xk7xk` |

Unless you know that the symbol sets I used were `!@#$%^&*()-=_+<>` for hex and `wkxmg80437` for decimal, you wouldn't immediately know how to convert between these two particular number systems. This is the basis of DRE.

In the above example, if we think of `$*%%#@` as plaintext and `m0xk7xk` as ciphertext, then we have an encryption system. This particular example is pretty easy to crack using known plaintext attack, since there are only `10! = 3,628,800` possible ciphertext symbol sets. But we can extend this to larger symbol sets that complicate an attacker's mission. For example:

| base-90 &rarr; base-79                                                                                 |
|:-------------------------------------------------------------------------------------------------------|
| `This is a secret message written in base-90.` &rarr; `p%,J54dnb'XI<TH?}YSL0HY5Tq('_'NIjjGDWVkHX75*?b` |

This ciphertext is harder to crack. The symbol sets used were:

**Plaintext symbol set (base-90):**<br>`E G)Z@o+."2i5;Q^6c~K}J9zXbIr&Fd4A'n_L,yfC*gx7#kTUDV1$SWhHjuOP%vwNt?-Ra:(><qps{B!m/Yl3M=e08`

**Ciphertext symbol set (base-79):**<br>`<?pzL%B3W~qUSX;xPhVTH$s&:YMojuDd.7)kJ5IGN=>8n(4-1^g9A#'_@b+irl"ewc*QE0,aC}ym/KO`

These two pieces of information together form the **key**.

<hr>

## Demo: how to use dre-basic

1. Let's choose the following symbol sets to encrypt and decrypt with (these are SECRET):<br><br>
	**Plaintext symbol set (base-90):**<br>`E G)Z@o+."2i5;Q^6c~K}J9zXbIr&Fd4A'n_L,yfC*gx7#kTUDV1$SWhHjuOP%vwNt?-Ra:(><qps{B!m/Yl3M=e08`<br><br>
	**Ciphertext symbol set (base-79):**<br>`<?pzL%B3W~qUSX;xPhVTH$s&:YMojuDd.7)kJ5IGN=>8n(4-1^g9A#'_@b+irl"ewc*QE0,aC}ym/KO`

<br>

2. We now create our DRE object with the following code:
```
pt_symbols = r'''E G)Z@o+."2i5;Q^6c~K}J9zXbIr&Fd4A'n_L,yfC*gx7#kTUDV1$SWhHjuOP%vwNt?-Ra:(><qps{B!m/Yl3M=e08'''
ct_symbols = r'''<?pzL%B3W~qUSX;xPhVTH$s&:YMojuDd.7)kJ5IGN=>8n(4-1^g9A#'_@b+irl"ewc*QE0,aC}ym/KO'''

dre = DRE(pt_symbols, ct_symbols)
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Note that our key (seen at `dre.key`) is a combination of both the plaintext symbol set and the ciphertext symbol set.<br>

<br>

3. Now let's choose the following plaintext, which uses the base-90 symbol set above:
```
plaintext = 'This is a secret message!'
```

<br>

4. Encrypt:
```
ciphertext = dre.encrypt(plaintext)

ciphertext
>>> 'hgB<7yUD,w0Isi).?>d.QW4G)1w'
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Note that this ciphertext will change with each run as there is a small element of randomness when encrypting. I don't believe this adds to the security, it's just a design choice (see the code in `DRE.py` for the implementation).

<br>

5. Decrypt:
```
decrypted = dre.decrypt(ciphertext)
```

<br>

6. Just to make sure, we can check if the system works:
```
decrypted == plaintext
>>> True
```

<hr>

## Files

* `base_conversion.py` contains all the functionality for converting between arbitrary bases.<br>
* `DRE.py` contains the main cryptographic functions (encrypt/decrypt), as well as a code demo.
* `challenge.py` contains the challenge prompt and the initial code you'll need to start cracking my cipher.

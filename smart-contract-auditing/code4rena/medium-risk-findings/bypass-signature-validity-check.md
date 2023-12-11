---
description: Submitted by (3) cryptphi, also found by 0x1f8b and defsec
---

# Bypass signature validity check

### Summary:

[https://code4rena.com/reports/2022-08-rigor/#m-03-signature-checks-could-be-passed-when-signaturedecoderrecoverkey-returns-0](https://code4rena.com/reports/2022-08-rigor/#m-03-signature-checks-could-be-passed-when-signaturedecoderrecoverkey-returns-0)

It is possible to pass Signature Validity check with an SignatureDecoder.recoverKey() returns 0 whenever the builder and /or contractor have an existing approved hash for a data.

### Mitigation:

There should be a require check for `_recoveredSignature != 0` in `checkSignatureValidity()`.

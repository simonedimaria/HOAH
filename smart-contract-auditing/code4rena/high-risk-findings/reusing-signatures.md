---
description: >-
  Submitted by (11) sseefried, also found by 0xA5DF, Bahurum, bin2chen, byndooa,
  cccz, GalloDaSballo, hyh, kankodu, Lambda, and minhquanym
---

# Reusing signatures

### Summary:

[https://code4rena.com/reports/2022-08-rigor/#h-03-builder-can-call-communityescrow-again-to-reduce-debt-further-using-same-signatures](https://code4rena.com/reports/2022-08-rigor/#h-03-builder-can-call-communityescrow-again-to-reduce-debt-further-using-same-signatures)\
[https://code4rena.com/reports/2022-08-rigor/#h-04-project-funds-can-be-drained-by-reusing-signatures-in-some-cases](https://code4rena.com/reports/2022-08-rigor/#h-04-project-funds-can-be-drained-by-reusing-signatures-in-some-cases)\
[https://code4rena.com/reports/2022-08-rigor/#m-13-in-projectsetcomplete-the-signature-can-be-reused-when-the-first-call-is-reverted-for-some-reason](https://code4rena.com/reports/2022-08-rigor/#m-13-in-projectsetcomplete-the-signature-can-be-reused-when-the-first-call-is-reverted-for-some-reason)

Since there is no nonce in the data decoded at the beginning of function `escrow`, a builder can call the function multiple times reducing their debt as much as they wish.

### Mitigation:

Modify function `escrow` to check this nonce and update it after the debt has been reduced.

### TAGS: #sig 
***

---
description: >-
  Submitted by (11) MiloTruck, also found by __141345__, 0x52, 8olidity, cccz,
  Ch_301, codexploder, cryptonue, hansfriese, Ruhum, and sseefried
---

# Missing upper limit

### Summary:

[https://code4rena.com/reports/2022-08-rigor/#m-02-missing-upper-limit-definition-in-replacelenderfee-of-homefisol](https://code4rena.com/reports/2022-08-rigor/#m-02-missing-upper-limit-definition-in-replacelenderfee-of-homefisol)

The admin of the `HomeFi` contract can set `lenderFee` to greater than 100%, forcing calls to `lendToProject()` to all projects created in the future to revert.

### Mitigation:

Consider adding a reasonable fee rate bounds checks in the `replaceLenderFee()` function. This would prevent potential griefing and increase the trust of users in the contract.

---
description: _Submitted by (3) Bahurum, also found by bin2chen and cryptphi_
---

# Anyone can pass any proposal

### Summary:
https://code4rena.com/reports/2022-08-olympus#h-01-in-governancesol-it-might-be-impossible-to-activate-a-new-proposal-forever-after-failed-to-execute-the-previous-active-proposal

Before any `VOTES` are minted anyone can activate and execute an arbitrary proposal even with 0 votes cast. So an attacker can pass any proposal (i.e. change the `executor` + `admin` of the `Kernel`, gaining access to all permissioned functions and to funds held).

### Mitigation:
In `Governance.sol` check for a minimum VOTES totalSupply.

### TAGS:  #proposals

---
description: Submitted by (4) vlad_bochok, also found by indijanc, Lambda, and wastewa
---

# Signature verification can be bypass with zero-address

### Summary:

[https://code4rena.com/reports/2022-08-rigor/#h-05-add-members-to-the-not-yet-created-community](https://code4rena.com/reports/2022-08-rigor/#h-05-add-members-to-the-not-yet-created-community)

Anyone can add himself as a member of community for any future community. This can be done due to a combination of facts:

* Non initialized address storage values are defaulted to `address(0)`
* `addMember` doesn't check if community is already created
* `checkSignatureValidity` doesn't check for `address(0)`

### Mitigation:

1. `checkSignatureValidity`/`recoverKey` should revert the call if an `address == 0`.
2. `addMember` should have a `require(_communityId <= communityCount)`

### TAGS: #sig
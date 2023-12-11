---
description: Submitted by (3) berndartmueller, also found by byndooa and rbserver
---

# Useless NFT

### Summary:

__[_https://code4rena.com/reports/2022-08-rigor/#m-11-owner-of-project-nft-has-no-purpose_](https://code4rena.com/reports/2022-08-rigor/#m-11-owner-of-project-nft-has-no-purpose)__

Creating a new project mints a NFT to the `_sender` (builder). The `builder` of a project has special permissions and is required to perform various tasks.

However, if the minted NFT is transferred to a different address, the `builder` of a project stays the same and the new owner of the transferred NFT has no purpose and no permissions to access authorized functions in Rigor.

### Mitigation:

Consider preventing transferring the project NFT to a different address for now as long as there is no use-case for the NFT owner/holder or use the actual NFT owner as the `builder` of a project.

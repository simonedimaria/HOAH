---
description: _Submitted by (2) Trust, also found by Lambda_
---

# Can vote multiple times by transferring NFT in same block as proposal

### Summary:
https://code4rena.com/reports/2022-09-party/#h-01-partygovernance-can-vote-multiple-times-by-transferring-nft-in-same-block-as-proposal

https://www.trustindistrust.com/post/c4-audit-report-partydao

To make sure users don't vote twice, every proposal has `hasVoted` mapping to keep note of votes. Users are able to transfer their voting power by transferring their PartyGovernanceNFT. This is not an issue by itself, because if user A votes on proposal P, and then transfers his voting powers to user B and tries to vote on proposal P from user B's context, the number of votes calculated for B's vote is his power at proposal time. But the one critical weakness in this validation system is that _during_ the proposal creation block, the same votes may be re-used by different users.

### Mitigation:
Add additional check in `accept()` function:
```solidity
if (proposal.proposedTime == block.timestamp) {
require(proposal.votes == 0);
```
This will not allow `accept()` to be called in the sensitive block except to register the proposer's votes.

### TAGS:  #proposals

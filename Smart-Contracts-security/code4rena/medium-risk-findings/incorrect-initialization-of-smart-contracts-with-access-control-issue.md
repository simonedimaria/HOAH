---
description: Submitted by (4) Haipls, also found by byndooa, cryptphi, and TrungOre
---

# Incorrect initialization of smart contracts with Access Control issue

### Summary:

[https://code4rena.com/reports/2022-08-rigor/#m-14-incorrect-initialization-of-smart-contracts-with-access-control-issue](https://code4rena.com/reports/2022-08-rigor/#m-14-incorrect-initialization-of-smart-contracts-with-access-control-issue)

All next Impact depends on actions and attention from developers when deployed:

* Loss of funds
* Failure of the protocol, with the need for redeploy
* Loss of control over protocol elements (some smart contracts)
* The possibility of replacing contracts and settings with harmful ones\
  \
  Because:

1. Hardhat does not stop the process with a deploy and does not show failed transactions if they have occurred in some cases
2. Malicious agents can trace the protocol deployment transactions and insert their own transaction between them

### Mitigation:

1. Carry out checks at the initialization stage or redesign the deployment process with the initialization of contracts during deployment.
2. A good practice is to verify after each initialization

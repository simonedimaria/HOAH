---
description: Submitted by (4) MEP, also found by byndooa, Haipls, and minhquanym
---

# Copy of Lack of verification in hashes

### Summary:

__[_https://code4rena.com/reports/2022-08-rigor/#m-12-updateprojecthash-does-not-check-project-address_](https://code4rena.com/reports/2022-08-rigor/#m-12-updateprojecthash-does-not-check-project-address)__

In Project.sol, function `updateProjectHash` L162, `_data` (which is signed by builder and/or contractor) does not contain a reference to the project address. In all other external functions of Project.sol, `_data` contains the address of the project, used in this check:\
`require(_projectAddress == address(this), "Project::!projectAddress");`.

### Mitigation:


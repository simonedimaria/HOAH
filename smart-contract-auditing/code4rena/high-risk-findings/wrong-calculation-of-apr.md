---
description: Submitted by (2) Lambda, also found by rbserver
---

# Wrong calculation of APR

### Summary:

[https://code4rena.com/reports/2022-08-rigor/#h-06-wrong-apr-can-be-used-when-project-is-unpublished-and-published-again-](https://code4rena.com/reports/2022-08-rigor/#h-06-wrong-apr-can-be-used-when-project-is-unpublished-and-published-again-)

1. When publishing a project, if the `lentAmount` for the community is non-zero, calculate the interest before updating the APR.
2. Project A is unpublished, the `lentAmount` is still 1,000,000 USD.
3. During one year, no calls to `repayLender`, `reduceDebt`, or `escrow` happens, i.e. the interest is never added and the `lastTimestamp` not updated.
4. After one year, the project is published again in the same community. Because the FED raised interest rates, it is specified that the APR should be 5% from now on.
5. Another $1,000,000 is lent to the project by calling `lendToProject`. Now, `claimInterest` is called which calculates the interest of the last year for the first million. However, the function already uses the new APR of 5%, meaning the added interest is 50,000 USD instead of the correct 30,000 USD.

### Mitigation:

When publishing a project, if the `lentAmount` for the community is non-zero, calculate the interest before updating the APR.

### TAGS: #math 
---
description: Submitted by (4) minhquanym, also found by berndartmueller, Chom, and scaraven
---

# Possible DOS because unbounded loop can run out of gas

### Summary:

__[_https://code4rena.com/reports/2022-08-rigor/#m-10-possible-dos-in-lendtoproject-and-togglelendingneeded-function-because-unbounded-loop-can-run-out-of-gas_](https://code4rena.com/reports/2022-08-rigor/#m-10-possible-dos-in-lendtoproject-and-togglelendingneeded-function-because-unbounded-loop-can-run-out-of-gas)__

In `Project` contract, the `lendToProject()` function might not be available to be called if there are a lot of Task in `tasks[]` list of project. It means that the project cannot be funded by either builder or community owner.

This can happen because `lendToProject()` used `projectCost()` function. _**And the loop in `projectCost()` did not have a mechanism to stop**_**,** it’s only based on the length `taskCount`, and may take all the gas limit. If the gas limit is reached, this transaction will fail or revert.

{% hint style="warning" %}
Also, there should be a task limit.
{% endhint %}

### Mitigation:

Consider keeping value of `projectCost()` in a storage variable and update it when a task is added or updated accordingly.

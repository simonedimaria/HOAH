---
description: >-
  Submitted by (5) berndartmueller, also found by 0xA5DF, arcoun, rotcivegaf,
  and wastewa
---

# Invalid signature lead to Access Control

### Summary:

__[_https://code4rena.com/reports/2022-08-rigor/#m-05-anyone-can-create-disputes-if-contractor-is-not-set_](https://code4rena.com/reports/2022-08-rigor/#m-05-anyone-can-create-disputes-if-contractor-is-not-set)__

Calling the `Project.raiseDispute` function with an invalid `_signature`, for instance providing a `_signature` with a length of 66 will return `address(0)` as the recovered signer address.

If `_task` is set to `0` and the project does not have a `contractor`, the `require` checks will pass and `IDisputes(disputes).raiseDispute(_data, _signature);` is called. The same applies if a specific `_task` is given and if the task has a `subcontractor`. Then the check will also pass.

### Mitigation:

Consider checking the recovered `signer` address in `Project.raiseDispute` to not equal the zero-address:

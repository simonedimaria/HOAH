---
description: >-
  Submitted by (11) scaraven, also found by 0x52, auditor0517, Deivitto,
  hansfriese, Lambda, rbserver, simon135, smiling_heretic, sseefried, and
  TrungOre
---

# Arithmetic rounding

### Summary:

[https://code4rena.com/reports/2022-08-rigor/#h-02-builder-can-halve-the-interest-paid-to-a-community-owner-due-to-arithmetic-rounding](https://code4rena.com/reports/2022-08-rigor/#h-02-builder-can-halve-the-interest-paid-to-a-community-owner-due-to-arithmetic-rounding)

This issue occurs in the calculation of `noOfDays` in `returnToLender()` which calculates the number of days since interest has last been calculated. If a builder repays a very small amount of tokens every 1.9999 days, then the `noOfDays` will be rounded down to `1 days` however `lastTimestamp` is updated to the current timestamp anyway, so the builder essentially accumulates only 1 day of interest after 2 days.

{% hint style="info" %}
Tip: Calculate interest by seconds and not by days
{% endhint %}

### Mitigation:

1\) Add a scalar to `noOfDays` so that any rounding which occurs is negligible or 2) Remove the `noOfDays` calculation and calculate interest in one equation which reduces arithmetic rounding

### TAGS: #math
***

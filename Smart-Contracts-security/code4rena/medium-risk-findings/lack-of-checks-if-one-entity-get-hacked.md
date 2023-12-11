---
description: Submitted by (3) 0xA5DF, also found by Lambda and sseefried
---

# Lack of checks if one entity get hacked

### Summary:

__[_https://code4rena.com/reports/2022-08-rigor/#m-06-attacker-can-drain-all-the-projects-within-minutes-if-admin-account-has-been-exposed_](https://code4rena.com/reports/2022-08-rigor/#m-06-attacker-can-drain-all-the-projects-within-minutes-if-admin-account-has-been-exposed)__

In case where the admin wallet has been hacked, the attacker can drain all funds out of the project within minutes. All the attacker needs is the admin to sign a single meta/normal tx. Even though the likelihood of the admin wallet being hacked might be low, the impact is critical.

### Mitigation:

Consider removing the meta tx for `HomeFi` `onlyAdmin` modifier (i.e. usg `msg.sender` instead of `_msgSender()`), given that it’s not going to be used that often it may be worth giving up the comfort for hardening security

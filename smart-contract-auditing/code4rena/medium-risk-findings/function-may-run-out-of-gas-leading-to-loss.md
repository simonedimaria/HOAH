---
description: _Submitted by (14) Lambda, also found by 0x52, Bahurum, Bnke0x0, KIntern_NA, lukris02, rbserver, Respx, rotcivegaf, Soosh, TomJ, Trust, V_B, and yixxas_
---

# Function may run out of gas leading to lost ETH

### Summary:

https://github.com/code-423n4/2022-09-frax-findings/issues/17

`frxETHMinter.depositEther` always iterates over all deposits that are possible with the current balance. However, when a lot of ETH was deposited into the contract / it was not called in a long time, this loop can reach the gas limit. When this happens, no more calls to `depositEther` are possible, as it will always run out of gas.

### Proof Of Concept:
Jerome Powell continues to rise interest rates, he just announced the next rate hike to 450%. The crypto market crashes, ETH is at 1 USD. Bob buys 100,000 ETH for 100,000 USD and deposits them into `frxETHMinter`. Because of this deposit, `numDeposit` within `depositEther` is equal to 3125. Therefore, every call to the function runs out of gas and it is not possible to deposit this ETH into the deposit contract.

### Mitigation:
It should be possible to specify an upper limit for the number of deposits such that progress is possible, even when a lot of ETH was deposited into the contract.

### TAGS:  #out-of-gas

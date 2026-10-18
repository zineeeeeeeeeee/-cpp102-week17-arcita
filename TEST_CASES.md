# Test Cases – Simulated Device Monitoring and Alert System

**Tested by:** Stanley Austin V. Arcita  
**Date:** 18 October 2026  
**Course:** CPP102 – Week 17

## Test Procedure

Testing was performed by executing a reconstructed copy of the revised Python program shared in this conversation. Each case ran in a separate Python process, starting with the five initial readings. Outputs were checked automatically against the expected strings and successful program exit. These results do not independently verify any later edits in the local VS Code or GitHub copy.

## Main Test Cases

| Test Case | Input or Action | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|
| TC01 | Choose `1` | Displays readings 28, 31, 35, 37, and 29 °C in order | Displayed all five readings in the correct order. | Pass |
| TC02 | Choose `2`, enter `33`, then choose `1` | Success message; 33 °C appears as Reading 6 | Displayed success message and Reading 6: 33 °C. | Pass |
| TC03 | Choose `2`, enter `abc` | `Invalid input. Enter a whole number only.`; readings unchanged | Rejected abc with whole-number error; five readings remained. | Pass |
| TC04 | Choose `2`, enter `-5` | `Invalid reading. Enter a value from 0 to 100.`; readings unchanged | Rejected -5 with 0–100 range error; five readings remained. | Pass |
| TC05 | Choose `2`, enter `120` | `Invalid reading. Enter a value from 0 to 100.`; readings unchanged | Rejected 120 with 0–100 range error; five readings remained. | Pass |
| TC06 | Choose `2`, enter `30`, then choose `3` | `30 °C -> WARNING` | Accepted 30 and displayed 30 °C -> WARNING. | Pass |
| TC07 | Choose `3` using initial readings | `35 °C -> WARNING` | Displayed 35 °C -> WARNING. | Pass |
| TC08 | Restart program; choose `4` | 5 readings; total 160; average 32.00 °C; min 28 °C; max 37 °C; NORMAL 2 (40.00%); WARNING 2 (40.00%); CRITICAL 1 (20.00%); overall status ATTENTION REQUIRED | Displayed 5 readings, total 160, average 32.00 °C, min 28 °C, max 37 °C; counts 2/2/1 and percentages 40.00%/40.00%/20.00%; ATTENTION REQUIRED. | Pass |
| TC09 | Enter `9` at the menu | `Invalid choice. Please enter a number from 1 to 5.`; menu repeats | Displayed invalid-choice message and repeated menu. | Pass |
| TC10 | Choose `5` | `Thank you for using the Device Monitoring System.`; program ends | Displayed exit message; process ended normally. | Pass |

## Extra Test Cases

| Test Case | Input or Action | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|
| TC11 | Choose `2`, press Enter without typing | `Invalid input. The reading cannot be empty.`; readings unchanged | Rejected empty input; five readings remained. | Pass |
| TC12 | Choose `2`, enter `3.5` | `Invalid input. Enter a whole number only.`; readings unchanged | Rejected 3.5 with whole-number error; five readings remained. | Pass |
| TC13 | Restart program; choose `2`, enter `33`, then choose `4` | 6 readings; total 193; average 32.17 °C; NORMAL 2 (33.33%); WARNING 3 (50.00%); CRITICAL 1 (16.67%); overall status ATTENTION REQUIRED | Displayed 6 readings, total 193, average 32.17 °C; NORMAL 2 (33.33%), WARNING 3 (50.00%), CRITICAL 1 (16.67%); ATTENTION REQUIRED. | Pass |
| TC14 | Choose `2`, enter `0`, then choose `3` | 0 °C accepted and classified NORMAL | Accepted 0 and displayed 0 °C -> NORMAL. | Pass |
| TC15 | Choose `2`, enter `100`, then choose `3` | 100 °C accepted and classified CRITICAL | Accepted 100 and displayed 100 °C -> CRITICAL. | Pass |
| TC16 | Choose `2`, enter `36`, then choose `3` | `36 °C -> CRITICAL` | Accepted 36 and displayed 36 °C -> CRITICAL. | Pass |

## Bugs Found and Fixed

No failures were found in the 16 executed test cases, so no code fixes were necessary during this test run. Boundary tests confirmed that 30 °C and 35 °C are WARNING, while 36 °C is CRITICAL. The program also accepted the valid extremes of 0 °C and 100 °C.

## Testing Conclusion

All 16 automated console test scenarios passed on the reconstructed version of the revised CPP102 Week 17 program. The checks covered menu navigation, valid and invalid input, classifications, summary calculations, and normal exit. This is a functional test of the shared code, not an independent verification of the current GitHub repository files.

**Tests passed:** 16 / 16  
**Tests failed:** 0 / 16  
**Final status:** PASS 

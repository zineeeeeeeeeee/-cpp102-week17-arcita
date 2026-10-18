# Test Cases – Simulated Device Monitoring and Alert System

**Tested by:** Stanley Austin V. Arcita  
**Date:** __________________  
**Course:** CPP102 – Week 17

## Test Procedure

Run the Python program in VS Code and enter the inputs shown below. For tests that require the initial five readings, restart the program first. Compare the output with the expected result, then fill in the **Actual Result** and **Pass/Fail** columns. Do not mark a test as passed until it has been run.

## Main Test Cases

| Test Case | Input or Action | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|
| TC01 | Choose `1` | Displays readings 28, 31, 35, 37, and 29 °C in order | Not yet recorded | Pending |
| TC02 | Choose `2`, enter `33`, then choose `1` | Success message; 33 °C appears as Reading 6 | Not yet recorded | Pending |
| TC03 | Choose `2`, enter `abc` | `Invalid input. Enter a whole number only.`; readings unchanged | Not yet recorded | Pending |
| TC04 | Choose `2`, enter `-5` | `Invalid reading. Enter a value from 0 to 100.`; readings unchanged | Not yet recorded | Pending |
| TC05 | Choose `2`, enter `120` | `Invalid reading. Enter a value from 0 to 100.`; readings unchanged | Not yet recorded | Pending |
| TC06 | Choose `2`, enter `30`, then choose `3` | `30 °C -> WARNING` | Not yet recorded | Pending |
| TC07 | Choose `3` using initial readings | `35 °C -> WARNING` | Not yet recorded | Pending |
| TC08 | Restart program; choose `4` | 5 readings; total 160; average 32.00 °C; min 28 °C; max 37 °C; NORMAL 2 (40.00%); WARNING 2 (40.00%); CRITICAL 1 (20.00%); overall status ATTENTION REQUIRED | Not yet recorded | Pending |
| TC09 | Enter `9` at the menu | `Invalid choice. Please enter a number from 1 to 5.`; menu repeats | Not yet recorded | Pending |
| TC10 | Choose `5` | `Thank you for using the Device Monitoring System.`; program ends | Not yet recorded | Pending |

## Extra Test Cases

| Test Case | Input or Action | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|
| TC11 | Choose `2`, press Enter without typing | `Invalid input. The reading cannot be empty.`; readings unchanged | Not yet recorded | Pending |
| TC12 | Choose `2`, enter `3.5` | `Invalid input. Enter a whole number only.`; readings unchanged | Not yet recorded | Pending |
| TC13 | Restart program; choose `2`, enter `33`, then choose `4` | 6 readings; total 193; average 32.17 °C; NORMAL 2 (33.33%); WARNING 3 (50.00%); CRITICAL 1 (16.67%); overall status ATTENTION REQUIRED | Not yet recorded | Pending |
| TC14 | Choose `2`, enter `0`, then choose `3` | 0 °C accepted and classified NORMAL | Not yet recorded | Pending |
| TC15 | Choose `2`, enter `100`, then choose `3` | 100 °C accepted and classified CRITICAL | Not yet recorded | Pending |
| TC16 | Choose `2`, enter `36`, then choose `3` | `36 °C -> CRITICAL` | Not yet recorded | Pending |

## Bugs Found and Fixed

No test results have been recorded yet. Document any issues found during testing, including the test case number, the incorrect behavior, the correction made, and the result after retesting.

**Boundary checks:** Temperatures below 30 °C are NORMAL; temperatures from 30 °C through 35 °C are WARNING; temperatures above 35 °C are CRITICAL. The `check_level()` function must use `temp <= danger` for the WARNING boundary so that 35 °C is not classified as CRITICAL.

## Testing Conclusion

The test plan covers menu navigation, displaying readings, valid and invalid inputs, classification boundaries, summary calculations, and program exit. The final number of passed and failed tests will be added after execution.

**Tests passed:** ____ / 16  
**Tests failed:** ____ / 16  
**Final status:** Pending testing

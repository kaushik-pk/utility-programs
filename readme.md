# Utility programs

## emi.py

#### Pre-requisites
- Python ( Python2.7 or Python3.6 )
- Pip ( pip or pip3 )
    - To install pip visit, https://www.geeksforgeeks.org/how-to-install-pip-on-windows/
- PrettyTable package
    - To install, run command "pip3 install prettytable"

#### Functionality

- Calculates monthly emi, total interest paid, monthly principal balance. 
- Calculate monthly emi, total interest paid, monthly principal balance based on additional payment ( pre-payment ) done.

```
Inputs - 

p - principal amount ( 4900000 )
r - rate of interest ( eg 0.069 for 6.9% )
t - tenure in months ( 360 )
is_prepayment - Whether pre-payment is planned ( True of False )
prepayment_month - Starting month from which pre-payment is planned
prepayment_amount - Monthly prepayment amount

Outputs - 

Monthly emi
Table to display month, initial principal, emi, interest amount in emi, principal amount in emi, prepayment amount
Total interest paid

```

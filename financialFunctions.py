import numpy as np
# pip install numpy-financial
import numpy_financial as npf

# Compute future value of $400 investment every month
# with an annual rate of 8% after 10 years
npf.fv(.08/12, 10*12, -400, -400)

# Calculate interest portion of payment on a loan of $3,000
# at 9.25% per year compounded monthly
# Period of loan (year)
period = np.arange(1*12) + 1
principle = 3000.00
# Interest Payment
ipmt = npf.ipmt(0.0925/12, period, 1*12, principle)
# Principle Payment
ppmt = npf.ppmt(0.0925/12, period, 1*12, principle)
for payment in period:
    index = payment - 1
    principle = principle + ppmt[index]
    print(f"{payment}   {np.round(ppmt[index], 2)}    {np.round(ipmt[index],2)}    {np.round(principle, 2)}")

# Compute number of payments to pay off $3,000 if you paid
# $150 per month with an interest rate of 9.25%
np.round(npf.nper(0.0925/12, -150, 3000.00), 2)

# Calculate net present value of cash flows of $4,000, $5,000
# $6,000, $7,000 after $15,000 investment with .08 rate per period
npf.npv(0.08, [-15000, 4000, 5000, 6000, 7000]).round(2)
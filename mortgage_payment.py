# FINE 33000 - Assignment 1
# Part 1 -- Mortgage Payments

class MortgagePayment:
        def __init__ (self, quotedRatePercent, amortYrs):
              # to store inputs
              self.r_nom = quotedRatePercent / 100.0 
              self.years = int(amortYrs)
              # this is converting nominal (compounded semi-annually) to EAR
              self.ear = (1 + self.r_nom / 2.0) ** 2 - 1.0


        def pva(self, r, n):
              # PV of annuity
              if r == 0:
                        return float(n)
              return (1.0 - (1.0 + r) ** (-n)) / r
        
        def round2(self, x):
               # to round to nearest cent
               return round(x + 1e-9, 2)
        
        def paymentForFrequency(self, principal, paymentsPerYear):
               # converting from EAR to periodic rate 
               m = paymentsPerYear
               r_p = (1.0 + self.ear) ** (1.0 / m) - 1.0
               n = self.years * m 
               pmt = principal / self.pva(r_p, n)
               return self.round2(pmt)
        
        def payments(self, principal):
               # return the monthly, semi-monthly, bi-weekly, etc
               mnthly = self.paymentForFrequency(principal, 12)
               semi_mnthly = self.paymentForFrequency(principal, 24)
               biwkly = self.paymentForFrequency(principal, 26)
               wkly = self.paymentForFrequency(principal, 52)
               rapid_bi = format(self.round2(mnthly / 2), ".2f") # accelerated = 1/2 of monthly
               rapid_wkly = format(self.round2(mnthly / 4), ".2f")
               return (mnthly, semi_mnthly, biwkly, wkly, rapid_bi, rapid_wkly)
        
 # To test: 

principal = float(input("Enter principal amount: "))
quotedRate = float(input("Enter quoted annual rate %: "))
amortYrs = int(input("Enter amortization years: "))

mp = MortgagePayment(quotedRate, amortYrs)
mnthly, semi_m, bi_w, weekly, rapid_bi, rapid_w = mp.payments(principal)

print("Monthly Payment: $" + str(mnthly))
print("Semi-monthly Payment: $" + str(semi_m))
print("Bi-weekly Payment: $" + str(bi_w))
print("Weekly Payment: $" + str(weekly))
print("Rapid Bi-Weekly Payment: $" + str(rapid_bi))
print("Rapid Weekly Payment: $" + str(rapid_w))




        
              














                       
# FINE 3300 - Assignment 1
# Part 2 -- Exchange Rates (USD -- CAD)

FILENAME = "BankOfCanadaExchangeRates (1).csv"  

class ExchangeRates:
    def __init__(self, filename):
        self.filename = filename
        self.latest_usd_cad = None  # CAD per 1 USD
        self.loadLatestUsdToCad()

    def loadLatestUsdToCad(self):
        
        f = open(self.filename, "r")
        text = f.read()
        f.close()
       
        linesRaw = text.strip().split("\n")
        lines = []
        for l in linesRaw:
            if l.strip() != "":
                lines.append(l)

        headerLine = lines[0]

        # header cells (to strip quotes/spaces)
        headCellsRaw = headerLine.split(",")
        header = []
        for h in headCellsRaw:
            header.append(h.strip().strip('"').strip("'"))

        # last (latest) data row 
        dataLine = lines[-1]
        dataCellsRaw = dataLine.split(",")
        lastRow = []
        for c in dataCellsRaw:
            lastRow.append(c.strip().strip('"').strip("'"))

        # find the USD/CAD column.
        usdIdx = -1
        for i in range(len(header)):
            if header[i] == "USD/CAD":
                usdIdx = i
                break

        # convert the text value to float. Also remove thousands commas if any.
        valText = lastRow[usdIdx].replace(",", "").strip()
        self.latest_usd_cad = float(valText)
        

    def convert(self, amount, from_currency, to_currency):
        # only proceed if a rate was loaded
        if self.latest_usd_cad is None:
            print("Exchange rate not loaded. Cannot convert.")
            return 0.00

        fc = from_currency.strip().upper()
        tc = to_currency.strip().upper()

        if fc == tc:
            return round(float(amount), 2)

        if fc == "USD" and tc == "CAD":
            return round(float(amount) * self.latest_usd_cad, 2)
        elif fc == "CAD" and tc == "USD":
            return round(float(amount) / self.latest_usd_cad, 2)
        else:
            print("Only USD and CAD conversions are supported.")
            return 0.00


# to test 
print("Exchange Rates (USD <-> CAD) using", FILENAME)
amount = float(input("Enter amount (e.g., 100000): ").strip())
fromCur = input("From currency (USD or CAD): ").strip()
toCur = input("To currency (USD or CAD): ").strip()

xr = ExchangeRates(FILENAME)
result = xr.convert(amount, fromCur, toCur)
print("Converted Amount: " + toCur.upper() + " $" + format(result, ".2f"))

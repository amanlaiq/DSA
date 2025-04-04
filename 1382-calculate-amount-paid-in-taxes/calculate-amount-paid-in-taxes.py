class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax = 0         # running total of tax to pay
        prev = 0        # tracks start of current tax bracket (exclusive)

        for upper, p in brackets:
            if income >= upper:
                # Fully within this bracket → tax the full range [prev, upper)
                tax += (upper - prev) * p / 100
                prev = upper  # move to the next bracket
            else:
                # Income ends within this bracket → tax only up to income
                tax += (income - prev) * p / 100
                return tax  # we're done

        # If income was more than all bracket ranges
        return tax

class Spreadsheet:

    def __init__(self, rows: int):
        self.mpp = {}

    def setCell(self, cell: str, value: int) -> None:
        self.mpp[cell] = value

    def resetCell(self, cell: str) -> None:
        self.mpp[cell] = 0

    def getValue(self, formula: str) -> int:
        formula = formula[1:]
        for i in range(len(formula)):
            if formula[i] == '+':
                s1, s2 = formula[:i], formula[i+1:]
                left = self.mpp.get(s1, 0) if s1[0].isupper() else int(s1)
                right = self.mpp.get(s2, 0) if s2[0].isupper() else int(s2)
                return left + right


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)

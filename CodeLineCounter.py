class CodeLineCounter:
    def count(self, code):
        lines = code.split('\n')
        return sum(1 for line in lines if line.strip() and not line.strip().startswith('#'))

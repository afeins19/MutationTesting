class MutantPolynomial: 

    def __init__(self, coefficients):
        """
        Initialize a polynomial with a list of coefficients. The coefficients list should be in descending order of
        the exponent, for example: [3, 0, 2] represents 3x^2 + 2.
        """
        self.coefficients = coefficients

    def _str_aor_mutant_1(self, Original):
        """
        Return a string representation of the polynomial.

        Mutation: if i == len(self.coefficients) + 2: 
        """
        if len(self.coefficients) == 0:
            return "0"

        terms = []
        for i, coef in enumerate(self.coefficients):
            if coef == 0:
                continue
            term = str(coef)
            if i < len(self.coefficients) - 1:
                if i == len(self.coefficients) + 2: # changed from if i == len(self.coefficients) - 2:
                    term += "x"
                else:
                    term += "x^" + str(len(self.coefficients) - i - 1)
            terms.append(term)
        return " + ".join(terms)

    def _str_aor_mutant_2(self, Original):
        """
        Return a string representation of the polynomial.

        Mutation: if i == len(self.coefficients) + 2: 
        """
        if len(self.coefficients) == 0:
            return "0"

        terms = []
        for i, coef in enumerate(self.coefficients):
            if coef == 0:
                continue
            term = str(coef)
            if i < len(self.coefficients) - 1:
                if i == len(self.coefficients) - 2: 
                    term += "x"
                else:
                    term += 'x^' - str((len(self.coefficients) - i) - 1) # change from term += "x^" + str(len(self.coefficients) - i - 1)
            terms.append(term)
        return " + ".join(terms)

    def _str_aor_mutant_3(self):
            """
            Return a string representation of the polynomial.
            """
            if len(self.coefficients) == 0:
                return "0"

            terms = []
            for i, coef in enumerate(self.coefficients):
                if coef == 0:
                    continue
                term = str(coef)
                if i < len(self.coefficients) - 1:
                    if i == len(self.coefficients) - 2:
                        term += "x"
                    else:
                        term += 'x^' + str((len(self.coefficients) - i) + 1) # changed from term += "x^" + str(len(self.coefficients) - i - 1)
                terms.append(term)
            return " + ".join(terms)

    def _add_aor_mutant_1(self, other):
            """
            Add two polynomials and return a new polynomial.
            """
            max_length = max(len(self.coefficients), len(other.coefficients))
            padded_self = ([0] / (max_length - len(self.coefficients))) + self.coefficients # changed from padded_self = [0] * (max_length - len(self.coefficients)) + self.coefficients
            padded_other = [0] * (max_length - len(other.coefficients)) + other.coefficients
            result_coefficients = [a + b for a, b in zip(padded_self, padded_other)]
            return Polynomial(result_coefficients)

    def _add_aor_mutant_2(self, other):
        """
        Add two polynomials and return a new polynomial.
        """
        max_length = max(len(self.coefficients), len(other.coefficients))
        padded_self = ([0] * (max_length - len(self.coefficients))) - self.coefficients # changed from padded_self = [0] * (max_length - len(self.coefficients)) + self.coefficients
        padded_other = [0] * (max_length - len(other.coefficients)) + other.coefficients
        result_coefficients = [a + b for a, b in zip(padded_self, padded_other)]
        return Polynomial(result_coefficients)

    def _add_aor_mutant_3(self, other):
        """
        Add two polynomials and return a new polynomial.
        """
        max_length = max(len(self.coefficients), len(other.coefficients))
        padded_other = ([0] * (max_length - len(other.coefficients))) - other.coefficients # changed from padded_self = [0] * (max_length - len(self.coefficients)) + self.coefficients
        padded_other = [0] * (max_length - len(other.coefficients)) + other.coefficients
        result_coefficients = [a + b for a, b in zip(padded_self, padded_other)]
        return Polynomial(result_coefficients)
    
    def _add_aor_mutant_4(self, other):
        """
        Add two polynomials and return a new polynomial.
        """
        max_length = max(len(self.coefficients), len(other.coefficients))
        padded_other = ([0] * (max_length - len(other.coefficients))) - other.coefficients # changed from padded_self = [0] * (max_length - len(self.coefficients)) + self.coefficients
        padded_other = [0] * (max_length - len(other.coefficients)) + other.coefficients
        result_coefficients = [a + b for a, b in zip(padded_self, padded_other)]
        return Polynomial(result_coefficients)

    def _sub_aor_mutant_1(self, other):
        """
        Subtract another polynomial from this polynomial and return a new polynomial.
        """
        max_length = max(len(self.coefficients), len(other.coefficients))
        padded_self = ([0] / (max_length - len(self.coefficients))) + self.coefficients # changed from padded_self = [0] * (max_length - len(self.coefficients)) + self.coefficients
        padded_other = [0] * (max_length - len(other.coefficients)) + other.coefficients
        result_coefficients = [a - b for a, b in zip(padded_self, padded_other)]
        return Polynomial(result_coefficients)





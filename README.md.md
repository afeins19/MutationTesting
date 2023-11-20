# Introduction
Mutation Testing allows us to fill gaps that our tests dont cover. Though Passing Tests and code coverage are good reports of what we are testing, mutant testing allow us to test for something we are **not** testing. By modifying code in small and subtle ways, we introduce some unexpected behavior into our program. When we detect that this mutant code still passes our tests, we save that it has survived and we must either adjust our current tests or write new ones to capture it. 

# Mutation Tools & Operators
```toml 
[tool.poetry.dependencies]
python = "^3.10"
mutpy = "^0.6.1"
pytest = "^7.4.3"
coverage = "^7.3.2"
```

mutpy offers some mutations. Ive selected these to test the Polynomial.py file as they will result in mutants that arent incompetent.

## Selected mutations 
- AOR - arithmetic operator replacement
- ASR - assignment operator replacement 
- COI conditional operator insertion 
- LCR - logical connector replacement 
- LOR - logical operator replacement 
- SIR - slice index remove 
# Mutation Report 
## Command
```bash
(mutationtesting-py3.10) @afeins19 ➜ /workspaces/MutationTesting (main) $ mut.py --target Polynomial.py --unit-test PolyTest.py -o AOR ASR COI LCR LOR SIR - m > generated_mutatants.txt
```

## output (generated_mutants.txt)
``` Shell
[*] Mutation score [4.14335 s]: 0.0%
   - all: 74
   - killed: 0 (0.0%)
   - survived: 34 (45.9%)
   - incompetent: 40 (54.1%)
   - timeout: 0 (0.0%)
```
Its evident that the current test cases are susceptible to mutants. I will search for surviving mutants from the report and implement them as methods. 
# Creating Mutants
I will create a new file called MutantPolynomials. This file will hold the original methods as well as mutant methods for each function where mutants survived. After running mutpy, I found that many of the surviving mutants used AOR, ASR and in a few instances COI to break the code. ASR and AOR resulted in the most code breakage and this makes sense as many of the functions of polynomial.py rely on specific arithmetic operator placement and arrangement.   

## Example Mutant:
```python
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
```

## Modifying The Test Script

```python

# example: updated test_str() test function to handle mutants

def test_str():

    """Modified tests will account for AOR mutants"""

    # Original

    poly = Polynomial([3, 0, 2])

    assert str(poly) == "3x^2 + 2"

  

    # mutant tests (AOR)

    mutant_poly = MutantPolynomial(poly.coefficients)

  

    mutated_str_1 = mutant_poly._str_aor_mutant_1(poly)

    assert not str(mutated_str_1) == "3x^2 + 2"

  

    mutated_str_2 = mutant_poly._str_aor_mutant_2(poly)

    assert not str(mutated_str_2) == "3x^2 + 2"

  

    mutated_str_3 = mutant_poly._str_aor_mutant_3(poly)

    assert not str(mutated_str_3) == "3x^2 + 2"
```

# Conclusion 
Mutpy created a wide array of mutants. Most that got through by far were AOR and ASR changes. This makes sense as were working with arithmetic operations in most of the functions. Writing multiple tests to ensure functions like Polynomail.add() and Polynomial.str() have protections where ever mutations can be made (each arithmetic operator) will make the code more robust. 

from main import lex, parse, proveFormula

testcases = {
    'P or not P': True,
    'P and not P': False,
    'forall x. P(x) implies (Q(x) implies P(x))': True,
    'exists x. (P(x) implies forall y. P(y))': True,
    'forall (x),y. (P((x),y) or not P(x,(y)))': True,
    'not (A and B) implies (not A or not B)': True,
    'not A or not B implies not (A and B)': True,
    'not (A or B) implies (not A and not B)': True,
    '(not A and not B) implies not (A or B)': True,
    '(A and B) implies (B and A)': True,
    '(A or B) implies (B or A)': True,
    '(A or B) or C implies A or (B or C)': True,
    'A or (B or C) implies (A or B) or C': True
}


def main():
    actual_results = {}
    for theorem, expected_result in testcases.items():
        tokens = lex(theorem)
        formula = parse(tokens)
        actual_result = proveFormula({}, formula)
        tag = 'Proved' if actual_result else 'Cannot prove'
        print(f"{tag} {theorem}\n")
        actual_results[theorem] = actual_result
        assert actual_result == expected_result

    for theorem, actual_result in actual_results.items():
        print(f'Theorem: {theorem} => {actual_result}')


if __name__ == '__main__':
    main()


# apl-source:1
# مثال 194 — غربال إراتوستينس
# apl-source:2
# Sieve of Eratosthenes
# apl-source:3
# Demonstrates: قوائم منطقية، حلقات متداخلة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/194-sieve-primes.apl
# apl-source:6

# apl-source:7
def غربال(حد):
    # apl-source:8
    أولي = [True for _ in range(حد + 1)]
    # apl-source:9
    أولي[0] = False
    # apl-source:10
    أولي[1] = False
    # apl-source:11
    for س in range(2, حد + 1):
        # apl-source:12
        if أولي[س]:
            # apl-source:13
            م = س * س
            # apl-source:14
            while م <= حد:
                # apl-source:15
                أولي[م] = False
                # apl-source:16
                م = م + س
    # apl-source:17
    return [س for س in range(حد + 1) if أولي[س]]
# apl-source:18

# apl-source:19
أولية = غربال(50)
# apl-source:20
print("الأعداد الأولية حتى 50:", أولية)
# apl-source:21
print("عددها:", len(أولية))
# apl-source:22

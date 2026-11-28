
# apl-source:1
# مثال 320 — عد الأولية وقائمتها حتى ن
# apl-source:2
# Primes up to N
# apl-source:3
# Demonstrates: غربال مع إحصاء
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/320-sieve-count.apl
# apl-source:6

# apl-source:7
def أولية_حتى(حد):
    # apl-source:8
    أولي = [True for _ in range(حد + 1)]
    # apl-source:9
    أولي[0] = False
    # apl-source:10
    if حد >= 1:
        # apl-source:11
        أولي[1] = False
    # apl-source:12
    س = 2
    # apl-source:13
    while س * س <= حد:
        # apl-source:14
        if أولي[س]:
            # apl-source:15
            م = س * س
            # apl-source:16
            while م <= حد:
                # apl-source:17
                أولي[م] = False
                # apl-source:18
                م = م + س
        # apl-source:19
        س = س + 1
    # apl-source:20
    return [رقم for رقم in range(2, حد + 1) if أولي[رقم]]
# apl-source:21

# apl-source:22
قائمة = أولية_حتى(100)
# apl-source:23
print("أولية حتى 100:", قائمة)
# apl-source:24
print("عددها:", len(قائمة))
# apl-source:25
print("عدد الأولية حتى 1000:", len(أولية_حتى(1000)))
# apl-source:26

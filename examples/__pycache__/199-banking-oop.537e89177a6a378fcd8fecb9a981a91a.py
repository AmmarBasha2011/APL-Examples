
# apl-source:1
# مثال 199 — نظام بنكي بسيط بالكائنات
# apl-source:2
# Simple banking system with classes
# apl-source:3
# Demonstrates: صنف، دوال، كشف حساب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/199-banking-oop.apl
# apl-source:6

# apl-source:7
class حساب:
    # apl-source:8
    def __init__(ذات, مالك, رصيد):
        # apl-source:9
        ذات.مالك = مالك
        # apl-source:10
        ذات.رصيد = رصيد
        # apl-source:11
        ذات.سجل = []
# apl-source:12

    # apl-source:13
    def أودع(ذات, مبلغ):
        # apl-source:14
        ذات.رصيد = ذات.رصيد + مبلغ
        # apl-source:15
        ذات.سجل.append("إيداع: " + str(مبلغ))
        # apl-source:16
        return ذات.رصيد
# apl-source:17

    # apl-source:18
    def اسحب(ذات, مبلغ):
        # apl-source:19
        if مبلغ > ذات.رصيد:
            # apl-source:20
            return "رصيد غير كاف"
        # apl-source:21
        ذات.رصيد = ذات.رصيد - مبلغ
        # apl-source:22
        ذات.سجل.append("سحب: " + str(مبلغ))
        # apl-source:23
        return ذات.رصيد
# apl-source:24

    # apl-source:25
    def كشف(ذات):
        # apl-source:26
        print("=== كشف حساب:", ذات.مالك, "===")
        # apl-source:27
        for حركة in ذات.سجل:
            # apl-source:28
            print(" -", حركة)
        # apl-source:29
        print("الرصيد الحالي:", ذات.رصيد)
# apl-source:30

# apl-source:31
ح = حساب("أحمد", 1000)
# apl-source:32
ح.أودع(500)
# apl-source:33
ح.اسحب(200)
# apl-source:34
ح.اسحب(5000)
# apl-source:35
ح.كشف()
# apl-source:36

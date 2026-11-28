
# apl-source:1
# مثال 357 — حسابات بنكية متعددة
# apl-source:2
# Multiple bank accounts
# apl-source:3
# Demonstrates: تحويل بين الحسابات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/357-bank-accounts.apl
# apl-source:6

# apl-source:7
class حساب_بنكي:
    # apl-source:8
    def __init__(ذات, مالك, رصيد):
        # apl-source:9
        ذات.مالك = مالك
        # apl-source:10
        ذات.رصيد = رصيد
# apl-source:11

    # apl-source:12
    def حول_إلى(ذات, آخر, مبلغ):
        # apl-source:13
        if مبلغ > ذات.رصيد:
            # apl-source:14
            print("فشل التحويل: رصيد", ذات.مالك, "غير كاف")
            # apl-source:15
            return False
        # apl-source:16
        ذات.رصيد = ذات.رصيد - مبلغ
        # apl-source:17
        آخر.رصيد = آخر.رصيد + مبلغ
        # apl-source:18
        return True
# apl-source:19

    # apl-source:20
    def اطبع_رصيد(ذات):
        # apl-source:21
        print(ذات.مالك, ":", ذات.رصيد)
# apl-source:22

# apl-source:23
أ = حساب_بنكي("أحمد", 1000)
# apl-source:24
ب = حساب_بنكي("سارة", 500)
# apl-source:25
أ.حول_إلى(ب, 300)
# apl-source:26
أ.اطبع_رصيد()
# apl-source:27
ب.اطبع_رصيد()
# apl-source:28
أ.حول_إلى(ب, 10000)
# apl-source:29

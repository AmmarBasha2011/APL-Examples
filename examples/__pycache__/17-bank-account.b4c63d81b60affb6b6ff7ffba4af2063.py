
# apl-source:1
# مثال 17 — نظام حساب بنكي مبسّط
# apl-source:2
# Simplified Bank Account System
# apl-source:3
# Demonstrates: classes, methods, self, transactions list
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/17-bank-account.apl
# apl-source:6

# apl-source:7
class الحساب:
    # apl-source:8
    def __init__(ذات, رقم, رصيد_أول):
        # apl-source:9
        ذات.رقم = رقم
        # apl-source:10
        ذات.رصيد = رصيد_أول
        # apl-source:11
        ذات.سجل = []
# apl-source:12

    # apl-source:13
    def إيداع(ذات, مبلغ):
        # apl-source:14
        if مبلغ <= 0:
            # apl-source:15
            return False
        # apl-source:16
        ذات.رصيد = ذات.رصيد + مبلغ
        # apl-source:17
        ذات.سجل = ذات.سجل + ["إيداع " + str(مبلغ)]
        # apl-source:18
        return True
# apl-source:19

    # apl-source:20
    def سحب(ذات, مبلغ):
        # apl-source:21
        if مبلغ <= 0:
            # apl-source:22
            return False
        # apl-source:23
        if مبلغ > ذات.رصيد:
            # apl-source:24
            return False
        # apl-source:25
        ذات.رصيد = ذات.رصيد - مبلغ
        # apl-source:26
        ذات.سجل = ذات.سجل + ["سحب " + str(مبلغ)]
        # apl-source:27
        return True
# apl-source:28

    # apl-source:29
    def تحويل(ذات, إلى, مبلغ):
        # apl-source:30
        if ذات.سحب(مبلغ) == True:
            # apl-source:31
            إلى.إيداع(مبلغ)
            # apl-source:32
            return True
        # apl-source:33
        return False
# apl-source:34

    # apl-source:35
    def كشف(ذات):
        # apl-source:36
        return "حساب " + str(ذات.رقم) + ": رصيد " + str(ذات.رصيد) + " — عمليات: " + str(len(ذات.سجل))
# apl-source:37

# apl-source:38
حساب_أ = الحساب("1001", 5000)
# apl-source:39
حساب_ب = الحساب("1002", 1000)
# apl-source:40

# apl-source:41
print("=== نظام حساب بنكي ===")
# apl-source:42
print(حساب_أ.كشف())
# apl-source:43
print(حساب_ب.كشف())
# apl-source:44
print("")
# apl-source:45
print("إيداع 1500 لحساب أ: " + str(حساب_أ.إيداع(1500)))
# apl-source:46
print("سحب 2000 لحساب أ: " + str(حساب_أ.سحب(2000)))
# apl-source:47
print("سحب 99999 (أكبر من الرصيد): " + str(حساب_أ.سحب(99999)))
# apl-source:48
print("")
# apl-source:49
print("تحويل 1000 من أ إلى ب: " + str(حساب_أ.تحويل(حساب_ب, 1000)))
# apl-source:50
print("")
# apl-source:51
print("الرصيد النهائي:")
# apl-source:52
print("  " + حساب_أ.كشف())
# apl-source:53
print("  " + حساب_ب.كشف())
# apl-source:54

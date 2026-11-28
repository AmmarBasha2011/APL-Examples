
# apl-source:1
# مثال 236 — نمط المحوّل
# apl-source:2
# Adapter pattern
# apl-source:3
# Demonstrates: توحيد واجهتين مختلفتين
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/236-adapter.apl
# apl-source:6

# apl-source:7
class طابعة_قديمة:
    # apl-source:8
    def اطبع_نص(ذات, نص_الدخل):
        # apl-source:9
        print("[طابعة قديمة]", نص_الدخل)
# apl-source:10

# apl-source:11
class محول_طابعة:
    # apl-source:12
    def __init__(ذات, قديمة):
        # apl-source:13
        ذات.قديمة = قديمة
# apl-source:14

    # apl-source:15
    def طباعة_موحدة(ذات, محتوى):
        # apl-source:16
        ذات.قديمة.اطبع_نص("محتوى: " + محتوى)
# apl-source:17

# apl-source:18
def أرسل_للطباعة(هدف, محتوى):
    # apl-source:19
    هدف.طباعة_موحدة(محتوى)
# apl-source:20

# apl-source:21
محول = محول_طابعة(طابعة_قديمة())
# apl-source:22
أرسل_للطباعة(محول, "تقرير المبيعات")
# apl-source:23

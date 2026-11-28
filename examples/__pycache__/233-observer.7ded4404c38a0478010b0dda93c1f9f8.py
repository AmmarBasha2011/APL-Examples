
# apl-source:1
# مثال 233 — نمط المراقب
# apl-source:2
# Observer pattern
# apl-source:3
# Demonstrates: اشتراك وإشعار
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/233-observer.apl
# apl-source:6

# apl-source:7
class ناشر:
    # apl-source:8
    def __init__(ذات):
        # apl-source:9
        ذات.مشتركون = []
# apl-source:10

    # apl-source:11
    def اشترك(ذات, مشترك):
        # apl-source:12
        ذات.مشتركون.append(مشترك)
# apl-source:13

    # apl-source:14
    def أشعر(ذات, خبر):
        # apl-source:15
        for مشترك in ذات.مشتركون:
            # apl-source:16
            مشترك.استلم(خبر)
# apl-source:17

# apl-source:18
class مشترك:
    # apl-source:19
    def __init__(ذات, اسم):
        # apl-source:20
        ذات.اسم = اسم
# apl-source:21

    # apl-source:22
    def استلم(ذات, خبر):
        # apl-source:23
        print(ذات.اسم, "استلم:", خبر)
# apl-source:24

# apl-source:25
ن = ناشر()
# apl-source:26
ن.اشترك(مشترك("أحمد"))
# apl-source:27
ن.اشترك(مشترك("سارة"))
# apl-source:28
ن.أشعر("عدد جديد صدر!")
# apl-source:29

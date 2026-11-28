
# apl-source:1
# مثال 358 — مدرسة وطلاب ومواد
# apl-source:2
# School, students and courses
# apl-source:3
# Demonstrates: علاقات بين الكائنات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/358-school.apl
# apl-source:6

# apl-source:7
class طالب:
    # apl-source:8
    def __init__(ذات, اسم):
        # apl-source:9
        ذات.اسم = اسم
        # apl-source:10
        ذات.مواد = []
# apl-source:11

    # apl-source:12
    def سجل_مادة(ذات, مادة):
        # apl-source:13
        ذات.مواد.append(مادة)
# apl-source:14

# apl-source:15
class مادة:
    # apl-source:16
    def __init__(ذات, اسم, س_معتمدة):
        # apl-source:17
        ذات.اسم = اسم
        # apl-source:18
        ذات.س_معتمدة = س_معتمدة
# apl-source:19

# apl-source:20
رياضيات = مادة("رياضيات", 4)
# apl-source:21
علوم = مادة("علوم", 3)
# apl-source:22

# apl-source:23
أ = طالب("أحمد")
# apl-source:24
أ.سجل_مادة(رياضيات)
# apl-source:25
أ.سجل_مادة(علوم)
# apl-source:26

# apl-source:27
مجموع_س_معتمدة = 0
# apl-source:28
print("مواد", أ.اسم, ":")
# apl-source:29
for م in أ.مواد:
    # apl-source:30
    print(" -", م.اسم, "(", م.س_معتمدة, "س_معتمدة)")
    # apl-source:31
    مجموع_س_معتمدة = مجموع_س_معتمدة + م.س_معتمدة
# apl-source:32
print("إجمالي الس_معتمدة:", مجموع_س_معتمدة)
# apl-source:33

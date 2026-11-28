
# apl-source:1
# مثال 459 — قصة بقوالب
# apl-source:2
# Mad libs story
# apl-source:3
# Demonstrates: تعبئة قالب بكلمات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/459-mad-libs.apl
# apl-source:6

# apl-source:7
def املأ(قالب, مقاطع):
    # apl-source:8
    أجزاء = قالب.split("[x]")
    # apl-source:9
    ناتج = أجزاء[0]
    # apl-source:10
    for ي in range(len(مقاطع)):
        # apl-source:11
        ناتج = ناتج + مقاطع[ي] + أجزاء[ي + 1]
    # apl-source:12
    return ناتج
# apl-source:13

# apl-source:14
قالب = "في يوم مشمس، ذهب [x] إلى [x] لشراء [x] وعاد سعيدا"
# apl-source:15
print(املأ(قالب, ["عمار", "السوق", "الخبز"]))
# apl-source:16

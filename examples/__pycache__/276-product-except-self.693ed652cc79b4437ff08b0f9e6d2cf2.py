
# apl-source:1
# مثال 276 — حاصل ضرب ما عدا الذات
# apl-source:2
# Product of array except self
# apl-source:3
# Demonstrates: جداول بادئة ولاحقة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/276-product-except-self.apl
# apl-source:6

# apl-source:7
def حاصل_عدا_الذات(قائمة):
    # apl-source:8
    ن = len(قائمة)
    # apl-source:9
    نتيجة = [1 for _ in range(ن)]
    # apl-source:10
    بادئة = 1
    # apl-source:11
    for ي in range(ن):
        # apl-source:12
        نتيجة[ي] = بادئة
        # apl-source:13
        بادئة = بادئة * قائمة[ي]
    # apl-source:14
    لاحقة = 1
    # apl-source:15
    for ي in range(ن):
        # apl-source:16
        ز = ن - 1 - ي
        # apl-source:17
        نتيجة[ز] = نتيجة[ز] * لاحقة
        # apl-source:18
        لاحقة = لاحقة * قائمة[ز]
    # apl-source:19
    return نتيجة
# apl-source:20

# apl-source:21
print(حاصل_عدا_الذات([1, 2, 3, 4]))
# apl-source:22
print(حاصل_عدا_الذات([2, 3, 4, 5]))
# apl-source:23

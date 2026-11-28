
# apl-source:1
def فيب(ن):
    # apl-source:2
    if ن < 2:
        # apl-source:3
        return ن
    # apl-source:4
    return فيب(ن - 1) + فيب(ن - 2)
# apl-source:5

# apl-source:6
def فيب_تكراري(عدد):
    # apl-source:7
    if عدد < 2:
        # apl-source:8
        return عدد
    # apl-source:9
    السابق = 0
    # apl-source:10
    الحالي = 1
    # apl-source:11
    كرارة = 2
    # apl-source:12
    while كرارة <= عدد:
        # apl-source:13
        التالي = السابق + الحالي
        # apl-source:14
        السابق = الحالي
        # apl-source:15
        الحالي = التالي
        # apl-source:16
        كرارة = كرارة + 1
    # apl-source:17
    return الحالي
# apl-source:18

# apl-source:19
print("=== متتالية فيبوناتشي ===")
# apl-source:20
print("أول 8 حدود:")
# apl-source:21
الحدود = 0
# apl-source:22
while الحدود < 8:
    # apl-source:23
    print(f"  فيب({الحدود}) = {فيب(الحدود)}")
    # apl-source:24
    الحدود = الحدود + 1
# apl-source:25
print("")
# apl-source:26
print("فيب(10) تكراري: " + str(فيب_تكراري(10)))
# apl-source:27
print("فيب(20) تكراري: " + str(فيب_تكراري(20)))
# apl-source:28
print("فيب(50) تكراري: " + str(فيب_تكراري(50)))
# apl-source:29

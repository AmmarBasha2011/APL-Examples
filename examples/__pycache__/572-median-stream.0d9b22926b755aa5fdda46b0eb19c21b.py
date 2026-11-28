
# apl-source:1
# مثال 572 — وسيط التدفق
# apl-source:2
# Running median
# apl-source:3
# Demonstrates: وسيط تدفق، كوميتان، موازنة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/572-median-stream.apl
# apl-source:6

# apl-source:7
def تأكد_يساوي(فعلي, متوقع, اسم):
    # apl-source:8
    if فعلي != متوقع:
        # apl-source:9
        print("فشل:", اسم, "| متوقع:", متوقع, "| فعلي:", فعلي)
        # apl-source:10
        قياسي_نظام_اخرج(1)
    # apl-source:11
    print("ناجح:", اسم)
# apl-source:12

# apl-source:13

# apl-source:14
# وسيط تدفق بكوميتين (أدنى وأقصى)
# apl-source:15
أدنى_كومة = list()
# apl-source:16
أقصى_كومة = list()
# apl-source:17

# apl-source:18
def ادفع(كومة, قيمة, أدنى):
    # apl-source:19
    كومة.append(قيمة)
    # apl-source:20
    i = len(كومة) - 1
    # apl-source:21
    while i > 0:
        # apl-source:22
        أب = (i - 1) // 2
        # apl-source:23
        if أدنى and كومة[i] < كومة[أب]:
            # apl-source:24
            م = كومة[i]
            # apl-source:25
            كومة[i] = كومة[أب]
            # apl-source:26
            كومة[أب] = م
            # apl-source:27
            i = أب
        # apl-source:28
        elif not أدنى and كومة[i] > كومة[أب]:
            # apl-source:29
            م = كومة[i]
            # apl-source:30
            كومة[i] = كومة[أب]
            # apl-source:31
            كومة[أب] = م
            # apl-source:32
            i = أب
        # apl-source:33
        else:
            # apl-source:34
            break
# apl-source:35

# apl-source:36
def اسحب(كومة, أدنى):
    # apl-source:37
    قمة = كومة[0]
    # apl-source:38
    كومة[0] = كومة[len(كومة) - 1]
    # apl-source:39
    كومة.pop()
    # apl-source:40
    i = 0
    # apl-source:41
    while True:
        # apl-source:42
        أفضل = i
        # apl-source:43
        for ابن in [2 * i + 1, 2 * i + 2]:
            # apl-source:44
            if ابن < len(كومة):
                # apl-source:45
                if أدنى and كومة[ابن] < كومة[أفضل]:
                    # apl-source:46
                    أفضل = ابن
                # apl-source:47
                if not أدنى and كومة[ابن] > كومة[أفضل]:
                    # apl-source:48
                    أفضل = ابن
        # apl-source:49
        if أفضل == i:
            # apl-source:50
            break
        # apl-source:51
        م = كومة[i]
        # apl-source:52
        كومة[i] = كومة[أفضل]
        # apl-source:53
        كومة[أفضل] = م
        # apl-source:54
        i = أفضل
    # apl-source:55
    return قمة
# apl-source:56

# apl-source:57
def أضف_رقم(ن):
    # apl-source:58
    if len(أقصى_كومة) == 0 or ن <= 0 - أقصى_كومة[0]:
        # apl-source:59
        ادفع(أقصى_كومة, 0 - ن, True)
    # apl-source:60
    else:
        # apl-source:61
        ادفع(أدنى_كومة, ن, True)
    # apl-source:62
    if len(أقصى_كومة) > len(أدنى_كومة) + 1:
        # apl-source:63
        ادفع(أدنى_كومة, 0 - اسحب(أقصى_كومة, True), True)
    # apl-source:64
    if len(أدنى_كومة) > len(أقصى_كومة):
        # apl-source:65
        ادفع(أقصى_كومة, 0 - اسحب(أدنى_كومة, True), True)
# apl-source:66

# apl-source:67
def الوسيط():
    # apl-source:68
    if len(أقصى_كومة) > len(أدنى_كومة):
        # apl-source:69
        return 0 - أقصى_كومة[0]
    # apl-source:70
    return ((0 - أقصى_كومة[0]) + أدنى_كومة[0]) / 2
# apl-source:71

# apl-source:72
for ن in [5, 15, 1, 3]:
    # apl-source:73
    أضف_رقم(ن)
    # apl-source:74
    print("بعد", ن, ":", الوسيط())
# apl-source:75
تأكد_يساوي(الوسيط(), 4, "وسيط [5,15,1,3]")
# apl-source:76
أضف_رقم(8)
# apl-source:77
تأكد_يساوي(الوسيط(), 5, "وسيط [5,15,1,3,8]")
# apl-source:78

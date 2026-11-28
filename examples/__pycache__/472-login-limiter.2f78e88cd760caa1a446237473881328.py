
# apl-source:1
# مثال 472 — محدد محاولات الدخول
# apl-source:2
# Login attempt limiter
# apl-source:3
# Demonstrates: قفل بعد 3 محاولات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/472-login-limiter.apl
# apl-source:6

# apl-source:7
كلمة_صحيحة = "سر123"
# apl-source:8
محاولات = ["خطأ1", "خطأ2", "خطأ3", "سر123"]
# apl-source:9
فاشلة = 0
# apl-source:10
مقفل = False
# apl-source:11

# apl-source:12
for محاولة in محاولات:
    # apl-source:13
    if مقفل:
        # apl-source:14
        print("الحساب مقفل")
        # apl-source:15
        break
    # apl-source:16
    if محاولة == كلمة_صحيحة:
        # apl-source:17
        print("دخول ناجح")
        # apl-source:18
        break
    # apl-source:19
    else:
        # apl-source:20
        فاشلة = فاشلة + 1
        # apl-source:21
        print("محاولة خاطئة", فاشلة)
        # apl-source:22
        if فاشلة >= 3:
            # apl-source:23
            مقفل = True
# apl-source:24

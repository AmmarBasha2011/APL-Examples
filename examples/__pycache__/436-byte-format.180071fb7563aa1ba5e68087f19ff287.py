
# apl-source:1
# مثال 436 — تنسيق أحجام الملفات
# apl-source:2
# Byte size formatting
# apl-source:3
# Demonstrates: KB MB GB
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/436-byte-format.apl
# apl-source:6

# apl-source:7
def حجم_نص(بايت):
    # apl-source:8
    مقاييس = ["بايت", "كيلوبايت", "ميجابايت", "جيجابايت"]
    # apl-source:9
    قيمة = بايت
    # apl-source:10
    مرتبة = 0
    # apl-source:11
    while قيمة >= 1024 and مرتبة < 3:
        # apl-source:12
        قيمة = قيمة / 1024
        # apl-source:13
        مرتبة = مرتبة + 1
    # apl-source:14
    return str(int(قيمة * 100) / 100) + " " + مقاييس[مرتبة]
# apl-source:15

# apl-source:16
print(حجم_نص(512))
# apl-source:17
print(حجم_نص(2048))
# apl-source:18
print(حجم_نص(5242880))
# apl-source:19
print(حجم_نص(3221225472))
# apl-source:20

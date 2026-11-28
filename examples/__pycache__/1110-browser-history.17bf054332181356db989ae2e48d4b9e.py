
# apl-source:1
# مثال 1110 — سجل المتصفح
# apl-source:2
# Browser history
# apl-source:3
# Demonstrates: قائمة ومؤشر
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1110-browser-history.apl
# apl-source:6

# apl-source:7
# الزيارة تقطع كل ما أمام المؤشر
# apl-source:8
# والرجوع والتقدم يحركان المؤشر داخل حدود القائمة
# apl-source:9

# apl-source:10
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:11
  if فعلي != متوقع:
    # apl-source:12
    print("فشل:", اسم)
    # apl-source:13
    print("  متوقع:", متوقع)
    # apl-source:14
    print("  فعلي:", فعلي)
    # apl-source:15
    قياسي_نظام_اخرج(1)
  # apl-source:16
  print("ناجح:", اسم)
# apl-source:17

# apl-source:18
class سجل_متصفح:
    # apl-source:19
    def __init__(ذات, بداية):
        # apl-source:20
        ذات.صفحات = [بداية]
        # apl-source:21
        ذات.موضع = 0
# apl-source:22

    # apl-source:23
    def زر(ذات, رابط):
        # apl-source:24
        ذات.صفحات = ذات.صفحات[:ذات.موضع + 1]
        # apl-source:25
        ذات.صفحات = ذات.صفحات + [رابط]
        # apl-source:26
        ذات.موضع = ذات.موضع + 1
# apl-source:27

    # apl-source:28
    def ارجع_خطوات(ذات, ك):
        # apl-source:29
        ذات.موضع = ذات.موضع - ك
        # apl-source:30
        if ذات.موضع < 0:
            # apl-source:31
            ذات.موضع = 0
        # apl-source:32
        return ذات.صفحات[ذات.موضع]
# apl-source:33

    # apl-source:34
    def تقدم_خطوات(ذات, ك):
        # apl-source:35
        ذات.موضع = ذات.موضع + ك
        # apl-source:36
        if ذات.موضع > (len(ذات.صفحات) - 1):
            # apl-source:37
            ذات.موضع = len(ذات.صفحات) - 1
        # apl-source:38
        return ذات.صفحات[ذات.موضع]
# apl-source:39

# apl-source:40
م = سجل_متصفح("leetcode.com")
# apl-source:41
م.زر("google.com")
# apl-source:42
م.زر("facebook.com")
# apl-source:43
م.زر("youtube.com")
# apl-source:44
تأكد_يساوي(م.ارجع_خطوات(1), "facebook.com", "رجوع أول")
# apl-source:45
تأكد_يساوي(م.ارجع_خطوات(1), "google.com", "رجوع ثان")
# apl-source:46
تأكد_يساوي(م.تقدم_خطوات(1), "facebook.com", "تقدم")
# apl-source:47
م.زر("linkedin.com")
# apl-source:48
تأكد_يساوي(م.تقدم_خطوات(2), "linkedin.com", "تقدم بلا مجال")
# apl-source:49
تأكد_يساوي(م.ارجع_خطوات(2), "google.com", "رجوع خطوتين")
# apl-source:50
تأكد_يساوي(م.ارجع_خطوات(7), "leetcode.com", "رجوع للبداية")
# apl-source:51

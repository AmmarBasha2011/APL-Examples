
# apl-source:1
# مثال 417 — كيانات HTML
# apl-source:2
# HTML entities
# apl-source:3
# Demonstrates: تهريب وفك تهريب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/417-html-entities.apl
# apl-source:6

# apl-source:7
def اهرب_اتش(نص_الدخل):
    # apl-source:8
    ناتج = نص_الدخل.replace("&", "&amp;")
    # apl-source:9
    ناتج = ناتج.replace("<", "&lt;")
    # apl-source:10
    ناتج = ناتج.replace(">", "&gt;")
    # apl-source:11
    ناتج = ناتج.replace('"', "&quot;")
    # apl-source:12
    return ناتج
# apl-source:13

# apl-source:14
def افكك_اتش(نص_الدخل):
    # apl-source:15
    ناتج = نص_الدخل.replace("&lt;", "<")
    # apl-source:16
    ناتج = ناتج.replace("&gt;", ">")
    # apl-source:17
    ناتج = ناتج.replace("&quot;", '"')
    # apl-source:18
    ناتج = ناتج.replace("&amp;", "&")
    # apl-source:19
    return ناتج
# apl-source:20

# apl-source:21
مهرب = اهرب_اتش('<div class="x">أ & ب</div>')
# apl-source:22
print("مهرب:", مهرب)
# apl-source:23
print("مفكوك:", افكك_اتش(مهرب))
# apl-source:24

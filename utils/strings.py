import string, re, unicodedata
def strip_accent(text):
    """
    Strips the accents, replace the dd
    """
    return unicodedata.normalize("NFKD", text.replace("đ", "d").replace("Đ", "d")).encode("ascii", "ignore").decode(
        "utf-8")

def normalize_text(text):
    return strip_accent(text).lower()
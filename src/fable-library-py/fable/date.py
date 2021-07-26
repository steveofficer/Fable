from .util import DateKind
from datetime import datetime, timezone, tzinfo
import re

formatRegExp = re.compile(r"(\w)\1*")


def op_Subtraction(x, y):
    return x - y


def create(year, month, day, h=0, m=0, s=0, ms=0, kind=None):
    if kind == DateKind.UTC:
        date = datetime(
            year=year, month=month, day=day, hour=h, minute=m, second=s, microsecond=ms * 1000, tzinfo=timezone.utc
        )
    else:
        date = datetime(year, month, day, h, m, s, ms * 1000)

    return date


def year(d):
    return d.year


def dateToStringWithCustomFormat(date, format, utc):
    def match(m):
        match = m.group()
        m = match[:1]
        print(match)

        rep = None
        if m == "y":
            y = date.astimezone(timezone.utc).year if utc else date.year
            rep = y % 100 if len(match) < 4 else y
        elif m == "M":
            rep = date.astimezone(timezone.utc).month if utc else date.month
        elif m == "H":
            rep = date.astimezone(timezone.utc).hour if utc else date.hour
        elif m == "m":
            rep = date.astimezone(timezone.utc).minute if utc else date.minute
        elif m == "s":
            rep = date.astimezone(timezone.utc).second if utc else date.second
        elif m == "f":
            rep = date.astimezone(timezone.utc).microsecond if utc else date.microsecond
            rep = rep // 1000

        if rep:
            return f"0{rep}" if (rep < 10 and len(match) > 1) else f"{rep}"
        else:
            return match
        return ""

    ret = formatRegExp.sub(match, format)
    return ret

    # return format.replace(/(\w)\1*/g, (match) => {
    #     let rep = Number.NaN;
    #     switch (match.substring(0, 1)) {
    #         case "y":
    #             const y = utc ? date.getUTCFullYear() : date.getFullYear();
    #             rep = match.length < 4 ? y % 100 : y;
    #             break;
    #         case "M":
    #             rep = (utc ? date.getUTCMonth() : date.getMonth()) + 1;
    #             break;
    #         case "d":
    #             rep = utc ? date.getUTCDate() : date.getDate();
    #             break;
    #         case "H":
    #             rep = utc ? date.getUTCHours() : date.getHours();
    #             break;
    #         case "h":
    #             const h = utc ? date.getUTCHours() : date.getHours();
    #             rep = h > 12 ? h % 12 : h;
    #             break;
    #         case "m":
    #             rep = utc ? date.getUTCMinutes() : date.getMinutes();
    #             break;
    #         case "s":
    #             rep = utc ? date.getUTCSeconds() : date.getSeconds();
    #             break;
    #         case "f":
    #             rep = utc ? date.getUTCMilliseconds() : date.getMilliseconds();
    #             break;
    #     }
    #     if (Number.isNaN(rep)) {
    #         return match;
    #     }
    #     else {
    #         return (rep < 10 && match.length > 1) ? "0" + rep : "" + rep;
    #     }


# def dateToStringWithOffset(date, format=None):
#     d = new Date(date.getTime() + ((_a = date.offset) !== null && _a !== void 0 ? _a : 0));
#     if (typeof format !== "string") {
#         return d.toISOString().replace(/\.\d+/, "").replace(/[A-Z]|\.\d+/g, " ") + dateOffsetToString(((_b = date.offset) !== null && _b !== void 0 ? _b : 0));
#     }
#     else if (format.length === 1) {
#         switch (format) {
#             case "D":
#             case "d": return dateToHalfUTCString(d, "first");
#             case "T":
#             case "t": return dateToHalfUTCString(d, "second");
#             case "O":
#             case "o": return dateToISOStringWithOffset(d, ((_c = date.offset) !== null && _c !== void 0 ? _c : 0));
#             default: throw new Error("Unrecognized Date print format");
#         }

#     else:
#         return dateToStringWithCustomFormat(d, format, True)


def dateToStringWithKind(date, format=None):
    utc = date.tzinfo == timezone.utc
    if not format:
        return date.isoformat() if utc else str(date)

    elif len(format) == 1:
        if format == "D" or format == "d":
            return dateToHalfUTCString(date, "first") if utc else str(date.date())
        elif format == "T" or format == "t":
            return dateToHalfUTCString(date, "second") if utc else str(date.time())
        elif format == "O" or format == "o":
            return dateToISOString(date, utc)
        else:
            raise Exception("Unrecognized Date print format")

    else:
        return dateToStringWithCustomFormat(date, format, utc)


def toString(date, format, provider=None):
    if date.tzinfo:
        return dateToStringWithOffset(date, format)

    return dateToStringWithKind(date, format)


def now():
    return datetime.now()


def utcNow():
    return datetime.utcnow()


def toLocalTime(date):
    return date.astimezone()


def compare(x, y):
    if x == y:
        return 0

    if x < y:
        return -1

    return 1


def equals(x, y):
    return x == y


def maxValue():
    return datetime.max


def minValue():
    return datetime.min


def op_Addition(x, y):
    return x + y

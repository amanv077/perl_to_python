# Define the SMTP suffixes
smtp_suffix = {
    "ezweb.ne.jp": "ezweb.ne.jp",
    "softbank.ne.jp": "softbank.ne.jp",
    "i.softbank.jp": "i.softbank.jp",
    "docomo.ne.jp": "docomo.ne.jp",
    "disney.ne.jp": "disney.ne.jp",
    "ymobile.ne.jp": "ymobile.ne.jp",
    "gmail.com": "gmail.com"
}

# Define the SMTP server configurations
smtp_server = {
    "ezweb.ne.jp": {
        "mx": 1,
        "max": 1,
        "1": "27.86.106.68",
        "per": 7,
        "thread": 25,
        "pwait": 200,
        "twait": 200,
        "swait": 2 * 60
    },
    "softbank.ne.jp": {
        "mx": 1,
        "max": 4,
        "1": "117.46.11.71",
        "2": "117.46.5.71",
        "3": "117.46.11.71",
        "4": "117.46.5.71",
        "per": 8,
        "thread": 35,
        "pwait": 200,
        "twait": 200,
        "swait": 2 * 60
    },
    "i.softbank.jp": {
        "mx": 1,
        "max": 4,
        "1": "117.46.9.104",
        "2": "117.46.7.40",
        "3": "117.46.9.104",
        "4": "117.46.7.40",
        "per": 7,
        "thread": 40,
        "pwait": 200,
        "twait": 200,
        "swait": 2 * 60
    },
    "docomo.ne.jp": {
        "mx": 4,
        "max": 4,
        "1": "213.136.68.34",
        "2": "213.136.68.34",
        "3": "213.136.68.34",
        "4": "213.136.68.34",
        "per": 5,
        "thread": 4,
        "pwait": 500,
        "twait": 3 * 60 * 1000,  # milliseconds
        "swait": 15 * 60
    },
    "disney.ne.jp": {
        "mx": 1,
        "max": 2,
        "1": "117.46.7.41",
        "2": "117.46.5.73",
        "per": 8,
        "thread": 30,
        "pwait": 200,
        "twait": 200,
        "swait": 2 * 60
    },
    "ymobile.ne.jp": {
        "mx": 1,
        "max": 2,
        "1": "117.46.7.43",
        "2": "117.46.5.75",
        "per": 8,
        "thread": 30,
        "pwait": 200,
        "twait": 200,
        "swait": 2 * 60
    },
    "gmail.com": {
        "mx": 1,
        "max": 5,
        "1": "74.125.140.27",
        "2": "64.233.163.27",
        "3": "74.125.200.27",
        "4": "64.233.188.27",
        "5": "74.125.28.26",
        "per": 8,
        "thread": 18,
        "pwait": 200,
        "twait": 200,
        "swait": 2 * 60
    }
}

# Define the SMTP CRLF
smtp_cr = "\r\n"

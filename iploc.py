import geocoder, fontstyle

red = "\033[31m"

yellow = "\033[93m"

green = "\033[32m"

blue = "\033[34m"

purple = "\033[35m"

cyan = "\033[36m"

lightred = "\033[91m"

lightgreen = "\033[92m"

lightblue = "\033[94m"

lightcyan = "\033[96m"

print(fontstyle.apply(lightcyan + """

        ×±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±×

        |   _____  ___  __             |

        |   \_   \/ _ \/ /  ___   ___  |

        |    / /\/ /_)/ /  / _ \ / __| |

        | /\/ /_/ ___/ /__| (_) | (__  |

        | \____/\/   \____/\___/ \___| |

        |                              |

        | [#] Coder   : 7Security      |

        | [#] Version : 1.7            |

        ×±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±×

""", "bold/bold"))

ask = input(fontstyle.apply(lightgreen + "Enter IP : ", "bold/bold"))

des = geocoder.ipinfo(ask)

print(fontstyle.apply(yellow + """

×—×—×—×—×—×—×—×—×—×

|     Results     |

×—×—×—×—×—×—×—×—×—×""", "bold/bold"))

print(fontstyle.apply(lightgreen + f"[#] City      : {des.city}", "bold/bold"))

print(fontstyle.apply(f"[#] Country   : {des.country}", "bold/bold"))

print(fontstyle.apply(lightgreen + f"[#] IP        : {des.ip}", "bold/bold"))

print(fontstyle.apply(f"[#] Latitude  : {des.lat}", "bold/bold"))

print(fontstyle.apply(lightgreen + f"[#] Longitude : {des.lng}", "bold/bold"))

print(fontstyle.apply(f"[#] ISP       : {des.org}", "bold/bold"))

print(fontstyle.apply(lightgreen + f"[#] ZIP code  : {des.postal}", "bold/bold"))

print(fontstyle.apply(f"[#] State     : {des.state}", "bold/bold"))

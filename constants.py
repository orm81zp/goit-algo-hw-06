graph_with_weight = {
    "Kyiv": {"Zhytomyr": 140, "Uman'": 215},
    "Uman'": {"Kyiv": 215, "Vinnytsia": 160},
    "Vinnytsia": {"Uman'": 160, "Zhytomyr": 155, "Ternopil": 235},
    "Zhytomyr": {"Kyiv": 140, "Vinnytsia": 155, "Lutks": 265},
    "Ternopil": {"Vinnytsia": 235, "Lviv": 127},
    "Lutks": {"Zhytomyr": 265, "Lviv": 155},
    "Lviv": {"Lutks": 155, "Ternopil": 127},
}

graph = {
    "Kyiv": ["Zhytomyr", "Uman'"],
    "Uman'": ["Kyiv", "Vinnytsia"],
    "Vinnytsia": ["Uman'", "Zhytomyr", "Ternopil"],
    "Zhytomyr": ["Kyiv", "Vinnytsia", "Lutks"],
    "Ternopil": ["Vinnytsia", "Lviv"],
    "Lutks": ["Zhytomyr", "Lviv"],
    "Lviv": ["Lutks", "Ternopil"],
}

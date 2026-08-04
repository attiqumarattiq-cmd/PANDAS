import pandas as pd 

df = pd.DataFrame({
    "Your Name":
    [
        "Your buddy",
        "Your gangster",
        "Your lover",
    ],
    "Your Gender":
    [
        "Male",
        "Custom",
        "Female",
    ],
    "Your age":
    [
        45,
        34,
        56,
    ]
})


print(df["Your age"])
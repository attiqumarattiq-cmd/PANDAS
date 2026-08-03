import pandas as pd 

df = pd.DataFrame({
    "Name": [
        "Mr.Akbar",
        "Rafta",
        "Aliyan",
    ],
    "Age": [22, 35, 58],
    "Sex": ["Male", "Male", "Female"]
})

df.to_excel("my_data.xlsx", index=False)

print("File saved successfully!") 
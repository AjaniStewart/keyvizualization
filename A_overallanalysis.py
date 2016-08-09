
# coding: utf-8

# In[3]:

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\NYUK12STEM\\Desktop\\Batch_2485769_batch_results.csv")
only_main = df[["Input.img_id", "Answer.ans"]]
s = pd.DataFrame({'Count':only_main.groupby(["Input.img_id", "Answer.ans"]).size()}).reset_index()
s.set_index(s["Input.img_id"])
s["Percent"] = pd.Series(s["Count"]/20 * 100, index=s.index)

location = pd.DataFrame(columns=["Location", "Number"])
color = pd.DataFrame(columns=["Colors","Number"])
rowc = [["BN",47], ["LBN",40], ["LBB", 38], ["WN",42], ["WLB",49],["WB",39]]
for row in rowc:
    color.loc[len(color)] = row
color["Percentage"] = pd.Series(color.Number / 80 * 100)
color.set_index("Color", inplace=True)
print color
color.plot(kind="bar")
rows = [["Bot_left",63],["Top_Left",67],["Bot_Right",61],["Top_Right",64]]
for row in rows:
    location.loc[len(location)] = row
location["Percentage"] = pd.Series(location.Number / 120 * 100)
print location
location.set_index("Location", inplace=True) #Fixed!!!
location.plot(kind="bar")
plt.show()


# In[59]:

p = df[["WorkerId","Input.img_id","Answer.ans"]]

p.loc[(df['Input.img_id'].str.contains('bot_left')),'Location'] =  p[(df['Input.img_id'].str.contains('bot_left'))]['Input.img_id'].str[:8]
p.loc[(p["Input.img_id"].str.contains('bot_right')),"Location"] = p[(df['Input.img_id'].str.contains('bot_right'))]["Input.img_id"].str[:9]
p.loc[(p["Input.img_id"].str.contains('top_right')), "Location"] = p[(df['Input.img_id'].str.contains('top_right'))]["Input.img_id"].str[:9]
p.loc[(p["Input.img_id"].str.contains('top_left')), "Location"] = p[(df['Input.img_id'].str.contains('top_left'))]["Input.img_id"].str[:8]
p.loc[(p["Input.img_id"].str.contains('same')), "Location"] = "N/A"

p.loc[(p["Input.img_id"].str.contains("_bn")), "Color"] = p[(df['Input.img_id'].str.contains('_bn'))]["Input.img_id"].str[-2:]
p.loc[(p["Input.img_id"].str.contains("_lbn")), "Color"] = p[(df['Input.img_id'].str.contains('_lbn'))]["Input.img_id"].str[9:12]
p.loc[(p["Input.img_id"].str.contains("_lbb")), "Color"] = p[(df['Input.img_id'].str.contains('_lbb'))]["Input.img_id"].str[9:12]
p.loc[(p["Input.img_id"].str.contains("_wn")), "Color"] = p[(df['Input.img_id'].str.contains('_wn'))]["Input.img_id"].str[10:12]
p.loc[(p["Input.img_id"].str.contains("_wb")), "Color"] = p[(df['Input.img_id'].str.contains('_wb'))]["Input.img_id"].str[10:12]
p.loc[(p["Input.img_id"].str.contains("_wlb")), "Color"] = p[(df['Input.img_id'].str.contains('_wlb'))]["Input.img_id"].str[9:12]
p.loc[(p["Input.img_id"].str.contains("same")), "Color"] = "N/A"

p.loc[(p["Answer.ans"] == "Yes") & (p["Input.img_id"] !="same_identicon1.png"),"Correct"] = "No"
p.loc[(p["Answer.ans"] == "No") & (p["Input.img_id"] != "same_identicon1.png"), "Correct"] = "Yes"
p.loc[(p["Answer.ans"] == "Yes") & (p["Input.img_id"] =="same_identicon1.png"),"Correct"] = "Yes"
p.loc[(p["Answer.ans"] == "No") & (p["Input.img_id"] == "same_identicon1.png"), "Correct"] = "No"

del p["Answer.ans"]
del p["Input.img_id"]
p.to_csv("c:\\Users\\NYUK12STEM\\Desktop\\Final.csv")
print p

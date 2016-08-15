import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.style.use("ggplot")

df = pd.read_csv("C:\\Users\\NYUK12STEM\\Desktop\\Batch_2485769_batch_results.csv")
r = df[(df["WorkTimeInSeconds"] > 15)] #to attempt to remove results from people who didn't even try(25% of people) fuck 'em
only_main = r[["Input.img_id", "Answer.ans"]]
s = pd.DataFrame({'Count':only_main.groupby(["Input.img_id", "Answer.ans"]).size()}).reset_index()
s.set_index(s["Input.img_id"])
s["Percent"] = pd.Series(s["Count"]/20 * 100, index=s.index)
s = s[(s["Answer.ans"] == "Yes")]
#s[(s["Input.img_id"].str.contains("_bn"))]["Count"].sum()

location = pd.DataFrame(columns=["Location", "Number Wrong"])
color = pd.DataFrame(columns=["Colors","Number Wrong"])
rowc = [["BN",s[(s["Input.img_id"].str.contains("_bn"))]["Count"].sum()],
        ["LBN",s[(s["Input.img_id"].str.contains("_lbn"))]["Count"].sum()],
        ["LBB", s[(s["Input.img_id"].str.contains("_lbb"))]["Count"].sum()],
        ["WN",s[(s["Input.img_id"].str.contains("_wn"))]["Count"].sum()],
        ["WLB",s[(s["Input.img_id"].str.contains("_wlb"))]["Count"].sum()],
        ["WB",s[(s["Input.img_id"].str.contains("_wb"))]["Count"].sum()]]
for row in rowc:
    color.loc[len(color)] = row
color["Percentage"] = pd.Series(color["Number Wrong"] / 80 * 100)
color.set_index("Colors", inplace=True)
#color.to_csv("c:\\Users\\NYUK12STEM\\Desktop\\color_results.csv")
print color
color.plot(kind="bar")
rows = [["Bot_left",s[(s["Input.img_id"].str.contains("bot_left"))]["Count"].sum()],
        ["Top_Left",s[(s["Input.img_id"].str.contains("top_left"))]["Count"].sum()],
        ["Bot_Right",s[(s["Input.img_id"].str.contains("bot_right"))]["Count"].sum()],
        ["Top_Right",s[(s["Input.img_id"].str.contains("top_right"))]["Count"].sum()]]
for row in rows:
    location.loc[len(location)] = row
location["Percentage"] = pd.Series(location["Number Wrong"] / 120 * 100)
#location.to_csv("c:\\Users\\NYUK12STEM\\Desktop\\location_results.csv")
print location
location.set_index("Location", inplace=True)
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

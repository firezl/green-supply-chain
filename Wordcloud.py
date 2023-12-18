import matplotlib.pyplot as plt
from wordcloud import WordCloud

words = (
    "Purchase " * 2
    + "Waste Recycle "
    + "Taxonomy "
    + " Sustainable Supply Chain Management " * 5
    + "Cooperation "
    + "Pipeline "
    + "Network Design "
    + "Collaboration " * 2
    + "Contract Judicial"
    + "Supplier Selection " * 10
    + "Environmental Management System" * 2
    + "Environmental Performance " * 2
    + "Green Supply Chain Process Integration "
    + "Inventory Planning" * 2
    + "Sustainable Food Grain Supply Chains"
    + "Sustainable Performance" * 2
    + "Green Practices "
    + "Green Human Resource Management "
    + "Green-Sensitive Parties "
    + "Firm Performance "
    + "Business Competitive Performance "
    + "Internet-of-Things " * 2
    + "Block Chains"
    + "Global "
    + "Green Talent Management "
    + "Data Mining "
    + "Manufacturing Process "
    + "Design "
    + "Carbon Emissions "
    + "Logistics "
    + "Logistics "
    + "Demand "
    + "GIS "
)

wordcloud = WordCloud(
    background_color="white",
    width=1000,
    height=860,
    margin=2,
).generate(words)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
wordcloud.to_file("wordcloud.png")

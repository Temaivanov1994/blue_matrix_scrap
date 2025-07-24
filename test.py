import json

t1 = {
    " A. O. Smith Corporation (AOS) ": {
        "Risks": "Residential Markets. U.S. Existing Home Sales, a driver of Remodeling, which impacts Residential Water Heaters, declined from 2022 through 2024. They are more stable this year but are still modestly declining and the current levels of Existing Home Sales are much lower than several years ago. A lack of inventory of homes for sale and high home prices are other restraints in these markets. Mortgage rates remain considerably higher than 18 months ago.\nCommercial Markets. Part of our macro thesis is Commercial markets will broadly weaken in 2H25 owing to tariff uncertainties, government layoffs and deportations.\nChina Uncertainty. China Water Heater and Treatment markets are weak. Retail spending has improved somewhat, but housing markets remain pressured.\nShare Loss. Over the last decade, AOS has lost share in Residential WHs. Tankless water heater demand growth has exceeded conventional tank and the company has been behind this trend. Key customer Sears went bankrupt. We estimate Home Depot-HD-NR (Rheem brands) has outperformed Lowes-LOW-NR (A.O. Smith brands) in the category.\n",
        "Price": "N/A\n",
        "Scrap:Time": "17:07:2025 19:51"
    }
}
t2 = {
    " A. O. Smith Corporation (AOS) ": {
        "Risks": "Residential Markets. U.S. Existing Home Sales, a driver of Remodeling, which impacts Residential Water Heaters, declined from 2022 through 2024. They are more stable this year but are still modestly declining and the current levels of Existing Home Sales are much lower than several years ago. A lack of inventory of homes for sale and high home prices are other restraints in these markets. Mortgage rates remain considerably higher than 18 months ago.\nCommercial Markets. Part of our macro thesis is Commercial markets will broadly weaken in 2H25 owing to tariff uncertainties, government layoffs and deportations.\nChina Uncertainty. China Water Heater and Treatment markets are weak. Retail spending has improved somewhat, but housing markets remain pressured.\nShare Loss. Over the last decade, AOS has lost share in Residential WHs. Tankless water heater demand growth has exceeded conventional tank and the company has been behind this trend. Key customer Sears went bankrupt. We estimate Home Depot-HD-NR (Rheem brands) has outperformed Lowes-LOW-NR (A.O. Smith brands) in the category.\n",
        "Price": "N/A\n",
        "Scrap:Time": "17:07:2025 19:51"
    }
}
t3 = {
    " ACI Worldwide, Inc. (ACIW) ": {
        "Risks": "Competition: Fintech is a highly competitive sector, and the companies ACI competes against may offer similar products or may have similar strategies. This may put pressure on ACI, including in terms of its operating budget, market share, and its ability to remain relevant with its clients.\nRegulatory: ACI operates in a highly regulated industry. Any changes in regulations or failure to comply can result in hefty fines and reputational damage.\nTechnological: The fintech industry is rapidly evolving, and failure to keep up with technological advancements can potentially make ACI offerings obsolete.\nEconomic: Macro downturns can lead to reduced spending by financial institutions, impacting ACI’s revenue. Currency fluctuations can also affect the company's revenue and earnings.\n",
        "Price": "Our price target of $77 is based on 18x/16x our '25/'26E EV/EBITDA.\n",
        "Scrap:Time": "17:07:2025 19:51"
    }
}

t4 =[" Walt Disney Co. (DIS) "]: {
        "Source": "bluematrix.com",
        "Tiket": " Walt Disney Co. (DIS) ",
        "Risks": "Downside risks to our DIS investment thesis include: any potential recessionary impact on consumer spending, media partner and sponsorship demand and pricing; continued cord-cutting pressures on retaining subscribers and their fees that support new content creation; programming that misses the mark on consumer taste and demand; the above impacts on advertising impressions and pricing; geopolitical issues, FX rates, and macroeconomic impacts on international visitation to theme parks; competition for video consumers’ time and the ability to monetize that usage via advanced advertising and subscriptions. Also, advertisers have been allocating more of their budgets toward experiences and away from linear television and traditional print media, which could mean more competition for a smaller ad budget. Advertising technologies that rely on first- and third-party data of actual viewership could also be a risk if DIS audiences are not at the levels that advertisers expected. If viewership falls significantly, DIS may be forced to shut some channels and lose those subscriber fees and ad impressions.\n",
        "Price": "We place a 50% weight on our $128/sh DCF, 10% on our discounted P/E metric-based $152/sh, and 40% on our $127/sh SOTP metric\n"
    }
        

tiket = " Walt Disney Co. (DIS) "

def isFresh(data):
    return data == t1
    
    

if __name__ == "__main__": 
    
    with open("async_data.json","r",encoding="utf-8") as file:
        data_list = json.load(file)
    #print(isFresh(t2))   
    
    
    
    
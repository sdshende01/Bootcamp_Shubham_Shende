# ETF/Mutual Funds Analyzer for Retail Individual Investors

**Stage:** Stage 01

## Problem Statement
Individual investors have varying degrees of risk aversion depending on factors such as:

- Active and passive income  
- Financial literacy  
- Past experience with investments  
- Monthly expenses  
- Net worth  
- Future financial goals or expected expenses  

Human judgment can sometimes fail in providing optimal investment advice. Retail investors may also choose inappropriate investment products due to influence from greed or misinformation.  

This project aims to categorize investors based on their risk tolerance and recommend ETFs or Mutual Funds that align with their expected returns.  

## ML Use Cases
1. **Classification of Investors:** Categorize investors based on risk profile.  
2. **Return Forecasting of ETF/MF Products (Optional):** Predict potential returns to guide better decision-making.  
3. **Portfolio Diversification Recommendations:** Suggest complementary investment products once a certain level of wealth is achieved.  

## Goal
### Goals
- Build a simple predictive model for various index mutual fund performance.  
- Provide Retail Individual Investors (RIIs) with insights.  
- Deliver outputs in an interpretable format.  
- Recommend funds aligned with investor risk profiles and diversification needs.  

### Lifecycle
1. **Data Collection**: Gather NAV data of mutual funds along with benchmark index data.  
2. **Data Cleaning**: Handle missing values, align dates, normalize and structure data for analysis.  
3. **Exploratory Data Analysis**: Study return patterns, volatility, and correlation with the index.  
4. **Modeling**: Implement baseline predictive models to forecast returns.  
5. **Evaluation**: Assess model accuracy.  
6. **Delivery**: Provide predictive notebook for actionable insights.  

### Deliverables
- `/data/` → Raw and cleaned NAV + Nifty50 datasets.  
- `/src/` → Scripts for preprocessing, feature engineering, modeling, and evaluation.  
- `/notebooks/` → Jupyter notebooks for EDA and modeling experiments.  
- `/docs/` → Stakeholder memo / framing slides explaining problem, goals, and recommendations.  
- `README.md` → Project overview including goals, lifecycle, and deliverables.  


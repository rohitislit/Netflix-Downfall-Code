# The Downfall of Netflix 📉

**Using COVID-19 Cases and Vaccination Data to Predict Netflix’s Stock Price**  
*Author: Rohit Sriram*  
*Publication Date: September 2022*

---

## 📌 Introduction

Netflix, a major player in the streaming industry and a FAANG company, experienced rapid stock growth during the COVID-19 pandemic. In November 2021, it hit an all-time high of $691. However, in early 2022, Netflix lost nearly 970,000 subscribers in Q2 alone, leading to a steep stock decline. Meanwhile, competitors like Disney+ and HBO Max saw increased subscriptions, with Disney+ even surpassing Netflix.

---

## 📈 Stock Price Background

Stocks reflect investor confidence. As Netflix grew, so did its stock — until early 2022. After peaking in early 2021, Netflix's price fell sharply, signaling reduced confidence among shareholders.

---

## 🦠 COVID-19's Influence

COVID-19 led to over 92 million cases and 1 million+ deaths in the U.S. With people quarantined at home, Netflix saw a subscriber boost. However, as restrictions lifted in 2022, its momentum slowed.

---

## 📊 Data Trends

### 📉 COVID-19 Case Trend
- Cases rose through 2020, peaked in early 2022, then declined.
  
### 💵 Netflix Stock Price Trend
- Stock mirrored COVID case trends initially.
- Peaked in late 2021, then declined as lockdowns eased.

### 💉 Vaccination Trend
- Vaccinations rose in late 2020–early 2021.
- Netflix stock dipped slightly during this time, with a more noticeable decline as vaccinations spiked again in late 2021.

---

## 🔁 3D Modeling

A 3D model was created using:
- **X-axis:** Vaccination numbers  
- **Y-axis:** COVID-19 case counts  
- **Z-axis:** Netflix stock prices

Surprisingly, stock prices increased with higher vaccinations and lower case numbers — likely due to investor confidence in economic reopening rather than lockdown streaming habits.

---

## 📈 Linear Regression

Two separate linear regression models were used:
1. **COVID-19 cases vs Netflix stock price**
2. **Vaccination count vs Netflix stock price**

Both showed **positive correlations** — contrary to expectations. Investors likely anticipated continued growth during the pandemic.

---

## 📊 Multiple Linear Regression

A combined regression model using both vaccination and case data predicted Netflix stock price:
- **Predicted:** \$602.4
- **Actual:** \$546.7  
- **Error:** ~10%

This demonstrates decent predictive performance using only two independent features.

---

## 🧠 Conclusion

Linear and multiple regression models using pandemic data offer insights into Netflix’s stock movements. Although COVID-19 trends affected performance, **competition** and **content quality** also played critical roles.

> For example: Disney+ gained 7.9 million new subscribers in early 2022 alone.

Future models could be expanded to other streaming services or economic sectors for early trend detection and strategic planning.

---

## 🔗 References

1. [Netflix Stock History - Yahoo Finance](https://finance.yahoo.com/quote/NFLX/history?p=NFLX)
2. [Our World in Data: COVID Vaccinations](https://ourworldindata.org/covid-vaccinations)
3. [WHO COVID-19 Dashboard](https://covid19.who.int/data)
4. [Disney Passes Netflix in Subscribers](https://deadline.com/2022/08/disney-just-passed-netflix-in-total-streaming-subscribers-1235089361/)

---

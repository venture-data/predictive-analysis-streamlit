import streamlit as st
import random
import plotly.graph_objects as go
import matplotlib.pyplot as plt

def generate_forecast(target_revenue):
    facebook_spend_percentage = random.uniform(8, 10)
    google_spend_percentage = random.uniform(3, 5)
    total_spend = facebook_spend_percentage + google_spend_percentage #target_revenue * (facebook_spend_percentage + google_spend_percentage) / 100

    facebook_revenue_percentage = random.uniform(32, 35)
    google_revenue_percentage = random.uniform(14, 16)
    organic_revenue_percentage = 100 - (facebook_revenue_percentage + google_revenue_percentage)
    facebook_revenue = target_revenue * facebook_revenue_percentage / 100
    google_revenue = target_revenue * google_revenue_percentage / 100
    organic_revenue = target_revenue * organic_revenue_percentage / 100

    return total_spend, facebook_revenue, google_revenue, organic_revenue

# Streamlit app
st.title("Revenue Forecast App")

# Input form
target_revenue = st.number_input("Enter the target revenue:", min_value=0.0, step=1.0)
months = ["January", "February", "March", "April", "May", "June" ,"July", "August",
          "September", "October", "November", "December"]
selected_month = st.selectbox("Select a month:", months)

if st.button("Forecast"):
    total_spend, facebook_revenue, google_revenue, organic_revenue = generate_forecast(target_revenue)
    facebook_spend_percentage = (total_spend / target_revenue) * 100 * random.uniform(8, 10) / (random.uniform(8, 10) + random.uniform(3, 5))
    google_spend_percentage = (total_spend / target_revenue) * 100 * random.uniform(3, 5) / (random.uniform(8, 10) + random.uniform(3, 5))

    st.subheader("Forecast for " + selected_month)
    st.write("Total Spend: $", round(total_spend, 2))
    st.write("Facebook Spend: $", round(total_spend * (facebook_spend_percentage / (facebook_spend_percentage + google_spend_percentage)), 2))
    st.write("Google Spend: $", round(total_spend * (google_spend_percentage / (facebook_spend_percentage + google_spend_percentage)), 2))

    st.write("Facebook Revenue: $", round(facebook_revenue, 2))
    st.write("Google Revenue: $", round(google_revenue, 2))
    st.write("Organic Revenue: $", round(organic_revenue, 2))

    # Visualization - Pie Chart
    labels = ['Facebook Revenue', 'Google Revenue', 'Organic Revenue']
    values = [facebook_revenue, google_revenue, organic_revenue]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig.update_layout(title="Revenue Composition", height=400)
    st.plotly_chart(fig)

    # Visualization - Bar Chart
    categories = ['Spend', 'Facebook Revenue', 'Google Revenue', 'Organic Revenue']
    amounts = [total_spend, facebook_revenue, google_revenue, organic_revenue]

    plt.figure(figsize=(10, 6))
    plt.bar(categories, amounts)
    plt.xlabel('Categories')
    plt.ylabel('Amount ($)')
    plt.title('Revenue Breakdown')
    st.pyplot(plt)

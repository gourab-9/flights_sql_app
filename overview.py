import streamlit as st

def main():
    st.title('Welcome to Your Ultimate Flight Information Dashboard! ⋆｡˚ ✈︎ ✈️ ⋆ ')

    # Overview Section
    st.header('Overview:')
    st.write("Explore the world of flights with our comprehensive dashboard designed to provide you with real-time insights "
             "and analytics on flight data between cities in India. Whether you're a frequent traveler or planning your next journey, "
             "our dashboard is your go-to tool for fetching price details and visualizing traffic patterns.")

    # Key Features Section
    st.header('Key Features:')
    st.subheader('Price Comparison:')
    st.write("- Effortlessly compare flight prices between any two cities in India.")
    st.write("- Get instant and accurate fare details to make informed decisions for your travel plans.")

    st.subheader('Real-time Data:')
    st.write("- Our dashboard fetches real-time data to ensure that you have the most up-to-date information at your fingertips.")

    st.subheader('Analytics and Visualization:')
    st.write("- Dive into the fascinating world of flight traffic patterns with our interactive analytics page.")
    st.write("- Explore visually appealing graphs and charts that provide insights into the popularity and trends of flight routes.")

    st.subheader('User-Friendly Interface:')
    st.write("- Intuitive design for a seamless user experience.")
    st.write("- Easily navigate through different features and visualize data without any hassle.")

    # How to Use Section
    st.header('How to Use:')
    st.subheader('Flight Search:')
    st.write("- Select your departure and destination cities.")
    st.write("- Click 'Search' to fetch the latest flight prices.")

    st.subheader('Analytics Page:')
    st.write("- Head to the Analytics section to discover interesting and valuable insights.")
    st.write("- Explore various graphs to understand the dynamics of flight traffic between cities.")

    # Why Choose Section
    st.header('Why Choose [Your Project Name]?')
    st.write("- Reliability: Trust our real-time data for accurate and dependable flight information.")
    st.write("- User-Centric Design: We prioritize simplicity and ease of use to enhance your overall experience.")
    st.write("- Comprehensive Analytics: Gain valuable insights to make smarter travel decisions.")

    st.write("Embark on a journey of discovery with [Your Project Name]—your ultimate companion in the world of flight information.")

if __name__ == "__main__":
    main()

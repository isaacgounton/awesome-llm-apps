# Import the required libraries
import streamlit as st
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.yfinance import YFinanceTools

# Set up the Streamlit app
st.title("AI Investment Agent 📈🤖")
st.caption("This app allows you to compare the performance of two stocks and generate detailed reports.")

# Get OpenAI API key from user
openai_api_key = st.text_input("OpenAI API Key", type="password")

if openai_api_key:
    # Create an instance of the Agent
    agent = Agent(
        llm=OpenAIChat(model="gpt-4o", api_key=openai_api_key),
        tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
        show_tool_calls=True,
        markdown=True
    )

    # Input fields for the stocks to compare
    stock1 = st.text_input("Enter the first stock symbol")
    stock2 = st.text_input("Enter the second stock symbol")

    if stock1 and stock2:
        # Get the response from the Agent
        query = f"Compare {stock1} to {stock2}. Use every tool you have."
        response = agent.run(query, stream=False)
        st.write(response.content)
import streamlit as st

from load_css import local_css
from customer_profile import CustomerProfile
from customers_data import CustomersData

#***********************************************************************************************************************
#***********************************************************************************************************************
local_css('style.css')

#***********************************************************************************************************************
#***********************************************************************************************************************
st.title('Customer Profiling')

customersData = CustomersData()

#***********************************************************************************************************************
#***********************************************************************************************************************
st.header('Raw Data')

@st.cache
def load_customers_data_to_streamlit():
    dataPandas = customersData.load_data_pandas()
    return dataPandas

dataLoadingState = st.text('Loading customers data...')
dfCustomersPandas = load_customers_data_to_streamlit()
dataLoadingState.text('Loading customers data... DONE!')

if st.checkbox('Show Raw Data'):
    st.write(dfCustomersPandas)

#***********************************************************************************************************************
#***********************************************************************************************************************
st.header('Customer Profile')

form = st.form(key='customer_profile')

customerId = form.text_input(label='Enter Customer ID')

getProfileButton = form.form_submit_button(label='Get Profile')

if getProfileButton:
    dataLoadingState = st.text('Loading customer profile...')

    customerInfo = customersData.get_customer_data(dfCustomersPandas, int(customerId))

    customerProfile = CustomerProfile(
        userId=customerInfo['UserId'],
        averageOddValuePerSelection=float(customerInfo['AverageOddValuePerSelection']),
        totalNumberOfCouspons=float(customerInfo['TotalNumberOfCoupons']),
        averageNumberOfSelectionsPerCoupon=float(customerInfo['AverageNumberOfSelectionsPerCoupon']),
        averageCouponStake=float(customerInfo['AverageCouponStake']),
        averageCouponReturn=float(customerInfo['AverageCouponReturn']),
        highestCouponStake=float(customerInfo['HighestCouponStake']),
        highestCouponReturn=float(customerInfo['HighestCouponReturn']),
        totalStake=float(customerInfo['TotalStake']),
        totalReturn=float(customerInfo['TotalReturn']),
        netEarnings=float(customerInfo['NetEarnings']),
        percentageReturnOnStake=float(customerInfo['PercentageReturnOnStake']),
        winningStatus=float(customerInfo['WinningStatus'])
    )

    dataLoadingState.text('Loading customer profile... DONE!')

    winningStatusText = ''
    if customerProfile.winningStatus == 1.0:
        winningStatusText = "<span class='highlight_green'>WINNING</span>"

    if customerProfile.winningStatus == -1.0:
        winningStatusText = "<span class='highlight_red'>LOSING</span>"

    st.write(f'Customer ID: {customerProfile.userId}')
    st.write(f'Average Odd Value Per Selection: {customerProfile.averageOddValuePerSelection}')
    st.write(f'Total Number of Coupons: {customerProfile.totalNumberOfCouspons}')
    st.write(f'Average Number of Selections Per Coupon: {customerProfile.averageNumberOfSelectionsPerCoupon}')
    st.write(f'Average Coupon Stake: {customerProfile.averageCouponStake}')
    st.write(f'Average Coupon Return: {customerProfile.averageCouponReturn}')
    st.write(f'Highest Coupon Stake: {customerProfile.highestCouponStake}')
    st.write(f'Highest Coupon Return: {customerProfile.highestCouponReturn}')
    st.write(f'Total Stake: {customerProfile.totalStake}')
    st.write(f'Total Return: {customerProfile.totalReturn}')
    st.write(f'Net Earnings: {customerProfile.netEarnings}')
    st.write(f'Percentage Return on Stake: {customerProfile.percentageReturnOnStake}')

    # winningStatusText = f"<div>Winning Status: <span class='highlight green'>WINNING</span></div>"
    st.markdown(f'Winning Status: {winningStatusText}', unsafe_allow_html=True)








# 301961
















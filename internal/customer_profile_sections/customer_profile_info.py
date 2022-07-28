import streamlit as st

from datamodel.customer_profile import CustomerProfile
from utils.show_data import show_data
from utils.layout import insert_blank
from utils.format_data import get_date_string, get_gender_string


def show_customer_profile_info(customerProfile: CustomerProfile):
    st.subheader("Info")

    col1, col2, col3 = st.columns(3)

    show_data(label="User ID", value=customerProfile.userId, inBold=True, column=col1)
    show_data(label="User Platform ID", value=customerProfile.userPlatformId, inBold=True, column=col2)
    insert_blank(column=col3)

    show_data(label="First Name", value=customerProfile.firstName, inBold=True, column=col1)
    show_data(label="Last Name", value=customerProfile.lastName, inBold=True, column=col2)
    show_data(label="User Type", value=customerProfile.userTypeName, inBold=True, column=col3)

    show_data(label="Username", value=customerProfile.username, inBold=True, column=col1)
    show_data(label="Email", value=customerProfile.email, inBold=True, column=col2)
    show_data(label="Verification Level", value=customerProfile.verificationLevelName, inBold=True, column=col3)

    show_data(
        label="Subscription Date",
        value=get_date_string(dateKey=customerProfile.subscriptionDateKey),
        inBold=True,
        column=col1,
    )
    show_data(label="Country", value=customerProfile.countryName, inBold=True, column=col2)
    show_data(label="Currency", value=customerProfile.userCurrencyName, inBold=True, column=col3)

    show_data(label="Gender", value=get_gender_string(gender=customerProfile.gender), inBold=True, column=col1)
    show_data(
        label="Birth Date", value=get_date_string(dateKey=customerProfile.birthDateKey), inBold=True, column=col2
    )
    show_data(label="Age", value=customerProfile.age, inBold=True, column=col3)

    show_data(label="Street Address", value=customerProfile.streetAddress, inBold=True, column=col1)
    show_data(label="Town", value=customerProfile.town, inBold=True, column=col2)
    show_data(label="Zip Code", value=customerProfile.zipCode, inBold=True, column=col3)

    show_data(label="Phone", value=customerProfile.phone, inBold=True, column=col1)
    show_data(label="Mobile Phone", value=customerProfile.mobilePhone, inBold=True, column=col2)
    show_data(label="IP Address", value=customerProfile.clientIP, inBold=True, column=col3)

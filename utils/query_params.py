import streamlit as st
from enum import Enum
from datamodel.constants import DEFAULT_USER_ID


class QueryParams(str, Enum):
    USER_ID = "UserId"


def manage_query_params() -> dict:
    queryParams = st.experimental_get_query_params()

    # if QueryParams.USER_ID not in queryParams.keys():
    #     queryParamsToAdd = {QueryParams.USER_ID.value: [DEFAULT_USER_ID]}
    #     queryParams.update(queryParamsToAdd)
    #     st.experimental_set_query_params(**queryParams)

    return queryParams


# Note: DO NOT update query params, it messes with the caching!
# def update_query_params(userId: str):
#     queryParams = st.experimental_get_query_params()
#
#     if QueryParams.USER_ID in queryParams.keys():
#         queryParams[QueryParams.USER_ID.value] = [userId]
#     else:
#         queryParamsToAdd = {
#             QueryParams.USER_ID.value: [userId]
#         }
#         queryParams.update(queryParamsToAdd)
#
#     st.experimental_set_query_params(**queryParams)

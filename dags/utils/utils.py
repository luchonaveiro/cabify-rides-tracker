"Utils functions"

import imaplib
from datetime import datetime
import pandas as pd


def filter_mail_inbox(imap: imaplib.IMAP4_SSL, date_from: str, date_to: str):
    """
    Return INBOX mails IDs from no-reply@cabify.com for a specified date range

    """
    imap.select("INBOX")
    peya_typ, peya_data = imap.search(None, '(FROM "no-reply@cabify.com")')
    date_typ, date_data = imap.search(None, f'(SINCE "{date_from}" BEFORE "{date_to}")')
    ids = list(set(peya_data[0].split()) & set(date_data[0].split()))

    return ids


def create_dataframe(
    email_id: int,
    date: datetime,
    base_price: float,
    processing_fee: float,
    high_demand_fee: float,
    total_price: float,
    trip_duration: str,
):
    """
    Creates the Cabify dataframe to insert on the DB
    """
    base_price = base_price if base_price is not None else 0.00
    processing_fee = processing_fee if processing_fee is not None else 0.00
    high_demand_fee = high_demand_fee if high_demand_fee is not None else 0.00
    total_price = total_price if total_price is not None else 0.00

    cabify_df = pd.DataFrame(
        {
            "id": [email_id],
            "date": [date],
            "base_price": [base_price],
            "processing_fee": [processing_fee],
            "high_demand_fee": [high_demand_fee],
            "total_price": [total_price],
            "trip_duration": [trip_duration],
        }
    )

    return cabify_df

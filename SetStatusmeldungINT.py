import sys
import time
from datetime import datetime, timezone

from Curl_11_GenerateToken import Curl_11_GenerateToken
from Curl_12_GenerateMsgSignature import Curl_12_GenerateMsgSignature
from Curl_13_GenerateSignature64 import Curl_13_GenerateSignature64
from Curl_14_GenerateAndSendCurlRequest import Curl_14_GenerateAndSendCurlRequest

# from Utils.Accounts.BundID_Accounts import BundID_Accounts
# from Utils.TestDaten.BundID_ZBP_TestDaten import BundID_ZBP_TestDaten

if __name__ == '__main__':

    # Wenn eine neuer Antrag erstellt werden soll, muss überSAMl eine neue Applikation ID erstellt werden

    text_content = "Senden einer Nachricht via Rest mit einem Anhang(pdf)"

    # title = "Test Via REST mit Anhang (pdf)"
    title = "Antrag auf Elterngeld"

    stork_qa_level = "1"
    cert_passwort = "abc123"
    url = "https://int.zbp.bund.de"

    handle = ""
    current_timestamp = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
    application_id = "d853e553-306e-4989-ba4b-1963a56450bb"

    # created_date = BundID_Accounts.HANDLE_REST_INT_CREATED_DATE_INT
    # created_date = "2025-01-14T15:15:42.198Z"
    now = datetime.now(timezone.utc)

    # Format the datetime in the required format
    created_date = now.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"

    # status = "NONE" # <None> # Zusetzen von ZBP # FEHLER
    # status = "INITIATED"  # Antrag in Erstellung # Zusetzen von Onlinedienst
    # status = "SUBMITTED"  # Antrag versendet # Zusetzen von Onlinedienst
    # status = "RECEIVED"  # Antrag eingegangen # Zusetzen von Fachverfahren
    # status = "PROCESSING"  # Antrag in Prüfung # Zusetzen von Fachverfahren
    # status = "ACTION_REQUIRED"
    status = "PROCESSING"

# Erstellung eines Tokens ##############################################################################################

    curl_11_generate_token = Curl_11_GenerateToken()
    curl_11_generate_token.create_token()
    time.sleep(2)

# Generierung der msg-signatur und der signatur.b64Erstellung eines Tokens #############################################

    curl_12_generate_msg_signature = Curl_12_GenerateMsgSignature(
        text_content=text_content,
        date=current_timestamp,
        title=title,
        strok_qa_level=stork_qa_level,
        handle=handle)

    curl_12_generate_msg_signature.create_printf_set_statusmeldung(
        status=status,
        application_id=application_id,
        created_date=created_date,
    )

    curl_12_generate_msg_signature.send_printf_set_statusmeldung()
    time.sleep(5)

    curl_13_generate_signature_64 = Curl_13_GenerateSignature64()
    curl_13_generate_signature_64.create_signature()
    time.sleep(1)

# Erstellung und senden des Curl commands ##############################################################################

    curl_14_generate_and_send_curl_request = Curl_14_GenerateAndSendCurlRequest(
        url=url,
        cert_passwort=cert_passwort,
        date=current_timestamp,
        text_content=text_content,
        title=title,
        strok_qa_level=stork_qa_level,
        handle=handle)

    curl_14_generate_and_send_curl_request.create_curl_command_set_statusmeldung(
        status=status,
        application_id=application_id,
        created_date=created_date,
        )

    curl_14_generate_and_send_curl_request.send_curl_command_set_statusmeldung()


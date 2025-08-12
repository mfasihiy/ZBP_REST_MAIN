import datetime
import os
import sys
import time

# from Utils.Accounts.BundID_Accounts import BundID_Accounts

from Curl_11_GenerateToken import Curl_11_GenerateToken
from Curl_12_GenerateMsgSignature import Curl_12_GenerateMsgSignature
from Curl_13_GenerateSignature64 import Curl_13_GenerateSignature64
from Curl_14_GenerateAndSendCurlRequest import Curl_14_GenerateAndSendCurlRequest

if __name__ == '__main__':

    """
    Tested 12.08 
    PASS
    """

    with open("response.json", "w") as f:
        pass

    stork_qa_level = "1"
    cert_passwort = "abc123"
    url = "https://int.zbp.bund.de"
    # handle = "60638836-f219-4ce7-b03a-2f2441d20ac6"
    handle = "4656d80b-5600-4217-a226-7309b055d7d4"
    current_timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")

    anhang_pfad = "Utils/Anhaenge/"

    anhang_1 = "eicar.txt"
    anhang_2 = "115.pdf"
    anhang_3 = "Aktivitäten.jpg"
    anhang_4 = "Autotest_Anmeldeoptionen.tif"

    mimeType_anhang_1 = "image/bmp"
    mimeType_anhang_2 = "application/pdf"
    mimeType_anhang_3 = "image/jpeg"
    mimeType_anhang_4 = "image/tiff"

########################################################################################################################

    title = f" [SOGETI] Rest mit 1 Anhang: {anhang_1}"
    text_content = title

    retrievalConfirmationAddress = None

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
        handle=handle,
        retrievalConfirmationAddress=retrievalConfirmationAddress)

    anhang_sha_sum, contentLength = curl_12_generate_msg_signature.\
        create_printf_command_send_msg_with_1_attachment_return_shasum_and_content_lenght_from_attachement(
        anhang=anhang_1,
        anhang_pfad=anhang_pfad)

    curl_12_generate_msg_signature.send_printf_command_send_msg_with_attachment()
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
        handle=handle,
        retrievalConfirmationAddress=retrievalConfirmationAddress)

    curl_14_generate_and_send_curl_request.create_curl_command_send_msg_with_attachments(
        anhang=anhang_1,
        anhang_pfad=anhang_pfad,
        shasum_attachement=anhang_sha_sum,
        contentLength=contentLength,
        mimetype=mimeType_anhang_1
    )

    time.sleep(5)
    http_status = curl_14_generate_and_send_curl_request.send_curl_command_send_msg_with_attachment()

    try:
        assert http_status == 200, f"Expected HTTP status 200, but got {http_status}"

        print(f"✅ Test Passed: HTTP status {http_status} is as expected!")

    except AssertionError as e:
        print(f"❌ Test failed: {e}")
        raise






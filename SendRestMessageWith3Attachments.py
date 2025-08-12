import datetime
import os
import sys
import time

from Curl_11_GenerateToken import Curl_11_GenerateToken
from Curl_12_GenerateMsgSignature import Curl_12_GenerateMsgSignature
from Curl_13_GenerateSignature64 import Curl_13_GenerateSignature64
from Curl_14_GenerateAndSendCurlRequest import Curl_14_GenerateAndSendCurlRequest
from Utils.Accounts.BundID_Accounts import BundID_Accounts
from Utils.TestDaten.BundID_ZBP_TestDaten import BundID_ZBP_TestDaten

if __name__ == '__main__':

    """
    Tested 09.12 
    PASS
    """

########################################################################################################################

    stork_qa_level = "1"
    cert_passwort = "#MiFFo8755-Xz7"
    url = "https://int.zbp.bund.de"

########################################################################################################################

    handle = BundID_Accounts.HANDLE_REST_INT
    current_timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")

    anhang_pfad = "../../../Utils/Anhänge/"

    anhang_1 = "16bitt.bmp"
    anhang_2 = "115.pdf"
    anhang_3 = "Autotest_Anmeldeoptionen.tif"

    mimeType_anhang_1 = "image/bmp"
    mimeType_anhang_2 = "application/pdf"
    mimeType_anhang_3 = "image/tiff"


########################################################################################################################

    text_content = f" [SOGETI] Rest mit 3 Anhaengen: {anhang_1}-{anhang_2}-{anhang_3}"
    title = text_content

    retrievalConfirmationAddress=None

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

    shasum_anhang_1,\
        contentLength_anhang_1,\
        shasum_anhang_2,\
        contentLength_anhang_2,\
        shasum_anhang_3,\
        contentLength_anhang_3  = curl_12_generate_msg_signature.\
        create_printf_command_send_msg_with_3_attachment_return_shasum_and_content_lenght_from_attachement(
        anhang_1 = anhang_1,
        anhang_2 = anhang_2,
        anhang_3 = anhang_3,
        anhang_pfad = anhang_pfad,
    )

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

    curl_14_generate_and_send_curl_request.create_curl_command_send_msg_3_attachments(
        anhang_1=anhang_1,
        anhang_2=anhang_2,
        anhang_3=anhang_3,
        anhang_pfad=anhang_pfad,
        shasum_anhang_1=shasum_anhang_1,
        shasum_anhang_2=shasum_anhang_2,
        shasum_anhang_3=shasum_anhang_3,
        contentLength_anhang_1=contentLength_anhang_1,
        contentLength_anhang_2=contentLength_anhang_2,
        contentLength_anhang_3=contentLength_anhang_3,
        mimetype_anhang_1=mimeType_anhang_1,
        mimetype_anhang_2=mimeType_anhang_2,
        mimetype_anhang_3=mimeType_anhang_3,
    )

    time.sleep(5)

    curl_14_generate_and_send_curl_request.send_curl_command_send_msg_with_attachment()






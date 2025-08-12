import datetime
import time

# from Utils.Accounts.BundID_Accounts import BundID_Accounts
# from Utils.TestDaten.BundID_ZBP_TestDaten import BundID_ZBP_TestDaten

from Curl_11_GenerateToken import Curl_11_GenerateToken
from Curl_12_GenerateMsgSignature import Curl_12_GenerateMsgSignature
from Curl_13_GenerateSignature64 import Curl_13_GenerateSignature64
from Curl_14_GenerateAndSendCurlRequest import Curl_14_GenerateAndSendCurlRequest

if __name__ == '__main__':

    with open("response.json", "w") as f:
        pass

    cert_passwort = "abc123"
    stork_qa_level = "1"
    url = "https://int.zbp.bund.de"

########################################################################################################################

    handle = "60638836-f219-4ce7-b03a-2f2441d20ac6"

    current_timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
    title = f" [SOGETI] REST Test ohne Anhang"
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

    curl_12_generate_msg_signature.create_printf_command_send_msg()

    curl_12_generate_msg_signature.send_printf_command_send_msg()
    time.sleep(5)

    curl_13_generate_signature_64 = Curl_13_GenerateSignature64()
    curl_13_generate_signature_64.create_signature()
    time.sleep(1)

# Erstellung und senden des Curl commands ###############################

    curl_14_generate_and_send_curl_request = Curl_14_GenerateAndSendCurlRequest(
        url=url,
        cert_passwort=cert_passwort,
        date=current_timestamp,
        text_content=text_content,
        title=title,
        strok_qa_level=stork_qa_level,
        handle=handle,
        retrievalConfirmationAddress=retrievalConfirmationAddress)

    curl_14_generate_and_send_curl_request.create_curl_command_send_msg_without_attachment()

    time.sleep(5)
    http_status = curl_14_generate_and_send_curl_request.send_curl_command_send_msg_without_attachment()

    try:
        assert http_status == 200, f"Expected HTTP status 200, but got {http_status}"

        print(f"✅ Test Passed: HTTP status {http_status} is as expected!")

    except AssertionError as e:
        print(f"❌ Test failed: {e}")
        # Optionally, you can raise the error again if you want the test to fail
        raise


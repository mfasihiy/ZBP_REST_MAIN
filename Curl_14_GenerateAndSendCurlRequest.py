import json
import re
import subprocess
import sys

# from BundID_ZBP_SeleniumFramework.TestDaten.BundID_TestDaten import BundID_TestDaten

class Curl_14_GenerateAndSendCurlRequest:

    def __init__(self, cert_passwort,
                 date,
                 title,
                 handle,
                 strok_qa_level,
                 text_content,
                 retrievalConfirmationAddress="string",
                 url="https://int.zbp.bund.de"):

        # Das programm benötigt den token der gespeichert wurde
        with open('tokens/token.txt', 'r') as file:
            self.token = file.read().strip()

        with open('signature.b64', 'r') as file:
            self.signature = file.read().strip()

        # Definiere die Variablen
        self.handle = handle
        self.password = cert_passwort
        self.text_content = text_content

        self.git_bash_path = "C:\\Program Files\\Git\\git-bash.exe"
        self.date = date
        self.title = title
        self.strok_qa_level = strok_qa_level
        self.url = url

        if retrievalConfirmationAddress == None:
            self.retrievalConfirmationAddress = "string"

    def create_curl_command_send_msg_without_attachment(self):

        curl_command = (
            f"curl -v -k -4 -X 'PUT' '{self.url}/v6/mailbox/messages' "
            f"-H 'accept: application/json' "
            f"-H 'Authorization: Bearer {self.token}' "
            f"-H 'Content-Type: multipart/form-data' "
            f"-F 'json={{\"content\":\"{{\\\"mailboxUuid\\\": \\\"{self.handle}\\\","
            f"\\\"stork_qaa_level\\\": {self.strok_qa_level},"
            f"\\\"sender\\\": \\\"Sogeti_Test_Verfahren_02\\\","
            f"\\\"title\\\": \\\"{self.date}: {self.title}\\\","
            f"\\\"content\\\": \\\"{self.text_content}\\\","
            f"\\\"service\\\": \\\"Sogeti_Test_Verfahren_02\\\","
            f"\\\"retrievalConfirmationAddress\\\": \\\"{self.retrievalConfirmationAddress}\\\","
            f"\\\"replyAddress\\\": \\\"string\\\","
            f"\\\"attachments\\\":[],"
            f"\\\"reference\\\": \\\"string\\\","
            f"\\\"senderUrl\\\": \\\"string\\\"}}\","
            f" \"sha512sum\":\"{self.signature}\"}}' "
            f"--cert-type P12 --cert priv.p12:{self.password} "
            f"-i -s -o response.json"
        )

        with open("CurlCommand_send_msg_without_attachment.sh", "w") as file:
            file.write(curl_command)

        # Ausgabe des angepassten curl-Befehls
        print("4.1 ) Generated - CurlCommand_send_msg_without_attachment.sh")
        print(curl_command)

    def send_curl_command_send_msg_without_attachment(self):

        pfad_zum_sh_file = "CurlCommand_send_msg_without_attachment.sh"

        print("4.2 ) Send the request via Git-Bash-Sh command")

        # Ausführen des Befehls mit Git-Bash
        result = subprocess.run([self.git_bash_path, pfad_zum_sh_file], capture_output=True, text=True)

        print("#######################################################################################################")
        print("                                         RESPONSE                                                      ")
        print("")
        print(f"{result.stdout}")
        print(f"{result.stderr}")

        status_code = None
        json_response = None

        try:
            with open("response.json", "r") as file:
                lines = file.readlines()

            if not lines:
                print("❌ Error: Empty response file!")
                return

            # Extract HTTP status code from the first line
            first_line = lines[0].strip()
            print("First line of response:", first_line)

            match = re.search(r"HTTP/1\.\d (\d+)", first_line)
            if match:
                status_code = int(match.group(1))
                print(f"Extracted HTTP Status: {status_code}")

                # Find where JSON starts (after an empty line)
                json_start_index = None
                for i, line in enumerate(lines):
                    if line.strip() == "":  # JSON starts after the first empty line
                        json_start_index = i + 1
                        break

                if json_start_index is not None and json_start_index < len(lines):
                    json_response = "".join(lines[json_start_index:]).strip()

                    try:
                        parsed_json = json.loads(json_response)  # Now it should work correctly
                        print("📜 Parsed JSON Response:", json.dumps(parsed_json, indent=4))
                    except json.JSONDecodeError as e:
                        print(f"❌ JSON Parsing Error: {e}")
                        print("Raw JSON Data:", json_response)

                else:
                    print("❌ Error: No JSON body found in response!")

            else:
                print("❌ Error: Could not find HTTP status in response file!")

        except FileNotFoundError:
            print("❌ Error: Response JSON file not found!")

        if result.returncode != 0:
            print("Shell execution error:")
            print(result.stderr)

        return status_code

    def send_curl_command_send_msg_with_attachment(self):

        pfad_zum_sh_file = "CurlCommand_send_msg_with_attachment.sh"

        print("4.2 ) Send the request via Git-Bash-Sh command")

        # Ausführen des Befehls mit Git-Bash
        result = subprocess.run([self.git_bash_path, pfad_zum_sh_file], capture_output=True, text=True)

        print("#######################################################################################################")
        print("                                         RESPONSE                                                      ")
        print("")
        print(f"{result.stdout}")

        status_code = None
        json_response = None

        try:
            with open("response.json", "r") as file:
                lines = file.readlines()

            if not lines:
                print("❌ Error: Empty response file!")
                return

            # Extract HTTP status code from the first line
            first_line = lines[0].strip()
            print("First line of response:", first_line)

            match = re.search(r"HTTP/1\.\d (\d+)", first_line)
            if match:
                status_code = int(match.group(1))
                print(f"Extracted HTTP Status: {status_code}")

                # Find where JSON starts (after an empty line)
                json_start_index = None
                for i, line in enumerate(lines):
                    if line.strip() == "":  # JSON starts after the first empty line
                        json_start_index = i + 1
                        break

                if json_start_index is not None and json_start_index < len(lines):
                    json_response = "".join(lines[json_start_index:]).strip()

                    try:
                        parsed_json = json.loads(json_response)  # Now it should work correctly
                        print("📜 Parsed JSON Response:", json.dumps(parsed_json, indent=4))
                    except json.JSONDecodeError as e:
                        print(f"❌ JSON Parsing Error: {e}")
                        print("Raw JSON Data:", json_response)

                else:
                    print("❌ Error: No JSON body found in response!")

            else:
                print("❌ Error: Could not find HTTP status in response file!")

        except FileNotFoundError:
            print("❌ Error: Response JSON file not found!")

        if result.returncode != 0:
            print("Shell execution error:")
            print(result.stderr)

        return status_code

    def create_curl_command_send_msg_with_attachments(self, anhang,anhang_pfad, shasum_attachement,contentLength,mimetype="application/pdf"):

        curl_command = (
            f"curl -v -k -4 -X 'PUT' '{self.url}/v6/mailbox/messages' "
            f"-H 'accept: application/json' "
            f"-H 'Authorization: Bearer {self.token}' "
            f"-H 'Content-Type: multipart/form-data' "
            f"-F 'json={{\"content\":\"{{\\\"mailboxUuid\\\":\\\"{self.handle}\\\","
            f"\\\"stork_qaa_level\\\":{self.strok_qa_level},"
            f"\\\"sender\\\":\\\"Sogeti_Test_Verfahren_02\\\","
            f"\\\"title\\\":\\\"{self.date}: {self.title}\\\","
            f"\\\"content\\\":\\\"{self.text_content}\\\","
            f"\\\"service\\\":\\\"Sogeti_Test_Verfahren_02\\\","
            f"\\\"senderUrl\\\":\\\"string\\\","
            f"\\\"reference\\\":\\\"string\\\","
            f"\\\"retrievalConfirmationAddress\\\":\\\"{self.retrievalConfirmationAddress}\\\","
            f"\\\"replyAddress\\\":\\\"string\\\","
            f"\\\"applicationId\\\":null,"
            f"\\\"attachments\\\":[{{\\\"filename\\\":\\\"{anhang}\\\","
            f"\\\"sha512sum\\\":\\\"{shasum_attachement}\\\","
            f"\\\"contentLength\\\":{contentLength}}}]}}\","
            f"\"sha512sum\":\"{self.signature}\"}}' "
            f"-F 'files=@{anhang_pfad}{anhang};type={mimetype}' "
            f"--cert-type P12 --cert priv.p12:{self.password} "
            f"-i -s -o response.json"
        )

        with open("CurlCommand_send_msg_with_attachment.sh", "w") as file:
            file.write(curl_command)

        # Ausgabe des angepassten curl-Befehls
        print("4.1 ) Generated - CurlCommand_send_msg_with_attachment.sh")
        print(curl_command)

    def create_curl_command_send_msg_2_attachments(self, anhang_pfad,
                                                   anhang_1,
                                                   anhang_2,
                                                   shasum_anhang_1,
                                                   shasum_anhang_2,
                                                   contentLength_anhang_1,
                                                   contentLength_anhang_2,
                                                   mimetype_anhang_1,
                                                   mimetype_anhang_2):

        curl_command = (
            f"curl -k -X 'PUT' '{self.url}/v6/mailbox/messages' "
            f"-H 'accept: application/json' "
            f"-H 'Authorization: Bearer {self.token}' "
            f"-H 'Content-Type: multipart/form-data' "
            f"-F 'json={{\"content\":\"{{\\\"mailboxUuid\\\":\\\"{self.handle}\\\","
            f"\\\"stork_qaa_level\\\":{self.strok_qa_level},"
            f"\\\"sender\\\":\\\"Testing_verfahren_01\\\","
            f"\\\"title\\\":\\\"{self.date}: {self.title}\\\","
            f"\\\"content\\\":\\\"{self.text_content}\\\","
            f"\\\"service\\\":\\\"Testing_verfahren_01\\\","
            f"\\\"senderUrl\\\":\\\"string\\\","
            f"\\\"reference\\\":\\\"string\\\","
            f"\\\"retrievalConfirmationAddress\\\":\\\"{self.retrievalConfirmationAddress}\\\","
            f"\\\"replyAddress\\\":\\\"string\\\","
            f"\\\"applicationId\\\":null,"
            f"\\\"attachments\\\":[{{\\\"filename\\\":\\\"{anhang_1}\\\","
            f"\\\"sha512sum\\\":\\\"{shasum_anhang_1}\\\","
            f"\\\"contentLength\\\":{contentLength_anhang_1}}},"
            f"{{\\\"filename\\\":\\\"{anhang_2}\\\","
            f"\\\"sha512sum\\\":\\\"{shasum_anhang_2}\\\","
            f"\\\"contentLength\\\":{contentLength_anhang_2}}}]}}\","
            f"\"sha512sum\":\"{self.signature}\"}}' "
            f"-F 'files=@{anhang_pfad}{anhang_1};type={mimetype_anhang_1}' "
            f"-F 'files=@{anhang_pfad}{anhang_2};type={mimetype_anhang_2}' "
            f"--cert-type P12 --cert priv.p12:{self.password} "
            f"-i -s -o response.json"
        )

        print(curl_command)

        with open("examples/CurlCommand_send_msg_with_attachment.sh", "w") as file:
            file.write(curl_command)

        # Ausgabe des angepassten curl-Befehls
        print("4.1 ) Generated - CurlCommand_send_msg_with_attachment.sh")

    def create_curl_command_send_msg_3_attachments(self, anhang_pfad,
                                                   anhang_1,
                                                   anhang_2,
                                                   anhang_3,
                                                   shasum_anhang_1,
                                                   shasum_anhang_2,
                                                   shasum_anhang_3,
                                                   contentLength_anhang_1,
                                                   contentLength_anhang_2,
                                                   contentLength_anhang_3,
                                                   mimetype_anhang_1,
                                                   mimetype_anhang_2,
                                                   mimetype_anhang_3):

        curl_command = (
            f"curl -k -X 'PUT' '{self.url}/v6/mailbox/messages' "
            f"-H 'accept: application/json' "
            f"-H 'Authorization: Bearer {self.token}' "
            f"-H 'Content-Type: multipart/form-data' "
            f"-F 'json={{\"content\":\"{{\\\"mailboxUuid\\\":\\\"{self.handle}\\\","
            f"\\\"stork_qaa_level\\\":{self.strok_qa_level},"
            f"\\\"sender\\\":\\\"Testing_verfahren_01\\\","
            f"\\\"title\\\":\\\"{self.date}: {self.title}\\\","
            f"\\\"content\\\":\\\"{self.text_content}\\\","
            f"\\\"service\\\":\\\"Testing_verfahren_01\\\","
            f"\\\"senderUrl\\\":\\\"string\\\","
            f"\\\"reference\\\":\\\"string\\\","
            f"\\\"retrievalConfirmationAddress\\\":\\\"{self.retrievalConfirmationAddress}\\\","
            f"\\\"replyAddress\\\":\\\"string\\\","
            f"\\\"applicationId\\\":null,"
            f"\\\"attachments\\\":[{{\\\"filename\\\":\\\"{anhang_1}\\\","
            f"\\\"sha512sum\\\":\\\"{shasum_anhang_1}\\\","
            f"\\\"contentLength\\\":{contentLength_anhang_1}}},"
            f"{{\\\"filename\\\":\\\"{anhang_2}\\\","
            f"\\\"sha512sum\\\":\\\"{shasum_anhang_2}\\\","
            f"\\\"contentLength\\\":{contentLength_anhang_2}}},"
            f"{{\\\"filename\\\":\\\"{anhang_3}\\\","
            f"\\\"sha512sum\\\":\\\"{shasum_anhang_3}\\\","
            f"\\\"contentLength\\\":{contentLength_anhang_3}"
            f"}}]}}\","
            f"\"sha512sum\":\"{self.signature}\"}}' "
            f"-F 'files=@{anhang_pfad}{anhang_1};type={mimetype_anhang_1}' "
            f"-F 'files=@{anhang_pfad}{anhang_2};type={mimetype_anhang_2}' "
            f"-F 'files=@{anhang_pfad}{anhang_3};type={mimetype_anhang_3}' "
            f"--cert-type P12 --cert priv.p12:{self.password} "
            f"-i -s -o response.json"
        )

        print(curl_command)

        with open("examples/CurlCommand_send_msg_with_attachment.sh", "w") as file:
            file.write(curl_command)

        # Ausgabe des angepassten curl-Befehls
        print("4.1 ) Generated Curl request send msg")




    def send_curl_command_send_msg_x_attachment(self):

        pfad_zum_sh_file = "examples/CurlCommand_send_msg_with_attachment.sh"

        print("4.2 ) Send the request via Git-Bash-Sh command")

        # Ausführen des Befehls mit Git-Bash
        result = subprocess.run([self.git_bash_path, pfad_zum_sh_file], capture_output=True, text=True)

        print("#######################################################################################################")
        print("                                         RESPONSE                                                      ")
        print("")
        print(f"{result.stdout}")


    def create_curl_command_set_statusmeldung(self, status, application_id, created_date, reference="string"):

        # Definiere den curl-Befehl als formatierbare Zeichenkette

        curl_command = (
            f"curl -k -X 'POST' 'https://int.zbp.bund.de/v6/mailbox/applications/states' "
            f"-H 'accept: application/json' "
            f"-H 'Content-Type: application/json' "
            f"-H 'Authorization: Bearer {self.token}' "
            f"-d '{{\"content\":\"{{\\\"status\\\":\\\"{status}\\\","
            f"\\\"applicationId\\\":\\\"{application_id}\\\","
            f"\\\"additionalInformation\\\":{{\\\"de\\\":\\\"string\\\"}},"
            f"\\\"statusDetails\\\":{{\\\"de\\\":\\\"String\\\"}},"
            f"\\\"reference\\\":\\\"string\\\","
            f"\\\"publicServiceName\\\":{{\\\"de\\\":\\\"Sogeti_Test_Verfahren_02\\\"}},"
            f"\\\"senderName\\\":\\\"Sogeti_Test_Verfahren_02\\\","
            f"\\\"createdDate\\\":\\\"{created_date}\\\"}}\","
            f"\"sha512sum\":\"{self.signature}\"}}'"
            f" --cert-type P12 --cert priv.p12:{self.password} "
            f"-i -s -o response.json"
        )

        with open("CurlCommand_statusmeldung.sh", "w") as file:
            file.write(curl_command)

        # Ausgabe des angepassten curl-Befehls
        print("4.1 ) Generated Curl Request Statusmeldung")
        print(curl_command)
        print("")

    def send_curl_command_set_statusmeldung(self):

        pfad_zum_sh_file = "CurlCommand_statusmeldung.sh"

        print("4.2 ) Send the request via Git-Bash-Sh command")

        # Ausführen des Befehls mit Git-Bash
        result = subprocess.run([self.git_bash_path, pfad_zum_sh_file], capture_output=True, text=True)

        print("#######################################################################################################")
        print("                                         RESPONSE                                                      ")
        print("")
        print(f"{result.stdout}")
        print(f"{result.stderr}")




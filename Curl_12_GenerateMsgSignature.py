import hashlib
import os
import subprocess
import sys

# from BundID_ZBP_SeleniumFramework.TestDaten.BundID_TestDaten import BundID_TestDaten


class Curl_12_GenerateMsgSignature:

    def __init__(self, date,title, handle, strok_qa_level, text_content,retrievalConfirmationAddress="string"):

        # Definiere die Variablen
        self.anhang_list = None
        self.mimetype_list = None
        self.contentLength_list = None
        self.shasum_list = None
        self.text_content = text_content
        self.handle = handle
        self.password = "abc123"

        self.git_bash_path = "C:\\Program Files\\Git\\git-bash.exe"
        self.date = date
        self.title = title
        self.strok_qa_level = strok_qa_level

        if retrievalConfirmationAddress is None:
            self.retrievalConfirmationAddress = "string"

        self.generate_msg_signatur_sh_file = "generate_msg_signatur.sh"

    def create_printf_command_send_msg(self):

        printf_command = (
            f"printf '{{\"mailboxUuid\": \"{self.handle}\","
            f"\"stork_qaa_level\": {self.strok_qa_level},"
            f"\"sender\": \"Sogeti_Test_Verfahren_02\","
            f"\"title\": \"{self.date}: {self.title}\","
            f"\"content\": \"{self.text_content}\","
            f"\"service\": \"Sogeti_Test_Verfahren_02\","
            f"\"retrievalConfirmationAddress\": \"{self.retrievalConfirmationAddress}\","
            f"\"replyAddress\": \"string\","
            f"\"attachments\":[],"
            f"\"reference\": \"string\","
            f"\"senderUrl\": \"string\"}}' | openssl dgst -sha512 -sign sva.pem -out msg-signatur.txt"
        )

        print(printf_command)

        with open(self.generate_msg_signatur_sh_file,"w") as file:
            file.write(printf_command)

    def send_printf_command_send_msg(self):

        pfad_zum_sh_file = self.generate_msg_signatur_sh_file

        # Ausführen des Befehls mit Git-Bash
        result = subprocess.run([self.git_bash_path, pfad_zum_sh_file], capture_output=True, text=True)

        print("2 ) Generated - msg-signatur.txt - via Git-Bash-Sh command", result.stdout)

    def create_printf_command_send_msg_with_1_attachment_return_shasum_and_content_lenght_from_attachement(self, anhang_pfad, anhang):

        sha512_hash = hashlib.sha512()
        anhang_with_path = anhang_pfad+anhang

        with open(anhang_with_path, "rb") as f:
            # Lese die Datei in Blöcken, um den Speicherverbrauch zu minimieren
            for byte_block in iter(lambda: f.read(4096), b""):
                sha512_hash.update(byte_block)

        shasum_attachement = sha512_hash.hexdigest()
        contentLength = os.path.getsize(anhang_with_path)

        printf_command = (
            f"printf '{{\"mailboxUuid\":\"{self.handle}\","
            f"\"stork_qaa_level\":{self.strok_qa_level},"
            f"\"sender\":\"Sogeti_Test_Verfahren_02\","
            f"\"title\":\"{self.date}: {self.title}\","
            f"\"content\":\"{self.text_content}\","
            f"\"service\":\"Sogeti_Test_Verfahren_02\","
            f"\"senderUrl\":\"string\","
            f"\"reference\":\"string\","
            f"\"retrievalConfirmationAddress\":\"{self.retrievalConfirmationAddress}\","
            f"\"replyAddress\":\"string\","
            f"\"applicationId\":null,"
            f"\"attachments\":[{{\"filename\":\"{anhang}\",\"sha512sum\":\"{shasum_attachement}\","
            f"\"contentLength\":{contentLength}}}]}}' | openssl dgst -sha512 -sign sva.pem -out msg-signatur.txt"
        )

        print(printf_command)

        with open(self.generate_msg_signatur_sh_file,"w") as file:
            file.write(printf_command)

        return shasum_attachement, contentLength

    def create_printf_command_send_msg_with_2_attachment_return_shasum_and_content_lenght_from_attachement(self, anhang_1,anhang_2, anhang_pfad=""):

        anhang_list = [anhang_1,anhang_2]

# Erster Anhang
        ################################################################################################################

        sha512_hash = hashlib.sha512()
        anhang_1_with_path = anhang_pfad+anhang_list[0]

        with open(anhang_1_with_path, "rb") as f:
            # Lese die Datei in Blöcken, um den Speicherverbrauch zu minimieren
            for byte_block1 in iter(lambda: f.read(4096), b""):
                sha512_hash.update(byte_block1)

        shasum_anhang_1 = sha512_hash.hexdigest()
        contentLength_anhang_1 = os.path.getsize(anhang_1_with_path)

# Zweiter Anhang
        # ##############################################################################################################

        sha512_hash = hashlib.sha512()
        anhang_2_with_path = anhang_pfad+anhang_list[1]

        with open(anhang_2_with_path, "rb") as f:
            # Lese die Datei in Blöcken, um den Speicherverbrauch zu minimieren
            for byte_block1 in iter(lambda: f.read(4096), b""):
                sha512_hash.update(byte_block1)

        shasum_anhang_2 = sha512_hash.hexdigest()
        contentLength_anhang_2 = os.path.getsize(anhang_2_with_path)

        shasum_list = [shasum_anhang_1,shasum_anhang_2]
        contentLength_list = [contentLength_anhang_1,contentLength_anhang_2]

########################################################################################################################

        printf_command = (
            f"printf '{{\"mailboxUuid\":\"{self.handle}\","
            f"\"stork_qaa_level\":{self.strok_qa_level},"
            f"\"sender\":\"Testing_verfahren_01\","
            f"\"title\":\"{self.date}: {self.title}\","
            f"\"content\":\"{self.text_content}\","
            f"\"service\":\"Testing_verfahren_01\","
            f"\"senderUrl\":\"string\","
            f"\"reference\":\"string\","
            f"\"retrievalConfirmationAddress\":\"{self.retrievalConfirmationAddress}\","
            f"\"replyAddress\":\"string\","
            f"\"applicationId\":null,"
            f"\"attachments\":["
            f"{{\"filename\":\"{anhang_list[0]}\","
            f"\"sha512sum\":\"{shasum_list[0]}\","
            f"\"contentLength\":{contentLength_list[0]}}},"
            f"{{\"filename\":\"{anhang_list[1]}\","
            f"\"sha512sum\":\"{shasum_list[1]}\","
            f"\"contentLength\":{contentLength_list[1]}}}"
            f"]}}'"
            f" | openssl dgst -sha512 -sign privcer.pem -out msg-signatur.txt"
        )

        print(printf_command)

        with open(self.generate_msg_signatur_sh_file,"w") as file:
            file.write(printf_command)

        return shasum_list[0], contentLength_list[0], shasum_list[1] , contentLength_list[1]

    def create_printf_command_send_msg_with_3_attachment_return_shasum_and_content_lenght_from_attachement(self, anhang_1,anhang_2, anhang_3, anhang_pfad=""):

# Erster Anhang
        ################################################################################################################

        sha512_hash = hashlib.sha512()
        anhang_1_with_path = anhang_pfad+anhang_1

        with open(anhang_1_with_path, "rb") as f:
            # Lese die Datei in Blöcken, um den Speicherverbrauch zu minimieren
            for byte_block1 in iter(lambda: f.read(4096), b""):
                sha512_hash.update(byte_block1)

        shasum_anhang_1 = sha512_hash.hexdigest()
        contentLength_anhang_1 = os.path.getsize(anhang_1_with_path)

# Zweiter Anhang
        # ##############################################################################################################

        sha512_hash = hashlib.sha512()
        anhang_2_with_path = anhang_pfad+anhang_2

        with open(anhang_2_with_path, "rb") as f:
            # Lese die Datei in Blöcken, um den Speicherverbrauch zu minimieren
            for byte_block1 in iter(lambda: f.read(4096), b""):
                sha512_hash.update(byte_block1)

        shasum_anhang_2 = sha512_hash.hexdigest()
        contentLength_anhang_2 = os.path.getsize(anhang_2_with_path)


# Dritter Anhang
    ####################################################################################################################

        sha512_hash = hashlib.sha512()
        anhang_3_with_path = anhang_pfad+anhang_3

        with open(anhang_3_with_path, "rb") as f:
            # Lese die Datei in Blöcken, um den Speicherverbrauch zu minimieren
            for byte_block1 in iter(lambda: f.read(4096), b""):
                sha512_hash.update(byte_block1)

        shasum_anhang_3 = sha512_hash.hexdigest()
        contentLength_anhang_3 = os.path.getsize(anhang_3_with_path)

        printf_command = (
            f"printf '{{\"mailboxUuid\":\"{self.handle}\","
            f"\"stork_qaa_level\":{self.strok_qa_level},"
            f"\"sender\":\"Testing_verfahren_01\","
            f"\"title\":\"{self.date}: {self.title}\","
            f"\"content\":\"{self.text_content}\","
            f"\"service\":\"Testing_verfahren_01\","
            f"\"senderUrl\":\"string\","
            f"\"reference\":\"string\","
            f"\"retrievalConfirmationAddress\":\"{self.retrievalConfirmationAddress}\","
            f"\"replyAddress\":\"string\","
            f"\"applicationId\":null,"
            f"\"attachments\":["
            f"{{\"filename\":\"{anhang_1}\","
            f"\"sha512sum\":\"{shasum_anhang_1}\","
            f"\"contentLength\":{contentLength_anhang_1}}},"
            f"{{\"filename\":\"{anhang_2}\","
            f"\"sha512sum\":\"{shasum_anhang_2}\","
            f"\"contentLength\":{contentLength_anhang_2}}},"
            f"{{\"filename\":\"{anhang_3}\","
            f"\"sha512sum\":\"{shasum_anhang_3}\","
            f"\"contentLength\":{contentLength_anhang_3}}}"
            f"]}}'"
            f" | openssl dgst -sha512 -sign privcer.pem -out msg-signatur.txt"
        )

        print(printf_command)

        with open(self.generate_msg_signatur_sh_file,"w") as file:
            file.write(printf_command)

        return shasum_anhang_1, contentLength_anhang_1, shasum_anhang_2, contentLength_anhang_2, shasum_anhang_3, contentLength_anhang_3

    def send_printf_command_send_msg_with_attachment(self):

        pfad_zum_sh_file = self.generate_msg_signatur_sh_file

        # Ausführen des Befehls mit Git-Bash
        result = subprocess.run([self.git_bash_path, pfad_zum_sh_file], capture_output=True, text=True)

        print("2 ) Generated - msg_signatur.sh - via Git-Bash-Sh command", result.stdout)

    def create_printf_set_statusmeldung(self, status, application_id, created_date):

        printf_command = (
            f"printf '{{\"status\":\"{status}\","
            f"\"applicationId\":\"{application_id}\","
            f"\"additionalInformation\":{{\"de\":\"string\"}},"
            f"\"statusDetails\":{{\"de\":\"String\"}},"
            f"\"reference\":\"string\","
            f"\"publicServiceName\":{{\"de\":\"Sogeti_Test_Verfahren_02\"}},"
            f"\"senderName\":\"Sogeti_Test_Verfahren_02\","
            f"\"createdDate\":\"{created_date}\"}}' | openssl dgst -sha512 -sign sva.pem -out msg-signatur.txt"
        )

        # Ausgabe des generierten Befehls
        print(printf_command)

        with open(self.generate_msg_signatur_sh_file,"w") as file:
            file.write(printf_command)

    def send_printf_set_statusmeldung(self):

        pfad_zum_sh_file = self.generate_msg_signatur_sh_file

        # Ausführen des Befehls mit Git-Bash
        result = subprocess.run([self.git_bash_path, pfad_zum_sh_file], capture_output=True, text=True)

        print("2 ) Generated - msg-signatur.txt - via Git-Bash-Sh command", result.stdout)




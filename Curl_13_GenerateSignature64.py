
import subprocess
import time


class Curl_13_GenerateSignature64:

    def __init__(self):

        # Pfad zu Git-Bash (standardmäßig, passe ggf. an, falls du es woanders installiert hast)
        self.git_bash_path = "C:\\Program Files\\Git\\git-bash.exe"

    def create_signature(self):

        paf_zum_sh_file = "generate_signatureb64.sh"

        # Ausführen des Befehls mit Git-Bash
        subprocess.run([self.git_bash_path, paf_zum_sh_file], capture_output=True, text=True)

        # Ausgabe des Befehls
        print("3 ) Generated - signature.b64 - via Git-Bash-Sh command")

        time.sleep(5)


if __name__ == '__main__':

    generate_token_and_signed_msg = Curl_13_GenerateSignature64()
    generate_token_and_signed_msg.create_signature()









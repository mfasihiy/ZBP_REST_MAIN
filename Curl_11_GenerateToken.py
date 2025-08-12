
import subprocess
import time


class Curl_11_GenerateToken:

    def __init__(self):

        # Pfad zu Git-Bash (standardmäßig, passe ggf. an, falls du es woanders installiert hast)
        self.git_bash_path = "C:\\Program Files\\Git\\bin\\bash.exe"

# Erstellung des Tokens ################################################################################################

    def create_token(self):
        pfad_zum_jwt_file = "tokens/Generate_jwt.sh"

        # Ausführen des Befehls mit Git-Bash
        result = subprocess.run([self.git_bash_path, pfad_zum_jwt_file], capture_output=True, text=True)

        # speichern des tokens in einem file ###########################################################################
        print("Token ist: ", result.stdout)

        with open("tokens/token.txt", 'w') as file:
            file.write(result.stdout)

        time.sleep(3)


if __name__ == '__main__':

    generate_token_and_signed_msg = Curl_11_GenerateToken()
    generate_token_and_signed_msg.create_token()









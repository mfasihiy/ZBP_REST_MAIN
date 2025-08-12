
privateKey="sva.pem"
issuedAt=$(date +%s)
expiresAt=$(date --date='+1 hour' +%s)
signer="Sogeti_Test_Verfahren_02"
roles="THIRD_PARTY"
# rem roles="THIRD_PARTY" roles="MANAGEMENT_TOKEN"

header=$(echo -n '{"typ":"JWT","alg":"RS512"}' | openssl base64 -e -A | tr '+/' '-_' | tr -d '=')
payload=$(echo -n "{\"iat\":$issuedAt,\"exp\":$expiresAt,\"signer\":\"$signer\",\"roles\":[\"$roles\"]}" | openssl base64 -e -A | tr '+/' '-_' | tr -d '=')
signature=$(echo -n "$header.$payload" | openssl dgst -sha512 -sign $privateKey | openssl base64 -e -A | tr '+/' '-_' | tr -d '=')

# Print Full JWT
echo "$header.$payload.$signature"


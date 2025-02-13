token1=$(curl -s -k -H -v --request POST --data '{ "role_id": "REDACTED", "secret_id": "REDACTED" }' ${VAULT_ADDR}/v1/auth/approle/login | jq -r .auth.client_token)
echo $token1

# approle above must have 
token2=$(curl -s -X POST -H "X-Vault-Request: true" -H "X-Vault-Token: $token1" -d '{"policies":["kv-all"], "ttl":"1h"}' $VAULT_ADDR/v1/auth/token/create-orphan | jq -r .auth.client_token)
echo $token2

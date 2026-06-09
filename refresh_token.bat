ENCODED=$(echo -n "$CLIENT_ID:$CLIENT_SECRET" | base64);

url -X POST "https://accounts.spotify.com/api/token" \
    -H "Authorization: Basic $ENCODED" \
    -H "Content-Type: "application/x-www-form-urlencoded"" \
    -d "grant_type=refresh_token" \
    -d "refresh_token=$REFRESH_TOKEN"

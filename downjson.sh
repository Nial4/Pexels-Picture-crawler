for(( i=1;i<=1000;i++))
do
echo $i
curl -H "Authorization: Your Token" \
  "https://api.pexels.com/v1/search/?page="$i"&per_page=80&query=summer" -o summer$i.json
done

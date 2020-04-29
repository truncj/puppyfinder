# puppyfinder

## Purpose

Get emailed when a new pet meets your [Petfinder](https://www.petfinder.com) search criteria

## Config 

### config.json 

```json
{
  "sender_user": "xxxxxx@gmail.com",
  "sender_pass": "xxxxxx",
  "recipients": [
    "aaaaaaa@gmail.com",
    "bbbbbbb@gmail.com"
  ],
  "timeout": 60,
  "params": {
      "breed": "Labrador Retriever",
      "age": "Baby",
      "location": "10001",
      "animal_type": "Dog",
      "status": "Adoptable",
      "sort": "recent",
      "limit": 100
  }
}
```

### creds.json

```json
{
  "client_id": "{petfinder_client_id}",
  "client_secret": "{petfinder_client_secret}",
  "rebrandly_token": "{rebrandly_token}",
  "rebrandly_workspace": "{rebrandly_workspace}"
}
```

## Docker

`docker run -d -v /{path_to_config}/:/config --name puppyfinder notronswanson/puppyfinder:latest`

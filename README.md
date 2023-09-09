# Start DEV
`docker-compose --env-file .env.dev -f docker-compose.dev.yml up -d --build`
# Start PROD
`docker-compose --env-file .env.prod -f docker-compose.dev.yml up -d --build`
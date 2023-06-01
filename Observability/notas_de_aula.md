
### Para rodar no wsl
Entra na pasta que esta o prometheus.yml no terminal wsl
` docker run -p 9090:9090 -v "$(pwd)/prometheus.yml":/etc/prometheus/prometheus.yml -d prom/prometheus `


` docker run -d -p 9100:9100 quay.io/prometheus/node-exporter:v1.2.2 `


` docker compose up -d `
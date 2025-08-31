# Python Microservices DevOps Assignment

## Steps to Run Locally

```bash
docker compose up --build
```
- Frontend: http://localhost:8080
- Backend: http://localhost:5000/api/data
- Logger: http://localhost:9000/log
- PostgreSQL: running internally

## CI/CD Pipeline
- GitHub Actions workflow (`.github/workflows/ci.yml`)
- Builds & pushes Docker images to DockerHub (dd0870)
- Sends email alert on failure

## Terraform (AWS Deployment)
```bash
cd terraform
terraform init
terraform plan
terraform apply
```
- Deploys EC2 instance with Docker + Compose
- Access frontend via EC2 Public IP on port 8080

## Screenshots (Add here)
1. Docker Compose containers running (local)
2. Successful GitHub Actions build
3. DockerHub images pushed
4. AWS frontend working in browser

## Reflection Answers
**Hardest part:** Debugging multi-service orchestration and healthchecks across Docker + AWS.  
**How CI/CD + IaC helps:** Automates build, deploy, infra provisioning; reduces manual effort, ensures repeatability.

# MotoGlimplse & Wildography — DevOps Cloud Deployment Project

A full DevOps project where I built and deployed a web application with two image upload sections:

- **MotoGlimplse** → Upload motorcycle photography
- **Wildography** → Upload wildlife photography

This repo documents the complete DevOps journey: from local development → Docker → CI/CD → Kubernetes → Cloud.

---

## 🔥 Project Highlights

- Webapp built and containerized with Docker
- Docker image pushed to DockerHub
- CI/CD pipeline to build + push image automatically
- Kubernetes deployment with manifests (Deployment, Service, Ingress)
- Cloud deployment (EKS / AKS / GKE)
- Optional monitoring/logging (Prometheus/Grafana + centralized logs)

---

## 🧱 Architecture (High Level)

![Architecture Diagram](docs/images/architecture.png)

**Flow:**
User → Load Balancer / Ingress → Kubernetes Service → Pods (Webapp) → Storage

---

## 🚀 Quick Start (Local)

### Option 1: Run using Docker (recommended)

```bash
docker pull <YOUR_DOCKERHUB_USERNAME>/motoglimplse-wildography:latest
docker run -p 5000:5000 <YOUR_DOCKERHUB_USERNAME>/motoglimplse-wildography:latest

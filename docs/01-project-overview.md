# Project Overview

## What is MotoGlimplse & Wildography?

This is a simple webapp with a clean UI and two upload sections:

- **MotoGlimplse**: Upload and display motorcycle images
- **Wildography**: Upload and display wildlife images

The main goal is not just the app — but the full DevOps lifecycle:
containerization, automation, orchestration, and cloud deployment.

---

## Goals of this project

- Build a deployable webapp
- Package it into a Docker image
- Push image to DockerHub
- Automate builds with CI
- Deploy into Kubernetes using manifests
- Deploy Kubernetes into cloud
- Add production-level features (Ingress, TLS, monitoring)

---

## Repository Structure

- `/app` → webapp source code
- `/k8s` → Kubernetes YAML manifests
- `/.github/workflows` → CI/CD pipelines
- `/docs` → documentation + screenshots

---

## Current Status

✅ Webapp created  
✅ Docker image built  
✅ Container runs locally  
✅ Image pushed to DockerHub  

Next:
- CI pipeline build + push
- Kubernetes manifests
- Cloud deployment

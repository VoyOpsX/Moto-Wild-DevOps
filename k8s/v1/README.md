Web App v1 — GKE Overview
Overview
This project hosts version 1 of the web app on Google Kubernetes Engine (GKE), pulling the container image directly from Docker Hub and exposing it to the internet via a GCP HTTP(S) Load Balancer through a Kubernetes Ingress resource.

Architecture
Internet
   │
   ▼
GCP HTTP(S) Load Balancer
   │  (provisioned by GKE Ingress Controller)
   ▼
Kubernetes Ingress
   │
   ▼
NodePort Service
   │
   ▼
GKE Pods  ←  Docker Hub Image (webapp:v1)

Components
Docker Hub — The pre-built webapp:v1 image is stored on Docker Hub and referenced directly in the Kubernetes Deployment. No local build or private registry needed.
GKE Cluster — A managed Kubernetes cluster on GCP that pulls the image and runs it as a set of replicated pods.
Deployment — Defines how the app runs: which image to use, how many pod replicas, and resource limits.
Service (NodePort) — Exposes the pods within the cluster so the Ingress can route traffic to them.
Ingress + GCE Load Balancer — A Kubernetes Ingress with the gce annotation triggers GCP to automatically provision an HTTP(S) Load Balancer, giving the app a stable public IP.

Key Notes

The image is pulled from Docker Hub as dockerhub-username/webapp:v1 with no additional registry setup.
GKE handles cluster infrastructure, scaling, and health checks automatically.
The GCP Load Balancer provisions automatically when the Ingress resource is applied — no manual LB setup required.
The app is accessible via the public IP assigned to the Ingress within a few minutes of deployment.

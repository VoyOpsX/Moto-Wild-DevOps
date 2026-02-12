
---

# ✅ docs/03-ci-cd.md

```md
# CI/CD Pipeline

## Goal

Automate the following steps on every push to `main`:

- Run lint/tests (optional)
- Build Docker image
- Push image to DockerHub

Then (CD):
- Deploy updated image to Kubernetes cluster

---

## CI Pipeline (Build + Push)

### Trigger
- On push to `main`
- On pull request

### Steps
1. Checkout code
2. Install dependencies
3. Run tests (optional)
4. Build Docker image
5. Login to DockerHub
6. Push image

Screenshot:
![CI Run](images/ci-run.png)

---

## CD Pipeline (Deploy to Kubernetes)

### Trigger
- After successful CI build

### Steps
1. Authenticate to cloud
2. Update Kubernetes deployment image
3. Apply manifests
4. Verify rollout

Screenshot:
![CD Run](images/cd-run.png)

---

## Workflow YAML Files

- `.github/workflows/ci.yml`
- `.github/workflows/cd.yml`

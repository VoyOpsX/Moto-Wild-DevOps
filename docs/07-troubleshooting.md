# Troubleshooting

This page contains real issues faced during development and deployment.

Recruiters LOVE this because it shows real-world debugging.

---

## Docker Issues

### Issue: Port not accessible
Fix: `docker run -p 5000:5000 ...`

---

## Kubernetes Issues

### Issue: ImagePullBackOff
Fix:
- check DockerHub image name
- ensure public repo OR use imagePullSecrets

---

## CI/CD Issues

### Issue: DockerHub login failed in GitHub Actions
Fix:
- use GitHub secrets
- correct username/token

---

## Cloud Issues

### Issue: Ingress not creating LoadBalancer
Fix:
- install ingress controller properly
- check cloud IAM permissions

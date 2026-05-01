# 🚀 Ephemeral PR Environments (Local Platform Engineering)

## **The Problem**
In modern development teams, developers often face "staging bottlenecks" where multiple people trying to test different features on a single staging server leads to configuration drift and testing conflicts.

## **The Solution**
This project implements a **just-in-time infrastructure** model. Using a custom CI/CD pipeline, every Pull Request (PR) automatically triggers the creation of a completely isolated Kubernetes namespace. The application is built and deployed into this sandbox, allowing for independent testing. Once the PR is merged or closed, the environment is automatically destroyed.

## **The Architecture**

<img width="2816" height="1536" alt="Gemini_Generated_Image_q43fkxq43fkxq43f" src="https://github.com/user-attachments/assets/b15da249-9073-4b2f-b6fe-411d22016e15" />

<br>

*   **Application:** Python FastAPI microservice.
*   **Orchestration:** Kubernetes (Minikube) for resource isolation via Namespaces.
*   **CI/CD:** GitHub Actions.
*   **Runner:** Self-Hosted Linux Runner (Ubuntu 24.04) to bridge the cloud with local infrastructure.
*   **Automation Logic:** Bash/Sed scripting for dynamic manifest transformation.

---

## **Technical Deep Dive**

### **1. Dynamic Isolation**
Every environment is scoped to a unique namespace titled `pr-<number>`. This ensures that Networking (Services), Compute (Pods), and Configuration (Env Vars) never collide between different features.

### **2. Just-In-Time Image Injection**
To optimize for speed and cost, the pipeline uses `minikube docker-env`. Instead of pushing to an external registry, the runner builds the image directly into the Minikube node's internal cache.

### **3. Manifest Transformation**
We use `sed` as a lightweight configuration manager to inject the GitHub PR metadata into the Kubernetes `deployment.yaml` on the fly:
*   **Image Tagging:** Ensures the deployment pulls the specific version built for that PR.
*   **Environment Variables:** Injects the PR number into the application layer for visibility.

---

## **How to Run Locally**

### **Prerequisites**
*   **OS:** Ubuntu 24.04 LTS
*   **K8s:** Minikube (Driver: Docker)
*   **Automation:** GitHub Self-Hosted Runner configured with label `local-dev`

### **Setup**
1.  **Start the Cluster:**
    ```bash
    minikube start --driver=docker
    ```
2.  **Start the Runner:**
    ```bash
    cd ~/actions-runner && ./run.sh
    ```
3.  **Trigger the Flow:**
    Create a new branch, push a change, and open a Pull Request on GitHub.

### **Accessing the Environment**
Once the GitHub Action turns green, run:
```bash
minikube service ephemeral-service --url -n pr-<PR_NUMBER>
```

---

## **Key Learning Outcomes**
*   Mastered **Kubernetes Namespacing** for resource isolation.
*   Implemented **Self-Hosted Runners** to securely connect GitHub Actions to private infrastructure.
*   Automated the **Infrastructure Lifecycle** (Provisioning -> Deployment -> Teardown).
*   Optimized DevOps workflows for **Cost Efficiency** using local virtualization.

---

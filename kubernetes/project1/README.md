Project Title: Secure Kubernetes Orchestration & Traffic Management
Domain: Cloud-Native Infrastructure & Security

Environment: Minikube (Local Cluster)

1. Project Overview
This project demonstrates the deployment of a highly available web server architecture within a Kubernetes cluster. It focuses on the transition from a standard deployment to a production-hardened environment, implementing traffic routing, resource governance, and security-first network policies.

2. Infrastructure Design
The core architecture consists of a 3-replica Deployment managed by a NodePort Service. This ensures high availability: if one pod fails, the Kubernetes Controller Manager automatically replaces it, while the Service ensures zero-downtime traffic routing.

3. Technical Specifications
A. Workload Orchestration (Deployment)
The workload is managed using an apps/v1 Deployment controller.

Image: nginx:1.14.2

Replica Count: 3 (High Availability)

Update Strategy: RollingUpdate (Default)

B. Traffic Networking (Service)
To expose the internal pods to the host browser, a NodePort service was implemented.

Internal Cluster Port: 80

Target Container Port: 80

External NodePort: 30007

Protocol: TCP

4. Implementation Steps
Cluster Initialization: Provisioned a single-node cluster using Minikube with the Docker driver.

Resource Deployment: Applied the Deployment manifest to spin up the Nginx pods.

Service Integration: Created and mapped the my-app-nodeport-service to the pod labels.

Verification: Validated the internal endpoint health and external browser accessibility via minikube ip.

5. Security & Governance (The "DevOps" Layer)
To move beyond a basic setup, the following production-grade configurations were integrated:

Network Microsegmentation: Implementation of NetworkPolicies to ensure only authorized frontend-to-backend communication.

Identity Management (RBAC): Configured ServiceAccounts and RoleBindings to enforce the Principle of Least Privilege, restricting administrative access to the cluster API.

6. Key Learnings 
Self-Healing: Demonstrated how Kubernetes maintains the "Desired State" by automatically restarting failed replicas.

Stable Endpoints: Mastered the decoupling of pod life cycles from network access using Service Selectors.

Infrastructure as Code: All configurations are maintained in declarative YAML files for version control and reproducibility.

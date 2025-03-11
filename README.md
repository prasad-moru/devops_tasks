# DevOps and Programming Tasks

This repository contains solutions to various DevOps and programming challenges, including CI/CD pipelines, Docker configurations, Kubernetes setups, and algorithm implementations.

## Repository Structure

```
.
│   Name - Devops Test.docx
│
├───CI-CD_Pipeline
│       argocd-app-config.yaml       # ArgoCD application configurations
│       Deployment_Pipeline.yaml     # Deployment pipeline definition
│       github-workflow.yaml         # GitHub Actions CI workflow
│
├───Decimal Digit Transformation in Java
│       decimal_digit_transformation.py  # Calculates 3 + 33 + 333 + 3333
│
├───Dockerfile
│       default.conf                 # Nginx configuration
│       Dockerfile                   # Multi-stage Docker build definition
│
├───Fibonacci Sum Calculator in Python
│       fibsum_cal.py               # Calculates sum of even Fibonacci numbers
│
├───Intersection of Sorted Arrays
│       arr_insertion.py            # Finds common elements in sorted arrays
│
├───kubernete_statfulsets
│       nginx_app.conf              # Nginx app configuration for K8s
│       service.yaml                # Kubernetes service definition
│       StatefulSet.yaml            # StatefulSet configuration
│
├───log_processingn_OOPS
│       class-diagram.mermaid       # Class diagram for OOP implementation
│       log_processing_oops.py      # Object-oriented log processor
│       sample.log                  # Sample log data
│
└───log_processing_scripts
        log_processing_script.sh    # Shell script for log processing
        sample.log                  # Sample log data
```

## Solutions Overview

### CI/CD Pipeline

A comprehensive CI/CD pipeline using GitHub Actions and ArgoCD for deploying Nginx applications:

- **GitHub Actions** for build automation, testing, and security scanning
- **ArgoCD** for GitOps-based deployments to Kubernetes
- Integrations with **SonarQube**, **Trivy**, and **HashiCorp Vault**

### Docker Configuration

Multi-stage Dockerfile for Nginx with security hardening:

- Uses minimal base images
- Implements security best practices
- Runs as non-root user
- Includes health checks

### Kubernetes StatefulSets

Kubernetes configurations for stateful applications:

- StatefulSet definition with persistent storage
- Service configurations
- Nginx application config

### Programming Challenges

#### Decimal Digit Transformation

Calculates the sum of 3 + 33 + 333 + 3333 for a given decimal digit X.

Example when X=3:
- First term: 3
- Second term: 33
- Third term: 333
- Fourth term: 3333
- Sum: 3 + 33 + 333 + 3333 = 3702

#### Fibonacci Sum Calculator

Efficiently calculates the sum of the first 100 even-valued Fibonacci numbers using mathematical optimization:

- Directly generates even Fibonacci numbers
- Uses the pattern that every third Fibonacci number is even
- Implements an optimized algorithm with O(n) time complexity

#### Intersection of Sorted Arrays

Finds the common elements between two sorted arrays without duplicates:

- Implements a two-pointer approach for optimal efficiency
- Includes alternative HashSet implementation
- Handles edge cases properly

#### Log Processing

Two implementations of log processing systems:

1. **Shell Script Version**:
   - Uses grep, sed, awk, and sort for efficient text processing
   - Extracts ERROR and WARN log entries
   - Formats output as CSV

2. **Object-Oriented Version**:
   - Python implementation with proper class structure
   - Separates concerns with dedicated classes
   - Includes error handling and type checking

## Usage

Each directory contains standalone solutions that can be used independently:

### Running the CI/CD Pipeline

1. Add the GitHub workflow YAML to your `.github/workflows/` directory
2. Configure the required secrets in your GitHub repository
3. Set up ArgoCD with the provided application configuration

### Building the Docker Image

```bash
docker build -t nginx-app:latest .
```

### Deploying to Kubernetes

```bash
kubectl apply -f kubernete_statfulsets/StatefulSet.yaml
kubectl apply -f kubernete_statfulsets/service.yaml
```

### Running the Python Scripts

```bash
# Decimal Digit Transformation
python Decimal\ Digit\ Transformation\ in\ Java/decimal_digit_transformation.py

# Fibonacci Sum Calculator
python Fibonacci\ Sum\ Calculator\ in\ Python/fibsum_cal.py

# Array Intersection
python Intersection\ of\ Sorted\ Arrays/arr_insertion.py

# Log Processing (OOP)
python log_processingn_OOPS/log_processing_oops.py
```

### Running the Log Processing Shell Script

```bash
chmod +x log_processing_scripts/log_processing_script.sh
./log_processing_scripts/log_processing_script.sh log_processing_scripts/sample.log
```


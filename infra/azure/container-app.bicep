// --------------------------------------------------------------------------
// container-app.bicep
//
// Infrastructure-as-Code stub for deploying this skeleton to Azure
// Container Apps (our Phase 1 deployment target: Container Services).
//
// This is intentionally NOT wired up to real resources yet — this session
// is scaffold-only. In the deployment session we will fill in:
//   - Container Apps Environment
//   - Container Registry reference (image built from infra/docker/Dockerfile)
//   - Scaling rules (min/max replicas) -- ties into our later autoscaling lab
//   - Environment variables (LLM_PROVIDER etc, from config.py contract)
//
// Naming convention note (enterprise pattern): resource names follow
// <workload>-<env>-<region> so the same template can be parameterized
// across dev/staging/prod without duplication.
// --------------------------------------------------------------------------

param location string = resourceGroup().location
param environmentName string = 'dev'
param containerAppName string = 'langgraph-rag-agent-${environmentName}'

// TODO: add Container Apps Environment resource
// TODO: add Container App resource referencing the built image
// TODO: add scale rule block (min replicas 0 for free-tier cost control,
//       max replicas N) -- this is our future autoscaling exercise

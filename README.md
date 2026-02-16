# Docker Hub Login with GitHub Actions

This repository demonstrates how to log into Docker Hub using GitHub Actions and secrets.

## 🔧 Setup Required

### 1. Create Docker Hub Access Token
1. Go to [Docker Hub](https://hub.docker.com/)
2. Click your profile → **Account Settings**
3. Go to **Security** tab
4. Click **New Access Token**
5. Give it a name (e.g., "github-actions")
6. Copy the generated token

### 2. Add GitHub Secrets
1. Go to your GitHub repository
2. Click **Settings** tab
3. Go to **Secrets and variables** → **Actions**
4. Click **New repository secret**
5. Add these secrets:
   - `DOCKERHUB_USERNAME`: Your Docker Hub username
   - `DOCKERHUB_TOKEN`: The access token you created

## 🚀 How It Works

The workflow:
1. Runs on Ubuntu latest
2. Logs into Docker Hub using your secrets
3. Verifies the login was successful
4. Shows your Docker username

## 📋 Workflow Triggers

- Push to main/master branch
- Pull requests to main/master branch
- Manual dispatch (run manually from Actions tab)

## 🔍 What to Expect

When the workflow runs, you'll see:
- Docker login process
- Docker system information
- Confirmation of successful login with your username

## 📝 Next Steps

Once login is working, you can extend this to:
- Build Docker images
- Push images to Docker Hub
- Deploy containers
- Run multi-stage builds

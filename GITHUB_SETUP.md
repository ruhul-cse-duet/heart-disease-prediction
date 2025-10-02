# 🐙 GitHub Setup Guide

Complete guide for setting up your Heart Disease Prediction project on GitHub with automated CI/CD.

## 🚀 Quick Setup

### 1. Create GitHub Repository

1. **Create New Repository**
   - Go to GitHub.com
   - Click "New Repository"
   - Name: `heart-disease-prediction`
   - Description: "Heart Disease Prediction System using Streamlit and Machine Learning"
   - Make it Public
   - Initialize with README: ❌ (we already have one)

2. **Initial Push**
   ```bash
   # Navigate to your project directory
   cd "E:\Data Science\ML_and_DL_project\Heart Disease Prediction Streamlit"
   
   # Initialize git repository
   git init
   
   # Add all files
   git add .
   
   # Initial commit
   git commit -m "Initial commit: Heart Disease Prediction System"
   
   # Add remote origin (replace USERNAME with your GitHub username)
   git remote add origin https://github.com/USERNAME/heart-disease-prediction.git
   
   # Push to GitHub
   git push -u origin main
   ```

## 🔧 Configure GitHub Settings

### 1. Repository Settings

1. **Branch Protection**
   - Go to Settings → Branches
   - Add rule for `main` branch
   - ✅ Require pull request reviews
   - ✅ Require status checks to pass
   - ✅ Require up-to-date branches

2. **Secrets Configuration**
   - Go to Settings → Secrets and variables → Actions
   - Add the following secrets if needed:
     ```
     DOCKER_USERNAME=your-docker-username
     DOCKER_PASSWORD=your-docker-password
     ```

### 2. GitHub Pages (Optional)

Enable GitHub Pages for documentation:
1. Go to Settings → Pages
2. Source: Deploy from a branch
3. Branch: main
4. Folder: / (root)

## 🤖 GitHub Actions Workflows

The project includes two automated workflows:

### 1. Continuous Integration (`ci.yml`)

**Triggers:**
- Push to `main` or `develop`
- Pull requests to `main`

**Features:**
- ✅ Python 3.12 compatibility testing
- ✅ Code quality checks (flake8, black, isort)
- ✅ Security scanning with Trivy
- ✅ Application startup testing

### 2. Docker Build (`docker-build.yml`)

**Triggers:**
- Push to `main` or `develop`
- Pull requests to `main`
- Release creation

**Features:**
- 🐳 Multi-platform Docker builds (AMD64, ARM64)
- 📦 Automatic image publishing to GitHub Container Registry
- 🏷️ Semantic versioning tags
- ✅ Build attestation for security

## 📦 GitHub Container Registry

Your Docker images will be automatically published to:
```
ghcr.io/USERNAME/heart-disease-prediction:latest
ghcr.io/USERNAME/heart-disease-prediction:main
ghcr.io/USERNAME/heart-disease-prediction:v1.0.0
```

### Pull and Run

```bash
# Pull the latest image
docker pull ghcr.io/USERNAME/heart-disease-prediction:latest

# Run the container
docker run -p 8501:8501 ghcr.io/USERNAME/heart-disease-prediction:latest
```

## 🏷️ Release Management

### Creating Releases

1. **Semantic Versioning**
   - Use format: `v1.0.0`, `v1.1.0`, `v2.0.0`
   - Major: Breaking changes
   - Minor: New features
   - Patch: Bug fixes

2. **Create Release**
   ```bash
   # Tag the release
   git tag -a v1.0.0 -m "Release version 1.0.0"
   git push origin v1.0.0
   ```

3. **GitHub Release Page**
   - Go to Releases → Create a new release
   - Choose tag: v1.0.0
   - Title: Heart Disease Prediction System v1.0.0
   - Add release notes

### Automated Release Notes

The workflows will automatically:
- Build Docker images for releases
- Generate build attestations
- Create security reports

## 🔍 Monitoring and Insights

### 1. GitHub Insights

Monitor your project with:
- **Insights → Pulse**: Activity overview
- **Insights → Contributors**: Contribution statistics
- **Insights → Traffic**: Views and clones
- **Insights → Dependency graph**: Dependencies

### 2. Security

- **Security → Security advisories**: Vulnerability alerts
- **Security → Dependabot**: Automated dependency updates
- **Security → Code scanning**: Security issues

### 3. Actions

- **Actions**: View workflow runs
- **Actions → Runners**: Self-hosted runners (if any)

## 🤝 Collaboration Features

### 1. Issues

Create issue templates:

```markdown
<!-- .github/ISSUE_TEMPLATE/bug_report.md -->
---
name: Bug Report
about: Create a report to help us improve
title: '[BUG] '
labels: bug
assignees: ''
---

**Describe the bug**
A clear description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior.

**Expected behavior**
What you expected to happen.

**Screenshots**
If applicable, add screenshots.

**Environment:**
- OS: [e.g. iOS]
- Browser: [e.g. chrome, safari]
- Version: [e.g. 22]
```

### 2. Pull Request Template

```markdown
<!-- .github/pull_request_template.md -->
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Tests pass locally
- [ ] Added new tests
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
```

### 3. Discussions

Enable GitHub Discussions for:
- Q&A about the project
- Feature requests
- General discussions
- Show and tell

## 📊 Project Management

### 1. GitHub Projects

Create a project board:
1. Go to Projects → New project
2. Choose "Board" template
3. Add columns: Backlog, In Progress, Review, Done
4. Link issues and pull requests

### 2. Milestones

Create milestones for major versions:
- v1.0.0 - Initial release
- v1.1.0 - Enhanced features
- v2.0.0 - Major updates

## 🔐 Security Best Practices

### 1. Dependency Management

- Enable Dependabot alerts
- Review security advisories
- Keep dependencies updated

### 2. Code Scanning

GitHub will automatically:
- Scan for security vulnerabilities
- Check for coding best practices
- Monitor for credential leaks

### 3. Supply Chain Security

- Use signed commits
- Enable branch protection
- Review workflow permissions

## 📱 Mobile and Social

### 1. Repository Topics

Add relevant topics:
```
machine-learning, healthcare, streamlit, docker, python, 
heart-disease, prediction, medical-ai, data-science
```

### 2. Social Preview

Customize your repository's social preview:
- Go to Settings → General
- Upload a custom image (1280x640px)

## 🎯 Next Steps

After setup:

1. **⭐ Star the repository** (if you want others to find it easily)
2. **👀 Watch releases** to get notifications
3. **🍴 Enable discussions** for community interaction
4. **📊 Set up project boards** for task management
5. **🤖 Configure Dependabot** for security updates

## 🆘 Troubleshooting

### Common Issues

1. **Workflow Failures**
   - Check Actions tab for detailed logs
   - Verify secrets are properly set
   - Check file permissions

2. **Docker Registry Issues**
   - Ensure GitHub Container Registry is enabled
   - Check package permissions
   - Verify authentication

3. **Branch Protection**
   - Ensure required checks are properly configured
   - Check that status checks exist

---

**Ready to collaborate! 🚀**


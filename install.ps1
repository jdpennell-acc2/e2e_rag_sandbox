# 1. Configure Persistent User Environment Variables
[System.Environment]::SetEnvironmentVariable("LANGFUSE_SECRET_KEY", "<value>", "User")
[System.Environment]::SetEnvironmentVariable("LANGFUSE_PUBLIC_KEY", "<value>", "User")
[System.Environment]::SetEnvironmentVariable("LANGFUSE_BASE_URL", "http://localhost:3000", "User")

# Apply variables to the current active terminal session immediately
$env:LANGFUSE_SECRET_KEY = [System.Environment]::GetEnvironmentVariable("LANGFUSE_SECRET_KEY", "User")
$env:LANGFUSE_PUBLIC_KEY = [System.Environment]::GetEnvironmentVariable("LANGFUSE_PUBLIC_KEY", "User")
$env:LANGFUSE_BASE_URL = [System.Environment]::GetEnvironmentVariable("LANGFUSE_BASE_URL", "User")

Write-Host "✅ Environment variables configured successfully!" -ForegroundColor Green

# 2. Upgrade Package Installer & Install Core Ecosystem SDKs
python -m pip install --upgrade pip
pip install openinference-instrumentation-openai opentelemetry-api opentelemetry-sdk langfuse qdrant-client requests

Write-Host "✅ All dependencies and Python libraries installed!" -ForegroundColor Green

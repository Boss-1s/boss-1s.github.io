const GITHUB_USER = 'Boss-1s';
const GITHUB_REPO = 'boss-1s.github.io';
const BRANCH = 'from-the-beginning,-again';

const API_URL = encodeURIComponent(`https://api.github.com/repos/${GITHUB_USER}/${GITHUB_REPO}/actions/workflows/publish.yml/runs?branch=${BRANCH}&status=success&per_page=1`);

// Check every 3 minutes (180,000 ms) to stay well within GitHub's 60/hr unauthenticated rate limit
const CHECK_INTERVAL = 180000;

let initialRunId = null;
let updateTimer = null;

async function checkDeploymentStatus() {
try {
    const response = await fetch(API_URL, { cache: 'no-store' });
    if (!response.ok) return;

    const data = await response.json();

    // Ensure at least one successful workflow run exists
    if (!data.workflow_runs || data.workflow_runs.length === 0) return;

    const latestRun = data.workflow_runs[0];
    const latestRunId = latestRun.id;

    // Record the active deployment ID on initial page load
    if (!initialRunId) {
    initialRunId = latestRunId;
    return;
    }

    // If a newer workflow run has succeeded, notify the user immediately
    if (latestRunId !== initialRunId) {
    clearInterval(updateTimer);
    showUpdateNotification();
    }
} catch (error) {
    console.error('Deployment check failed:', error);
}
}

function showUpdateNotification() {
if (document.getElementById('site-update-banner')) return;

const banner = document.createElement('div');
banner.id = 'site-update-banner';
banner.innerHTML = `
    <span>A new version of this site is live!</span>
    <button onclick="window.location.reload(true)">Refresh</button>
`;

Object.assign(banner.style, {
    position: 'fixed',
    bottom: '20px',
    right: '20px',
    backgroundColor: '#33ff00',
    color: '#000000',
    padding: '12px 18px',
    borderRadius: '8px',
    boxShadow: '0 4px 12px rgba(0,0,0,0.15)',
    display: 'flex',
    alignItems: 'center',
    gap: '12px',
    zIndex: '9999',
    fontFamily: 'system-ui, sans-serif',
    fontSize: '14px'
});

const btn = banner.querySelector('button');
Object.assign(btn.style, {
    backgroundColor: '#01550d',
    color: '#fff',
    border: 'none',
    padding: '6px 12px',
    borderRadius: '4px',
    cursor: 'pointer',
    fontWeight: 'bold'
});

document.body.appendChild(banner);
}

document.addEventListener('DOMContentLoaded', () => {
    console.log('Starting deployment status checks...');
    checkDeploymentStatus(); // Initial check on page load
    updateTimer = setInterval(checkDeploymentStatus, CHECK_INTERVAL);
});
const API_BASE = import.meta.env.VITE_API_URL || ''

function getUrl(path) {
  return `${API_BASE}${path}`
}

export async function predictElective(profile) {
  const response = await fetch(getUrl('/api/predict'), {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(profile),
  })

  if (!response.ok) {
    const errorData = await response.json().catch(() => ({}))
    throw new Error(errorData.detail || `Request failed with status ${response.status}`)
  }

  return response.json()
}

export async function checkHealth() {
  const response = await fetch(getUrl('/api/health'))
  if (!response.ok) {
    throw new Error('Health check failed')
  }
  return response.json()
}

export async function getInfo() {
  const response = await fetch(getUrl('/api/info'))
  if (!response.ok) {
    throw new Error('Failed to fetch info')
  }
  return response.json()
}
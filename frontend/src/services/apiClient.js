// Simple API Client using fetch
// TODO: Adjust backend URL or use config from YAML if needed

const BASE_URL = "http://localhost:8000"

export async function getTasks() {
  const res = await fetch(`${BASE_URL}/tasks`)
  if (!res.ok) throw new Error('Failed to fetch tasks')
  return res.json()
}

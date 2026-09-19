# Elective Recommendation Frontend

React + Vite frontend for the Elective Recommendation System.

## Setup

```bash
cd frontend
npm install
```

## Development

```bash
npm run dev
```

Opens at http://localhost:5173

## Build for Production

```bash
npm run build
```

Output in `dist/` directory.

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `VITE_API_URL` | Backend API base URL | `http://127.0.0.1:8000` |

Create a `.env` file from `.env.example` to customize.

## Features

- Academic scores input (7 sliders, 0-100)
- Interest ratings (6 sliders, 1-5)
- Real-time prediction via FastAPI backend
- Top 3 recommendations with horizontal bar chart
- Student profile summary
- Loading and error states
- Responsive design (mobile to desktop)
- Accessible form controls

## Tech Stack

- React 18
- Vite 5
- Recharts (visualization)
- CSS Variables (theming)
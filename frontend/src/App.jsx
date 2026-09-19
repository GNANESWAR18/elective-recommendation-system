import { useState } from 'react'
import Header from './components/Header'
import AcademicScores from './components/AcademicScores'
import InterestSelector from './components/InterestSelector'
import RecommendButton from './components/RecommendButton'
import RecommendationCard from './components/RecommendationCard'
import RecommendationChart from './components/RecommendationChart'
import ProfileSummary from './components/ProfileSummary'
import ErrorMessage from './components/ErrorMessage'
import LoadingSpinner from './components/LoadingSpinner'
import { predictElective } from './services/api'

const initialScores = {
  programming_score: 70,
  mathematics_score: 70,
  database_score: 65,
  ai_score: 60,
  ml_score: 60,
  web_score: 65,
  data_science_score: 60,
}

const initialInterests = {
  interest_ai: 3,
  interest_web: 3,
  interest_data: 3,
  interest_programming: 3,
  interest_cloud: 3,
  interest_security: 3,
}

function App() {
  const [scores, setScores] = useState(initialScores)
  const [interests, setInterests] = useState(initialInterests)
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const handleScoreChange = (key, value) => {
    setScores(prev => ({ ...prev, [key]: value }))
  }

  const handleInterestChange = (key, value) => {
    setInterests(prev => ({ ...prev, [key]: value }))
  }

  const handleRecommend = async () => {
    setLoading(true)
    setError(null)
    setResult(null)

    try {
      const profile = { ...scores, ...interests }
      const data = await predictElective(profile)
      setResult(data)
    } catch (err) {
      setError(err.message || 'Unable to get a recommendation. Please make sure the backend is running.')
    } finally {
      setLoading(false)
    }
  }

  const handleReset = () => {
    setScores(initialScores)
    setInterests(initialInterests)
    setResult(null)
    setError(null)
  }

  return (
    <div className="app">
      <Header />
      <main className="container">
        <section className="section" aria-labelledby="academic-heading">
          <h2 id="academic-heading" className="section-title">Student Academic Performance</h2>
          <p className="section-subtitle">Rate your academic scores (0–100)</p>
          <AcademicScores scores={scores} onChange={handleScoreChange} />
        </section>

        <section className="section" aria-labelledby="interests-heading">
          <h2 id="interests-heading" className="section-title">Student Interests</h2>
          <p className="section-subtitle">Rate your interest level (1 = Low, 5 = High)</p>
          <InterestSelector interests={interests} onChange={handleInterestChange} />
        </section>

        <RecommendButton
          onClick={handleRecommend}
          loading={loading}
          disabled={loading}
        />

        <ErrorMessage message={error} onDismiss={() => setError(null)} />

        {result && (
          <>
            <RecommendationCard
              recommendedElective={result.recommended_elective}
              confidence={result.confidence}
            />
            <RecommendationChart recommendations={result.top_recommendations} />
            <ProfileSummary scores={scores} interests={interests} />
          </>
        )}

        {result && (
          <div className="reset-section">
            <button className="btn btn-secondary" onClick={handleReset}>
              Start Over
            </button>
          </div>
        )}
      </main>
      <footer className="footer">
        <p>Elective Recommendation System • Synthetic dataset • Not a substitute for academic advising</p>
      </footer>
    </div>
  )
}

export default App
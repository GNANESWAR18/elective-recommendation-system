const SCORE_FIELDS = [
  { key: 'programming_score', label: 'Programming Score' },
  { key: 'mathematics_score', label: 'Mathematics Score' },
  { key: 'database_score', label: 'Database Score' },
  { key: 'ai_score', label: 'AI Score' },
  { key: 'ml_score', label: 'ML Score' },
  { key: 'web_score', label: 'Web Development Score' },
  { key: 'data_science_score', label: 'Data Science Score' },
]

function ScoreInput({ label, value, onChange, key }) {
  const handleInput = (e) => {
    const val = Math.min(100, Math.max(0, parseInt(e.target.value) || 0))
    onChange(key, val)
  }

  const handleSlider = (e) => {
    onChange(key, parseInt(e.target.value))
  }

  return (
    <div className="score-input">
      <label htmlFor={key} className="score-label">
        <span className="score-label-text">{label}</span>
        <span className="score-value">{value}</span>
      </label>
      <div className="score-controls">
        <input
          type="range"
          id={key}
          min="0"
          max="100"
          value={value}
          onChange={handleSlider}
          className="score-slider"
          aria-label={label}
        />
        <input
          type="number"
          min="0"
          max="100"
          value={value}
          onChange={handleInput}
          className="score-number"
          aria-label={`${label} value`}
        />
      </div>
    </div>
  )
}

function AcademicScores({ scores, onChange }) {
  return (
    <div className="scores-grid" role="group" aria-labelledby="academic-heading">
      {SCORE_FIELDS.map(field => (
        <ScoreInput
          key={field.key}
          label={field.label}
          value={scores[field.key]}
          onChange={onChange}
        />
      ))}
    </div>
  )
}

export default AcademicScores
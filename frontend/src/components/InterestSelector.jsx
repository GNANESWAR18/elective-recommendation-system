const INTEREST_FIELDS = [
  { key: 'interest_ai', label: 'AI' },
  { key: 'interest_web', label: 'Web Development' },
  { key: 'interest_data', label: 'Data Science' },
  { key: 'interest_programming', label: 'Programming' },
  { key: 'interest_cloud', label: 'Cloud Computing' },
  { key: 'interest_security', label: 'Cyber Security' },
]

const INTEREST_LABELS = {
  1: 'Low',
  2: 'Low-Med',
  3: 'Medium',
  4: 'Med-High',
  5: 'High',
}

function InterestInput({ label, value, onChange, key }) {
  const handleChange = (e) => {
    onChange(key, parseInt(e.target.value))
  }

  return (
    <div className="interest-input">
      <label htmlFor={key} className="interest-label">
        <span className="interest-label-text">{label}</span>
        <span className="interest-value">{INTEREST_LABELS[value]}</span>
      </label>
      <input
        type="range"
        id={key}
        min="1"
        max="5"
        value={value}
        onChange={handleChange}
        className="interest-slider"
        aria-label={label}
      />
      <div className="interest-scale" aria-hidden="true">
        <span>1</span>
        <span>2</span>
        <span>3</span>
        <span>4</span>
        <span>5</span>
      </div>
    </div>
  )
}

function InterestSelector({ interests, onChange }) {
  return (
    <div className="interests-grid" role="group" aria-labelledby="interests-heading">
      {INTEREST_FIELDS.map(field => (
        <InterestInput
          key={field.key}
          label={field.label}
          value={interests[field.key]}
          onChange={onChange}
        />
      ))}
    </div>
  )
}

export default InterestSelector
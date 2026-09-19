const SCORE_LABELS = {
  programming_score: 'Programming',
  mathematics_score: 'Mathematics',
  database_score: 'Database',
  ai_score: 'AI',
  ml_score: 'ML',
  web_score: 'Web Development',
  data_science_score: 'Data Science',
}

const INTEREST_LABELS = {
  interest_ai: 'AI',
  interest_web: 'Web Development',
  interest_data: 'Data Science',
  interest_programming: 'Programming',
  interest_cloud: 'Cloud Computing',
  interest_security: 'Cyber Security',
}

const INTEREST_TEXT = {
  1: 'Low',
  2: 'Low-Medium',
  3: 'Medium',
  4: 'Medium-High',
  5: 'High',
}

function ProfileSection({ title, items, renderValue }) {
  return (
    <div className="profile-section">
      <h3 className="profile-section-title">{title}</h3>
      <dl className="profile-list">
        {items.map(({ key, label }) => (
          <div key={key} className="profile-item">
            <dt className="profile-label">{label}</dt>
            <dd className="profile-value">{renderValue(key)}</dd>
          </div>
        ))}
      </dl>
    </div>
  )
}

function ProfileSummary({ scores, interests }) {
  const scoreItems = Object.entries(SCORE_LABELS).map(([key, label]) => ({ key, label }))
  const interestItems = Object.entries(INTEREST_LABELS).map(([key, label]) => ({ key, label }))

  return (
    <section className="section profile-summary" aria-labelledby="profile-heading">
      <h2 id="profile-heading" className="section-title">Student Profile Summary</h2>
      <div className="profile-grid">
        <ProfileSection
          title="Academic Performance"
          items={scoreItems}
          renderValue={(key) => scores[key]}
        />
        <ProfileSection
          title="Interests"
          items={interestItems}
          renderValue={(key) => INTEREST_TEXT[interests[key]]}
        />
      </div>
    </section>
  )
}

export default ProfileSummary
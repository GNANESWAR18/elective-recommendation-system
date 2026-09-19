function RecommendationCard({ recommendedElective, confidence }) {
  return (
    <section className="section recommendation-card" aria-labelledby="rec-heading">
      <h2 id="rec-heading" className="section-title">Recommended Elective</h2>
      <div className="recommendation-main">
        <div className="recommendation-name">{recommendedElective}</div>
        <div className="recommendation-confidence">
          <span className="confidence-label">Confidence</span>
          <span className="confidence-value">{confidence}%</span>
        </div>
      </div>
    </section>
  )
}

export default RecommendationCard
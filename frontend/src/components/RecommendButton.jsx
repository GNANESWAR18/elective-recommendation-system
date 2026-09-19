function RecommendButton({ onClick, loading, disabled }) {
  return (
    <button
      type="button"
      className="btn btn-primary recommend-btn"
      onClick={onClick}
      disabled={disabled}
      aria-busy={loading}
    >
      {loading ? (
        <>
          <span className="spinner" aria-hidden="true"></span>
          <span>Analyzing your profile...</span>
        </>
      ) : (
        'Get My Recommendation'
      )}
    </button>
  )
}

export default RecommendButton
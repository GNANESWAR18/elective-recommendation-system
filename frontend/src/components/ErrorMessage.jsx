function ErrorMessage({ message, onDismiss }) {
  if (!message) return null

  return (
    <div className="error-message" role="alert">
      <span className="error-icon" aria-hidden="true">⚠</span>
      <p className="error-text">{message}</p>
      <button type="button" className="error-dismiss" onClick={onDismiss} aria-label="Dismiss error">
        ×
      </button>
    </div>
  )
}

export default ErrorMessage